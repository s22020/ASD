#a = [5,7,6,3]
def insertion_sort(a):
  for j in range(1, len(a)):
    key = a[j]
    i = j-1
    while i>-1 and a[i] > key:
      a[i+1] = a[i]
      i = i-1
    a[i+1] = key
  return a

#print(a)
