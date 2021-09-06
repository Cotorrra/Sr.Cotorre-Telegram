from src.core.formating import format_text


def format_tarot(tarot):
    text = f"<b>{tarot['name']}</b>\n"
    up_text = format_text(tarot['up'])
    down_text = format_text(tarot['down'])
    text += f"Carta de Tarot" \
            f"\n\nNormal" \
            f"\n- <i>{up_text}</i>" \
            f"\n\nInvertido" \
            f"\n- <i>{down_text}</i>" \
            f"\n\n"
    text += f"🖌{tarot['illustrator']}" \
            f"\n{tarot['set']} #{tarot['number']}."
    return text
