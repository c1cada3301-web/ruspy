
import re
from .ruspy_dict import RUSPY_DICT
try:
    from .ruspy_user_dict import USER_IDENTIFIERS
except ImportError:
    USER_IDENTIFIERS = {}

def transpile_line(line, dictionary=RUSPY_DICT, user_dict=USER_IDENTIFIERS):
    # Сначала заменяем строковые значения (например, '__главный__')
    for rus, eng in dictionary.items():
        if rus.startswith("'__") and rus.endswith("__'"):
            line = line.replace(rus, eng)
        elif rus.startswith('"__') and rus.endswith('__"'):
            line = line.replace(rus, eng)
    # Затем заменяем остальные ключевые слова
    for rus, eng in sorted(dictionary.items(), key=lambda x: -len(x[0])):
        if rus.startswith("'__") and rus.endswith("__'"):
            continue
        if rus.startswith('"__') and rus.endswith('__"'):
            continue
        line = re.sub(rf'\b{rus}\b', eng, line)
    # Теперь заменяем пользовательские идентификаторы
    for rus, eng in sorted(user_dict.items(), key=lambda x: -len(x[0])):
        line = re.sub(rf'\b{rus}\b', eng, line)
    # Дополнительно заменяем слова из пользовательского словаря внутри строковых литералов
    def replace_in_string_literals(match):
        s = match.group(0)
        for rus, eng in sorted(user_dict.items(), key=lambda x: -len(x[0])):
            s = s.replace(rus, eng)
        return s
    line = re.sub(r"(['\"])(.*?)(['\"])", replace_in_string_literals, line)
    return line

def transpile_file(input_path, output_path, dictionary=RUSPY_DICT, user_dict=USER_IDENTIFIERS):
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            new_line = transpile_line(line, dictionary, user_dict)
            outfile.write(new_line)
