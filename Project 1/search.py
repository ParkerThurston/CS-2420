'Testing linear Search vs Binary Search vs Jump Search'
from time import perf_counter
from random import seed, sample
import math

def linear_search (lyst, target):
    'searches elements from left to right'
    if len(lyst) == 0:
        return False
    else:
        for x in lyst:
            if  x == target:
                return True
            else:
                continue
        return False

def binary_search (lyst, target):
    'This function starts at the middle and if the target is lesser then or greater then halves the list again in that half and repeats'
    if len(lyst) == 0:
        return False
    middle = len(lyst) //2
    if lyst[middle] == target:
        return True
    elif target < lyst[middle]:
        return binary_search(lyst[:middle], target)
    else:
        return binary_search(lyst[middle + 1:], target)

def jump_search (lyst, target):
    'This function jumps until it pasts the target, then it turn around and does a linear_search'
    jump_dist = round(math.sqrt(len(lyst)))
    if len(lyst) == 0:
        return False
    for x in range(len(lyst)):
        if len(lyst)< (x+1)*jump_dist:
            return linear_search(lyst[(x-1)*jump_dist:], target)
        elif target > lyst[x*jump_dist]:
            continue
        elif lyst[x*jump_dist] == target:
            return True
        elif target < lyst[x*jump_dist]:
            return linear_search(lyst[(x-1)*jump_dist:x*jump_dist], target)

DATA_SIZE = 1000000
def make_data():
    'This function makes the sample data that I use for testing'
    seed(0)
    data = sample(range(DATA_SIZE * 3), k=DATA_SIZE)
    data.sort()
    while True:
        yield data

def main():
    'Main function: test the beginning, middle, and end elements of linear sort, binary sort, and jump search'
    gen = make_data()
    test_lyst=next(gen)

    print("Linear Search")
    print("beginning number")
    start = perf_counter()
    print(linear_search(test_lyst, test_lyst[0]))
    end = perf_counter()
    print(end-start, "seconds")

    print("middle number")
    start = perf_counter()
    print(linear_search(test_lyst, test_lyst[(DATA_SIZE // 2) - 1]))
    end=perf_counter()
    print(end-start, "seconds")

    print("end number")
    start = perf_counter()
    print(linear_search(test_lyst, test_lyst[-1]))
    end=perf_counter()
    print(end-start, "seconds")

    print("number not in list")
    start = perf_counter()
    print(linear_search(test_lyst, DATA_SIZE * 4))
    end = perf_counter()
    print(end-start, "seconds")
    
    print("Binary Search")
    print("beginning number")
    start = perf_counter()
    print(binary_search(test_lyst, test_lyst[0]))
    end = perf_counter()
    print(end-start, "seconds")

    print("middle number")
    start = perf_counter()
    print(binary_search(test_lyst, test_lyst[(DATA_SIZE // 2) - 1]))
    end=perf_counter()
    print(end-start, "seconds")

    print("end number")
    start = perf_counter()
    print(binary_search(test_lyst, test_lyst[-1]))
    end=perf_counter()
    print(end-start, "seconds")

    print("number not in list")
    start = perf_counter()
    print(binary_search(test_lyst, DATA_SIZE * 4))
    end = perf_counter()
    print(end-start, "seconds")

    print("Jump Search")
    print("beginning number")
    start = perf_counter()
    print(jump_search(test_lyst, test_lyst[0]))
    end = perf_counter()
    print(end-start, "seconds")

    print("middle number")
    start = perf_counter()
    print(jump_search(test_lyst, test_lyst[(DATA_SIZE // 2) - 1]))
    end=perf_counter()
    print(end-start, "seconds")

    print("end number")
    start = perf_counter()
    print(jump_search(test_lyst, test_lyst[-1]))
    end=perf_counter()
    print(end-start, "seconds")

    print("number not in list")
    start = perf_counter()
    print(jump_search(test_lyst, DATA_SIZE * 4))
    end = perf_counter()
    print(end-start, "seconds")

if __name__ == "__main__":
    main()
