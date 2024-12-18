import sys

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print(f"Pas assez d’arguments pour le script '{sys.argv[0]}'")
    else:
        print(f"Nombre d'arguments : {len(sys.argv)}")
        for arg in sys.argv:
            print(arg)
