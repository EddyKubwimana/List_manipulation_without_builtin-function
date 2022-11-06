# sort a list without a built in function
import time

timing = time.time()


def sort(listname):
    swap = False
    while not swap:
        swap = True
        for i in range(1, len(listname)):

            if listname[i] < listname[i - 1]:
                swap = False
                swapper = listname[i]
                listname[i] = listname[i - 1]
                listname[i - 1] = swapper
    return listname


number = [100, 200, 4, 10, -4, 76, 868, 200, 547, 5467, 54, 1, 4.6, 0, 10]
print(sort(number))
print(time.time() - timing)

# analysis of time complexity compare to the builtin function sort
tim2 = time.time()
print(sorted(number))
print(time.time() - tim2)


