import sys

class MaxHeap:
    
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.queue = [0] * (self.maxsize + 1)
        #self.queue[0] = sys.maxsize
        #self.FRONT = 1
    
    def __str__(self):
        return str(self.queue)
    
    def buildHeap(self):
        n = len(self.queue)
        for i in range(n // 2, 0 , -1):
            self.maxHeapify(i, n)
            
    def maxHeapify(self, index, n):
        if not self.isLeaf(index):
            if(self.queue[index] < self.queue[self.leftChild(index)] or self.queue[index] < self.queue[self.rightChild(index)]):
                
                if(self.queue[self.leftChild(index)] > self.queue[self.rightChild(index)]):
                    self.swap(index, self.leftChild(index))
                    self.maxHeapify(self.leftChild(index), 0)
                
                else:
                    self.swap(index, self.rightChild(index))
                    self.maxHeapify(self.rightChild(index), 0)
                    
    def heapSort(self):
        self.buildHeap()
        n = len(self.queue)
        sortedList = []
        for i in range(len(self.queue) - 1, 0, -1):
            sortedList.append(self.queue[0])
            self.queue[0], self.queue[i] = self.queue[i], self.queue[0]
            n = n - 1
            self.maxHeapify(0, n)
        return sortedList
    
    def insert(self, element):
        
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.queue[self.size] = element
        
        current = self.size
        
        while(self.queue[current] > self.queue[self.root(current)]):
            self.swap(current, self.root(current))
            current = self.root(current)
    
    def root(self, index): 
        return index // 2
    
    def leftChild(self, index): 
        return 2 * index

    def rightChild(self, index):
        return (2 * index) + 1
    
    def isLeaf(self, index):
        if index >= (self.size // 2) and index <= self.size:
            return True
        return False
    
    def swap(self, i, parentIndex):
        self.queue[i], self.queue[parentIndex] = self.queue[parentIndex], self.queue[i]

if __name__ == "__main__": 
      
    print('The maxHeap is ') 
      
    maxHeap = MaxHeap(6) 
    maxHeap.insert(7) 
    maxHeap.insert(9) 
    maxHeap.insert(4) 
    maxHeap.insert(8) 
    maxHeap.insert(6) 
    maxHeap.insert(3) 
  
    print("build: ", maxHeap)
    
    sortedList = []
    sortedList = maxHeap.heapSort()
    print("ascending sorted: ", sortedList)