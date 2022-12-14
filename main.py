from math import factorial


def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
        return fact


print(iterative_factorial(5))


def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n - 1)
        temp = temp * n


print(recur_factorial(5))


def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


print(recur_factorial(5))


def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i + 1:]
            together = front + back
            permute(together, letter + pocket)


print(permute("ABC", ""))


def permutations(str):
    for p in range(factorial(len(str))):
        print("".join(str))
        i = len(str) - 1
        while i > 0 and str[i - 1] > str[i]:
            i -= 1
            str[i:] = reversed(str[i:])
            if i > 0:
                q = 1
                while str[i - 1] > str[q]:
                    q += 1
                    temp = str[i - 1]
                    str[i - 1] = str[q]
                    str[q] = temp


s = "abc"
s = list(s)
permutations(s)


# linear search
def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


arr = [2, 5, 8, 9, 10, 16, 22]
target = 10
print(search(arr, target))


# binary search iterative
def binary_itr(arr, start, end, target):

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid

    return start


arr = [2, 5, 8, 10, 16, 22, 25]
target = 10
result = binary_itr(arr, 0, len(arr)-1, target)


# binary search recursive
def binary_recur(arr, start, end, target):
    if end >= start:
        mid = start + end - 1 // 2

        if arr[mid] < target:
            binary_recur(arr, mid + 1, end, target)

        elif arr[mid] > target:
            return binary_recur(arr, start, mid - 1, target)
        else:
            return mid
    else:
        return -1


arr = [2, 5, 8, 10, 16, 22, 25]
target = 10
result = binary_recur(arr, 0, len(arr)-1, target)


# bubble sorting
def bubbleSorting(array):
    iterationsNumber = 0
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            iterationsNumber += 1
            if array[j] > arr[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                return array, iterationsNumber


# bubble sorting (alternative)
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def bubbleSort(array):
    iterationsNumber = 0
    for i in array:
        for j in range(len(array)-1):
            iterationsNumber += 1
            if array[j] > array[j+1]:
                swap(array, j, j + 1)
                return array, iterationsNumber


# sorting (insert)
def insertSort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j-1
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i -= 1
            array[i + 1] = key
            return array
