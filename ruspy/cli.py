from ruspy.transpiler import transpile_file
import argparse

def main():
    parser = argparse.ArgumentParser(description='Транспилятор "русский Python".')
    parser.add_argument('input', help='Входной файл с русским синтаксисом')
    parser.add_argument('-o', '--output', help='Файл для вывода результата', default='output.py')
    args = parser.parse_args()
    try:
        transpile_file(args.input, args.output)
        print(f'Транспиляция завершена. Результат: {args.output}')
    except Exception as e:
        print(f'Ошибка: {e}')

if __name__ == '__main__':
    main()
