

def format_text(text):
    text_format = {"[free]": "🗲",
                   "[fast]": "🗲",
                   "[elder_sign]": "🌟",
                   "[willpower]": "🗣",
                   "[combat]": "🤜",
                   "[intellect]": "📙",
                   "[agility]": "👟",
                   "[action]": "➡",
                   "[reaction]": "↩",
                   "[bless]": "❇",
                   "[curse]": "☣",
                   "[wild]": "❓",
                   "[skull]": "💀",
                   "[cultist]": "🧕",
                   "[tablet]": "🀄️",
                   "[elder_thing]": "🐙",
                   "[auto_fail]": "🦑",
                   "[mystic]": "🟣",
                   "[seeker]": "🟡",
                   "[guardian]": "🔵",
                   "[rogue]": "🟢",
                   "[survivor]": "🔴",
                   "[neutral]": "⚪",
                   "[mythos]": "⚫",
                   "[health]": "❤",
                   "[sanity]": "🧠",
                   "[per_investigator]": "👤",
                   "[doom]": "☄️",
                   "[clues]": "🔍",
                   # "</b>": "**",
                   # "<b>": "**",
                   "<em>": "<i>",
                   "</em>": "</i>",
                   # "<i>": "_",
                   # "</i>": "_",
                   # "<u>": "__",
                   # "</u>": "__",
                   "[[": "<b>",
                   "]]": "</b>",
                   "<cite>": "\n- ",
                   "</cite>": "",
                   }

    for key, value in text_format.items():
        text = text.replace(key, value)
    return text


def format_set(c):
    text = "%s #%s" % (c['pack_name'], str(c['position']))
    if "encounter_code" in c:
        text += ": %s #%s" % (c['encounter_name'], str(c['encounter_position']))
        if c['quantity'] > 1:
            text += "-%s" % str(c['encounter_position'] + c['quantity'] - 1)
    text += "."
    return text


def format_card_text(c, tag="text"):
    formating = {"\n": "\n"}
    text = format_text(c[tag]) if tag in c else ""
    for key, value in formating.items():
        text = text.replace(key, value)
    return text


def format_victory(c):
    if "victory" in c:
        return "<b>Victoria %s.</b>\n" % c['victory']
    else:
        return ""


def format_vengeance(c):
    if "vengeance" in c:
        return "<b>Venganza %s.</b>\n" % c['vengeance']
    else:
        return ""


def format_number(n):
    if int(n) == -2:
        return "X"
    else:
        return str(n)


def format_faction(c):
    if 'faction2_code' in c:
        return format_text("[%s]/[%s]" % (c['faction_code'], c['faction2_code']))
    else:
        return format_text("[%s]" % c['faction_code'])


faction_order = {
    "guardian": "0",
    "seeker": "1",
    "rogue": "2",
    "mystic": "3",
    "survivor": "4",
    "neutral": "5",
    "mythos": "6",
}


def format_illustrator(c):
    return "🖌 %s" % c['illustrator']


def format_name(c):
    return "<b>*%s</b>" % c['name'] if c['is_unique'] else "%s" % c['name']


def format_subtext(c):
    return ": <i>%s</i>" % c['subname'] if 'subname' in c else ""


def color_picker(c):
    colors = {
        "survivor": 0xcc3038,
        "rogue": 0x107116,
        "guardian": 0x2b80c5,
        "mystic": 0x4331b9,
        "seeker": 0xec8426,
        "neutral": 0x606060,
        "mythos": 0x000000,
    }
    return colors[c['faction_code']]

