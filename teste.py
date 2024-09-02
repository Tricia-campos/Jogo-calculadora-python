nmr1 = int(input("digite um numero:"))
nmr2 = int(input("digite um numero:"))
nmr3 = int(input("digite um numero:"))

maior = "x"

if nmr1 >= nmr2 and nmr1 >= nmr3:
    maior = "nmr1"
elif nmr2 >= nmr1 and nmr2 >= nmr3:
    maior = "nmr2"
else:
    maior = "nmr3"
print(maior)