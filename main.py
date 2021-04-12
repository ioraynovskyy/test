import sys


def print_start(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    a = 5
    b = 3
    print(f'a = {a} and b = {b} and python verions is {sys.version}.')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_start('Good, we can start!')

print('test success!')
