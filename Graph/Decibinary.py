def Decimal2Binary(num):

    if num >= 1:
        Decimal2Binary(num//2)
    print(num%2)

Decimal2Binary(24)
