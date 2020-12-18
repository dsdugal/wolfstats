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
    "goombas",
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
    "team_gibs",
    "team_kills"
]

DEFAULT_HEADERS = {
    "guid": 0,
    "team": 1,
    "start_time": 2,
    "end_time": 3
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
    1: "allies",
    2: "axis"
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

WSTAT_HEADERS = [
    "kills",
    "deaths",
    "suicides",
    "damage",
    "damage_received",
    "team_kills",
    "team_deaths"
    "team_damage_given"
    "team_damage_received"
    "shots",
    "hits",
    "headshots",
    "accuracy",
    "headshot_accuracy"
]
