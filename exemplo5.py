idade = int (input("Insira a sua idade: "))

if idade < 3:
    print("Bebê")
elif idade < 10:
    print("Infantil")
elif idade < 14:
    print("Junior")
elif idade < 17:
    print("Adolescente")
elif idade < 30:
    print("Jovem")
else: 
    print("Adulto")