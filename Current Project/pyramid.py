import sys
from hashmap import HashMap
from time import perf_counter

WEIGHT = 200
hm = HashMap()

numberofFunctionCalls = 0
numberOfCacheCalls = 0

def weight_on(r,c):
    global numberofFunctionCalls  
    numberofFunctionCalls += 1

    try:
        hm.get((r,c))
    except:
        if r == 0:
            result = 0.0
        elif c == 0:
            result = (WEIGHT + weight_on(r - 1,c))/2.0
        elif r == c:
            result = (WEIGHT + weight_on(r - 1,c - 1))/2.0 
        else:
            result = WEIGHT + (weight_on(r - 1,c - 1) + weight_on(r - 1,c))/2.0
        
        hm.set((r,c), result)

        return result
    else:
        global numberOfCacheCalls  
        numberOfCacheCalls += 1
        return hm.get((r,c))

def main():
    rows = int(sys.argv[1])

    with open("part3.txt", 'w') as f:
        start = perf_counter()

        for i in range(rows):
            for j in range(i + 1):
                print(f'{weight_on(i, j):.2f}', file=f, end=" ")
            print("\n",file=f)
       
        end = perf_counter()

        print(f"Elapsed Time: {end - start} seconds", file = f)
        print(f"Number of function calls: {numberofFunctionCalls}", file = f)
        print(f"Number of cache hits: {numberOfCacheCalls}",file = f)

if __name__ == "__main__":
    main()


