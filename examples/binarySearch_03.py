numbers = [1,2,3,4,5,6,7,8,9,10,11]

def binarySearch(arr, targetNum):
    start = 0
    end = len(arr) -1
    while(start <= end):
        midIndex = (start + end) //2
        indexValue = arr[midIndex]
        print(start, end, midIndex, "indexValue:", indexValue)

        if indexValue == targetNum:
            return midIndex
        elif indexValue < targetNum:
            start = midIndex + 1
        elif indexValue > targetNum:
            end = midIndex -1

        print("start:", start, "end:", end, "midIndex:",midIndex, "targetNum:", targetNum, "indexValue:", indexValue)

print(binarySearch(numbers, 4))