def min_coin_amount(num):

    count = 0
    while num >= 25:
        count += 1
        num = num - 25
    while num >= 10:
        count += 1
        num = num - 10
    while num >= 5:
        count += 1
        num = num - 5
    while num >= 1:
        count += 1
        num = num - 1
    return count



        