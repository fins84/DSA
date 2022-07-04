def n_Wrpconversion(number, base):
    if type(number) ==  str or type(base) == str:
        raise TypeError("Arguments cannot be character (integers only)")

    elif number<0 or base<0:
        raise ValueError("Argument values (number/base) cannot be negative")

    return n_conversion(number,base)


def n_conversion(number, base):
    if number < base:
        n = number
        return_val = number
        if n >= 10:
            n = chr(n+55)
            return_val = n
            
    else:
        n = number % base
        if n >= 10:
            n = chr(n+55)
        return_val = str((n_conversion(number//base, base))) + str(n)

    return return_val

# https://bradfieldcs.com/algos/recursion/converting-an-integer-to-a-string/
    
#main
try:
    print(n_Wrpconversion(50,16))
except Exception as e:
    print("Error: ", e)


