def bubble_sort(a):
  for j in range(0, len(a)):
    sorted = True
    for i in range(0,len(a)-j-1):
      if a[i] > a[i+1]:
        key = a[i+1]
        a[i+1] = a[i]
        a[i] = key
        print("Sortowanie przebieg ")
        sorted = False
    if sorted:
      break
