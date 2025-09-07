from googletrans import Translator
import os
import sys

# Импортируем официальный словарь для фильтрации стандартных ключевых слов и функций
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruspy_dict import RUSPY_DICT

def generate_user_dict(input_file, output_file):
    translator = Translator()
    user_dict = {}

    # Загружаем уже существующие пользовательские идентификаторы, если файл есть
    existing = {}
    if os.path.exists(output_file):
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location("ruspy_user_dict", output_file)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            existing = getattr(mod, "USER_IDENTIFIERS", {})
        except Exception:
            existing = {}

    with open(input_file, encoding="utf-8") as f:
        for line in f:
            word = line.strip()
            if not word or word.startswith("#"):
                continue
            # Пропускаем стандартные ключевые слова и функции (их переводить не надо)
            if word in RUSPY_DICT:
                continue
            # Пропускаем уже существующие пользовательские идентификаторы
            if word in existing:
                continue
            # Переводим слово на английский
            translation = translator.translate(word, src='ru', dest='en').text
            user_dict[word] = translation

    # Объединяем старые и новые идентификаторы
    all_user_dict = dict(existing)
    all_user_dict.update(user_dict)

    # Сохраняем как python-словарь
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("USER_IDENTIFIERS = {\n")
        for k, v in all_user_dict.items():
            f.write(f"    '{k}': '{v}',\n")
        f.write("}\n")

if __name__ == "__main__":
    generate_user_dict("словарь", "ruspy_user_dict.py")