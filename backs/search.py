from backs.formating import format_general_card_b, format_location_card_b, format_inv_card_b
from e_cards.formating import format_scenario_card, format_scenario_card_short, format_location_card_short, \
    format_agenda_card_f_short, format_act_card_f_short, format_treachery_card_short, format_enemy_card_short
from p_cards.formating import format_player_card, format_player_card_short, format_inv_card_f_short


def resolve_back_search(r_cards):
    responses = []
    titles = []
    ids = []
    for c in r_cards:
        if c['type_code'] == "investigator":
            text = "¡Carta de Investigador encontrada!\n"
            text += format_inv_card_b(c)
            titles.append(format_inv_card_f_short(c))

        elif c['type_code'] == "enemy":
            text = "¡Carta de Enemigo encontrada!\n"
            text += format_general_card_b(c)
            titles.append(format_enemy_card_short(c))

        elif c['type_code'] == "treachery":
            text = "¡Carta de Traición encontrada!\n"
            text += format_general_card_b(c)
            titles.append(format_treachery_card_short(c))

        elif c['type_code'] == 'act':
            text = "¡Carta de Acto encontrada!\n"
            text += format_general_card_b(c)
            titles.append(format_act_card_f_short(c))

        elif c['type_code'] == 'agenda':
            text = "¡Carta de Plan encontrada!\n"
            text += format_general_card_b(c)
            titles.append(format_agenda_card_f_short(c))

        elif c['type_code'] == 'location':
            text = "¡Carta de Lugar encontrada!\n"
            text += format_location_card_b(r_cards[0])
            titles.append(format_location_card_short(c))

        elif c['type_code'] == 'scenario':
            text = "¡Carta de Escenario encontrada!\n"
            text += format_scenario_card(c)
            titles.append(format_scenario_card_short(c))
        else:
            text = "¡Carta de Jugador encontrada!\n"
            text += format_player_card(c)
            titles.append(format_player_card_short(c))

        responses.append(text)
        ids.append(c['code'])

    return responses, ids, titles
