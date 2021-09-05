import logging
import os

import telegram.ext
from dotenv import load_dotenv
from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler

from src.core.utils import make_str_from_args
from src.e_cards.search import format_query_ec
from src.p_cards.search import format_query_pc
from src.response.response import look_for_player_card, look_for_deck, look_for_upgrades, look_for_mythos_card, \
    look_for_faq, look_for_rule, look_for_card_back, look_for_tarot


def ah(update: Update, context: CallbackContext) -> None:
    query = make_str_from_args(context.args) if len(context.args) > 1 else ""
    response = look_for_player_card(query)
    update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)


def mazo(update: Update, context: CallbackContext) -> None:
    try:
        code = context.args[0]
        tipo = context.args[1] if len(context.args) > 1 else ""
        response = look_for_deck(code, tipo)
        update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)

    except (IndexError, ValueError):
        update.message.reply_text("Error: Su uso es /mazo <id> <tipo:deck/decklist (opcional)>")


def mejora(update: Update, context: CallbackContext) -> None:
    try:
        code = context.args[0]
        tipo = context.args[1] if len(context.args) > 1 else ""
        response = look_for_upgrades(code, tipo)
        update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)

    except (IndexError, ValueError):
        update.message.reply_text("Error: Su uso es /mejora <id> <tipo:deck/decklist (opcional)>")


"""
def ahe_s(ctx, nombre, tipo="", subtitulo="", pack=""):
    query = format_query_ec(nombre, tipo, subtitulo, pack)
    response, embed = look_for_mythos_card(query)
    if embed:
        await ctx.send(response, embed=embed)
    else:
        await ctx.send(response)


def ahfaq_s(ctx, nombre, tipo="", subtitulo="", pack=""):
    query = format_query_ec(nombre, tipo, subtitulo, pack)
    response, embed = look_for_faq(query)
    if embed:
        await ctx.send(response, embed=embed)
    else:
        await ctx.send(response)

def ahReglas_s(ctx, regla):
    response, embed = look_for_rule(regla)
    if embed:
        await ctx.send(response, embed=embed)
    else:
        await ctx.send(response)


def ahback_s(ctx, nombre, tipo="", subtitulo="", pack=""):
    query = format_query_ec(nombre, tipo, subtitulo, pack)
    response, embed = look_for_card_back(query)
    if embed:
        await ctx.send(response, embed=embed)
    else:
        await ctx.send(response)
"""


def tarot(update: Update, context: CallbackContext) -> None:
    """Regresa una Carta de Tarot al Azar o bien busca una si le dieron argumentos"""
    query = make_str_from_args(context.args) if len(context.args) > 1 else ""
    response = look_for_tarot(query)
    update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)


load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')
updater = telegram.ext.Updater(TOKEN)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("ah", ah))
dispatcher.add_handler(CommandHandler("tarot", tarot))
dispatcher.add_handler(CommandHandler("mazo", mazo))
dispatcher.add_handler(CommandHandler("mejora", mejora))

print("HEEEEEEEE")
updater.start_polling()
updater.idle()
