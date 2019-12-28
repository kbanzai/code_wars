# https://www.codewars.com/kata/54dc6f5a224c26032800005c

def stock_list(listOfArt, listOfCat):
    if listOfArt and listOfCat:
        return " - ".join(
            "(%s : %s)" % (c, sum(map(lambda a: int(a.split()[1]) if a.split()[0][0] == c else 0, listOfArt)))
            for c in listOfCat
        )
    return ""