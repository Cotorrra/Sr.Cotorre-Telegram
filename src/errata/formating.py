from src.core.formating import format_text
from src.errata.errata import has_errata, get_errata_card


def format_errata_text(card_id, back=False):
    text = "<b><i>Errata</i></b>:\n"
    if has_errata(card_id):
        card = get_errata_card(card_id)
        if back and ('text_back' in card):
            text += "<i>%s</i>\n\n" % format_text(card['text_back'])
        elif 'text' in card:
            text += "<i>%s</i>\n\n" % format_text(card['text'])
        return text
    else:
        return ""
