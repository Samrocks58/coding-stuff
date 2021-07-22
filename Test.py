number = 1
a=1

factors=[]
Perfect_Numbers=[]


def SUM(list):
    Addition = 0
    for i in list:
        Addition += i
    return int(Addition)

while number < 9999999999999999999999999999999999999:
    division=number/a
    if float(division) == int(division):
        factors.append(a)
    if number == a:
        factors.remove(a)
        if number == SUM(factors):
            Perfect_Numbers.append(number)
            print(Perfect_Numbers)
            a = 1
            factors.clear()
            number += 1
        else:
            a = 1
            factors.clear()
            number += 1
    else:
        a += 1
print(Perfect_Numbers)
print("Done!!")