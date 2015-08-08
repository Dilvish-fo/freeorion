from functools import partial
import math
import random

import freeOrionAIInterface as fo  # pylint: disable=import-error
import FreeOrionAI as foAI
import AIDependencies as Dep
import AIstate
import ColonisationAI
import ShipDesignAI
from freeorion_tools import tech_is_complete, get_ai_tag_grade

empire_stars = {}
research_reqs = {}
choices = {}

REQS_PREREQS_IDX = 0
REQS_COST_IDX = 1
REQS_TIME_IDX = 2
REQS_PER_TURN_COST_IDX = 3


# TODO research AI no longer use this method, rename and move this method elsewhere
def get_research_index():
    empire_id = fo.empireID()
    research_index = empire_id % 2
    if foAI.foAIstate.aggression >= fo.aggression.aggressive:  # maniacal
        research_index = 2 + (empire_id % 3)  # so indices [2,3,4]
    elif foAI.foAIstate.aggression >= fo.aggression.typical:
        research_index += 1
    return research_index


def const_priority(this_const):
    """
    Returns function that returns constant result.
    :type this_const: float
    :rtype function
    """
    def wrapper(tech_name=""):
        return this_const
    return wrapper

priority_zero = const_priority(0.0)
priority_low = const_priority(0.1)
priority_one = const_priority(1.0)


def conditional_priority(func_if_true, func_if_false, cond_func=None, this_object=None, this_attr=None):
    """
    returns a priority dependent on a condition, either a function or an object attribute
    :type func_if_true: ()
    :type func_if_false: ()
    :type cond_func:(str) -> bool
    :type this_object: object
    :type this_attr:str
    :rtype float
    """
    def get_priority(tech_name=""):
        if cond_func:
            _cond_func = cond_func
        else:
            if this_object is not None:
                _cond_func = partial(getattr, this_object, this_attr)
            else:
                return priority_low()

        if _cond_func():
            return func_if_true(tech_name=tech_name)
        else:
            return func_if_false(tech_name=tech_name)
    return get_priority

MIL_IDX = 0
TROOP_IDX = 1
COLONY_IDX = 2

MAIN_SHIP_DESIGNER_LIST = []


def get_main_ship_designer_list():
    if not MAIN_SHIP_DESIGNER_LIST:
        MAIN_SHIP_DESIGNER_LIST.extend([ShipDesignAI.MilitaryShipDesigner(), ShipDesignAI.StandardTroopShipDesigner(),
                                        ShipDesignAI.StandardColonisationShipDesigner()])
    return MAIN_SHIP_DESIGNER_LIST


def ship_usefulness(base_priority_func, this_designer=None, tech_name=""):
    """

    :type base_priority_func: () _> bool
    :type this_designer: int | None
    """
    if this_designer is None:
        this_designer_list = get_main_ship_designer_list()
    elif isinstance(this_designer, int):
        this_designer_list = get_main_ship_designer_list()[:this_designer+1][-1:]
    else:
        return 0.0
    useful = 0.0
    for this_designer in this_designer_list:
        useful = max(useful, get_ship_tech_usefulness(tech_name, this_designer))
    return useful * base_priority_func()


def has_star(star_type):
    if star_type not in empire_stars:
        empire_stars[star_type] = len(AIstate.empireStars.get(star_type, [])) != 0
    return empire_stars[star_type]


def if_enemies(false_val=0.1, true_val=1.0, tech_name=""):
    return true_val if foAI.foAIstate.misc.get('enemies_sighted', {}) else false_val


def if_dict(this_dict, this_key, false_val=0.1, true_val=1.0, tech_name=""):
    return true_val if this_dict.get(this_key, False) else false_val


def if_tech_target(tech_target, false_val=0.1, true_val=1.0, tech_name=""):
    return true_val if tech_is_complete(tech_target) else false_val


def has_only_bad_colonizers():
    most_adequate = 0
    for specName in ColonisationAI.empire_colonizers:
        environs = {}
        this_spec = fo.getSpecies(specName)
        if not this_spec:
            continue
        for ptype in [fo.planetType.swamp, fo.planetType.radiated, fo.planetType.toxic, fo.planetType.inferno,
                      fo.planetType.barren, fo.planetType.tundra, fo.planetType.desert, fo.planetType.terran,
                      fo.planetType.ocean, fo.planetType.asteroids]:
            environ = this_spec.getPlanetEnvironment(ptype)
            environs.setdefault(environ, []).append(ptype)
        most_adequate = max(most_adequate, len(environs.get(fo.planetEnvironment.adequate, [])))
    return most_adequate == 0


def get_max_stealth_species():
    stealth_grades = {'BAD': -15, 'GOOD': 15, 'GREAT': 40, 'ULTIMATE': 60}
    stealth = -999
    stealth_species = ""
    for specName in ColonisationAI.empire_colonizers:
        this_spec = fo.getSpecies(specName)
        if not this_spec:
            continue
        this_stealth = stealth_grades.get(get_ai_tag_grade(list(this_spec.tags), "STEALTH"), 0)
        if this_stealth > stealth:
            stealth_species = specName
            stealth = this_stealth
    result = (stealth_species, stealth)
    return result


def get_initial_research_target():
    # TODO: consider cases where may want lesser target
    return Dep.ART_MINDS


def get_ship_tech_usefulness(tech, ship_designer):
    this_tech = fo.getTech(tech)
    if not this_tech:
        print "Invalid Tech specified"
        return 0
    unlocked_items = this_tech.unlockedItems
    unlocked_hulls = []
    unlocked_parts = []
    for item in unlocked_items:
        if item.type == fo.unlockableItemType.shipPart:
            unlocked_parts.append(item.name)
        elif item.type == fo.unlockableItemType.shipHull:
            unlocked_hulls.append(item.name)
    if not (unlocked_parts or unlocked_hulls):
        return 0
    old_designs = ship_designer.optimize_design(consider_fleet_count=False)
    new_designs = ship_designer.optimize_design(additional_hulls=unlocked_hulls, additional_parts=unlocked_parts,
                                                consider_fleet_count=False)
    if not (old_designs and new_designs):
        # AI is likely defeated; don't bother with logging error message
        return 0
    old_rating, old_pid, old_design_id, old_cost = old_designs[0]
    old_rating = old_rating
    new_rating, new_pid, new_design_id, new_cost = new_designs[0]
    new_rating = new_rating
    if new_rating > old_rating:
        ratio = (new_rating - old_rating) / (new_rating + old_rating)
        return ratio * 1.5 + 0.5
    else:
        return 0


def get_population_boost_priority(tech_name=""):
    return 2


def get_stealth_priority(tech_name=""):
    max_stealth_species = get_max_stealth_species()
    if max_stealth_species[1] > 0:
        print "Has a stealthy species %s. Increase stealth tech priority" % max_stealth_species[0]
        return 1.5
    else:
        return 0.1


def get_xeno_genetics_priority(tech_name=""):
    if foAI.foAIstate.aggression < fo.aggression.cautious:
        return get_population_boost_priority()
    if has_only_bad_colonizers():
        # Empire only have lousy colonisers, xeno-genetics are really important for them
        print "Empire has only lousy colonizers, increase priority to xeno_genetics"
        return get_population_boost_priority() * 3
    else:
        # TODO: assess number of planets with Adequate/Poor planets owned or considered for colonies
        return 0.6 * get_population_boost_priority()


def get_artificial_black_hole_priority(tech_name=""):
    if has_star(fo.starType.blackHole) or not has_star(fo.starType.red):
        print "Already have black hole, or does not have a red star to turn to black hole. Skipping ART_BLACK_HOLE"
        return 0
    for tech in Dep.SHIP_TECHS_REQUIRING_BLACK_HOLE:
        if tech_is_complete(tech):
            print "Solar hull is researched, needs a black hole to produce it. Research ART_BLACK_HOLE now!"
            return 999
    return 1


def get_hull_priority(tech_name):
    hull = 1
    offtrack_hull = 0.05

    chosen_hull = choices['hull']
    organic = hull if chosen_hull % 2 == 0 or choices['extra_organic_hull'] else offtrack_hull
    robotic = hull if chosen_hull % 2 == 1 or choices['extra_robotic_hull'] else offtrack_hull
    if ColonisationAI.got_ast:
        extra = choices['extra_asteroid_hull']
        asteroid = hull if chosen_hull == 2 or extra else offtrack_hull
        if asteroid == hull and not extra:
            organic = offtrack_hull
            robotic = offtrack_hull
    else:
        asteroid = 0
    if has_star(fo.starType.blue) or has_star(fo.starType.blackHole):
        extra = choices['extra_energy_hull']
        energy = hull if chosen_hull == 3 or extra else offtrack_hull
        if energy == hull and not extra:
            organic = offtrack_hull
            robotic = offtrack_hull
            asteroid = offtrack_hull
    else:
        energy = 0

    useful = max(
        get_ship_tech_usefulness(tech_name, ShipDesignAI.MilitaryShipDesigner()),
        get_ship_tech_usefulness(tech_name, ShipDesignAI.StandardTroopShipDesigner()),
        get_ship_tech_usefulness(tech_name, ShipDesignAI.StandardColonisationShipDesigner()))

    if foAI.foAIstate.misc.get('enemies_sighted', {}):
        aggression = 1
    else:
        aggression = 0.1

    if tech_name in Dep.ROBOTIC_HULL_TECHS:
        return robotic * useful * aggression
    elif tech_name in Dep.ORGANIC_HULL_TECHS:
        return organic * useful * aggression
    elif tech_name in Dep.ASTEROID_HULL_TECHS:
        return asteroid * useful * aggression
    elif tech_name in Dep.ENERGY_HULL_TECHS:
        return energy * useful * aggression
    else:
        return useful * aggression

# TODO boost genome bank if enemy is using bioterror
# TODO for supply techs consider starlane density and planet density

# initializing priority functions here within generate_research_orders() to avoid import race

# keys are "PREFIX1", as in "DEF" or "SPY"
primary_prefix_priority_funcs = {}

# keys are "PREFIX1_PREFIX2", as in "SHP_WEAPON"
secondary_prefix_priority_funcs = {}

# keys are individual full tech names
priority_funcs = {}

DEFAULT_PRIORITY = 0.5


def get_priority(tech_name):
    """
    Get tech priority. the default is just above. 0 if not useful (but doesn't hurt to research),
    < 0 to prevent AI to research it
    """
    name_parts = tech_name.split('_')
    primary_prefix = name_parts[0]
    secondary_prefix = '_'.join(name_parts[:2])
    if tech_name in priority_funcs:
        return priority_funcs[tech_name](tech_name=tech_name)
    elif secondary_prefix in secondary_prefix_priority_funcs:
        return secondary_prefix_priority_funcs[secondary_prefix](tech_name=tech_name)
    elif primary_prefix in primary_prefix_priority_funcs:
        return primary_prefix_priority_funcs[primary_prefix](tech_name=tech_name)

    # default priority for unseen techs
    if not tech_is_complete(tech_name):
        print "Tech %s does not have a priority, falling back to default." % tech_name

    return DEFAULT_PRIORITY


def calculate_research_requirements():
    """Calculate RPs and prerequisites of every tech, in (prereqs, cost, time)."""
    empire = fo.getEmpire()
    research_reqs.clear()

    completed_techs = get_completed_techs()
    for tech_name in fo.techs():
        if tech_is_complete(tech_name):
            research_reqs[tech_name] = ([], 0, 0, 0)
            continue
        this_tech = fo.getTech(tech_name)
        prereqs = [preReq for preReq in this_tech.recursivePrerequisites(empire.empireID) if preReq not in completed_techs]
        base_cost = this_tech.researchCost(empire.empireID)
        progress = empire.researchProgress(tech_name)
        cost = max(0.0, base_cost - progress)
        proportion_remaining = cost / max(base_cost, 1.0)
        this_time = this_tech.researchTime(fo.empireID())
        turns_needed = max(1, math.ceil(proportion_remaining * this_time))  # even if fully paid needs one turn
        per_turn_cost = float(base_cost) / max(1.0, this_time)

        # TODO: the following timing calc treats prereqs as inherently sequential; consider in parallel when able
        for prereq in prereqs:
            prereq_tech = fo.getTech(prereq)
            if not prereq_tech:
                continue
            base_cost = prereq_tech.researchCost(empire.empireID)
            progress = empire.researchProgress(prereq)
            prereq_cost = max(0.0, base_cost - progress)
            proportion_remaining = prereq_cost / max(base_cost, 1.0)
            this_time = prereq_tech.researchTime(fo.empireID())
            turns_needed += max(1, math.ceil(proportion_remaining * this_time))
            cost += prereq_cost
        research_reqs[tech_name] = (prereqs, cost, turns_needed, per_turn_cost)


def tech_cost_sort_key(tech_name):
    return research_reqs.get(tech_name, ([], 0, 0, 0))[REQS_COST_IDX]


def tech_time_sort_key(tech_name):
    return research_reqs.get(tech_name, ([], 0, 0, 0))[REQS_TIME_IDX]


def generate_research_orders():
    """generate research orders"""

    # initializing priority functions here within generate_research_orders() to avoid import race

    DEFENSIVE = foAI.foAIstate.aggression <= fo.aggression.cautious

    # keys are "PREFIX1", as in "DEF" or "SPY"
    if not primary_prefix_priority_funcs:
        primary_prefix_priority_funcs.update({
            Dep.DEFENSE_TECHS_PREFIX: const_priority(2.0) if DEFENSIVE else partial(if_enemies, 0.2)
            })

    # keys are "PREFIX1_PREFIX2", as in "SHP_WEAPON"
    if not secondary_prefix_priority_funcs:
        secondary_prefix_priority_funcs.update({
            Dep.WEAPON_PREFIX: partial(ship_usefulness, partial(if_enemies, 0.2), MIL_IDX)
            })

    if not priority_funcs:
        tech_handlers = (
            (
                Dep.PRO_MICROGRAV_MAN,
                conditional_priority(const_priority(3.5), priority_low, None, ColonisationAI, 'got_ast')
            ),
            (
                Dep.PRO_ORBITAL_GEN,
                conditional_priority(const_priority(3.0), priority_low, None, ColonisationAI, 'got_gg')
            ),
            (
                Dep.PRO_SINGULAR_GEN,
                conditional_priority(const_priority(3.0), priority_low, partial(has_star, fo.starType.blackHole))
            ),
            (
                Dep.GRO_XENO_GENETICS,
                get_xeno_genetics_priority
            ),
            (
                Dep.LRN_XENOARCH,
                priority_low if foAI.foAIstate.aggression < fo.aggression.typical else
                conditional_priority(const_priority(5.0), priority_low, None, ColonisationAI, 'gotRuins')
            ),
            (
                Dep.LRN_ART_BLACK_HOLE,
                get_artificial_black_hole_priority),
            (
                (Dep.GRO_GENOME_BANK,), priority_low
            ),
            (
                Dep.CON_CONC_CAMP,
                partial(priority_zero)
            ),
            (
                Dep.NEST_DOMESTICATION_TECH,
                priority_zero if foAI.foAIstate.aggression < fo.aggression.typical else conditional_priority(
                    const_priority(3.0), priority_low, None, ColonisationAI, 'got_nest')
            ),
            (
                Dep.UNRESEARCHABLE_TECHS,
                const_priority(-1.0)
            ),
            (
                Dep.UNUSED_TECHS,
                priority_zero
            ),
            (
                Dep.THEORY_TECHS,
                priority_zero
            ),
            (
                Dep.PRODUCTION_BOOST_TECHS,
                partial(if_dict, ColonisationAI.empire_status, 'industrialists', 0.6, 1.5)
            ),
            (
                Dep.RESEARCH_BOOST_TECHS,
                partial(if_tech_target, get_initial_research_target(), 2.1, 2.5)
            ),
            (
                Dep.PRODUCTION_AND_RESEARCH_BOOST_TECHS,
                const_priority(2.5)
            ),
            (
                Dep.POPULATION_BOOST_TECHS,
                get_population_boost_priority
            ),
            (
                Dep.SUPPLY_BOOST_TECHS,
                partial(if_tech_target, Dep.SUPPLY_BOOST_TECHS[0], 1.0, 0.5)
            ),
            (
                Dep.METER_CHANGE_BOOST_TECHS,
                const_priority(1.0)
            ),
            (
                Dep.DETECTION_TECHS,
                const_priority(0.5)
            ),
            (
                Dep.STEALTH_TECHS,
                get_stealth_priority
            ),
            (
                Dep.DAMAGE_CONTROL_TECHS,
                partial(if_enemies, 0.1, 0.5)
            ),
            (
                Dep.HULL_TECHS,
                get_hull_priority
            ),
            (
                Dep.ARMOR_TECHS,
                partial(ship_usefulness, if_enemies, MIL_IDX)
            ),
            (
                Dep.ENGINE_TECHS,
                partial(ship_usefulness, partial(if_dict, choices, 'engine', true_val=0.6), None)
            ),
            (
                Dep.FUEL_TECHS,
                partial(ship_usefulness, partial(if_dict, choices, 'fuel'), None)),
            (
                Dep.SHIELD_TECHS,
                partial(ship_usefulness, if_enemies, MIL_IDX)
            ),
            (
                Dep.TROOP_POD_TECHS,
                partial(ship_usefulness,
                        partial(if_enemies, 0.1, 0.3), TROOP_IDX)
            ),
            (
                Dep.COLONY_POD_TECHS,
                partial(ship_usefulness, const_priority(0.5), COLONY_IDX)
            ),
        )
        for k, v in tech_handlers:
            if isinstance(k, basestring):
                k = (k, )  # wrap single techs to tuple
            for tech in k:
                priority_funcs[tech] = v

    empire = fo.getEmpire()
    empire_id = empire.empireID
    print "Research Queue Management on turn %d:" % fo.currentTurn()
    print "ColonisationAI survey: got_ast %s, got_gg %s, gotRuins %s" % (ColonisationAI.got_ast, ColonisationAI.got_gg, ColonisationAI.gotRuins)
    resource_production = empire.resourceProduction(fo.resourceType.research)
    print "\nTotal Current Research Points: %.2f\n" % resource_production
    print "Techs researched and available for use:"
    completed_techs = sorted(list(get_completed_techs()))
    tlist = completed_techs+3*[" "]
    tlines = zip(tlist[0::3], tlist[1::3], tlist[2::3])
    for tline in tlines:
        print "%25s %25s %25s" % tline
    print

    #
    # report techs currently at head of research queue
    #
    research_queue = empire.researchQueue
    research_queue_list = get_research_queue_techs()
    tech_turns_left = {}
    if research_queue_list:
        print "Techs currently at head of Research Queue:"
        for element in list(research_queue)[:10]:
            tech_turns_left[element.tech] = element.turnsLeft
            this_tech = fo.getTech(element.tech)
            if not this_tech:
                print "Error: can't retrieve tech ", element.tech
                continue
            missing_prereqs = [preReq for preReq in this_tech.recursivePrerequisites(empire_id) if preReq not in completed_techs]
            # unlocked_items = [(uli.name, uli.type) for uli in this_tech.unlocked_items]
            unlocked_items = [uli.name for uli in this_tech.unlockedItems]
            if not missing_prereqs:
                print "    %25s allocated %6.2f RP -- unlockable items: %s " % (element.tech, element.allocation, unlocked_items)
            else:
                print "    %25s allocated %6.2f RP -- missing preReqs: %s -- unlockable items: %s " % (element.tech, element.allocation, missing_prereqs, unlocked_items)
        print

    #
    # calculate all research priorities, as in get_priority(tech) / total cost of tech (including prereqs)
    #
    rng = random.Random()
    rng.seed(fo.getEmpire().name + fo.getGalaxySetupData().seed)

    if '_selected' not in choices:
        choices['_selected'] = True
        choices['engine'] = rng.random() < 0.7
        choices['fuel'] = rng.random() < 0.7
        
        choices['hull'] = rng.randrange(4)
        choices['extra_organic_hull'] = rng.random() < 0.05
        choices['extra_robotic_hull'] = rng.random() < 0.05
        choices['extra_asteroid_hull'] = rng.random() < 0.05
        choices['extra_energy_hull'] = rng.random() < 0.05

    calculate_research_requirements()
    total_rp = empire.resourceProduction(fo.resourceType.research)

    if total_rp <= 0:  # No RP available - no research.
        return

    base_priorities = {}
    priorities = {}
    on_path_to = {}
    for tech_name in fo.techs():
        this_tech = fo.getTech(tech_name)
        if not this_tech or tech_is_complete(tech_name):
            continue
        base_priorities[tech_name] = priorities[tech_name] = get_priority(tech_name)

    # inherited priorities are modestly attenuated by total time
    TIMESCALE_PERIOD = 30.0
    for tech_name, priority in base_priorities.iteritems():
        if priority >= 0:
            turns_needed = max(research_reqs[tech_name][REQS_TIME_IDX], math.ceil(float(research_reqs[tech_name][REQS_COST_IDX]) / total_rp))
            time_attenuation = 2**(-max(0.0, turns_needed-5)/TIMESCALE_PERIOD)
            attenuated_priority = priority * time_attenuation
            for prereq in research_reqs.get(tech_name, ([], 0, 0, 0))[REQS_PREREQS_IDX]:
                if prereq in priorities and attenuated_priority > priorities[prereq]:  # checking like this to keep finished techs out of priorities
                    priorities[prereq] = attenuated_priority
                    on_path_to[prereq] = tech_name

    # final priorities are scaled by a combination of relative per-turn cost and relative total cost
    for tech_name, priority in priorities.iteritems():
        if priority >= 0:
            relative_turn_cost = max(research_reqs[tech_name][REQS_PER_TURN_COST_IDX], 0.1) / total_rp
            relative_total_cost = max(research_reqs[tech_name][REQS_COST_IDX], 0.1) / total_rp
            cost_factor = 2.0 / (relative_turn_cost + relative_total_cost)
            adjusted_priority = float(priority) * cost_factor
            # if priority > 1:
            #    print "tech %s has raw priority %.1f and adjusted priority %.1f, with %.1f total remaining cost, %.1f min turns needed and %.1f projected turns needed" % (tech_name, priority, adjusted_priority, research_reqs[tech_name][REQS_COST_IDX], research_reqs[tech_name][REQS_TIME_IDX], turns_needed)
            priorities[tech_name] = adjusted_priority

    #
    # put in highest priority techs until all RP spent, with  time then cost as minor sorting keys
    #
    possible = sorted(priorities.keys(), key=tech_cost_sort_key)
    possible.sort(key=tech_time_sort_key)
    possible.sort(key=priorities.__getitem__, reverse=True)

    missing_prereq_list = []
    print "Research priorities"
    print "    %25s %8s %8s %8s %25s %s" % ("Name", "Priority", "Cost", "Time", "As Prereq To", "Missing Prerequisties")
    for idx, tech_name in enumerate(possible[:20]):
        tech_info = research_reqs[tech_name]
        print "    %25s %8.6f %8.2f %8.2f %25s %s" % (tech_name, priorities[tech_name], tech_info[1], tech_info[2], on_path_to.get(tech_name, ""), tech_info[0])
        missing_prereq_list.extend([prereq for prereq in tech_info[0] if prereq not in possible[:idx] and not tech_is_complete(prereq)])
    print

    print "Prereqs seeming out of order:"
    print "    %25s %8s %8s %8s %8s %25s %s" % ("Name", "Priority", "Base Prio",  "Cost", "Time", "As Prereq To", "Missing Prerequisties")
    for tech_name in missing_prereq_list:
        tech_info = research_reqs[tech_name]
        print "    %25s %8.6f %8.6f %8.2f %8.2f %25s %s" % (tech_name, priorities[tech_name], base_priorities[tech_name], tech_info[1], tech_info[2], on_path_to.get(tech_name, ""), tech_info[0])


    print "enqueuing techs. already spent RP: %s total RP: %s" % (fo.getEmpire().researchQueue.totalSpent, total_rp)

    if fo.currentTurn() == 1 and not research_queue_list:
        fo.issueEnqueueTechOrder("GRO_PLANET_ECOL", -1)
        fo.issueEnqueueTechOrder("LRN_ALGO_ELEGANCE", -1)
    else:
        # some floating point issues can cause AI to enqueue every tech......
        queued_techs = set(get_research_queue_techs())
        while empire.resourceProduction(fo.resourceType.research) - empire.researchQueue.totalSpent > 0.001 and possible:
            to_research = possible.pop(0)  # get tech with highest priority
            if to_research not in queued_techs:
                fo.issueEnqueueTechOrder(to_research, -1)
                queued_techs.add(to_research)
                print "    enqueued tech " + to_research + "  : cost: " + str(fo.getTech(to_research).researchCost(empire.empireID)) + "RP"
                fo.updateResearchQueue()
        print


def get_completed_techs():
    """get completed and available for use techs"""
    return [tech for tech in fo.techs() if tech_is_complete(tech)]


def get_research_queue_techs():
    """ Get list of techs in research queue."""
    return [element.tech for element in fo.getEmpire().researchQueue]
