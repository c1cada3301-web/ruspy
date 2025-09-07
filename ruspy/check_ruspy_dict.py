import keyword
import builtins
import importlib.util
import sys
import os

# Получаем все ключевые слова Python
python_keywords = set(keyword.kwlist)

# Получаем все встроенные функции и исключения
python_builtins = set()
for name in dir(builtins):
    if not name.startswith('__') or name in ('__init__', '__main__', '__name__'):
        python_builtins.add(name)

# Список часто используемых технических терминов
common_terms = {
    'list', 'dict', 'set', 'tuple', 'str', 'bytes', 'bytearray', 'memoryview', 'int', 'float', 'complex', 'bool',
    'object', 'type', 'file', 'module', 'method', 'function', 'class', 'instance', 'attribute', 'argument', 'parameter',
    'iterator', 'generator', 'decorator', 'context_manager', 'exception', 'error', 'warning', 'import', 'package',
    'library', 'path', 'directory', 'folder', 'frame', 'stack', 'traceback', 'main', 'init', 'del', 'repr', 'call',
    'getitem', 'setitem', 'delitem', 'iter', 'next', 'enter', 'exit', 'eq', 'ne', 'lt', 'le', 'gt', 'ge', 'slots',
    'all', 'any', 'abs', 'len', 'sum', 'min', 'max', 'sorted', 'enumerate', 'zip', 'map', 'filter', 'range', 'reversed',
    'open', 'input', 'print', 'id', 'help', 'dir', 'globals', 'locals', 'vars', 'super', 'property', 'classmethod',
    'staticmethod', 'setattr', 'getattr', 'delattr', 'hasattr', 'isinstance', 'issubclass',
    'TypeError', 'ValueError', 'KeyError', 'IndexError', 'AttributeError', 'ImportError', 'NameError',
    'ZeroDivisionError', 'FileNotFoundError', 'IOError', 'OSError', 'RuntimeError', 'NotImplementedError',
    'StopIteration', 'StopAsyncIteration', 'AssertionError', 'MemoryError', 'SystemExit', 'KeyboardInterrupt',
    'GeneratorExit', 'BaseException', 'Exception', 'Warning', 'UserWarning', 'DeprecationWarning',
    'PendingDeprecationWarning', 'SyntaxWarning', 'RuntimeWarning', 'FutureWarning', 'ImportWarning',
    'UnicodeWarning', 'BytesWarning', 'ResourceWarning'
}

dict_path = os.path.join(os.path.dirname(__file__), 'ruspy_dict.py')
spec = importlib.util.spec_from_file_location("ruspy_dict", dict_path)
ruspy_dict_mod = importlib.util.module_from_spec(spec)
sys.modules["ruspy_dict"] = ruspy_dict_mod
spec.loader.exec_module(ruspy_dict_mod)
ruspy_dict = ruspy_dict_mod.RUSPY_DICT

missing = []
for word in sorted(python_keywords | python_builtins | common_terms):
    if word not in ruspy_dict:
        missing.append(word)

print('Слова, которых нет в официальном словаре RUSPY_DICT:')
for w in missing:
    print(w)
print(f'Всего отсутствует: {len(missing)}')
