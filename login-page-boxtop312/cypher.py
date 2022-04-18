cezar_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U",
                 "V", "W", "X", "Y", "Z"]
vinegrette_letters = [
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
     "x", "y", "z", " "],
    ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
     "y", "z", " ", "a"],
    ["c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
     "z", " ", "a", "b"],
    ["d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
     " ", "a", "b", "c"],
    ["e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ",
     "a", "b", "c", "d"],
    ["f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "a",
     "b", "c", "d", "e"],
    ["g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "a", "b",
     "c", "d", "e", "f"],
    ["h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "a", "b", "c",
     "d", "e", "f", "g"],
    ["i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "a", "b", "c", "d",
     "e", "f", "g", "h"],
    ["j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "a", "b", "c", "d", "e",
     "f", "g", "h", "i"],
    ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "a", "b", "c", "d", "e", "f",
     "g", "h", "i", "j"],
    ["l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "a", "b", "c", "d", "e", "f", "g",
     "h", "i", "j", "k"],
    ["m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "a", "b", "c", "d", "e", "f", "g", "h",
     "i", "j", "k", "l"],
    ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i",
     "j", "k", "l", "m"],
    ["o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
     "k", "l", "m", "n"],
    ["p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
     "l", "m", "n", "o"],
    ["q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
     "m", "n", "o", "p"],
    ["r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
     "n", "o", "p", "q"],
    ["s", "t", "u", "v", "w", "x", "y", "z", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
     "o", "p", "q", "r"],
    ["t", "u", "v", "w", "x", "y", "z", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
     "p", "q", "r", "s"],
    ["u", "v", "w", "x", "y", "z", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
     "q", "r", "s", "t"],
    ["v", "w", "x", "y", "z", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
     "r", "s", "t", "u"],
    ["w", "x", "y", "z", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
     "s", "t", "u", "v"],
    ["x", "y", "z", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
     "t", "u", "v", "w"],
    ["y", "z", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
     "u", "v", "w", "x"],
    ["z", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
     "v", "w", "x", "y"],
    [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
     "w", "x", "y", "z"]]


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


def get_collum(uselist, collumnum):
    newlist = []
    for x in range(len(uselist)):
        for y in range(len(uselist[x])):
            if uselist[x].index(uselist[x][y]) == collumnum:
                newlist.append(uselist[x][y])
    return newlist


def lengthen_key(text, key):
    newtext = ""
    i1 = 0
    for i in range(len(text)):
        if i1 >= len(key):
            i1 *= 0
        newtext += key[i1]
        i1 += 1
    return newtext


def cezar_encrypt(text, shift):
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
    return newtext


def cezar_decrypt(text, shift):
    shift *= -1
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
    return newtext


def vigenere_encrypt(text, key):
    newtext = ""
    for x in range(len(text)):
        x1 = vinegrette_letters[0].index(text[x])
        for y in range(len(lengthen_key(text, key))):
            if y > (len(lengthen_key(text, key)) + 1):
                y *= 0
            else:
                if x == y:
                    y1 = get_collum(vinegrette_letters, 0).index(lengthen_key(text, key)[y])
                    newtext += vinegrette_letters[x1][y1]
    return newtext


def vigenere_decrypt(string, key):
    string = string.strip()
    key = key.strip()
    text = []
    for i in range(len(string)):
        g = i
        if i >= len(key):
            g = i % len(key)
        x = (ord(string[i]) - ord(key[g])) % 26
        x += ord('A')
        text.append(chr(x))
    return "".join(text)


print(vigenere_encrypt("theeaglehaslanded", "america"))
# cezar_decrypt(str(input("input text: ")), int(input("input how much the text should be shifted\n can be negative or "
#                                                     "positive but not greater than 24: ")))
