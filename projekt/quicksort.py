#A = [7,15,24,1,5,18,9]
#p = 0
#r = len(A)-1

def partition(A,p,r):
  tmp = 0
  x = A[r]
  i = p - 1
  j = p
  for j in range(j,r):
    if A[j] <= x:
      i += 1
      tmp = A[j]
      A[j] = A[i]
      A[i] = tmp
  tmp = A[i+1]
  A[i+1] = A[r]
  A[r] = tmp
  return i+1

def quicksort(A,p,r):
  if p < r:
    q = partition(A,p,r)
    quicksort(A,p,q-1)
    quicksort(A,q+1,r)

#quicksort(A,p,r)
#print(A)
