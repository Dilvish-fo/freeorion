class FleetPlan(object):
    def ship_designs(self):
        """
        C++ signature:
            class boost::python::list ship_designs(class `anonymous namespace'::FleetPlanWrapper {lvalue})
        
        :rtype list
        """
        return list()

    def name(self):
        """
        C++ signature:
            class boost::python::api::object name(class `anonymous namespace'::FleetPlanWrapper {lvalue})
        
        :rtype object
        """
        return object()


class ItemSpec(object):
    @property
    def type(self):
        return unlockableItemType()

    @property
    def name(self):
        return str()


class MonsterFleetPlan(object):
    def ship_designs(self):
        """
        C++ signature:
            class boost::python::list ship_designs(class `anonymous namespace'::MonsterFleetPlanWrapper {lvalue})
        
        :rtype list
        """
        return list()

    def spawn_rate(self):
        """
        C++ signature:
            double spawn_rate(class `anonymous namespace'::MonsterFleetPlanWrapper {lvalue})
        
        :rtype float
        """
        return float()

    def spawn_limit(self):
        """
        C++ signature:
            int spawn_limit(class `anonymous namespace'::MonsterFleetPlanWrapper {lvalue})
        
        :rtype int
        """
        return int()

    def name(self):
        """
        C++ signature:
            class boost::python::api::object name(class `anonymous namespace'::MonsterFleetPlanWrapper {lvalue})
        
        :rtype object
        """
        return object()

    def location(self, number):
        """
        C++ signature:
            bool location(class `anonymous namespace'::MonsterFleetPlanWrapper {lvalue},int)
        
        :param number:
        :type number: int
        :rtype bool
        """
        return bool()


class PlayerSetupData(object):
    @property
    def empire_color(self):
        pass

    @property
    def player_name(self):
        pass

    @property
    def empire_name(self):
        pass

    @property
    def starting_species(self):
        pass


class SystemPosition(object):
    @property
    def y(self):
        return float()

    @property
    def x(self):
        return float()


class SystemPositionVec(object):
    def __delitem__(self, obj):
        """
        C++ signature:
            void __delitem__(class std::vector<struct SystemPosition,class std::allocator<struct SystemPosition> > {lvalue},struct _object *)
        
        :param obj:
        :type obj: object
        :rtype None
        """
        return None

    def extend(self, obj):
        """
        C++ signature:
            void extend(class std::vector<struct SystemPosition,class std::allocator<struct SystemPosition> > {lvalue},class boost::python::api::object)
        
        :param obj:
        :type obj: object
        :rtype None
        """
        return None

    def __getitem__(self, obj2):
        """
        C++ signature:
            class boost::python::api::object __getitem__(struct boost::python::back_reference<class std::vector<struct SystemPosition,class std::allocator<struct SystemPosition> > &>,struct _object *)
        
        :param obj2:
        :type obj2: object
        :rtype object
        """
        return object()

    def __contains__(self, obj):
        """
        C++ signature:
            bool __contains__(class std::vector<struct SystemPosition,class std::allocator<struct SystemPosition> > {lvalue},struct _object *)
        
        :param obj:
        :type obj: object
        :rtype bool
        """
        return bool()

    def __iter__(self):
        """
        C++ signature:
            struct boost::python::objects::iterator_range<struct boost::python::return_value_policy<struct boost::python::return_by_value,struct boost::python::default_call_policies>,class std::_Vector_iterator<class std::_Vector_val<struct SystemPosition,class std::allocator<struct SystemPosition> > > > __iter__(struct boost::python::back_reference<class std::vector<struct SystemPosition,class std::allocator<struct SystemPosition> > &>)
        
        :rtype iter
        """
        return iter()

    def __setitem__(self, obj1, obj2):
        """
        C++ signature:
            void __setitem__(class std::vector<struct SystemPosition,class std::allocator<struct SystemPosition> > {lvalue},struct _object *,struct _object *)
        
        :param obj1:
        :type obj1: object
        :param obj2:
        :type obj2: object
        :rtype None
        """
        return None

    def __len__(self):
        """
        C++ signature:
            unsigned int __len__(class std::vector<struct SystemPosition,class std::allocator<struct SystemPosition> > {lvalue})
        
        :rtype int
        """
        return int()

    def append(self, obj):
        """
        C++ signature:
            void append(class std::vector<struct SystemPosition,class std::allocator<struct SystemPosition> > {lvalue},class boost::python::api::object)
        
        :param obj:
        :type obj: object
        :rtype None
        """
        return None


class galaxySetupData(object):
    @property
    def age(self):
        return galaxySetupOption()

    @property
    def starlaneFrequency(self):
        return galaxySetupOption()

    @property
    def nativeFrequency(self):
        return galaxySetupOption()

    @property
    def planetDensity(self):
        return galaxySetupOption()

    @property
    def shape(self):
        return galaxyShape()

    @property
    def specialsFrequency(self):
        return galaxySetupOption()

    @property
    def monsterFrequency(self):
        return galaxySetupOption()

    @property
    def maxAIAggression(self):
        return aggression()

    @property
    def seed(self):
        return str()

    @property
    def size(self):
        return int()


class Enum(int):
    """Enum stub for docs, not really present in fo"""
    pass


class aggression(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    aggressive = None  # aggression(4, "aggressive")
    beginner = None  # aggression(0, "beginner")
    cautious = None  # aggression(2, "cautious")
    invalid = None  # aggression(-1, "invalid")
    maniacal = None  # aggression(5, "maniacal")
    turtle = None  # aggression(1, "turtle")
    typical = None  # aggression(3, "typical")

aggression.invalid = aggression(-1, "invalid")
aggression.beginner = aggression(0, "beginner")
aggression.turtle = aggression(1, "turtle")
aggression.cautious = aggression(2, "cautious")
aggression.typical = aggression(3, "typical")
aggression.aggressive = aggression(4, "aggressive")
aggression.maniacal = aggression(5, "maniacal")


class buildType(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    building = None  # buildType(1, "building")
    ship = None  # buildType(2, "ship")

buildType.building = buildType(1, "building")
buildType.ship = buildType(2, "ship")


class captureResult(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    capture = None  # captureResult(0, "capture")
    destroy = None  # captureResult(1, "destroy")
    retain = None  # captureResult(2, "retain")

captureResult.capture = captureResult(0, "capture")
captureResult.destroy = captureResult(1, "destroy")
captureResult.retain = captureResult(2, "retain")


class diplomaticMessageType(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    acceptProposal = None  # diplomaticMessageType(2, "acceptProposal")
    cancelProposal = None  # diplomaticMessageType(3, "cancelProposal")
    noMessage = None  # diplomaticMessageType(-1, "noMessage")
    peaceProposal = None  # diplomaticMessageType(1, "peaceProposal")
    warDeclaration = None  # diplomaticMessageType(0, "warDeclaration")

diplomaticMessageType.noMessage = diplomaticMessageType(-1, "noMessage")
diplomaticMessageType.warDeclaration = diplomaticMessageType(0, "warDeclaration")
diplomaticMessageType.peaceProposal = diplomaticMessageType(1, "peaceProposal")
diplomaticMessageType.acceptProposal = diplomaticMessageType(2, "acceptProposal")
diplomaticMessageType.cancelProposal = diplomaticMessageType(3, "cancelProposal")


class diplomaticStatus(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    peace = None  # diplomaticStatus(1, "peace")
    war = None  # diplomaticStatus(0, "war")

diplomaticStatus.war = diplomaticStatus(0, "war")
diplomaticStatus.peace = diplomaticStatus(1, "peace")


class galaxySetupOption(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    high = None  # galaxySetupOption(3, "high")
    invalid = None  # galaxySetupOption(-1, "invalid")
    low = None  # galaxySetupOption(1, "low")
    medium = None  # galaxySetupOption(2, "medium")
    none = None  # galaxySetupOption(0, "none")

galaxySetupOption.invalid = galaxySetupOption(-1, "invalid")
galaxySetupOption.none = galaxySetupOption(0, "none")
galaxySetupOption.low = galaxySetupOption(1, "low")
galaxySetupOption.medium = galaxySetupOption(2, "medium")
galaxySetupOption.high = galaxySetupOption(3, "high")


class galaxyShape(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    cluster = None  # galaxyShape(3, "cluster")
    elliptical = None  # galaxyShape(4, "elliptical")
    invalid = None  # galaxyShape(-1, "invalid")
    irregular1 = None  # galaxyShape(5, "irregular1")
    irregular2 = None  # galaxyShape(6, "irregular2")
    random = None  # galaxyShape(8, "random")
    ring = None  # galaxyShape(7, "ring")
    spiral2 = None  # galaxyShape(0, "spiral2")
    spiral3 = None  # galaxyShape(1, "spiral3")
    spiral4 = None  # galaxyShape(2, "spiral4")

galaxyShape.invalid = galaxyShape(-1, "invalid")
galaxyShape.spiral2 = galaxyShape(0, "spiral2")
galaxyShape.spiral3 = galaxyShape(1, "spiral3")
galaxyShape.spiral4 = galaxyShape(2, "spiral4")
galaxyShape.cluster = galaxyShape(3, "cluster")
galaxyShape.elliptical = galaxyShape(4, "elliptical")
galaxyShape.irregular1 = galaxyShape(5, "irregular1")
galaxyShape.irregular2 = galaxyShape(6, "irregular2")
galaxyShape.ring = galaxyShape(7, "ring")
galaxyShape.random = galaxyShape(8, "random")


class meterType(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    capacity = None  # meterType(30, "capacity")
    construction = None  # meterType(16, "construction")
    damage = None  # meterType(29, "damage")
    defense = None  # meterType(21, "defense")
    detection = None  # meterType(27, "detection")
    fuel = None  # meterType(18, "fuel")
    industry = None  # meterType(13, "industry")
    maxDefense = None  # meterType(9, "maxDefense")
    maxFuel = None  # meterType(6, "maxFuel")
    maxShield = None  # meterType(7, "maxShield")
    maxStructure = None  # meterType(8, "maxStructure")
    maxSupply = None  # meterType(11, "maxSupply")
    maxTroops = None  # meterType(10, "maxTroops")
    population = None  # meterType(12, "population")
    rebels = None  # meterType(24, "rebels")
    research = None  # meterType(14, "research")
    shield = None  # meterType(19, "shield")
    size = None  # meterType(25, "size")
    starlaneSpeed = None  # meterType(28, "starlaneSpeed")
    stealth = None  # meterType(26, "stealth")
    structure = None  # meterType(20, "structure")
    supply = None  # meterType(23, "supply")
    targetConstruction = None  # meterType(4, "targetConstruction")
    targetIndustry = None  # meterType(1, "targetIndustry")
    targetPopulation = None  # meterType(0, "targetPopulation")
    targetResearch = None  # meterType(2, "targetResearch")
    targetTrade = None  # meterType(3, "targetTrade")
    trade = None  # meterType(15, "trade")
    troops = None  # meterType(22, "troops")

meterType.targetPopulation = meterType(0, "targetPopulation")
meterType.targetIndustry = meterType(1, "targetIndustry")
meterType.targetResearch = meterType(2, "targetResearch")
meterType.targetTrade = meterType(3, "targetTrade")
meterType.targetConstruction = meterType(4, "targetConstruction")
meterType.maxFuel = meterType(6, "maxFuel")
meterType.maxShield = meterType(7, "maxShield")
meterType.maxStructure = meterType(8, "maxStructure")
meterType.maxDefense = meterType(9, "maxDefense")
meterType.maxTroops = meterType(10, "maxTroops")
meterType.maxSupply = meterType(11, "maxSupply")
meterType.population = meterType(12, "population")
meterType.industry = meterType(13, "industry")
meterType.research = meterType(14, "research")
meterType.trade = meterType(15, "trade")
meterType.construction = meterType(16, "construction")
meterType.fuel = meterType(18, "fuel")
meterType.shield = meterType(19, "shield")
meterType.structure = meterType(20, "structure")
meterType.defense = meterType(21, "defense")
meterType.troops = meterType(22, "troops")
meterType.supply = meterType(23, "supply")
meterType.rebels = meterType(24, "rebels")
meterType.size = meterType(25, "size")
meterType.stealth = meterType(26, "stealth")
meterType.detection = meterType(27, "detection")
meterType.starlaneSpeed = meterType(28, "starlaneSpeed")
meterType.damage = meterType(29, "damage")
meterType.capacity = meterType(30, "capacity")


class planetEnvironment(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    adequate = None  # planetEnvironment(3, "adequate")
    good = None  # planetEnvironment(4, "good")
    hostile = None  # planetEnvironment(1, "hostile")
    poor = None  # planetEnvironment(2, "poor")
    uninhabitable = None  # planetEnvironment(0, "uninhabitable")

planetEnvironment.uninhabitable = planetEnvironment(0, "uninhabitable")
planetEnvironment.hostile = planetEnvironment(1, "hostile")
planetEnvironment.poor = planetEnvironment(2, "poor")
planetEnvironment.adequate = planetEnvironment(3, "adequate")
planetEnvironment.good = planetEnvironment(4, "good")


class planetSize(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    asteroids = None  # planetSize(6, "asteroids")
    gasGiant = None  # planetSize(7, "gasGiant")
    huge = None  # planetSize(5, "huge")
    large = None  # planetSize(4, "large")
    medium = None  # planetSize(3, "medium")
    noWorld = None  # planetSize(0, "noWorld")
    small = None  # planetSize(2, "small")
    tiny = None  # planetSize(1, "tiny")
    unknown = None  # planetSize(-1, "unknown")

planetSize.unknown = planetSize(-1, "unknown")
planetSize.noWorld = planetSize(0, "noWorld")
planetSize.tiny = planetSize(1, "tiny")
planetSize.small = planetSize(2, "small")
planetSize.medium = planetSize(3, "medium")
planetSize.large = planetSize(4, "large")
planetSize.huge = planetSize(5, "huge")
planetSize.asteroids = planetSize(6, "asteroids")
planetSize.gasGiant = planetSize(7, "gasGiant")


class planetType(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    asteroids = None  # planetType(9, "asteroids")
    barren = None  # planetType(4, "barren")
    desert = None  # planetType(6, "desert")
    gasGiant = None  # planetType(10, "gasGiant")
    inferno = None  # planetType(2, "inferno")
    ocean = None  # planetType(8, "ocean")
    radiated = None  # planetType(3, "radiated")
    swamp = None  # planetType(0, "swamp")
    terran = None  # planetType(7, "terran")
    toxic = None  # planetType(1, "toxic")
    tundra = None  # planetType(5, "tundra")
    unknown = None  # planetType(-1, "unknown")

planetType.unknown = planetType(-1, "unknown")
planetType.swamp = planetType(0, "swamp")
planetType.toxic = planetType(1, "toxic")
planetType.inferno = planetType(2, "inferno")
planetType.radiated = planetType(3, "radiated")
planetType.barren = planetType(4, "barren")
planetType.tundra = planetType(5, "tundra")
planetType.desert = planetType(6, "desert")
planetType.terran = planetType(7, "terran")
planetType.ocean = planetType(8, "ocean")
planetType.asteroids = planetType(9, "asteroids")
planetType.gasGiant = planetType(10, "gasGiant")


class resourceType(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    industry = None  # resourceType(0, "industry")
    research = None  # resourceType(2, "research")
    trade = None  # resourceType(1, "trade")

resourceType.industry = resourceType(0, "industry")
resourceType.trade = resourceType(1, "trade")
resourceType.research = resourceType(2, "research")


class shipPartClass(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    armour = None  # shipPartClass(5, "armour")
    bombard = None  # shipPartClass(13, "bombard")
    colony = None  # shipPartClass(10, "colony")
    detection = None  # shipPartClass(7, "detection")
    fighters = None  # shipPartClass(2, "fighters")
    fuel = None  # shipPartClass(9, "fuel")
    general = None  # shipPartClass(12, "general")
    industry = None  # shipPartClass(14, "industry")
    missiles = None  # shipPartClass(1, "missiles")
    pointDefense = None  # shipPartClass(3, "pointDefense")
    productionLocation = None  # shipPartClass(17, "productionLocation")
    research = None  # shipPartClass(15, "research")
    shields = None  # shipPartClass(4, "shields")
    shortRange = None  # shipPartClass(0, "shortRange")
    starlaneSpeed = None  # shipPartClass(11, "starlaneSpeed")
    stealth = None  # shipPartClass(8, "stealth")
    trade = None  # shipPartClass(16, "trade")
    troops = None  # shipPartClass(6, "troops")

shipPartClass.shortRange = shipPartClass(0, "shortRange")
shipPartClass.missiles = shipPartClass(1, "missiles")
shipPartClass.fighters = shipPartClass(2, "fighters")
shipPartClass.pointDefense = shipPartClass(3, "pointDefense")
shipPartClass.shields = shipPartClass(4, "shields")
shipPartClass.armour = shipPartClass(5, "armour")
shipPartClass.troops = shipPartClass(6, "troops")
shipPartClass.detection = shipPartClass(7, "detection")
shipPartClass.stealth = shipPartClass(8, "stealth")
shipPartClass.fuel = shipPartClass(9, "fuel")
shipPartClass.colony = shipPartClass(10, "colony")
shipPartClass.starlaneSpeed = shipPartClass(11, "starlaneSpeed")
shipPartClass.general = shipPartClass(12, "general")
shipPartClass.bombard = shipPartClass(13, "bombard")
shipPartClass.industry = shipPartClass(14, "industry")
shipPartClass.research = shipPartClass(15, "research")
shipPartClass.trade = shipPartClass(16, "trade")
shipPartClass.productionLocation = shipPartClass(17, "productionLocation")


class shipSlotType(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    core = None  # shipSlotType(2, "core")
    external = None  # shipSlotType(0, "external")
    internal = None  # shipSlotType(1, "internal")

shipSlotType.external = shipSlotType(0, "external")
shipSlotType.internal = shipSlotType(1, "internal")
shipSlotType.core = shipSlotType(2, "core")


class starType(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    blackHole = None  # starType(6, "blackHole")
    blue = None  # starType(0, "blue")
    neutron = None  # starType(5, "neutron")
    noStar = None  # starType(7, "noStar")
    orange = None  # starType(3, "orange")
    red = None  # starType(4, "red")
    unknown = None  # starType(-1, "unknown")
    white = None  # starType(1, "white")
    yellow = None  # starType(2, "yellow")

starType.unknown = starType(-1, "unknown")
starType.blue = starType(0, "blue")
starType.white = starType(1, "white")
starType.yellow = starType(2, "yellow")
starType.orange = starType(3, "orange")
starType.red = starType(4, "red")
starType.neutron = starType(5, "neutron")
starType.blackHole = starType(6, "blackHole")
starType.noStar = starType(7, "noStar")


class techStatus(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    complete = None  # techStatus(2, "complete")
    researchable = None  # techStatus(1, "researchable")
    unresearchable = None  # techStatus(0, "unresearchable")

techStatus.unresearchable = techStatus(0, "unresearchable")
techStatus.researchable = techStatus(1, "researchable")
techStatus.complete = techStatus(2, "complete")


class techType(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    application = None  # techType(1, "application")
    refinement = None  # techType(2, "refinement")
    theory = None  # techType(0, "theory")

techType.theory = techType(0, "theory")
techType.application = techType(1, "application")
techType.refinement = techType(2, "refinement")


class unlockableItemType(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    building = None  # unlockableItemType(0, "building")
    invalid = None  # unlockableItemType(-1, "invalid")
    shipDesign = None  # unlockableItemType(3, "shipDesign")
    shipHull = None  # unlockableItemType(2, "shipHull")
    shipPart = None  # unlockableItemType(1, "shipPart")
    tech = None  # unlockableItemType(4, "tech")

unlockableItemType.invalid = unlockableItemType(-1, "invalid")
unlockableItemType.building = unlockableItemType(0, "building")
unlockableItemType.shipPart = unlockableItemType(1, "shipPart")
unlockableItemType.shipHull = unlockableItemType(2, "shipHull")
unlockableItemType.shipDesign = unlockableItemType(3, "shipDesign")
unlockableItemType.tech = unlockableItemType(4, "tech")


class visibility(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    basic = None  # visibility(1, "basic")
    full = None  # visibility(3, "full")
    invalid = None  # visibility(-1, "invalid")
    none = None  # visibility(0, "none")
    partial = None  # visibility(2, "partial")

visibility.invalid = visibility(-1, "invalid")
visibility.none = visibility(0, "none")
visibility.basic = visibility(1, "basic")
visibility.partial = visibility(2, "partial")
visibility.full = visibility(3, "full")


def add_special(number, string):
    """
    C++ signature:
        void add_special(int,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param number:
    :type number: int
    :param string:
    :type string: str
    :rtype None
    """
    return None


def all_empires():
    """
    C++ signature:
        int all_empires()
    :rtype int
    """
    return int()


def base_star_type_dist(arg):
    """
    C++ signature:
        int base_star_type_dist(enum StarType)
    
    :param arg:
    :type arg: starType
    :rtype int
    """
    return int()


def calc_typical_universe_width(number):
    """
    C++ signature:
        double calc_typical_universe_width(int)
    
    :param number:
    :type number: int
    :rtype float
    """
    return float()


def cluster_galaxy_calc_positions(arg, number1, number2, floating_number1, floating_number2):
    """
    C++ signature:
        void cluster_galaxy_calc_positions(class std::vector<struct SystemPosition,class std::allocator<struct SystemPosition> > {lvalue},unsigned int,unsigned int,double,double)
    
    :param arg:
    :type arg: SystemPositionVec
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :param floating_number1:
    :type floating_number1: float
    :param floating_number2:
    :type floating_number2: float
    :rtype None
    """
    return None


def create_building(string, number1, number2):
    """
    C++ signature:
        int create_building(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,int,int)
    
    :param string:
    :type string: str
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :rtype int
    """
    return int()


def create_fleet(string, number1, number2):
    """
    C++ signature:
        int create_fleet(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,int,int)
    
    :param string:
    :type string: str
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :rtype int
    """
    return int()


def create_monster(string, number):
    """
    C++ signature:
        int create_monster(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,int)
    
    :param string:
    :type string: str
    :param number:
    :type number: int
    :rtype int
    """
    return int()


def create_monster_fleet(number):
    """
    C++ signature:
        int create_monster_fleet(int)
    
    :param number:
    :type number: int
    :rtype int
    """
    return int()


def create_planet(arg, planet_type, number1, number2, string):
    """
    C++ signature:
        int create_planet(enum PlanetSize,enum PlanetType,int,int,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param arg:
    :type arg: planetSize
    :param planet_type:
    :type planet_type: planetType
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :param string:
    :type string: str
    :rtype int
    """
    return int()


def create_ship(string1, string2, string3, number):
    """
    C++ signature:
        int create_ship(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,int)
    
    :param string1:
    :type string1: str
    :param string2:
    :type string2: str
    :param string3:
    :type string3: str
    :param number:
    :type number: int
    :rtype int
    """
    return int()


def create_system(arg, string, floating_number1, floating_number2):
    """
    C++ signature:
        int create_system(enum StarType,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,double,double)
    
    :param arg:
    :type arg: starType
    :param string:
    :type string: str
    :param floating_number1:
    :type floating_number1: float
    :param floating_number2:
    :type floating_number2: float
    :rtype int
    """
    return int()


def current_turn():
    """
    C++ signature:
        int current_turn()
    :rtype int
    """
    return int()


def density_mod_to_planet_size_dist(arg1, arg2):
    """
    C++ signature:
        int density_mod_to_planet_size_dist(enum GalaxySetupOption,enum PlanetSize)
    
    :param arg1:
    :type arg1: galaxySetupOption
    :param arg2:
    :type arg2: planetSize
    :rtype int
    """
    return int()


def design_create(string1, string2, string3, item_list, string4, string5, boolean):
    """
    C++ signature:
        bool design_create(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class boost::python::list,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,bool)
    
    :param string1:
    :type string1: str
    :param string2:
    :type string2: str
    :param string3:
    :type string3: str
    :param item_list:
    :type item_list: list
    :param string4:
    :type string4: str
    :param string5:
    :type string5: str
    :param boolean:
    :type boolean: bool
    :rtype bool
    """
    return bool()


def design_get_monster_list():
    """
    C++ signature:
        class boost::python::list design_get_monster_list()
    :rtype list
    """
    return list()


def design_get_premade_list():
    """
    C++ signature:
        class boost::python::list design_get_premade_list()
    :rtype list
    """
    return list()


def elliptical_galaxy_calc_positions(arg, number, floating_number1, floating_number2):
    """
    C++ signature:
        void elliptical_galaxy_calc_positions(class std::vector<struct SystemPosition,class std::allocator<struct SystemPosition> > {lvalue},unsigned int,double,double)
    
    :param arg:
    :type arg: SystemPositionVec
    :param number:
    :type number: int
    :param floating_number1:
    :type floating_number1: float
    :param floating_number2:
    :type floating_number2: float
    :rtype None
    """
    return None


def empire_add_ship_design(number, string):
    """
    C++ signature:
        void empire_add_ship_design(int,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param number:
    :type number: int
    :param string:
    :type string: str
    :rtype None
    """
    return None


def empire_set_homeworld(number1, number2, string):
    """
    C++ signature:
        bool empire_set_homeworld(int,int,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :param string:
    :type string: str
    :rtype bool
    """
    return bool()


def empire_set_name(number, string):
    """
    C++ signature:
        void empire_set_name(int,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param number:
    :type number: int
    :param string:
    :type string: str
    :rtype None
    """
    return None


def empire_unlock_item(number, arg, string):
    """
    C++ signature:
        void empire_unlock_item(int,enum UnlockableItemType,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param number:
    :type number: int
    :param arg:
    :type arg: unlockableItemType
    :param string:
    :type string: str
    :rtype None
    """
    return None


def galaxy_shape_mod_to_planet_size_dist(arg1, arg2):
    """
    C++ signature:
        int galaxy_shape_mod_to_planet_size_dist(enum Shape,enum PlanetSize)
    
    :param arg1:
    :type arg1: galaxyShape
    :param arg2:
    :type arg2: planetSize
    :rtype int
    """
    return int()


def generate_sitrep(number, string1, arg, string2):
    """
    C++ signatures:
        void generate_sitrep(int,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class boost::python::dict,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        void generate_sitrep(int,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param number:
    :type number: int
    :param string1:
    :type string1: str
    :param arg:
    :type arg: dict
    :param string2:
    :type string2: str
    :rtype None
    """
    return None


def generate_starlanes(arg):
    """
    C++ signature:
        void generate_starlanes(enum GalaxySetupOption)
    
    :param arg:
    :type arg: galaxySetupOption
    :rtype None
    """
    return None


def get_all_objects():
    """
    C++ signature:
        class boost::python::list get_all_objects()
    :rtype list
    """
    return list()


def get_all_specials():
    """
    C++ signature:
        class boost::python::list get_all_specials()
    :rtype list
    """
    return list()


def get_all_species():
    """
    C++ signature:
        class boost::python::list get_all_species()
    :rtype list
    """
    return list()


def get_galaxy_setup_data():
    """
    C++ signature:
        struct GalaxySetupData get_galaxy_setup_data()
    :rtype galaxySetupData
    """
    return galaxySetupData()


def get_name(number):
    """
    C++ signature:
        class boost::python::api::object get_name(int)
    
    :param number:
    :type number: int
    :rtype object
    """
    return object()


def get_native_species():
    """
    C++ signature:
        class boost::python::list get_native_species()
    :rtype list
    """
    return list()


def get_owner(number):
    """
    C++ signature:
        int get_owner(int)
    
    :param number:
    :type number: int
    :rtype int
    """
    return int()


def get_playable_species():
    """
    C++ signature:
        class boost::python::list get_playable_species()
    :rtype list
    """
    return list()


def get_pos(number):
    """
    C++ signature:
        class boost::python::tuple get_pos(int)
    
    :param number:
    :type number: int
    :rtype tuple
    """
    return tuple()


def get_universe_width():
    """
    C++ signature:
        double get_universe_width()
    :rtype float
    """
    return float()


def get_x(number):
    """
    C++ signature:
        double get_x(int)
    
    :param number:
    :type number: int
    :rtype float
    """
    return float()


def get_y(number):
    """
    C++ signature:
        double get_y(int)
    
    :param number:
    :type number: int
    :rtype float
    """
    return float()


def invalid_object():
    """
    C++ signature:
        int invalid_object()
    :rtype int
    """
    return int()


def invalid_position():
    """
    C++ signature:
        double invalid_position()
    :rtype float
    """
    return float()


def irregular_galaxy_positions(arg, number, floating_number1, floating_number2):
    """
    C++ signature:
        void irregular_galaxy_positions(class std::vector<struct SystemPosition,class std::allocator<struct SystemPosition> > {lvalue},unsigned int,double,double)
    
    :param arg:
    :type arg: SystemPositionVec
    :param number:
    :type number: int
    :param floating_number1:
    :type floating_number1: float
    :param floating_number2:
    :type floating_number2: float
    :rtype None
    """
    return None


def jump_distance(number1, number2):
    """
    C++ signature:
        int jump_distance(int,int)
    
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :rtype int
    """
    return int()


def large_meter_value():
    """
    C++ signature:
        float large_meter_value()
    :rtype float
    """
    return float()


def linear_distance(number1, number2):
    """
    C++ signature:
        double linear_distance(int,int)
    
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :rtype float
    """
    return float()


def load_fleet_plan_list(string):
    """
    C++ signature:
        class boost::python::list load_fleet_plan_list(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param string:
    :type string: str
    :rtype list
    """
    return list()


def load_item_spec_list(string):
    """
    C++ signature:
        class boost::python::list load_item_spec_list(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param string:
    :type string: str
    :rtype list
    """
    return list()


def load_monster_fleet_plan_list(string):
    """
    C++ signature:
        class boost::python::list load_monster_fleet_plan_list(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param string:
    :type string: str
    :rtype list
    """
    return list()


def max_starlane_length():
    """
    C++ signature:
        int max_starlane_length()
    :rtype int
    """
    return int()


def min_system_separation():
    """
    C++ signature:
        double min_system_separation()
    :rtype float
    """
    return float()


def monster_frequency(arg):
    """
    C++ signature:
        int monster_frequency(enum GalaxySetupOption)
    
    :param arg:
    :type arg: galaxySetupOption
    :rtype int
    """
    return int()


def native_frequency(arg):
    """
    C++ signature:
        int native_frequency(enum GalaxySetupOption)
    
    :param arg:
    :type arg: galaxySetupOption
    :rtype int
    """
    return int()


def orbit_mod_to_planet_size_dist(number, arg):
    """
    C++ signature:
        int orbit_mod_to_planet_size_dist(int,enum PlanetSize)
    
    :param number:
    :type number: int
    :param arg:
    :type arg: planetSize
    :rtype int
    """
    return int()


def orbit_mod_to_planet_type_dist(number, planet_type):
    """
    C++ signature:
        int orbit_mod_to_planet_type_dist(int,enum PlanetType)
    
    :param number:
    :type number: int
    :param planet_type:
    :type planet_type: planetType
    :rtype int
    """
    return int()


def planet_available_foci(number):
    """
    C++ signature:
        class boost::python::list planet_available_foci(int)
    
    :param number:
    :type number: int
    :rtype list
    """
    return list()


def planet_get_focus(number):
    """
    C++ signature:
        class boost::python::api::object planet_get_focus(int)
    
    :param number:
    :type number: int
    :rtype object
    """
    return object()


def planet_get_size(number):
    """
    C++ signature:
        enum PlanetSize planet_get_size(int)
    
    :param number:
    :type number: int
    :rtype planetSize
    """
    return planetSize()


def planet_get_species(number):
    """
    C++ signature:
        class boost::python::api::object planet_get_species(int)
    
    :param number:
    :type number: int
    :rtype object
    """
    return object()


def planet_get_type(number):
    """
    C++ signature:
        enum PlanetType planet_get_type(int)
    
    :param number:
    :type number: int
    :rtype planetType
    """
    return planetType()


def planet_make_colony(number1, number2, string, floating_number):
    """
    C++ signature:
        bool planet_make_colony(int,int,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,double)
    
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :param string:
    :type string: str
    :param floating_number:
    :type floating_number: float
    :rtype bool
    """
    return bool()


def planet_make_outpost(number1, number2):
    """
    C++ signature:
        bool planet_make_outpost(int,int)
    
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :rtype bool
    """
    return bool()


def planet_set_focus(number, string):
    """
    C++ signature:
        void planet_set_focus(int,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param number:
    :type number: int
    :param string:
    :type string: str
    :rtype None
    """
    return None


def planet_set_size(number, arg):
    """
    C++ signature:
        void planet_set_size(int,enum PlanetSize)
    
    :param number:
    :type number: int
    :param arg:
    :type arg: planetSize
    :rtype None
    """
    return None


def planet_set_species(number, string):
    """
    C++ signature:
        void planet_set_species(int,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param number:
    :type number: int
    :param string:
    :type string: str
    :rtype None
    """
    return None


def planet_set_type(number, planet_type):
    """
    C++ signature:
        void planet_set_type(int,enum PlanetType)
    
    :param number:
    :type number: int
    :param planet_type:
    :type planet_type: planetType
    :rtype None
    """
    return None


def planet_size_mod_to_planet_type_dist(arg, planet_type):
    """
    C++ signature:
        int planet_size_mod_to_planet_type_dist(enum PlanetSize,enum PlanetType)
    
    :param arg:
    :type arg: planetSize
    :param planet_type:
    :type planet_type: planetType
    :rtype int
    """
    return int()


def remove_special(number, string):
    """
    C++ signature:
        void remove_special(int,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param number:
    :type number: int
    :param string:
    :type string: str
    :rtype None
    """
    return None


def ring_galaxy_calc_positions(arg, number, floating_number1, floating_number2):
    """
    C++ signature:
        void ring_galaxy_calc_positions(class std::vector<struct SystemPosition,class std::allocator<struct SystemPosition> > {lvalue},unsigned int,double,double)
    
    :param arg:
    :type arg: SystemPositionVec
    :param number:
    :type number: int
    :param floating_number1:
    :type floating_number1: float
    :param floating_number2:
    :type floating_number2: float
    :rtype None
    """
    return None


def roman_number(number):
    """
    C++ signature:
        class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > roman_number(unsigned int)
    
    :param number:
    :type number: int
    :rtype str
    """
    return str()


def set_name(number, string):
    """
    C++ signature:
        void set_name(int,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param number:
    :type number: int
    :param string:
    :type string: str
    :rtype None
    """
    return None


def set_universe_width(floating_number):
    """
    C++ signature:
        void set_universe_width(double)
    
    :param floating_number:
    :type floating_number: float
    :rtype None
    """
    return None


def special_has_location(string):
    """
    C++ signature:
        bool special_has_location(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param string:
    :type string: str
    :rtype bool
    """
    return bool()


def special_location(string, number):
    """
    C++ signature:
        bool special_location(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,int)
    
    :param string:
    :type string: str
    :param number:
    :type number: int
    :rtype bool
    """
    return bool()


def special_spawn_limit(string):
    """
    C++ signature:
        int special_spawn_limit(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param string:
    :type string: str
    :rtype int
    """
    return int()


def special_spawn_rate(string):
    """
    C++ signature:
        double special_spawn_rate(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param string:
    :type string: str
    :rtype float
    """
    return float()


def specials_frequency(arg):
    """
    C++ signature:
        int specials_frequency(enum GalaxySetupOption)
    
    :param arg:
    :type arg: galaxySetupOption
    :rtype int
    """
    return int()


def species_add_homeworld(string, number):
    """
    C++ signature:
        void species_add_homeworld(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,int)
    
    :param string:
    :type string: str
    :param number:
    :type number: int
    :rtype None
    """
    return None


def species_can_colonize(string):
    """
    C++ signature:
        bool species_can_colonize(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param string:
    :type string: str
    :rtype bool
    """
    return bool()


def species_get_planet_environment(string, planet_type):
    """
    C++ signature:
        enum PlanetEnvironment species_get_planet_environment(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,enum PlanetType)
    
    :param string:
    :type string: str
    :param planet_type:
    :type planet_type: planetType
    :rtype planetEnvironment
    """
    return planetEnvironment()


def species_preferred_focus(string):
    """
    C++ signature:
        class boost::python::api::object species_preferred_focus(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param string:
    :type string: str
    :rtype object
    """
    return object()


def species_remove_homeworld(string, number):
    """
    C++ signature:
        void species_remove_homeworld(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,int)
    
    :param string:
    :type string: str
    :param number:
    :type number: int
    :rtype None
    """
    return None


def spiral_galaxy_calc_positions(arg, number1, number2, floating_number1, floating_number2):
    """
    C++ signature:
        void spiral_galaxy_calc_positions(class std::vector<struct SystemPosition,class std::allocator<struct SystemPosition> > {lvalue},unsigned int,unsigned int,double,double)
    
    :param arg:
    :type arg: SystemPositionVec
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :param floating_number1:
    :type floating_number1: float
    :param floating_number2:
    :type floating_number2: float
    :rtype None
    """
    return None


def star_type_mod_to_planet_size_dist(arg1, arg2):
    """
    C++ signature:
        int star_type_mod_to_planet_size_dist(enum StarType,enum PlanetSize)
    
    :param arg1:
    :type arg1: starType
    :param arg2:
    :type arg2: planetSize
    :rtype int
    """
    return int()


def star_type_mod_to_planet_type_dist(arg, planet_type):
    """
    C++ signature:
        int star_type_mod_to_planet_type_dist(enum StarType,enum PlanetType)
    
    :param arg:
    :type arg: starType
    :param planet_type:
    :type planet_type: planetType
    :rtype int
    """
    return int()


def sys_add_starlane(number1, number2):
    """
    C++ signature:
        void sys_add_starlane(int,int)
    
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :rtype None
    """
    return None


def sys_get_num_orbits(number):
    """
    C++ signature:
        int sys_get_num_orbits(int)
    
    :param number:
    :type number: int
    :rtype int
    """
    return int()


def sys_get_planets(number):
    """
    C++ signature:
        class boost::python::list sys_get_planets(int)
    
    :param number:
    :type number: int
    :rtype list
    """
    return list()


def sys_get_star_type(number):
    """
    C++ signature:
        enum StarType sys_get_star_type(int)
    
    :param number:
    :type number: int
    :rtype starType
    """
    return starType()


def sys_get_starlanes(number):
    """
    C++ signature:
        class boost::python::list sys_get_starlanes(int)
    
    :param number:
    :type number: int
    :rtype list
    """
    return list()


def sys_remove_starlane(number1, number2):
    """
    C++ signature:
        void sys_remove_starlane(int,int)
    
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :rtype None
    """
    return None


def sys_set_star_type(number, arg):
    """
    C++ signature:
        void sys_set_star_type(int,enum StarType)
    
    :param number:
    :type number: int
    :param arg:
    :type arg: starType
    :rtype None
    """
    return None


def universe_age_mod_to_star_type_dist(arg1, arg2):
    """
    C++ signature:
        int universe_age_mod_to_star_type_dist(enum GalaxySetupOption,enum StarType)
    
    :param arg1:
    :type arg1: galaxySetupOption
    :param arg2:
    :type arg2: starType
    :rtype int
    """
    return int()


def user_string(string):
    """
    C++ signature:
        class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > user_string(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    
    :param string:
    :type string: str
    :rtype str
    """
    return str()
