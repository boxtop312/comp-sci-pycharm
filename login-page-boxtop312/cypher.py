cezar_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "o", "p", "q", "r", "s", "t", "u",
                 "v", "w", "x", "y", "z"]


def shiftlist(oglist, leftorright, howfar):
    newlist = []
    for i in range(len(oglist)):
        newlist.append("")

    if leftorright:
        for i in range(len(oglist)):
            if oglist[i] == oglist[(-1 * howfar)]:
                for ii in range(-1 * howfar, 0):
                    newlist[0 + howfar + ii] = oglist[ii]

                return newlist
            else:
                newlist[i + howfar] = oglist[i]
    else:
        howfar = (-1 * howfar) + 25
        for i in range(len(oglist)):
            if oglist[i] == oglist[(-1 * howfar)]:
                for ii in range(-1 * howfar, 0):
                    newlist[0 + howfar + ii] = oglist[ii]

                return newlist
            else:
                newlist[i + howfar] = oglist[i]


def cezar_crypt(text, shift):
    newtext = ""
    if shift < 0:
        howfar = abs(shift)
        leftorright = False
    else:
        howfar = shift
        leftorright = True
    shifted_list = shiftlist(cezar_letters, leftorright, howfar)
    for i in range(len(text)):
        for ii in range(len(cezar_letters)):
            if text[i].lower() == cezar_letters[ii]:
                newtext += shifted_list[ii]
                break
            elif text[i].lower() not in cezar_letters:
                newtext += text[i].lower()
                break

    print(newtext)


cezar_crypt(str(input("input text: ")), int(input("input how much the text should be shifted\n can be negative or "
                                                    "positive but not greater than 24.\n if you are decrypting put in "
                                                    "the reverse of the encryption number: ")))
