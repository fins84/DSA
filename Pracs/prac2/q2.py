def gcd_Iter(a, b):

    found = False
    while(found == False):
        if a == 0:
            return_val = b
            found = True
        elif b == 0:
            return_val = a
            found = True

        elif( a == b):
            return_val = a
            found = True
        else:
            n = a//b
            b = a%b
            a = (a - b)/n

        print("a: ", a, " b: ", b,"\n")

    return return_val

def gcd_WrpRecurs(a,b):
    if type(a) ==  str or type(b) == str:
        raise TypeError("Arguments cannot be character (integers only)")

    elif a<0 or b<0:
        raise ValueError("Argument values (number/base) cannot be negative")

    return gcd_Recurs(a,b)

def gcd_Recurs(a, b):
    if a == 0:
        return_val = b
    elif b == 0:
        return_val = a
    elif a == b:
        return_val = a   
    else:
        n = a//b
        b = a%b
        a = (a-b)/n
        return_val = gcd_Recurs(a, b)
    return return_val



#algorithm from https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
#kahn academy

#main
a = 15
b = -2
try:
    print(gcd_WrpRecurs(a,b))
except Exception as e:
    print("Error: ", e)