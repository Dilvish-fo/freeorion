""" The FreeOrionAI module contains the methods which can be made by the C AIInterface;
these methods in turn activate other portions of the python AI code."""
import pickle  # Python object serialization library
import sys
import random

# IMPORTANT! this import also execute python code to update freeOrionAIInterface interface,
# removing this import will brake AI in unexpected locations.
from freeorion_debug import handle_debug_chat, listener

import freeOrionAIInterface as fo  # interface used to interact with FreeOrion AI client  # pylint: disable=import-error
# pylint: disable=relative-import
import AIstate
import ColonisationAI
import ExplorationAI
import FleetUtilsAI
import InvasionAI
import MilitaryAI
import PlanetUtilsAI
import PriorityAI
import ProductionAI
import ResearchAI
import ResourcesAI
from freeorion_tools import UserString, chat_on_error, print_error
from freeorion_debug import Timer

main_timer = Timer('timer', write_log=True)
turn_timer = Timer('bucket', write_log=True)

using_statprof = False
try:
    import statprof
    # statprof.start()
    # using_statprof = True
except:
    pass


_capitols = {fo.aggression.beginner: UserString("AI_CAPITOL_NAMES_BEGINNER", ""),
             fo.aggression.turtle: UserString("AI_CAPITOL_NAMES_TURTLE", ""),
             fo.aggression.cautious: UserString("AI_CAPITOL_NAMES_CAUTIOUS", ""),
             fo.aggression.typical: UserString("AI_CAPITOL_NAMES_TYPICAL", ""),
             fo.aggression.aggressive: UserString("AI_CAPITOL_NAMES_AGGRESSIVE", ""),
             fo.aggression.maniacal: UserString("AI_CAPITOL_NAMES_MANIACAL", "")}

# AIstate
foAIstate = None


def initFreeOrionAI():  # pylint: disable=invalid-name
    """Called by client when Python AI starts, before any game new game starts or saved game is resumed."""
    ai_config = fo.getAIConfigStr()
    print "Initialized FreeOrion Python AI with ai_config string '%s'" % ai_config
    print(sys.path)


@chat_on_error
def startNewGame(aggression=fo.aggression.aggressive):  # pylint: disable=invalid-name
    """Called by client when a new game is started (but not when a game is loaded).
    Should clear any pre-existing state and set up whatever is needed for AI to generate orders."""
    turn_timer.start("Server Processing")
    print "New game started, AI Aggression level %d" % aggression

    # initialize AIstate
    global foAIstate
    foAIstate = AIstate.AIstate(aggression=aggression)
    foAIstate.session_start_cleanup()
    print "Initialized foAIstate class"
    planet_id = PlanetUtilsAI.get_capital()
    universe = fo.getUniverse()
    if planet_id is not None and planet_id != -1:
        planet = universe.getPlanet(planet_id)
        new_name = random.choice(_capitols.get(aggression, "").split('\n')).strip() + " " + planet.name
        print "Capitol City Names are: ", _capitols
        print "This Capitol New name is ", new_name
        res = fo.issueRenameOrder(planet_id, new_name)
        print "Capitol Rename attempt result: %d; planet now named %s" % (res, planet.name)


@chat_on_error
def resumeLoadedGame(saved_state_string):  # pylint: disable=invalid-name
    """Called by client to when resume a loaded game."""
    turn_timer.start("Server Processing")

    global foAIstate
    print "Resuming loaded game"
    try:
        # loading saved state
        foAIstate = pickle.loads(saved_state_string)
        foAIstate.session_start_cleanup()
    except:
        print "failed to parse saved state string"
        # assigning new state
        foAIstate = AIstate.AIstate(aggression=fo.aggression.aggressive)
        foAIstate.session_start_cleanup()
        print_error("Fail to load aiState form saved game")



@chat_on_error
def prepareForSave():  # pylint: disable=invalid-name
    """Called by client when the game is about to be saved, to let the Python AI know it should save any AI state
    information, such as plans or knowledge about the game from previous turns,
    in the state string so that they can be restored if the game is loaded."""
    print "Preparing for game save by serializing state"

    # serialize (convert to string) global state dictionary and send to AI client to be stored in save file
    dump_string = pickle.dumps(foAIstate)
    print "foAIstate pickled to string, about to send to server"
    fo.setSaveStateString(dump_string)


@chat_on_error
def handleChatMessage(sender_id, message_text):  # pylint: disable=invalid-name
    """Called when this player receives a chat message. sender_id is the player who sent the message, and
    message_text is the text of the sent message."""
    # print "Received chat message from " + str(senderID) + " that says: " + messageText + " - ignoring it"
    handle_debug_chat(sender_id, message_text)


@chat_on_error
def handleDiplomaticMessage(message):  # pylint: disable=invalid-name
    """Called when this player receives a diplomatic message update from the server,
    such as if another player declares war, accepts peace, or cancels a proposed peace treaty."""
    print "Received diplomatic %s message from empire %s to empire %s" % (message.type, message.sender, message.recipient)
    print "my empire id: %s" % fo.empireID()
    if message.type == fo.diplomaticMessageType.peaceProposal and message.recipient == fo.empireID():
        reply_sender = message.recipient
        reply_recipient = message.sender
        proposal_sender_player = fo.empirePlayerID(message.sender)
        fo.sendChatMessage(proposal_sender_player, "So, the Terran Hairless Plains Ape advising your empire wishes to scratch its belly for a while?")
        if (foAIstate.aggression == fo.aggression.beginner or
                foAIstate.aggression != fo.aggression.maniacal and random.random() < 1.0 / (((foAIstate.aggression + 0.01)*fo.currentTurn()/2)**0.5)):
            fo.sendChatMessage(proposal_sender_player, "OK, Peace offer accepted.")
            reply = fo.diplomaticMessage(reply_sender, reply_recipient, fo.diplomaticMessageType.acceptProposal)
            print "Sending diplomatic message to empire %s of type %s" % (reply_recipient, reply.type)
            fo.sendDiplomaticMessage(reply)
        else:
            fo.sendChatMessage(proposal_sender_player, "Maybe later. We are currently getting busy with Experimental Test Subject yo-Ma-ma.")


@chat_on_error
def handleDiplomaticStatusUpdate(status_update):  # pylint: disable=invalid-name
    """Called when this player receives and update about the diplomatic status between players, which may
    or may not include this player."""
    print "Received diplomatic status update to %s about empire %s and empire %s" % (status_update.status, status_update.empire1, status_update.empire2)


@chat_on_error
@listener
def generateOrders():  # pylint: disable=invalid-name
    """Called once per turn to tell the Python AI to generate and issue orders to control its empire.
    at end of this function, fo.doneTurn() should be called to indicate to the client that orders are finished
    and can be sent to the server for processing."""
    turn_timer.start("AI planning")
    empire = fo.getEmpire()
    # set the random seed (based on galaxy seed, empire ID and current turn)
    # for game-reload consistency 
    random_seed = str(fo.getGalaxySetupData().seed) + "%03d%05d" % (fo.empireID(), fo.currentTurn())
    random.seed(random_seed)
    aggression_name = fo.aggression.values[foAIstate.aggression].name

    if fo.currentTurn() == 1:
        declare_war_on_all()
        human_player = fo.empirePlayerID(1)
        fo.sendChatMessage(human_player,  '%s Empire (%s):\n"Ave, Human, morituri te salutant!"' % (empire.name, aggression_name))

    # turn cleanup !!! this was formerly done at start of every turn -- not sure why
    foAIstate.split_new_fleets()

    foAIstate.refresh()  # checks exploration border & clears roles/missions of missing fleets & updates fleet locs & threats
    foAIstate.report_system_threats()
    print("Calling AI Modules")

    action_list = [PriorityAI.calculate_priorities,
                   ExplorationAI.assign_scouts_to_explore_systems,
                   ColonisationAI.assign_colony_fleets_to_colonise,
                   InvasionAI.assign_invasion_fleets_to_invade,
                   MilitaryAI.assign_military_fleets_to_systems,
                   FleetUtilsAI.generate_fleet_orders_for_fleet_missions,
                   FleetUtilsAI.issue_fleet_orders_for_fleet_missions,
                   ResearchAI.generate_research_orders,
                   ProductionAI.generateProductionOrders,
                   ResourcesAI.generate_resources_orders,
                   foAIstate.after_turn_cleanup,
                   ]

    for action in action_list:
        try:
            main_timer.start(action.__name__)
            action()
            main_timer.stop()
        except Exception as e:
            print_error(e, location=action.__name__)
    main_timer.end()
    turn_timer.end()
    turn_timer.start("Server_Processing")

    try:
        fo.doneTurn()
    except Exception as e:
        print_error(e)  # TODO move it to cycle above

    if using_statprof:
        try:
            statprof.stop()
            statprof.display()
            statprof.start()
        except:
            pass


# The following methods should probably be moved to the AIstate module, to keep this module more focused on implementing required interface
def declare_war_on_all():  # pylint: disable=invalid-name
    """Used to declare war on all other empires (at start of game)"""
    my_emp_id = fo.empireID()
    for emp_id in fo.allEmpireIDs():
        if emp_id != my_emp_id:
            msg = fo.diplomaticMessage(my_emp_id, emp_id, fo.diplomaticMessageType.warDeclaration)
            fo.sendDiplomaticMessage(msg)
