#add a number that is one less than the original until the addition number goes to 0
def sum(num):
    result = 0
    for i in range (num):
        result = result + num -i
    print(result)
sum(10)

