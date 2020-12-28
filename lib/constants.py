"""
x
"""

RELEASE_TIME = 1609459200 # ???

SUPPORTED_FORMAT = "json"

SUPPORTED_SCHEMAS = [
    0.1
]

DEFAULT_GAMETYPE = "Unknown"

EVENT_GROUPS = []

EVENT_LABELS = []

GAMETYPES = {
    5: "objective",
    6: "stopwatch"
}

DEFAULT_HEADERS = [
    "guid",
    "alias",
    "start_time",
    "end_time"
]

STAT_HEADERS = [
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

WSTAT_HEADERS = [
    "kills",
    "deaths",
    "suicides",
    "damage",
    "damage_received",
    "team_kills",
    "team_deaths",
    "team_damage_given",
    "team_damage_received",
    "shots",
    "hits",
    "headshots",
]

LINE_BREAK = "-" * 225 + "\n"

PLACEHOLDER = "-"

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