from src.p_cards.formating import format_player_card_deck


def format_assets(arr, title):
    text = ""
    if arr:
        text += "<i>%s:</i>" % title
        aux = []
        for (c, q) in arr:
            aux.append(format_player_card_deck(c, q))
        aux = sorted(aux)
        for c in aux:
            text += "\n- %s" % c[1:]
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
                "xp": "Experiencia necesaria: %s" % str(info['xp']),
                "assets": "Apoyos: (%s)" % str(info["assets_q"]) if info['assets_q'] > 0 else "",
                "events": "Eventos: (%s)" % str(info["events_q"]) if info['events_q'] > 0 else "",
                "skills": "Habilidades: (%s)" % str(info["skills_q"]) if info['skills_q'] > 0 else "",
                "treachery": "Traiciones/Enemigos: (%s)" % str(info["treachery_q"]) if info['treachery_q'] > 0 else "",
                }

    text = "%(name)s \n" \
           "%(investigator)s \n" \
           "%(xp)s \n\n" % formater

    if info['assets_q'] > 0:
        text += "%(assets)s \n" % formater
        text += format_all_assets(info)
        text += "\n"
    if info['events_q'] > 0:
        text += "%(events)s \n" % formater
        text += format_list_of_cards(info['events'])
        text += "\n"
    if info['skills_q'] > 0:
        text += "%(skills)s \n" % formater
        text += format_list_of_cards(info['skills'])
        text += "\n"
    if info['treachery_q'] > 0:
        text += "%(treachery)s \n" % formater
        text += format_list_of_cards(info['treachery'])
        text += "\n"
    if deck['user_id']:
        url = "https://es.arkhamdb.com/decklist/view/%s" % deck['id']
    else:
        url = "https://es.arkhamdb.com/deck/view/%s" % deck['id']
    text += f"Mazo en ArkhamDB: {url}"
    return text


def format_upgraded_deck(deck1, info):
    formater = {"name": "%s" % deck1['name'],
                "investigator": "<i>Mazo para %s</i>" % deck1['investigator_name'],
                "xp": "Experiencia utilizada: %s" % str(info['xp_diff']),
                }

    text = "%(name)s" \
           "%(investigator)s \n" \
           "%(xp)s\n\n" % formater

    if len(info['buys_in']) > 0:
        text += "Cartas añadidas:"
        text += format_list_of_cards_upgr(info["buys_in"])
        text += "\n"
    if len(info['buys_out']) > 0:
        text += "Cartas retiradas:"
        text += format_list_of_cards_upgr(info["buys_out"])
        text += "\n"
    if deck1['user_id']:
        url = "https://es.arkhamdb.com/decklist/view/%s" % deck1['id']
    else:
        url = "https://es.arkhamdb.com/deck/view/%s" % deck1['id']
    text += f"\nMazo en ArkhamDB: {url}"
    return text


def format_list_of_cards_upgr(arr):
    copy_arr = arr.copy()
    array = []

    while len(copy_arr) > 0:
        q = 0
        card = copy_arr[0]
        while card in copy_arr:
            q += 1
            copy_arr.remove(card)

        text = format_player_card_deck(card, q)
        array.append(text)
    array = sorted(array)
    text = ""
    for c in array:
        text += "\n- %s" % c[1:]

    return text


def format_list_of_cards(arr):
    text = ""
    aux = []
    for (c, q) in arr:
        aux.append(format_player_card_deck(c, q))
    aux = sorted(aux)
    for c in aux:
        text += "- %s\n" % c[1:]
    return text
