from core.formating import format_text
from p_cards.formating import format_inv_card_f_short, format_player_card_short


def format_assets(arr, title):
    text = ""
    if arr:
        text += "<i>%s:</i>" % title
        aux = []
        for (c, q) in arr:
            aux.append(format_player_card_short(c, q))
        aux = sorted(aux)
        for c in aux:
            text += "\n%s" % c[1:]
    return text


def format_all_assets(info):
    types = {"assets_h": "Mano", "assets_h2": "Mano x2", "assets_b": "Cuerpo",
             "assets_acc": "Accesorio", "assets_ar": "Arcano", "assets_ar2": "Arcano x2", "assets_ally": "Aliado",
             "assets_o": "Otros", "permanents": "Permanentes"}
    text = ""
    for key, value in types.items():
        if info[key]:
            text += "%s\n" % format_assets(info[key], value)
    return text


def format_deck(deck, info):
    formater = {"name": "%s" % deck['name'],
                "investigator": "<i>Mazo para %s</i>" % deck['investigator_name'],
                "xp": "Experiencia Necesaria: %s" % str(info['xp']),
                "assets": "Apoyos: (%s)" % str(info["assets_q"]) if info['assets_q'] > 0 else "",
                "events": "Eventos: (%s)" % str(info["events_q"]) if info['events_q'] > 0 else "",
                "skills": "Habilidades: (%s)" % str(info["skills_q"]) if info['skills_q'] > 0 else "",
                "treachery": "Traiciones/Enemigos: (%s)" % str(info["treachery_q"]) if info['treachery_q'] > 0 else "",
                }

    text = "%(name)s \n" \
           "%(investigator)s \n" \
           "%(xp)s \n" % formater

    if info['assets_q'] > 0:
        text += "%(assets)s \n" % formater
        text += format_all_assets(info)

    if info['events_q'] > 0:
        text += "%(events)s \n" % formater
        text += format_list_of_cards(info['events'])

    if info['skills_q'] > 0:
        text += "%(skills)s \n" % formater
        text += format_list_of_cards(info['skills'])

    if info['treachery_q'] > 0:
        text += "%(treachery)s \n" % formater
        text += format_list_of_cards(info['treachery'])

    return text, deck['name']


def format_upgraded_deck(deck1, info):
    formater = {"name": "%s" % deck1['name'],
                "investigator": "<i>Mazo para %s</i>" % deck1['investigator_name'],
                "xp": "Experiencia Utilizada: %s" % str(info['xp_diff']),
                }

    text = "%(name)s" \
           "%(investigator)s \n" \
           "%(xp)s" % formater

    if len(info['buys_out']) > 0:
        text += "Cambios (-):"
        text += format_list_of_cards(info["buys_out"])

    if len(info['buys_in']) > 0:
        text += "Cambios (+):"
        text += format_list_of_cards(info["buys_in"])

    # if in_out_len(info, 'arcane_upg') > 0:
    #   embed.add_field(name="Mejora de Investigación Arcana", value=format_upgrades(info, 'arcane_upg'), inline=False)

    # if len(info['parallel_buy']) > 0:
    #    embed.add_field(name="Mejora Especial (Agnes/Skids)", value=format_special_upgr(info), inline=False)

    # if in_out_len(info, 'adaptable') > 0:
    #    embed.add_field(name="Cambios por Adaptable (-):",
    #                    value=format_list_of_cards(format_in_out_upgr(info, "adaptable")[0]), inline=True)

    #    embed.add_field(name="Cambios por Adaptable (+)",
    #                    value=format_list_of_cards(format_in_out_upgr(info, "adaptable")[1]), inline=True)

    return text, deck1['name']


def format_list_of_cards(arr):
    text = ""
    aux = []
    for (c, q) in arr:
        aux.append(format_player_card_short(c, q))
    aux = sorted(aux)
    for c in aux:
        text += "%s\n" % c[1:]

    return text
