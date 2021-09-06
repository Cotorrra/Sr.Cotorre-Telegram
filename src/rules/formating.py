from src.core.formating import format_text


def format_rule(rule):
    text = f"<b>{rule['title']}</b>\n"
    text += "%s" % format_text(rule['text'])
    return text
