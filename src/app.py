import sys
from pathlib import Path

# Agregar la ruta base del proyecto (el padre de 'lib' y 'src') a sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

# sys.path.append(str(BASE_DIR))

# Importar la clase Dog desde lib.dog
from lib.dog import Dog
from lib.cat import Cat


# Usar la clase Dog
if __name__ == "__main__":
    my_dog = Dog("Fido", 5)
    my_cat = Cat("Almendra", 3)
    print(my_dog.bark())
    print(my_cat.bark())


