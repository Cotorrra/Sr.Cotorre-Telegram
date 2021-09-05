from src.core.formating import format_text, format_number, color_picker
from src.core.search import find_by_id


def format_xp(c):
    if "xp" in c:
        if c['xp'] == 0:
            text = ""
        elif c['exceptional']:
            text = " (%sE)" % c['xp']
        else:
            text = " (%s)" % c['xp']
    else:
        text = ""
    return text


def format_slot(c):
    formater = {
        "Accessory.": "Accesorio",
        "Ally.": "Aliado",
        "Arcane.": "Arcano",
        "Arcane x2.": "Dos Arcanos",
        "Body.": "Cuerpo",
        "Hand.": "Mano",
        "Hand x2.": "Dos Manos",
        "Tarot.": "Tarot"
    }
    text = ""
    if "real_slot" in c:
        for key, value in formater.items():
            traits = c["real_slot"] + "."
            if key in traits:
                text += value

    return text


def format_inv_skills(c):
    formater = {
        "will": "[willpower] %s " % c['skill_willpower'] if "skill_willpower" in c else "",
        "int": "[intellect] %s " % c['skill_intellect'] if "skill_intellect" in c else "",
        "com": "[combat] %s " % c['skill_combat'] if "skill_combat" in c else "",
        "agi": "[agility] %s" % c['skill_agility'] if "skill_agility" in c else "",
    }
    return format_text("%(will)s%(int)s%(com)s%(agi)s" % formater)


def format_skill_icons(c):
    formater = {
        "will": "[willpower]" * c['skill_willpower'] if "skill_willpower" in c else "",
        "int": "[intellect]" * c['skill_intellect'] if "skill_intellect" in c else "",
        "com": "[combat]" * c['skill_combat'] if "skill_combat" in c else "",
        "agi": "[agility]" * c['skill_agility'] if "skill_agility" in c else "",
        "wild": "[wild]" * c['skill_wild'] if "skill_wild" in c else "",
    }
    return format_text("%(will)s%(int)s%(com)s%(agi)s%(wild)s" % formater)


def format_health_sanity(c):
    return format_text("%s%s" % ("[health] %s " % format_number(c['health']) if "health" in c else "",
                                 "[sanity] %s" % format_number(c['sanity']) if "sanity" in c else ""))


def get_color_by_investigator(deck, cards):
    inv_id = deck['investigator_code']
    inv_card = find_by_id(inv_id, cards)
    return color_picker(inv_card)


def format_sub_text_short(c):
    if 'real_text' in c:
        if "subname" in c and "Campaign Log" in c['real_text']:
            return ": __%s__" % c['subname']
    return ""
