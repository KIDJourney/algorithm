from operator import lt

class Heap:
    def __init__(self, cmp=lt):
        self.elements = [0]
        self.heap_size = 0
        self.cmp = cmp

    def up(self, pos):
        while pos // 2 > 0 :
            if not self.cmp(self.elements[pos//2], self.elements[pos]):
                self.elements[pos], self.elements[pos//2] = self.elements[pos//2], self.elements[pos]
            pos = pos // 2
    
    def down(self, pos):
        while pos* 2 <= self.heap_size:
            mc = self.minchild(pos)
            if self.cmp(self.elements[mc] , self.elements[pos]):
                self.elements[mc] , self.elements[pos] = self.elements[pos] , self.elements[mc]
            pos = mc

    def insert(self, element):
        self.elements.append(element)
        self.heap_size += 1
        self.up(self.heap_size)

    def pop(self):
        if self.heap_size <= 0:
            raise ValueError("Not Available elements")
        value = self.elements[1]
        self.elements[1] = self.elements[self.heap_size]
        self.heap_size -= 1 
        self.down(1) 
        return value

    def minchild(self, pos):
        if pos*2+1 > self.heap_size:
            return pos * 2
        else :
            if self.cmp(self.elements[pos*2+1], self.elements[pos * 2]):
                return pos * 2 + 1
            else :
                return pos * 2

    def empty(self):
        return self.heap_size == 0

def show_heap(heap):
    bfs = [1]
    heap_size = len(heap)
    while bfs:
        node = bfs[:]
        bfs = []
        print([heap[i] for i in node])
        for i in node:
            if i * 2 < heap_size:
                bfs.append(i*2)
            if i * 2 + 1 < heap_size:
                bfs.append(i*2 + 1)