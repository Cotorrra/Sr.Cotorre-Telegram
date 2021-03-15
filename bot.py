import os
import telegram
import telegram.ext
import requests
from dotenv import load_dotenv
from telegram.ext import CommandHandler, MessageHandler, Filters, InlineQueryHandler

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


def handle_text(update, context):
    text_received = update.message.text
    update.message.reply_text(f'did you said "{text_received}" ?')


def send_help(update, context):
    res = "¿Necesitas ayuda?: \n" \
          "\n- !ahj [nombre] ~[subtitulo]~ ([extra]): Busca cartas en ArkhamDB.\n" \
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
          "\n- !ahu [numero] [numero] Busca en ArkhamDB ambos mazos y muestra las mejoras realizadas en los mazos." \
          "Si mejoraste el mazo con ArkhamDB puedes también entregarle sólo el número del mazo más reciente."
    update.message.reply_text(res)


"""
def look_for_card_back(ctx):

    query = ' '.join(ctx.message.content.split()[1:])

    f_cards = [c for c in ah_all_cards if c["double_sided"]]
    r_cards = card_search(query, f_cards, use_ec_keywords)

    response = resolve_back_search(r_cards)

    return response

def look_for_player_card(ctx):
    query = ' '.join(ctx.message.content.split()[1:])

    r_cards = card_search(query, ah_player, use_pc_keywords)

    response = resolve_search(r_cards)

    return response


def look_for_deck(ctx, code: str):
    deck = find_deck(code)
    if not deck:
        response = "Mazo no encontrado"
        await ctx.send(response)
    else:
        deck_info = extract_deck_info(deck, ah_all_cards)
        embed = format_deck(deck, deck_info)
        response = "¡Mazo Encontrado!"

    return response


def look_for_encounter(message):
    query = ' '.join(ctx.message.content.split()[1:])

    r_cards = card_search(query, ah_encounter, use_ec_keywords)
    response, embed = resolve_search(r_cards)

    if embed:
        await ctx.send(response, embed=embed)
    else:
        await ctx.send(response)


def look_for_upgrades(message):
    query = ctx.message.content.split()[1:]

    response, embed = search_for_upgrades(query, ah_player)
    if embed:
        await ctx.send(response, embed=embed)
    else:
        await ctx.send(response)
 
"""


def error_func(update, context):
    update.message.reply_text("Hubo un error :c")


def start_func(update, context):
    update.message.reply_text('Sr. "Co-Torre" está preparado c:')

def inline_

dispatcher.add_handler(CommandHandler("start", start_func))
dispatcher.add_handler(CommandHandler("help", send_help))
dispatcher.add_error_handler(error_func)

# add an handler for normal text (not commands)
dispatcher.add_handler(MessageHandler(Filters.text, handle_text))
inline_handler = InlineQueryHandler()
dispatcher.add_handler(inline_handler)

updater.start_polling()
updater.idle()

