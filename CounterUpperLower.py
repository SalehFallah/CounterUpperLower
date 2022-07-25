text = input('Please give a text :')


def myfunc(name):
    ups = 0
    lows = 0
    for item in text:
        if item.isupper():
            ups += 1
        if item.islower():
            lows += 1
    print("Number of uppercase is : ", ups, '\nand number of lowercase is ', lows)


myfunc(text)
