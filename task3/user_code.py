def fibanacci_num(num):

    fib1 = 0

    fib2 = 1

    stroka=""

    for _ in range(1, num + 1):

        fib1, fib2 = fib1 + fib2, fib1

        stroka+=str(fib1)

        stroka+=" "

    return stroka

