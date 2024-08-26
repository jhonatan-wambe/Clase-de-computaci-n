import random

print("\n*** Bienvenido a El casino Ganamucho ***")
print("Lanzando dados ......")
min = 1
max = 12
val = random.randint(min,max)

print(f"Numero de dados: {val}")

if val == 7 or val == 11:
    print("¡¡ Ganador !!")
elif val == 2 or val == 3 or val == 12:
    print(" ** Perdedor **")
else:
    print("\n** Fase tiros secundarios **")
    print("Lanzando dados ......")
    val2 = random.randint(min,max)
    print(f"Numero de dados: {val2}")
    if val2 == 7:
        print("** Perdedor **")
    elif val2 == val:
        print("¡¡ Ganador !!")
    else:
        print("\n** sigue jugando **")
        print("Lanzando dados ......")
        val3 = random.randint(min,max)
        print(f"Numero de dados: {val3}")
        if val3 == 7:
            print("** Perdedor **")
        elif val3 == val2:
            print("¡¡ Ganador !!")
        else:
            print("\n** Ultima Oportunidad **")
            print("Lanzando dados ....")
            val4 = random.randint(min,max)
            print(f"Numero de dados: {val4}")
            if val4 == 7:
                print("** Perdedor **")
            elif val4 == val3:
                print("¡¡ Ganador !!")
            else:
                print("¡¡ Lanzaste 5 veces perdido por W !!")
