lst1 = []
lst2 = []
lst3 = []
while True:
    a = input("Введите элемент в список 1: ")
    try:
        num = int(a)
        lst1.append(num)
    except ValueError:
        break

while True:
    a = input("Введите элемент в список 2: ")
    try:
        num = int(a)
        lst2.append(num)
    except ValueError:
        break

while True:
    a = input("Введите элемент в список 3: ")
    try:
        num = int(a)
        lst3.append(num)
    except ValueError:
        break


for a in lst1:
    if a in lst2 and a not in lst3:
        print(a)
