from heapq import merge


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n|    wellcome to the word guesser   |\n|   only words for words that "
      "are   |\n|        not names or phrases       |\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


def wordlesolver(notletters, fixedletters, unfixedletters):
    wordbank = open("words.txt", "r")
    wordbank = wordbank.read()
    wordbank = wordbank.split()  # now word bank is a list

    fiveletterwords = open("5leterwords.txt", "r") # this is a txt file with 12,478 words I got the words from
    # https://www.bestwordlist.com/5letterwords.htm

    fivewordbank = fiveletterwords.read()
    fivewordbank = fivewordbank.split()  # now five word bank is also a list

    wordbank = list(
        merge(wordbank, fivewordbank))  # now word bank is a combination of word bank and five word bank as one

    removedwords = []
    wordlen = 5

    oldwords = []
    for i in wordbank:
        oldwords.append(i)

    removetoolong(oldwords, removedwords, wordlen)

    oldwords = []
    for i in wordbank:
        oldwords.append(i)

    for i in oldwords:
        for ii in i:
            if ii.lower() in notletters and i not in removedwords:
                removedwords.append(i)
                wordbank.remove(i)
                # print("removed word with letters in not letters")
                print(len(wordbank))
                break
        for q in unfixedletters:
            if q != "_":
                if q not in i.lower() and i not in removedwords:
                    removedwords.append(i)
                    wordbank.remove(i)
                    # print("removed word with letters not in yellow letters")
                    print(len(wordbank))
                    break
        for ii in range(0, len(i)):
            if i not in removedwords and fixedletters[ii] != "_" and fixedletters[ii] != i[ii].lower():
                removedwords.append(i)
                wordbank.remove(i)
                # print("removed word because of green letters")
                print(len(wordbank))
                break
            elif i not in removedwords and unfixedletters[ii] != "_" and unfixedletters[ii] == i[ii].lower():
                removedwords.append(i)
                wordbank.remove(i)
                # print("removed word because of yellow letters")
                print(len(wordbank))
                break

    duplicatewords = []
    print("removing duplicates")
    removetoolong(wordbank, removedwords, wordlen)
    for i in wordbank:
        for ii in wordbank:
            if ii.lower() == i.lower() and ii != i and i not in duplicatewords:
                duplicatewords.append(i)
                wordbank.remove(i)
                print(len(wordbank))
                break
    if "chaplain" in wordbank:
        wordbank.remove("chaplain")
        print(len(wordbank))

    printresult(wordbank)


def printresult(wordbank):
    print("length of word bank: " + str(len(wordbank)))
    if len(wordbank) % 10 == 0:
        for i in range(int(len(wordbank) / 10)):
            for ii in range(0, 10):
                print(wordbank[ii + i], " ", end="")
            print("")
    elif len(wordbank) % 9 == 0:
        for i in range(int(len(wordbank) / 9)):
            for ii in range(0, 9):
                print(wordbank[ii + i], " ", end="")
            print("")
    elif len(wordbank) % 8 == 0:
        for i in range(int(len(wordbank) / 8)):
            for ii in range(0, 8):
                print(wordbank[ii + i], " ", end="")
            print("")
    elif len(wordbank) % 7 == 0:
        for i in range(int(len(wordbank) / 7)):
            for ii in range(0, 7):
                print(wordbank[ii + i], " ", end="")
            print("")
    elif len(wordbank) % 6 == 0:
        for i in range(int(len(wordbank) / 6)):
            for ii in range(0, 6):
                print(wordbank[ii + i], " ", end="")
            print("")
    elif len(wordbank) % 5 == 0:
        for i in range(int(len(wordbank) / 5)):
            for ii in range(0, 5):
                print(wordbank[ii + i], " ", end="")
            print("")
    elif len(wordbank) % 4 == 0:
        for i in range(int(len(wordbank) / 4)):
            for ii in range(0, 4):
                print(wordbank[ii + i], " ", end="")
            print("")
    elif len(wordbank) % 3 == 0:
        for i in range(int(len(wordbank) / 3)):
            for ii in range(0, 3):
                print(wordbank[ii + i], " ", end="")
            print("")
    elif len(wordbank) % 2 == 0:
        for i in range(int(len(wordbank) / 2)):
            for ii in range(0, 2):
                print(wordbank[ii + i], " ", end="")
            print("")
    else:
        if isprime(len(wordbank)):
            for i in range(len(wordbank)):
                print(wordbank[i])
        elif len(wordbank) == 1:
            print(wordbank[0])
        else:
            for i in range(len(wordbank)):
                for ii in range(0, 10):
                    print(wordbank[ii + (i * 10)], " ", end="")
                print("")


def isprime(x):
    if x > 1:
        for n in range(2, x):
            if (x % n) == 0:
                return False
        else:
            return True
    else:
        return False


def removetoolong(wordbank, removedwords, wordlen):
    for i in wordbank:
        if len(i) != wordlen and i not in removedwords:
            removedwords.append(i)
            wordbank.remove(i)
            # print("removed word too long")
            print(len(wordbank))
    return wordbank


wordgame = int(input("input what word game you are solving\n0 for Wordle: "))
if wordgame == 0:
    notletters = (input("input the letters that are not in the word: "))
    fixedletters = str(input("input the letters that are green, use underscores for the blank spaces and dont put in "
                             "yellow letters.\n for example o_u_t: "))
    unfixedletters = str(
        input("input the yellow letters where they are yellow, use underscores for blank spaces.\n for "
              "example t_y_e: "))
    wordlesolver(notletters, fixedletters, unfixedletters)
