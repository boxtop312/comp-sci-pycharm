from heapq import merge
# wordbank = open("words.txt", "r")
# wordbank = wordbank.read()
# wordbank = wordbank.split()  # now word bank is a list
#
# fiveletterwords = open("5leterwords.txt", "r")
# fivewordbank = fiveletterwords.read()
# fivewordbank = fivewordbank.split()  # now five word bank is also a list
#
# wordbank = list(merge(wordbank, fivewordbank))  # now word bank is a combination of word bank and five word bank as one
#
# oldwords = []
# for i in wordbank:
#     oldwords.append(i)


def wordlesolver():
    wordbank = open("words.txt", "r")
    wordbank = wordbank.read()
    wordbank = wordbank.split()  # now word bank is a list

    fiveletterwords = open("5leterwords.txt", "r")
    fivewordbank = fiveletterwords.read()
    fivewordbank = fivewordbank.split()  # now five word bank is also a list

    wordbank = list(
        merge(wordbank, fivewordbank))  # now word bank is a combination of word bank and five word bank as one

    oldwords = []
    for i in wordbank:
        oldwords.append(i)
    removedwords = []
    wordlen = 5
    notletters = (input("input the letters that are not in the word:"))
    fixedletters = str(input("input the letters that are green, use underscores for the blank spaces and dont put in "
                             "yellow letters.\n for example o_u_t:"))
    unfixedletters = str(
        input("input the yellow letters where they are yellow, use underscores for blank spaces.\n for "
              "example t_y_e:"))

    for i in oldwords:
        if len(i) != wordlen and i not in removedwords:
            removedwords.append(i)
            wordbank.remove(i)
            # print("removed word too long")
            print(len(wordbank))
        else:
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
    for i in wordbank:
        if len(i) != wordlen:
            removedwords.append(i)
            wordbank.remove(i)
        for ii in wordbank:
            if ii.lower() == i.lower() and ii != i and i not in duplicatewords:
                duplicatewords.append(i)
                wordbank.remove(i)
                break
    if "chaplain" in wordbank:
        wordbank.remove("chaplain")

    print("length of word bank: " + str(len(wordbank)) + "\n")
    print(wordbank)


def generalpurpose():
    removedwords = []
    wordlen = int(input("input the number of letters in the word"))
    notletters = (input("input the letters that are not in the word:"))
    fixedletters = str(input("input the letters that are correct, use underscores for the blank spaces \n for example "
                             "o_u_t:"))
    if wordlen == 5:
        wordbank = open("words.txt", "r")
        wordbank = wordbank.read()
        wordbank = wordbank.split()  # now word bank is a list

        fiveletterwords = open("5leterwords.txt", "r")
        fivewordbank = fiveletterwords.read()
        fivewordbank = fivewordbank.split()  # now five word bank is also a list

        wordbank = list(
            merge(wordbank, fivewordbank))  # now word bank is a combination of word bank and five word bank as one

        oldwords = []
        for i in wordbank:
            oldwords.append(i)
    else:
        wordbank = open("words.txt", "r")
        wordbank = wordbank.read()
        wordbank = wordbank.split()  # now word bank is a list

        fiveletterwords = open("5leterwords.txt", "r")
        fivewordbank = fiveletterwords.read()
        fivewordbank = fivewordbank.split()  # now five word bank is also a list

        wordbank = list(
            merge(wordbank, fivewordbank))  # now word bank is a combination of word bank and five word bank as one

        twoletterwords = open("2leterwords.txt", "r")
        twowordbank = twoletterwords.read()
        twowordbank = twowordbank.split()

        wordbank = list(merge(wordbank, twowordbank))

        oldwords = []
        for i in wordbank:
            oldwords.append(i)

    for i in oldwords:
        if len(i) != wordlen and i not in removedwords:
            removedwords.append(i)
            wordbank.remove(i)
            # print("removed word too long")
            print(len(wordbank))
        else:
            for ii in i:
                if ii.lower() in notletters and i not in removedwords:
                    removedwords.append(i)
                    wordbank.remove(i)
                    # print("removed word with letters in not letters")
                    print(len(wordbank))
                    break
            for ii in range(0, len(i)):
                if i not in removedwords and fixedletters[ii] != "_" and fixedletters[ii] != i[ii].lower():
                    removedwords.append(i)
                    wordbank.remove(i)
                    # print("removed word because of green letters")
                    print(len(wordbank))
                    break

    duplicatewords = []
    for i in wordbank:
        if len(i) != wordlen:
            removedwords.append(i)
            wordbank.remove(i)
        for ii in wordbank:
            if ii.lower() == i.lower() and ii != i and i not in duplicatewords:
                duplicatewords.append(i)
                wordbank.remove(i)
                break

    print("length of word bank: " + str(len(wordbank)) + "\n")
    print(wordbank)


wordgame = int(input("input what word game you are solving\n 0 for wordle 1 for general purpose: "))
if wordgame == 0:
    wordlesolver()
elif wordgame == 1:
    generalpurpose()
