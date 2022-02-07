from heapq import merge


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n|    wellcome to the word guesser   |\n|   only words for words that "
      "are   |\n|        not names or phrases       |\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


def wordlesolver(notletters, fixedletters, unfixedletters):
    wordbank = open("words.txt", "r")
    wordbank = wordbank.read()
    wordbank = wordbank.split()  # now word bank is a list

    fiveletterwords = open("5leterwords.txt", "r")
    fivewordbank = fiveletterwords.read()
    fivewordbank = fivewordbank.split()  # now five word bank is also a list

    scrabblewords = open("scrabble aproved words.txt", "r")
    scrabblewordbank = scrabblewords.read()
    scrabblewordbank = scrabblewordbank.split()

    wordbank = list(
        merge(wordbank, fivewordbank))  # now word bank is a combination of word bank and five word bank as one

    oldwords = []
    for i in wordbank:
        oldwords.append(i)

    removedwords = []
    wordlen = 5

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
    print("removing duplicates")
    for i in wordbank:
        if len(i) != wordlen:
            removedwords.append(i)
            wordbank.remove(i)
            print(len(wordbank))
        for ii in wordbank:
            if ii.lower() == i.lower() and ii != i and i not in duplicatewords:
                duplicatewords.append(i)
                wordbank.remove(i)
                print(len(wordbank))
                break
    if "chaplain" in wordbank:
        wordbank.remove("chaplain")
        print(len(wordbank))

    print("double checking")
    oldwords = []
    for i in wordbank:
        oldwords.append(i)

    for i in wordbank:
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

    print("length of word bank: " + str(len(wordbank)) + "\n")
    for i in range(int(len(wordbank)/9)):
        for ii in range(0,8):
            print(wordbank[ii+i], " ", end="")
        print("")


def generalpurpose():
    removedwords = []
    wordlen = int(input("input the number of letters in the word: "))
    notletters = (input("input the letters that are not in the word: "))
    fixedletters = str(input("input the letters that are correct, use underscores for the blank spaces \n for example "
                             "o_u_t: "))
    if wordlen == 2:
        wordbank = open("words.txt", "r")
        wordbank = wordbank.read()
        wordbank = wordbank.split()  # now word bank is a list

        twoletterwords = open("2leterwords.txt", "r")
        twowordbank = twoletterwords.read()
        twowordbank = twowordbank.split()

        scrabblewords = open("scrabble aproved words.txt", "r")
        scrabblewordbank = scrabblewords.read()
        scrabblewordbank = scrabblewordbank.split()

        wordbank = list(merge(wordbank, twowordbank))

        oldwords = []
        for i in wordbank:
            oldwords.append(i)
    elif wordlen == 3:
        wordbank = open("words.txt", "r")
        wordbank = wordbank.read()
        wordbank = wordbank.split()  # now word bank is a list

        threeletterwords = open("3leterwords.txt", "r")
        threewordbank = threeletterwords.read()
        threewordbank = threewordbank.split()

        scrabblewords = open("scrabble aproved words.txt", "r")
        scrabblewordbank = scrabblewords.read()
        scrabblewordbank = scrabblewordbank.split()

        wordbank = list(merge(wordbank, threewordbank))

        oldwords = []
        for i in wordbank:
            oldwords.append(i)
    elif wordlen == 4:
        wordbank = open("words.txt", "r")
        wordbank = wordbank.read()
        wordbank = wordbank.split()  # now word bank is a list

        fourletterwords = open("4leterwords.txt", "r")
        fourwordbank = fourletterwords.read()
        fourwordbank = fourwordbank.split()

        scrabblewords = open("scrabble aproved words.txt", "r")
        scrabblewordbank = scrabblewords.read()
        scrabblewordbank = scrabblewordbank.split()

        wordbank = list(merge(wordbank, fourwordbank))

        oldwords = []
        for i in wordbank:
            oldwords.append(i)
    elif wordlen == 5:
        wordbank = open("words.txt", "r")
        wordbank = wordbank.read()
        wordbank = wordbank.split()  # now word bank is a list

        fiveletterwords = open("5leterwords.txt", "r")
        fivewordbank = fiveletterwords.read()
        fivewordbank = fivewordbank.split()  # now five word bank is also a list

        scrabblewords = open("scrabble aproved words.txt", "r")
        scrabblewordbank = scrabblewords.read()
        scrabblewordbank = scrabblewordbank.split()

        wordbank = list(
            merge(wordbank, fivewordbank))  # now word bank is a combination of word bank and five
        # word bank as one

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

        twoletterwords = open("2leterwords.txt", "r")
        twowordbank = twoletterwords.read()
        twowordbank = twowordbank.split()

        threeletterwords = open("3leterwords.txt", "r")
        threewordbank = threeletterwords.read()
        threewordbank = threewordbank.split()

        fourletterwords = open("4leterwords.txt", "r")
        fourwordbank = fourletterwords.read()
        fourwordbank = fourwordbank.split()

        scrabblewords = open("scrabble aproved words.txt", "r")
        scrabblewordbank = scrabblewords.read()
        scrabblewordbank = scrabblewordbank.split()

        wordbank = list(merge(wordbank, twowordbank, threewordbank, fourwordbank, fivewordbank))

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


def wordtwister():
    a_count = 0
    b_count = 0
    c_count = 0

    letters = str(input("input the letters you have, include duplicates: "))
    usedwords = input("input the words you have allready gotten as a list: ")

    if len(letters) == 3:
        wordbank = open("words.txt", "r")
        wordbank = wordbank.read()
        wordbank = wordbank.split()  # now word bank is a list

        threeletterwords = open("3leterwords.txt", "r")
        threewordbank = threeletterwords.read()
        threewordbank = threewordbank.split()

        scrabblewords = open("scrabble aproved words.txt", "r")
        scrabblewordbank = scrabblewords.read()
        scrabblewordbank = scrabblewordbank.split()

        wordbank = list(merge(wordbank, threewordbank, scrabblewordbank))
    else:
        if len(letters) == 4:
            wordbank = open("words.txt", "r")
            wordbank = wordbank.read()
            wordbank = wordbank.split()  # now word bank is a list

            threeletterwords = open("3leterwords.txt", "r")
            threewordbank = threeletterwords.read()
            threewordbank = threewordbank.split()

            fourletterwords = open("4leterwords.txt", "r")
            fourwordbank = fourletterwords.read()
            fourwordbank = fourwordbank.split()

            scrabblewords = open("scrabble aproved words.txt", "r")
            scrabblewordbank = scrabblewords.read()
            scrabblewordbank = scrabblewordbank.split()

            wordbank = list(merge(wordbank, threewordbank, fourwordbank, scrabblewordbank))

        else:
            if len(letters) == 5:
                wordbank = open("words.txt", "r")
                wordbank = wordbank.read()
                wordbank = wordbank.split()  # now word bank is a list

                threeletterwords = open("3leterwords.txt", "r")
                threewordbank = threeletterwords.read()
                threewordbank = threewordbank.split()

                fourletterwords = open("4leterwords.txt", "r")
                fourwordbank = fourletterwords.read()
                fourwordbank = fourwordbank.split()

                fiveletterwords = open("5leterwords.txt", "r")
                fivewordbank = fiveletterwords.read()
                fivewordbank = fivewordbank.split()  # now five word bank is also a list

                scrabblewords = open("scrabble aproved words.txt", "r")
                scrabblewordbank = scrabblewords.read()
                scrabblewordbank = scrabblewordbank.split()

                wordbank = list(merge(wordbank, threewordbank, fourwordbank, fivewordbank, scrabblewordbank))  # now
                # word bank is a combination of word bank and five word bank and the three and four wordbanks and the
                # scrabble word bank

            else:
                wordbank = open("words.txt", "r")
                wordbank = wordbank.read()
                wordbank = wordbank.split()  # now word bank is a list

                fiveletterwords = open("5leterwords.txt", "r")
                fivewordbank = fiveletterwords.read()
                fivewordbank = fivewordbank.split()  # now five word bank is also a list

                threeletterwords = open("3leterwords.txt", "r")
                threewordbank = threeletterwords.read()
                threewordbank = threewordbank.split()

                fourletterwords = open("4leterwords.txt", "r")
                fourwordbank = fourletterwords.read()
                fourwordbank = fourwordbank.split()

                scrabblewords = open("scrabble aproved words.txt", "r")
                scrabblewordbank = scrabblewords.read()
                scrabblewordbank = scrabblewordbank.split()

                wordbank = list(merge(wordbank, threewordbank, fourwordbank, fivewordbank, scrabblewordbank))

    oldwords = []
    removedwords = []
    for i in wordbank:
        oldwords.append(i)

    for i in oldwords:
        if i not in removedwords or len(letters) < len(i) <= 2:
            removedwords.append(i)
            wordbank.remove(i)
            # print("removed word too long or too short")
            print(len(wordbank))
        else:
            for ii in i:
                if i not in removedwords or ii.lower() not in letters:
                    removedwords.append(i)
                    wordbank.remove(i)
                    # print("removed word with letters in not letters")
                    print(len(wordbank))
                    break
            if i not in removedwords or i.lower() in usedwords:
                removedwords.append(i)
                wordbank.remove(i)
                # print("removed word that was allready used")
                print(len(wordbank))

    print("length of word bank: " + str(len(wordbank)) + "\n")
    print(wordbank)


wordgame = int(input("input what word game you are solving\n0 for Wordle 1 for Hangman 2 for Word Twister: "))
if wordgame == 0:
    notletters = (input("input the letters that are not in the word: "))
    fixedletters = str(input("input the letters that are green, use underscores for the blank spaces and dont put in "
                             "yellow letters.\n for example o_u_t: "))
    unfixedletters = str(
        input("input the yellow letters where they are yellow, use underscores for blank spaces.\n for "
              "example t_y_e: "))
    wordlesolver(notletters, fixedletters, unfixedletters)
elif wordgame == 1:
    generalpurpose()
elif wordgame == 2:
    wordtwister()
