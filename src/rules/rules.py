import json

from src.core.utils import load_from_repo


def load_rules():
    """
    Carga el archivo de taboo.
    :return:
    """
    file_src = 'data/rules/rules.json'

    info = load_from_repo(file_src)

    info['rules'] = json.dumps(info['rules'])
    info['rules'] = json.loads(info['rules'])

    return info


