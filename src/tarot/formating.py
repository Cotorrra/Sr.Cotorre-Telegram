from src.core.formating import format_text


def format_tarot(tarot):
    text = f"**{tarot['name']}**\n"
    up_text = format_text(tarot['up'])
    down_text = format_text(tarot['down'])
    text += f"Carta de Tarot" \
            f"\n\nNormal" \
            f"\n- __{up_text}__" \
            f"\n\nInvertido" \
            f"\n- __{down_text}__" \
            f"\n\n"
    text += f"🖌{tarot['illustrator']}" \
            f"\n{tarot['set']} #{tarot['number']}."
    return text
