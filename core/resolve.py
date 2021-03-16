from e_cards.formating import format_enemy_card, format_treachery_card, format_act_card_f, format_agenda_card_f, \
    format_location_card_f, format_scenario_card, format_enemy_card_short, format_treachery_card_short, \
    format_location_card_short, format_act_card_f_short, format_agenda_card_f_short, format_scenario_card_short
from p_cards.formating import format_inv_card_f, format_player_card, format_inv_card_f_short, format_player_card_short


def resolve_search(r_cards):
    responses = []
    titles = []
    ids = []
    for c in r_cards:
        if c['type_code'] == "investigator":
            text = "¡Carta de Investigador encontrada!\n"
            text += format_inv_card_f(c)
            titles.append(format_inv_card_f_short(c)[1:])

        elif c['type_code'] == "enemy":
            text = "¡Carta de Enemigo encontrada!\n"
            text += format_enemy_card(c)
            titles.append(format_enemy_card_short(c)[1:])

        elif c['type_code'] == "treachery":
            text = "¡Carta de Traición encontrada!\n"
            text += format_treachery_card(c)
            titles.append(format_treachery_card_short(c)[1:])

        elif c['type_code'] == 'act':
            text = "¡Carta de Acto encontrada!\n"
            text += format_act_card_f(c)
            titles.append(format_act_card_f_short(c)[1:])

        elif c['type_code'] == 'agenda':
            text = "¡Carta de Plan encontrada!\n"
            text += format_agenda_card_f(c)
            titles.append(format_agenda_card_f_short(c)[1:])

        elif c['type_code'] == 'location':
            text = "¡Carta de Lugar encontrada!\n"
            text += format_location_card_f(c)
            titles.append(format_location_card_short(c)[1:])

        elif c['type_code'] == 'scenario':
            text = "¡Carta de Escenario encontrada!\n"
            text += format_scenario_card(c)
            titles.append(format_scenario_card_short(c)[1:])
        else:
            text = "¡Carta de Jugador encontrada!\n"
            text += format_player_card(c)
            titles.append(format_player_card_short(c)[1:])

        responses.append(text)
        ids.append(c['code'])

    return responses, ids, titles
