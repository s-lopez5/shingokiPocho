###Autor 1: Antonio Vila Leis
###Autor 2: Santiago López Silva
import sys
import re

def separar(data):
    return data.split()

def read(): 
    try:
        for x in range(6):
            dato = input()
            if x == 4:            
                data = separar(dato)
            elif x == 5:
                if input() != "SATISFIABLE":
                    raise Exception("No existe solución")   
    except:
        print("No existe solución.")

    digit = list()
    blacks = list()
    for x in data:
        if x[0] == "c" and x[1] == "e":
            n = list()
            n = [str(num) for num in re.split('(|,|)' ,x) if num.isdigit() or num == "a" or num == "b" or num == "c"]
            digit.append(n[len(n) - 1])
        
        elif x[0] == "b" and x[1] == "l":
            dupla = list()
            dupla.append(int(x[(x.index('(')+1):x.index(',')]))
            dupla.append(int(x[(x.index(',')+1):x.index(')')]))
            blacks.append(dupla)
    hitori = list()
    hitori.append(digit)
    hitori.append(blacks)
    return hitori

def draw_tab(digit, black):
    i = 0
    j = 0
    aux = 0
    for x in digit:
        for y in black:
            if (y[0] == i) and (y[1] == j):
                aux = 1
                sys.stdout.write("* ")

        if aux == 1:
            aux = 0
        else:
            sys.stdout.write(str(x) + " ")
            
        if i >= (pow(len(digit), 0.5)-1):
            i = 0
            j += 1
            sys.stdout.write("\n")
        else: i += 1
    
            
hitori = read()
draw_tab(hitori[0], hitori[1])




