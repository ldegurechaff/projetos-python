import time, sys
import winsound
rel = time.ctime()

for i in range(0, 5):
    sys.stdout.write("\r{}".format(i))
    sys.stdout.flush()
    time.sleep(1)


print("||||CALCULADORA PYTHON ||||", rel)

print("\nDigite um operador aritmetico")
op = str(input(""))
if op == "+":
    print("SOMA")
    print("DIGITE OS VALORES")
    print("N1 :")
    n1 = int(input())
    print("n2: ")
    n2 = int(input())
    total = n1 + n2
    print("O total eh ", total)
    winsound.PlaySound("congratg.wav", winsound.SND_FILENAME)
else :
    if op == "-":
        print("SUB")
        print("DIGITE OS VALORES")
        print("N1 :")
        n1 = int(input())
        print("n2: ")
        n2 = int(input())
        total = n1 - n2
        print("O total eh ", total)
        winsound.PlaySound("teste.wav", winsound.SND_FILENAME)
if op == "*":
        print("MULT")
        print("DIGITE OS VALORES")
        print("N1 :")
        n1 = int(input())
        print("n2: ")
        n2 = int(input())
        total = n1 * n2
        print("O total eh ", total)
        winsound.PlaySound("teste.wav", winsound.SND_FILENAME)
else :
    if op == "/":
            print("DIVISAO")
            print("DIGITE OS VALORES")
            print("N1 :")
            n1 = int(input())
            print("n2: ")
            n2 = int(input())
            total = n1 / n2
            print("O total eh ", total)
            winsound.PlaySound("teste.wav", winsound.SND_FILENAME)

