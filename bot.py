import logging
import os
from uuid import uuid4

import telegram.ext
from dotenv import load_dotenv
from telegram import Update, ParseMode, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import CallbackContext, CommandHandler, InlineQueryHandler

from src.core.formating import get_thumbnail_image, format_card_text, format_text
from src.core.resolve import resolve_search
from src.core.search import card_search
from src.core.utils import make_str_from_args, get_title
from src.e_cards.search import format_query_ec
from src.p_cards.search import format_query_pc
from src.response.response import look_for_player_card, look_for_deck, look_for_upgrades, look_for_mythos_card, \
    look_for_faq, look_for_rule, look_for_card_back, look_for_tarot, look_for_cards


def mazo(update: Update, context: CallbackContext) -> None:
    try:
        code = context.args[0]
        tipo = context.args[1] if len(context.args) > 1 else ""
        response = look_for_deck(code, tipo)
        update.message.reply_text(response, parse_mode=ParseMode.HTML)

    except (IndexError, ValueError):
        update.message.reply_text("Error: Su uso es /mazo [id] [deck/decklist (opcional)]")


def mejora(update: Update, context: CallbackContext) -> None:
    try:
        code = context.args[0]
        tipo = context.args[1] if len(context.args) > 1 else ""
        response = look_for_upgrades(code, tipo)
        update.message.reply_text(response, parse_mode=ParseMode.HTML)

    except (IndexError, ValueError):
        update.message.reply_text("Error: Su uso es /mejora [id] [deck/decklist (opcional)]")


"""
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
"""


def inline_query(update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    query = update.inline_query.query

    if query == "":
        return

    response = look_for_cards(query)
    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title=get_title(c),
            input_message_content=InputTextMessageContent(resolve_search([c]), parse_mode=ParseMode.HTML),
            thumb_url=get_thumbnail_image(c),
            description=format_card_text(c)
        ) for c in response[0:5]]

    update.inline_query.answer(results)


def tarot(update: Update, context: CallbackContext) -> None:
    query = make_str_from_args(context.args) if len(context.args) > 1 else ""
    response = look_for_tarot(query)
    update.message.reply_text(response, parse_mode=ParseMode.HTML)


load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')
updater = telegram.ext.Updater(TOKEN)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("mejora", mejora))
dispatcher.add_handler(CommandHandler("mazo", mazo))
dispatcher.add_handler(CommandHandler("tarot", tarot))
dispatcher.add_handler(InlineQueryHandler(inline_query))

print("HEEEEEEEE")
updater.start_polling()
updater.idle()


