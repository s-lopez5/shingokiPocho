###Autor 1: Antonio Vila Leis
###Autor 2: Santiago López Silva
import sys

def to_list(table):
    return list(table)

def leer ():
    a = open(sys.argv[1])
    b = a.read()
    c = to_list(b)
    
    num = 0
    i = 0
    j = 0
    string = ""

    for x in c:
        if x == "\n":
            string += "\n"
            num = i
            i = 0
            j += 1
        else: 
            string += "cell(" + str(i) + "," + str(j) + "," + x + ")."
            i += 1
    string2 = "row(0.." + str(num-1) + ").\ncolumn(0.. " + str(num-1) + ").\n"
    string2 += string
    s = open(sys.argv[1].replace("txt","lp"), "w+")
    s.write(string2)
    a.close
    s.close

leer()


