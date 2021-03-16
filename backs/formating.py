from core.formating import format_faction, format_name, format_subtext, format_card_text, format_illustrator, \
    format_set, color_picker


def format_inv_card_b(c):
    formater = {"class": format_faction(c),
                "name": format_name(c),
                "subname": format_subtext(c),
                "deck_req": "%s \n" % format_card_text(c, "back_text") if "back_text" in c else "",
                "artist": format_illustrator(c),
                "pack": format_set(c),
                "flavour": "<i>%s</i>\n" % c['back_flavor'] if "back_flavor" in c else "",
                }
    text = "%(class)s %(name)s %(subname)s " \
           "%(deck_req)s \n" \
           "%(flavour)s" \
           "%(artist)s \n" \
           "%(pack)s" % formater

    return text


def format_location_card_b(c):
    formater = {"name": format_name(c),
                "back": "%s \n" % format_card_text(c, "back_text") if "back_text" in c else "",
                "artist": format_illustrator(c),
                "pack": format_set(c),
                "flavour": "<i>%s</i>\n" % c['back_flavor'] if "back_flavor" in c else "",
                }
    text = "%(name)s" \
           "%(back)s \n" \
           "%(flavour)s" \
           "%(artist)s \n" \
           "%(pack)s" % formater

    return text


def format_general_card_b(c):
    formater = {"name": format_name(c),
                "subname": format_subtext(c),
                "back": "%s \n" % format_card_text(c, "back_text") if "back_text" in c else "",
                "pack": format_set(c),
                "flavour": "<i>%s</i>\n" % c['back_flavor'] if "back_flavor" in c else "",
                }
    text = "%(name)s %(subname)s" \
           "%(back)s \n" \
           "%(flavour)s" \
           "%(pack)s" % formater

    return text
