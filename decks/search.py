import requests

from decks.deck import check_upgrade_rules
from decks.formating import format_upgraded_deck


def find_deck(code: str):
    link = 'https://es.arkhamdb.com/api/public/deck/%s' % code
    req = requests.get(link)
    if req.url != link:
        link = 'https://es.arkhamdb.com/api/public/decklist/%s' % code
        req = requests.get(link)
        if req.url != link:
            return {}
    return req.json()


def find_former_deck(code: str):
    curr_deck = find_deck(code)
    if curr_deck:
        former_code = str(curr_deck["previous_deck"])
        former_deck = find_deck(former_code)
        if former_deck:
            return former_deck
        else:
            return False
    return False


def search_for_upgrades(query, cards):
    if len(query) >= 2:
        deck1 = find_deck(query[0])
        deck2 = find_deck(query[1])
        if not deck1 or deck2:
            response = "No encontre uno de los mazos."
            code = "0"
            title = "No existe uno de esos mazos."
        else:
            info = check_upgrade_rules(deck1, deck2, cards)
            response = "¡Encontré una Mejora!\n" + format_upgraded_deck(deck1, info)
            code = query[0]
            title = deck1['name']

    elif len(query) == 1:
        deck1 = find_deck(query[0])
        deck2 = find_former_deck(query[0])
        if not deck1:
            response = "No encontré el mazo."
            code = "0"
            title = "No existe ese mazo."
        elif not deck2:
            response = "El Mazo dado no contiene una mejora."
            code = "0"
            title = "No existe ese mazo."
        else:
            info = check_upgrade_rules(deck2, deck1, cards)
            response = "¡Encontré una Mejora!\n" + format_upgraded_deck(deck1, info)
            code = query[0]
            title = deck1['name']

    else:
        response = "Uso de !ahu [numero] [numero] o bien !ahu [numero]"
        code = "0"
        title = "Búsqueda inválida."

    return response, code, title

