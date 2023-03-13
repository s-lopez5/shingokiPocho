###Autor 1: Noelia Suarez Tuñas 
###Autor 2: Santiago López Silva
import sys

def to_list(table):
    return list(table)

def leer ():
    a = open(sys.argv[1])
    b = a.read()
    c = to_list(b)
    
    num = 0
    column = 0
    columnAux = 0
    row = 0
    string = ""
    neg = False

    for x in c:
        if x == "\n":
            string += "\n"
            num = column
            column = 0
            row += 1
        elif x == "-":
            neg = True
        else:      
            if neg == True:
                neg = False
                string += "number(" + str(column) + "," + str(row) + ",-" + x + ")."
                column += 1
            else:
                string += "number(" + str(column) + "," + str(row) + "," + x + ")."
                column += 1

    string2 = "row(0.." + str(num-1) + ").\ncolumn(0.." + str(num-1) + ").\n"
    string2 += string
    s = open(sys.argv[1].replace("txt","lp"), "w+")
    s.write(string2)
    a.close
    s.close

leer()


