<div align="center">

<img src="https://img.shields.io/pypi/v/ruspy-transpiler" alt="PyPI">
<img src="https://github.com/c1cada3301-web/ruspy/actions/workflows/publish-to-pypi.yml/badge.svg" alt="Build">
<img src="https://img.shields.io/codecov/c/github/c1cada3301-web/ruspy" alt="Coverage">
<img src="https://img.shields.io/badge/lint-passing-brightgreen" alt="Lint">

# Русский Python (ruspy-transpiler)

</div>

Транспилятор, позволяющий писать Python-код с русскими ключевыми словами, функциями и идентификаторами.

---

## Установка

1. Склонируйте репозиторий или скачайте исходный код.
2. Перейдите в папку проекта и установите пакет локально:
	 ```bash
	 pip install .
	 ```
	 или для разработки:
	 ```bash
	 pip install -e .
	 ```

## Структура проекта

- `ruspy/` — основной пакет
	- `transpiler.py` — логика транспиляции
	- `ruspy_dict.py` — официальный словарь (ключевые слова, функции, технические термины)
	- `ruspy_user_dict.py` — пользовательский словарь (ваши идентификаторы и сообщения)
	- `cli.py` — CLI-интерфейс
- `setup.py` — файл для установки
- `test_ruspy.py` — пример кода на русском синтаксисе

---

## Использование

### Через CLI

```bash
ruspy test_ruspy.py -o test_ruspy_out.py
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

### Новые команды CLI

```bash
# Пакетная обработка всех .py файлов в папке
ruspy --batch batch_test batch_out

# Статистика замен по словарям для файла
ruspy --stats test_ruspy.py

# Проверка словарей на дубли и пустые значения
ruspy --check-dict
```

---

## Интеграция с редакторами

### VS Code
1. Откройте папку проекта в VS Code.
2. В каталоге .vscode уже есть tasks.json для задачи "Ruspy Transpile".
3. Для запуска транспиляции нажмите Ctrl+Shift+B или выберите задачу "Ruspy Transpile" в палитре команд.
4. Для автоматической транспиляции при сохранении установите расширение "Run on Save" и добавьте в settings.json:
	 ```json
	 "runOnSave.commands": [
		 {
			 "match": "\\.py$",
			 "command": "workbench.action.tasks.runTask",
			 "args": "Ruspy Transpile"
		 }
	 ]
	 ```

### PyCharm
1. Откройте File → Settings → Tools → File Watchers.
2. Нажмите "+" → Custom.
3. Заполните:
	 - Name: Ruspy Transpile
	 - File type: Python
	 - Program: путь до ruspy.exe (например, venv\Scripts\ruspy.exe)
	 - Arguments: $FileName$ -o $FileNameWithoutExtension$_out.py
	 - Working directory: $ProjectFileDir$
4. Включите "Auto-save edited files to trigger the watcher".
5. Сохраните настройки.

Теперь транспиляция будет запускаться автоматически при сохранении .py-файла!

---

## Автоматические тесты

В проекте есть папка `tests/` с примерами тестов на pytest. Для запуска тестов:

```bash
pytest tests
# или
python -m pytest tests
```

Тесты проверяют корректность транспиляции и пакетной обработки файлов.

---

## Расширение словарей

- Для добавления новых переводов ключевых слов и функций — редактируйте `ruspy_dict.py` (официальный словарь, только ключевые слова, стандартные функции и технические термины).
- Для пользовательских идентификаторов и сообщений — используйте `ruspy_user_dict.py` (сюда попадают только ваши переменные, функции, сообщения и т.д.).

### Автоматическое обновление пользовательского словаря

Чтобы добавить новые пользовательские идентификаторы автоматически:
1. Добавьте новые слова (по одному на строку) в файл-список, например, `словарь`.
2. Запустите:
   ```bash
   python ruspy/trans_user_dict.py
   ```
   Новые слова будут переведены и добавлены в `ruspy_user_dict.py`. Уже существующие идентификаторы не будут затёрты, а новые просто добавятся.

### Проверка полноты

Для проверки, все ли термины переведены, используйте скрипт:
```bash
python check_ruspy_dict.py
```

---

## Список поддерживаемых ключевых слов и функций

Полный список — в файле [`ruspy_dict.py`](ruspy/ruspy_dict.py). Можно вывести через команду:
```bash
python -c "from ruspy.ruspy_dict import RUSPY_DICT; print(list(RUSPY_DICT.keys()))"
```

---

## Примеры кода

### Русский синтаксис (`test_ruspy.py`)
```python
функция приветствие(имя):
		печать('Привет,', имя)

если __имя__ == '__главный__':
		имя = ввод('Введите имя: ')
		приветствие(имя)
```

### После транспиляции (`test_ruspy_out.py`)
```python
def greeting(name):
		print('Hello,', name)

if __name__ == '__main__':
		name = input('Enter name: ')
		greeting(name)
```

---

## Документация и ресурсы

- [PyPI](https://pypi.org/project/ruspy-transpiler/)
- [GitHub](https://github.com/c1cada3301-web/ruspy)
- [Примеры](#примеры-кода)

---

## Быстрый запуск через Docker

```bash
docker build -t ruspy .
docker run --rm -v %cd%:/app ruspy ruspy test_ruspy.py -o test_ruspy_out.py
```

---

## Публикация своего пакета

1. Измените имя пакета в `pyproject.toml`.
2. Соберите и опубликуйте пакет:
	 ```bash
	 python -m build
	 twine upload dist/*
	 ```

---

## Лицензия

MIT License. См. файл [LICENSE](LICENSE).

---

## Контакты

- GitHub Issues: https://github.com/c1cada3301-web/ruspy/issues
- Email: shtrnv@ya.ru
- Telegram: [@cicada_web](https://t.me/cicada_web)

---

## Благодарности

Спасибо всем авторам идей, тестировщикам и вдохновителям! А особенно [@mcodeg](https://t.me/mcodeg), его Tik-Tok: <https://www.tiktok.com/@mcodeg_> 

---

## FAQ

**Q: Можно ли использовать свои словари?**  
A: Да, просто добавьте нужные пары в `ruspy_user_dict.py` или создайте свой файл и импортируйте его в транспилятор.  
Официальный словарь (`ruspy_dict.py`) содержит только ключевые слова и стандартные функции, пользовательский (`ruspy_user_dict.py`) — только ваши идентификаторы.

**Q: Как добавить поддержку нового языка?**  
A: Создайте отдельный словарь (например, `ruspy_dict_ua.py`) и добавьте опцию выбора словаря в CLI.

**Q: Как проверить, что всё работает?**  
A: Запустите автоматические тесты или используйте команду `ruspy --stats` для анализа замен.

**Q: Как интегрировать с редактором?**  
A: Смотрите раздел "Интеграция с редакторами" выше.

---

## История изменений (Changelog)

- v0.1.2 — Расширенный CLI, интеграция с редакторами, автоматические тесты, Dockerfile, README.md
- v0.1.0 — Первый релиз

---

<!-- Скриншоты или GIF работы CLI и интеграции с редакторами можно добавить ниже -->

---

Проект в стадии разработки. Приветствуются идеи и pull request'ы!
