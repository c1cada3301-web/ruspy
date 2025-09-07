
import argparse
import os
from ruspy.transpiler import transpile_file, transpile_line
from ruspy.ruspy_dict import RUSPY_DICT
from ruspy.ruspy_user_dict import USER_IDENTIFIERS

def print_stats(input_file):
    from collections import Counter
    stats = Counter()
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            for rus, eng in RUSPY_DICT.items():
                if rus in line:
                    stats[rus] += line.count(rus)
            for rus, eng in USER_IDENTIFIERS.items():
                if rus in line:
                    stats[rus] += line.count(rus)
    print('Статистика замен:')
    for k, v in stats.most_common():
        print(f'{k}: {v}')
    if not stats:
        print('Нет замен.')

def check_dicts():
    def check_dict(d, name):
        keys = list(d.keys())
        values = list(d.values())
        dups = set([k for k in keys if keys.count(k) > 1])
        empty_vals = [k for k, v in d.items() if not v]
        print(f'Проверка словаря {name}:')
        if dups:
            print(f'  Дубли ключей: {dups}')
        if empty_vals:
            print(f'  Пустые значения: {empty_vals}')
        if not dups and not empty_vals:
            print('  ОК')
    check_dict(RUSPY_DICT, 'RUSPY_DICT')
    check_dict(USER_IDENTIFIERS, 'USER_IDENTIFIERS')

def batch_transpile(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for fname in os.listdir(input_dir):
        if fname.endswith('.py'):
            in_path = os.path.join(input_dir, fname)
            out_path = os.path.join(output_dir, fname)
            transpile_file(in_path, out_path)
            print(f'Транспиляция {fname} завершена.')

def main():
    parser = argparse.ArgumentParser(description='Транспилятор "русский Python".')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--stats', action='store_true', help='Показать статистику замен по словарям для файла')
    group.add_argument('--check-dict', action='store_true', help='Проверить словари на дубли и пустые значения')
    group.add_argument('--batch', nargs=2, metavar=('INPUT_DIR', 'OUTPUT_DIR'), help='Пакетная обработка всех .py файлов в папке')
    parser.add_argument('input', nargs='?', help='Входной файл с русским синтаксисом')
    parser.add_argument('-o', '--output', help='Файл для вывода результата', default='output.py')
    args = parser.parse_args()

    if args.stats:
        if not args.input:
            print('Укажите файл для анализа статистики.')
            return
        print_stats(args.input)
    elif args.check_dict:
        check_dicts()
    elif args.batch:
        input_dir, output_dir = args.batch
        batch_transpile(input_dir, output_dir)
    elif args.input:
        try:
            transpile_file(args.input, args.output)
            print(f'Транспиляция завершена. Результат: {args.output}')
        except Exception as e:
            print(f'Ошибка: {e}')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
