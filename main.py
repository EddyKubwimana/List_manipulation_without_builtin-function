# sort a list without a built-in function
import time

timing = time.time()

#first function with which focus on comparing two paralel numbers
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
# second algorithm focus on finding a smallest number and arrange the rest compared to that number
def selection_sort (listname):
    index = 0
    while index != len(listname):
        for item in range(index, len(listname)):
            if listname[item] < listname[index]:
                listname[index], listname[item] = listname[item], listname[index]
        index = index+1
    return listname
#merge sort algorithm
def merge(right, left):
    r,l = 0, 0
    sorted_list = []
    while r < len(right) and l < len(left):
        if right[r] > left[l]:
            sorted_list.append(left[l])
            l += 1
        else:
            sorted_list.append(right[r])
            r += 1
    while r < len(right):
        sorted_list.append(right[r])

    while r < len(left):
        sorted_list.append(left[r])
    return sorted_list
def merge_sort(listname):
    if len(listname) < 2:
        return listname
    else :
      middle = len(listname)//2
      first_half = merge_sort(listname[:middle])
      second_half = merge_sort(listname[middle:])
      return merge(first_half, second_half)

#time complexity for sort algorithm

number = [100, 200, 4, 10, -4, 76, 868, 200, 547, 5467, 54, 1, 4.6, 0, 10]
print(sort(number))
print(time.time() - timing)

# analysis of time complexity compare to the builtin function sort
tim2 = time.time()
print(sorted(number))
print(time.time() - tim2)

#time complexity for selection algorithm
tim3 = time.time()
print(selection_sort(number))
print(time.time() - tim3)

#time complexity for merge_sort
tim4 = time.time()
print(merge_sort(number))
print(time.time() - tim4)


