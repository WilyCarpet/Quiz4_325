def letterCounter(myList):
    newList = []
    for word in myList:
        newList.append(len(str(word)))
    return newList



hello = [8,9,'hi']
print(hello)
hello = letterCounter(hello)

print(hello)