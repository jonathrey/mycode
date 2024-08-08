""" Room configuration for the RPG game."""

rooms = {
    "Hall": {
        "south": "Kitchen",
        "east": "Dining Room",
        "west": "Library",
        "down": "Basement",
        "item": "key"
    },
    "Kitchen": {
        "north": "Hall",
        "item": "monster"
    },
    "Dining Room": {
        "west": "Hall",
        "south": "Garden",
        "item": "potion"
    },
    "Garden": {
        "north": "Dining Room"
    },
    "Library": {
        "east": "Hall",
        "item": "book"
    },
    "Basement": {
        "up": "Hall",
        "item": "shield"
    }
}

