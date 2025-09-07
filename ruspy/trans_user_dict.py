from googletrans import Translator
import os
import sys
import re

# Импортируем официальный словарь для фильтрации стандартных ключевых слов и функций
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ruspy_dict import RUSPY_DICT

def extract_russian_identifiers_from_code(code):
    """
    Извлекает все идентификаторы (имена переменных, функций, классов и т.д.) на русском из кода.
    """
    # Ищем идентификаторы, начинающиеся с русской буквы или содержащие только русские буквы/цифры/_
    pattern = r'\b[а-яА-ЯёЁ_][а-яА-ЯёЁ0-9_]*\b'
    return set(re.findall(pattern, code))

def generate_user_dict_from_code(py_file, output_file):
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

    # Читаем исходный код и извлекаем идентификаторы
    with open(py_file, encoding="utf-8") as f:
        code = f.read()
    found = extract_russian_identifiers_from_code(code)

    # Фильтруем: только те, которых нет в официальном и пользовательском словаре
    new_words = [w for w in found if w not in RUSPY_DICT and w not in existing]

    # Переводим новые слова
    for word in new_words:
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
    # Пример использования: python trans_user_dict.py test_ruspy.py ruspy_user_dict.py
    import sys
    if len(sys.argv) < 2:
        print("Использование: python trans_user_dict.py <py-файл> [ruspy_user_dict.py]")
    else:
        py_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "ruspy_user_dict.py"
        generate_user_dict_from_code(py_file, output_file)