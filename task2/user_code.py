def ordered_num(num):
    prelast = 0
    last = 0
    flag = True
    while num != 0:
        prelast = last
        last = num % 10
        num = num // 10
        if last < prelast:
            flag = False
    if flag == True:
        return "YES"
    else:
        return "NO"

