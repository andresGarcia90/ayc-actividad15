class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def size(self):
      return self.currentSize

    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i][0] < self.heapList[i // 2][0]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i][1] > self.heapList[mc][1]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2][1] < self.heapList[i*2+1][1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1

# bh = BinHeap()
# bh.buildHeap( [[[5, 9], 2], [[8, 3], 83], [[4, 7], 412], [[0, 6], 454], [[8, 0], 101], [[3, 7], 1], [[1, 4], 679], [[7, 0], 846], [[1, 6], 459], [[8, 9], 893], [[8, 5], 85], [[9, 2], 766], [[2, 8], 336], [[3, 4], 980], [[5, 7], 181], [[7, 1], 683], [[0, 4], 77], [[3, 1], 556], [[2, 1], 872], [[9, 4], 862]])
