from time import perf_counter


def linear_search (lyst, target):
    if len(lyst) == 0:
        return False
    for x in lyst:
        if  x != target:
            continue
        else:
            return True
            break
    return False

    


def main ():
    test_lyst = [0,1,2,8,13,17,19,32,42]
    start = perf_counter()
    linear_search(test_lyst, 13)
    end = perf_counter()
    print(end-start)

if __name__ == "__main__":
    main()

