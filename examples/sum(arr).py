arr = [7,3,2,9]

def sum(arr):
    last = arr.pop()
    print("arr=>", arr)
    print("last=>", last)
    result = arr[0] + last

    last = arr.pop()
    print("arr2=>", arr)
    print("last2=>", last)
    result = result + last

    last = arr.pop()
    print("arr3=>", arr)
    print("last3=>", last)
    result = result + last
    return result


result = sum(arr)
print("result=>", result)