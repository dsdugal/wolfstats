"""
x
"""

# Constants

CATEGORY_HEADERS = [
    "ammo_given",
    "damage_given",
    "damage_received",
    "dynamite_defused",
    "dynamite_planted",
    "deaths",
    "flags_captured",
    "gibs",
    "health_given",
    "kills",
    "obj_captured",
    "obj_destroyed",
    "obj_returned",
    "obj_taken",
    "revives",
    "suicides",
    "team_damage_given",
    "team_damage_received",
    "team_deaths",
    "team_kills"
]

DEFAULT_HEADERS = {
    "guid": 0,
    "alias": 1,
    "team": 2,
    "start_time": 3,
    "end_time": 4
}

EVENT_GROUPS = []

EVENT_LABELS = []

GAMETYPES = {
    5: "objective",
    6: "stopwatch"
}

RELEASE_TIME = 1609459200 # ???

ROUNDS = {
    1: "A",
    2: "B"
}

TEAMS = {
    "allies": 1,
    "axis": 2
}

WEAPONS = [
    "airstrike",
    "artillery",
    "colt",
    "dynamite",
    "flamethrower"
    "goomba",
    "grenade",
    "knife",
    "luger",
    "mauser",
    "mg42",
    "mp40",
    "panzerfaust",
    "sten",
    "thompson",
    "venom",
]