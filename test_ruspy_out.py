from ruspy.transpiler import transpile_file

def greeting(name):
    print('Hello,', name)

if __name__ == '__main__':
    name = input('Enter name: ')
    greeting(name)

def sum(a, b): 
    return a + b