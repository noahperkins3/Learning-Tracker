import sys

class MinHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    # Returns position of parent node for the node currently at pos
    def parent(self, pos):
        return pos//2

    # Returns position of left child for the node currently at pos
    def leftChild(self, pos):
        return 2 * pos

    # Returns position of right child for the node currently at pos
    def rightChild(self, pos):
        return (2 * pos) + 1
    
    # Returns true if the passed node is a leaf node
    def isLeaf(self, pos):
        return pos*2 > self.size
    
    # Swaps two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    # Heapify the node at pos
    def minHeapify(self, pos):
        
        # If the node is a non-leaf node and greater than any of its children
        if not self.isLeaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
                self.Heap[pos] > self.Heap[self.rightChild(pos)]):

                # Swap with the left child and heapfiy the left child
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))

                # Swap with the right child and heapify the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    # Insert node into heap
    def insert(self, element):
        if self.size >= self.maxsize :
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    # Print the contents of the heap
    def Print(self):
        for i in range(1, (self.size//2) + 1):
            print(" PARENT : " + str(self.Heap[i])+ " LEFT CHILD :" +
                  str(self.Heap[2 * i])+" RIGHT CHILD : "+
                  str(self.Heap[2 * i + 1]))

    # Build the min heap using the minHeapify function
    def minHeap(self):
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)

    # Remove and return the minimum element from the heap
    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped
    
