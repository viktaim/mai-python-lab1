def tokenize(lst):
    mainLst = []
    separateElem = ''

    for elem in range(len(lst)):
        if lst[elem] != ' ' and lst[elem] not in ["/", "*"]:
            if lst[elem] == '-':
                if elem == 0:
                    separateElem += lst[elem]
                elif lst[elem-1] in ['-', '+', "/", "*"]:
                    separateElem += lst[elem]

            elif lst[elem] == "+":
                if elem == 0:
                    separateElem += ''
                elif lst[elem-1] in ['-', '+', "/", "*"]:
                    separateElem += ''
            else:
                separateElem += lst[elem]

        if lst[elem] in ["-", '+', "/", "*"]:
            if lst[elem] == '-':
                if elem != 0:

                    if lst[elem-1] not in ['-', '+', "/", "*"]:
                        mainLst.append(separateElem)
                        separateElem = ''
                        mainLst.append(lst[elem])

            elif lst[elem] == "+":
                if elem != 0:

                    if lst[elem-1] not in ['-', '+', "/", "*"]:
                        mainLst.append(separateElem)
                        separateElem = ''
                        mainLst.append(lst[elem])

            else:
                mainLst.append(separateElem)
                separateElem = ''
                mainLst.append(lst[elem])

        if elem == len(lst) - 1:
            mainLst.append(separateElem)

    return mainLst