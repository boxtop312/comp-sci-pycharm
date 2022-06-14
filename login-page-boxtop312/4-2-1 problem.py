import random
file = open("421 problem.txt", "a+")
file.write("4, 2, 1 problem if the number is true that means that it ends up in 4, 2, 1")
while True:
    x = random.randrange(1, 99999999999,1)
    used = []
    used.append(x)
    while x != 4:
        if x not in used:
            if x % 2:
                x = (3*x)+1
            else:
                x = x/2
        else:
            break
    file.write(str(x)+" True    ")
    print(x)
