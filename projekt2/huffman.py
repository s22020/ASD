import math

global heap_size

def min_heapify(A, i):
  l = 2 * i + 1
  r = 2 * i + 2

  if l < len(A) and A[l] < A[i]:
    smallest = l
  else:
    smallest = i

  if r < len(A) and A[r] < A[smallest]:
    smallest = r

  if smallest != i:
    A[i],A[smallest] = A[smallest],A[i]
    min_heapify(A, smallest)

  #return A

def build_min_heap(A):
  global heap_size
  heap_size = len(A) - 1
  for i in range(math.floor(len(A)/2), -1, -1):
    min_heapify(A, i)
    #print(A)
  #for i in range(len(A)-1, 0, -1):
  #  A[i],A[0] = A[0],A[i]
  #  min_heapify(A, i, 0)
  #print(A)
  #return A


B = [20,3,14,18,15,10]
C = build_min_heap(B)
print(C)


def add_heap(A, i):
    A.append(i)
    build_min_heap(A)

def pop_heap(A):
    global heap_size
    if heap_size < 1:
        return A.pop()
    smallest, A[0] = A[0], A.pop()
    heap_size -= 1
    min_heapify(A,0)
    return smallest
    
    

def make_dictionary(inpt):
    dictionary = {}
    for char in inpt:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary




# wyciaganie 2 najmniejsze elementy ze soba i scalic je zeby kody powstaly
def priority_queue(dictn):
    queue = []
    for key, val in dictn.items():
        add_heap(queue, (val,key))
    return queue


def make_tree(queue):
    while len(queue) > 1:
        x = pop_heap(queue)
        y = pop_heap(queue)
        add_heap(queue, (x[0] + y[0], '', x, y))
    return pop_heap(queue)

def compress(tree, binr, strg):
    if tree[1] != '':
        with open('compressed.txt', 'a') as f:
            f.write(f'{tree[1]}:{binr}\n')
        print(f'{tree[1]}:{binr}')
        strg = strg.replace(tree[1], binr)
        return strg
    strg = compress(tree[2], binr + "1", strg)
    strg = compress(tree[3], binr + "0", strg)
    return strg


def main():
    with open('input.txt', 'r') as f:
        text = f.read()

    dictn = make_dictionary(text)
    print(dictn)
    queue = priority_queue(dictn)
    parent_node = make_tree(queue)

    compressed = compress(parent_node, '', text)
    print("Compressed txt: \n")
    print(compressed)

    with open('compressed.txt', 'a', encoding='utf-8') as w:
        for i in range(0, len(compressed), 8):
            w.write(chr(int(compressed[i:8+i], 2)))

main()




# extract min - petla - dla i =1 do n - 1 (rozmiaru kolejki prio),  wybieram pierwszy element kolejki, zamieniam z ostatnim, ostatni wyjmuje z kolejki i to jest moj x (potrzbeuje x i y zeby je ze soba potem polaczyc i wstawiam jako ostatni element)
# przywracam jeszcze raz wlasnosc kopca (kopiec mi sie psuje bo zamieniam pierwszy z ostatnim), to jeszcze raz zamieniam pierwszy z ostatnim itp - az petla sie skonczy

