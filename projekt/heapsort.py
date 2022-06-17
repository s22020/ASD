import math

def max_heapify(A, n, i):
  l = i * 2 + 1
  r = l + 1

  if l <=  (n - 1) and A[l] > A[i]:
    largest = l
  else:
    largest = i

  if r <= (n - 1) and A[r] > A[largest]:
    largest = r

  if largest != i:
    tmp = A[i]
    A[i] = A[largest]
    A[largest] = tmp
    max_heapify(A, n, largest)

    #return A

def heap_sort(A):
  for i in range(math.floor(len(A)/2), -1, -1):
    max_heapify(A, len(A), i)
  for i in range(len(A)-1, 0, -1):
    tmp = A[i]
    A[i] = A[0]
    A[0] = tmp
    max_heapify(A, i, 0)


#B = [20,3,14,18,15,10]
#C = heap_sort(B)
#print(C)
