'Testing quicksort vs mergesort vs insertion sort vs selection sort'
from time import perf_counter
from random import seed, sample

def quicksort (lyst):
    '''This function chooses a midpoint value and moves the points less then it to the left and greater then it to the right then
    repeats again with those two halves'''
    if len(lyst) == 0:
        return lyst
    left_lyst = []
    right_lyst = []
    pivot_point = lyst[0]

    for i in range(len(lyst)):
        if lyst[i] < pivot_point:
            left_lyst.append(lyst[i])
        if lyst[i] > pivot_point:
            right_lyst.append(lyst[i])

    new_lyst = quicksort(left_lyst)
    new_lyst.append(pivot_point)
    new_lyst += quicksort(right_lyst)
    return new_lyst

def mergesort(lyst):
    '''This function divides the list until there is either one element in the list, or its sorted. Then it combies those '''
    def merge(lyst):
        if len(lyst) > 1:

            middle = len(lyst)//2
            left = lyst[:middle]
            right = lyst[middle:]

            merge(left)
            merge(right)

            l_index= 0
            r_index= 0
            i = 0

            while l_index< len(left) and r_index< len(right):
                if left[l_index] < right[r_index]:
                    lyst[i] = left[l_index]
                    l_index+= 1
                else:
                    lyst[i] = right[r_index]
                    r_index+= 1
                i += 1

            while l_index< len(left):
                lyst[i] = left[l_index]
                l_index+= 1
                i += 1

            while r_index< len(right):
                lyst[i] = right[r_index]
                r_index+= 1
                i += 1

    merge(lyst)
    return lyst


def selection_sort (lyst):
    '''This function selects the largest element and moves it to the end of current list and then does the next item until sorted'''    
    for i in range(len(lyst)):
        min_index = i

        for z in range(i+1, len(lyst)):
            if lyst[min_index] > lyst[z]:
                min_index = z
        
           
        lyst[i], lyst[min_index] = lyst[min_index], lyst[i]
    return lyst



def insertion_sort (lyst):
    'this function goes left to right through the elements and adds the next element into the sorted list to the left where it would go'
    for i in range(1, len(lyst)):
        curr_element = lyst[i]
        last_element = i-1

        while last_element >= 0 and curr_element <lyst[last_element]:
            lyst[last_element+1] = lyst[last_element]
            last_element-=1
        lyst[last_element+1] = curr_element

    return lyst

def is_sorted (lyst):
    'This function test to see if the list is sorted or not'
    for items in (range(len(lyst)-1)):
        if lyst[items] > lyst[items+1]:
            return False

    return True


DATA_SIZE = 1000
def make_data():
    'This function makes the sample data that I use for testing'
    seed(0)
    data = sample(range(DATA_SIZE * 3), k=DATA_SIZE)
    return data

def main():
    'Main function: tests quick sort, merge sort, insertion sort, and selection sort'
    gen = make_data()
    test_lyst=gen.copy()
    
    print("Quick Sort")
    start = perf_counter()
    print(quicksort(test_lyst))
    end = perf_counter()
    print(end-start, "seconds")
    
    print("Merge Sort")
    start = perf_counter()
    print(mergesort(test_lyst))
    end = perf_counter()
    print(end-start, "seconds")

    print("Selection Sort")
    start = perf_counter()
    print(selection_sort(test_lyst))
    end = perf_counter()
    print(end-start, "seconds")

    print("Insertion Sort")
    start = perf_counter()
    print(insertion_sort(test_lyst))
    end = perf_counter()
    print(end-start, "seconds")

    print("Is Sort")
    start = perf_counter()
    print(is_sorted(quicksort(test_lyst)))
    end = perf_counter()
    print(end-start, "seconds")

if __name__ == "__main__":
    main()
