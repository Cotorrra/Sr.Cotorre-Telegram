import os

import requests
import telegram.ext
from dotenv import load_dotenv
from telegram import InputTextMessageContent, InlineQueryResultArticle
from telegram.ext import CommandHandler, MessageHandler, Filters, InlineQueryHandler

from backs.search import resolve_back_search
from core.resolve import resolve_search
from core.search import card_search
from decks.deck import extract_deck_info
from decks.formating import format_deck
from decks.search import find_deck, search_for_upgrades
from e_cards.search import use_ec_keywords
from p_cards.search import use_pc_keywords

load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')
updater = telegram.ext.Updater(TOKEN)
dispatcher = updater.dispatcher

ah_all_cards = requests.get('https://es.arkhamdb.com/api/public/cards?encounter=1').json()

ah_player = requests.get('https://es.arkhamdb.com/api/public/cards?encounter=0').json()

# Encounter p_cards include: Special player p_cards, Weaknesses, enemies, acts, plans, etc.
ah_encounter = [c for c in ah_all_cards if "spoiler" in c]

raw_text = False
LISTENING = 0


def send_help(update, context):
    res = "¿Necesitas ayuda?: \n" \
          "(En general funcional igual que la versión de Discord) \n" \
          "\n- !ah [nombre] ~[subtitulo]~ ([extra]): Busca cartas en ArkhamDB.\n" \
          "[extra] puede contener ser lo siguiente: '0-5' nivel de la carta, " \
          "'G/B/R/M/S/N' la clase de la carta, P para permanente, U para único, E para excepcional, " \
          "C para característica.\n" \
          "Por ejemplo: \"!ahj Whisky (3S)\" devolverá el Whisky de Mosto Ácido de Supervivente de nivel 3. \n" \
          "\n- !ahm [nombre] ~[subtitulo]~: Busca cartas de encuentros (lugares, actos, escenarios, etc.) que no " \
          "sean cartas de jugador estándar. (¡Spoilers!) \n" \
          "\n- !ahback [nombre] ~[subtitulo]~ ([extra]): Muestra la parte de atrás de ciertas cartas que lo permiten." \
          "\n" \
          "El [extra] de !ahback y !ahm permiten buscar cartas por tipo: S: Escenario, A: Acto, P: Plan, T: Traicion," \
          "E: Enemigo, L: Lugar y J: Por cartas de jugador de encuentros." \
          "\n- !ahd [numero]: Busca en ArkhamDB el mazo dado y lo muestra, tanto público como privado.\n" \
          "Por el momento estos comandos sólo se pueden hacer mientras haces un @SrCotorre_bot \n" \

    update.message.reply_text(res)


def look_for_card_back(query):
    f_cards = [c for c in ah_all_cards if c["double_sided"]]
    r_cards = card_search(query, f_cards, use_ec_keywords)

    return resolve_back_search(r_cards)


def look_for_player_card(query):
    r_cards = card_search(query, ah_player, use_pc_keywords)
    return resolve_search(r_cards)


def look_for_deck(code):
    deck = find_deck(code)
    if not deck:
        response = ""
        title = "Mazo no encontrado"
    else:
        deck_info = extract_deck_info(deck, ah_all_cards)
        response, title = format_deck(deck, deck_info)

    return [response], [code], [title]


def look_for_encounter(query):
    r_cards = card_search(query, ah_encounter, use_ec_keywords)
    return resolve_search(r_cards)


# def look_for_upgrades(query):
#   return search_for_upgrades(query, ah_player)


def handle_query(command, query):
    response = ""
    if command == "!ahj":
        return look_for_player_card(query)

    elif command == "!ahe":
        return look_for_encounter(query)

    elif command == "!ahd":
        return look_for_deck(query)

    elif command == "!ahback":
        return look_for_card_back(query)

    else:
        return response, "00000", "Sin resultados"


def inline_fun(update, context):
    msg = update.inline_query.query
    print(msg)
    command = msg.split()[0]
    query = ' '.join(msg.split()[1:])
    responses, codes, titles = handle_query(command, query)

    results = list()
    for i in range(len(responses)):
        results.append(
            InlineQueryResultArticle(
                id=codes[i],
                title=titles[i],
                input_message_content=InputTextMessageContent(responses[i],
                                                              parse_mode=telegram.ParseMode.HTML)
            )
        )

    context.bot.answer_inline_query(update.inline_query.id, results)


# dispatcher.add_handler(CommandHandler("start", start_func))
dispatcher.add_handler(CommandHandler("help", send_help))
# dispatcher.add_handler(MessageHandler(Filters.text, handle_text))
# dispatcher.add_error_handler(error_func)
# add an handler for normal text (not commands)
inline_handler = InlineQueryHandler(inline_fun)
dispatcher.add_handler(inline_handler)

updater.start_polling()
updater.idle()
