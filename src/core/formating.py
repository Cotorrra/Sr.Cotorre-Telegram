
def create_embed(c, title, description, footnote=""):
    # TODO: Write this code
    url = "https://es.arkhamdb.com/card/%s" % c['code']
    # embed = "" # discord.Embed(title=title, description=description, color=color_picker(c), url=url)
        # embed.set_footer(text=footnote)
    # set_thumbnail_image(c, embed)
    text = f"**{title}**\n" \
           f"{description}"
    if footnote:
        text += f"{footnote}"

    return text


def format_text(text):
    text_format = {"[free]": "⚡",
                   "[fast]": "⚡",
                   "[elder_sign]": "[Arcano]",
                   "[willpower]": "🗣",
                   "[combat]": "👊",
                   "[intellect]": "📙",
                   "[agility]": "👟",
                   "[action]": "➡",
                   "[reaction]": "↪",
                   "[bless]": "[Bendición]",
                   "[curse]": "[Maldición]",
                   "[wild]": "❔",
                   "[skull]": "[Cráneo]",
                   "[cultist]": "[Sectario]",
                   "[tablet]": "[Tablilla]",
                   "[elder_thing]": "[Antiguo]",
                   "[auto_fail]": "[Fracaso Auto.]",
                   "[mystic]": "🟣",
                   "[seeker]": "🟠",
                   "[guardian]": "🔵",
                   "[rogue]": "🟢",
                   "[survivor]": "🔴",
                   "[neutral]": "⚪",
                   "[mythos]": "⚫",
                   "[health]": "❤",
                   "[sanity]": "🧠",
                   "[per_investigator]": "[Por Investigador]",
                   "[doom]": "[Perdición]",
                   "[clues]": "[Pistas]",
                   "</b>": "**",
                   "<b>": "**",
                   "<em>": "__",
                   "</em>": "__",
                   "<i>": "__",
                   "</i>": "__",
                   "<u>": "__",
                   "</u>": "__",
                   "[[": "**",
                   "]]": "**",
                   "<cite>": "\n— ",
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


def format_illus_pack(c, only_pack=False):
    formater = {"pack": format_set(c),
                "artist": "%s \n" % format_illustrator(c) if c['type_code'] != "scenario" else ""
                }
    if only_pack:
        return "%(pack)s" % formater
    else:
        return "%(artist)s" \
               "%(pack)s" % formater


def format_victory(c, override_spoiler=False):
    if "victory" in c:
        text = "**Victoria %s.**" % c['victory']
        return "%s \n" % text
    else:
        return ""


def format_vengeance(c, override_spoiler=False):
    if "vengeance" in c:
        text = "**Venganza %s.**" % c['vengeance']
        return "%s \n" % text
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


def set_thumbnail_image(c, embed, back=False):
    if "imagesrc" in c:
        if back:
            if "backimagesrc" in c:
                embed.set_thumbnail(url="https://arkhamdb.com%s" % c["backimagesrc"])
            else:
                embed.set_thumbnail(url="https://arkhamdb.com%s" % c["imagesrc"])
        else:
            embed.set_thumbnail(url="https://arkhamdb.com%s" % c["imagesrc"])


def format_illustrator(c):
    return "🖌 %s" % c['illustrator']


def format_name(c):
    return "*%s" % c['name'] if c['is_unique'] else "%s" % c['name']


def format_subtext(c):
    return ": _%s_" % c['subname'] if 'subname' in c else ""


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

