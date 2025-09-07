# Бейджи статуса
![PyPI](https://img.shields.io/pypi/v/ruspy-transpiler)
![Build](https://github.com/c1cada3301-web/ruspy/actions/workflows/publish-to-pypi.yml/badge.svg)
![Coverage](https://img.shields.io/codecov/c/github/c1cada3301-web/ruspy)
![Lint](https://img.shields.io/badge/lint-passing-brightgreen)


# Русский Python (ruspy-transpiler)

Транспилятор, позволяющий писать Python-код с русскими ключевыми словами, функциями и идентификаторами.


Установка

1. Склонируйте репозиторий или скачайте исходный код.
2. Перейдите в папку проекта и установите пакет локально:

```bash
pip install .
```

или для разработки:

```bash
pip install -e .
```

## Структура

- `ruspy/` — основной пакет
	- `transpiler.py` — логика транспиляции
	- `ruspy_dict.py` — официальный словарь (ключевые слова, функции, технические термины)
	- `ruspy_user_dict.py` — пользовательский словарь (ваши идентификаторы и сообщения)
	- `cli.py` — CLI-интерфейс
- `setup.py` — файл для установки
- `test_ruspy.py` — пример кода на русском синтаксисе

## Использование


### Через CLI

```bash
ruspy-transpiler test_ruspy.py -o test_ruspy_out.py
```
или
```bash
python -m ruspy.cli test_ruspy.py -o test_ruspy_out.py
```
- `test_ruspy.py` — ваш файл с русским синтаксисом.
- `test_ruspy_out.py` — результат на стандартном Python.

### Как библиотека

```python
from ruspy.transpiler import transpile_file
transpile_file('test_ruspy.py', 'test_ruspy_out.py')
```

## Расширение словарей

- Для добавления новых переводов ключевых слов и функций — редактируйте `ruspy_dict.py`.
- Для пользовательских идентификаторов и сообщений — используйте `ruspy_user_dict.py`.

## Проверка полноты

Для проверки, все ли термины переведены, используйте скрипт:

```bash
python check_ruspy_dict.py
```

---
Проект в стадии разработки. Приветствуются идеи и pull request'ы!
