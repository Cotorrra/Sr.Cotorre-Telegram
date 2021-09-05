from src.core.formating import format_text


def format_rule(rule):
    text = f"**{rule['title']}**\n"
    text += "%s" % format_text(rule['text'])
    return text
