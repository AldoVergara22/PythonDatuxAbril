import sys

def print_args(*args):
    4+5
    print("Los argumentos introducidos son:")
    for arg in args:
        print(arg)

# get arguments from command line
args = sys.argv[1:]

# call the function with the arguments
print_args(*args)
