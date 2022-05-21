from heapsort import heap_sort
from quicksort import quicksort
from mergesort import merge_sort
from insertionsort import insertion_sort
from random import random
from timeit import timeit

max_int = 500000
random = [int(random() * 100000) for i in range(0,max_int)]
sort = [i for i in range(0,max_int)]
reverse_sort = [i for i in range(max_int,0,-1)]

print("Heap sort execution time")
print("Random array: {time}".format(time=timeit(lambda: heap_sort(random), number=1)))
print("Sorted array: {time}".format(time=timeit(lambda: heap_sort(sort), number=1)))
print("Reverse sorted array: {time}".format(time=timeit(lambda: heap_sort(reverse_sort), number=1)))
#A = heap_sort(random)
#print(A)
print("\n")


print("Quick sort execution time")
#print("Random array: {time}".format(time=timeit(lambda: quicksort(random, 0, len(random)-1), number=1)))
#print("Sorted array: {time}".format(time=timeit(lambda: quicksort(sort, 0, len(sort)-1), number=1)))
#print("Reverse sorted array: {time}".format(time=timeit(lambda: quicksort(reverse_sort, 0, len(reverse_sort)-1), number=1)))
#B = quicksort(random, 0, len(random)-1)
#print(B)
print("\n")

print("Merge sort execution time")
print("Random array: {time}".format(time=timeit(lambda: merge_sort(random), number=1)))
print("Sorted array: {time}".format(time=timeit(lambda: merge_sort(sort), number=1)))
print("Reverse sorted array: {time}".format(time=timeit(lambda: merge_sort(reverse_sort), number=1)))
#C = merge_sort(random)
#print(C)
print("\n")

print("Insertion sort execution time")
print("Random array: {time}".format(time=timeit(lambda: insertion_sort(random), number=1)))
print("Sorted array: {time}".format(time=timeit(lambda: insertion_sort(sort), number=1)))
print("Reverse sorted array: {time}".format(time=timeit(lambda: insertion_sort(reverse_sort), number=1)))
