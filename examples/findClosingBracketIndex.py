def findClosingBracketIndex(str, openIndex):
    stack = []
    for index in range(openIndex, len(str)):
        if(str[index] == "["):
            stack.append(str[index])
        elif(str[index] =="]"):
            stack.pop()

        print(stack)
        print(str[index])

    return -1
string = "[[27]HELLO[84]]"
print(findClosingBracketIndex(string, 0))