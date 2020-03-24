from collections import Counter
from math import log, ceil
import heapq
from pprint import pprint

class HeapNode:
    def __init__(self, key, value):
        self.left=None
        self.right=None
        self.key=key
        self.value=value

    def __gt__(self, other):
        if(other == None):
            return -1
        if(not isinstance(other, HeapNode)):
            return -1
        return self.value > other.value

    def __lt__(self, other):
        if(other == None):
            return -1
        if(not isinstance(other, HeapNode)):
            return -1
        return self.value < other.value

def inorder(root):
    solution=[]

    current=root
    stack=[]
    done=0

    while(True):
        if current is not None:
            stack.append(current)
            current=current.left

        elif(stack):
            current=stack.pop()
            solution.append((current.key,current.value))
            current=current.right

        else:
            break

    return solution

class Compressor:
    def __init__(self, orignalSignal):
        self.orignalSignal=orignalSignal
        self.heap=[]

    def freqCounter(self):
        freqDict={}
        for value in self.orignalSignal:
            if value not in freqDict:
                freqDict[value]=0
            freqDict[value]+=1

        return freqDict

    def freqCounterInbuilt(self):
        return(dict(Counter(self.orignalSignal)))

    def maxCodeLength(self, freqDict):
        return(ceil(log(len(freqDict),2)))

    def fixedHuffmanCoding(self, freqDict, length):
        orignalSignal=self.orignalSignal
        tempDict,codeDict={},{}

        counter=0
        for key in freqDict:
            tempDict[key]=bin(counter)[2:].zfill(length)
            codeDict[bin(counter)[2:].zfill(length)]=key
            counter+=1

        compressedX=[]
        for value in X:
            compressedX.append(tempDict[value])

        return compressedX, codeDict

    def variableHuffmanCoding(self, freqDict):
        freqDict={key: value for key, value in sorted(freqDict.items(), key=lambda item: item[1])}

        for key in freqDict:
            node=HeapNode(key, freqDict[key])
            heapq.heappush(self.heap, node)

        while(len(self.heap)>1):
            node1=heapq.heappop(self.heap)
            node2=heapq.heappop(self.heap)

            merged=HeapNode(None, node1.value+node2.value)
            merged.left=node1
            merged.right=node2

            heapq.heappush(self.heap, merged)

class Decompressor:
    def __init__(self, compressedX, codeDict):
        self.compressedX=compressedX
        self.codeDict=codeDict

    def decompressor(self):
        orginalX=[]
        for value in self.compressedX:
            orginalX.append(self.codeDict[value])

        return orginalX

if __name__ == '__main__':
    X=[1,1,2,2,2,3,4]
    Compressor=Compressor(X)
    freqDict=Compressor.freqCounter()
    maxCodeLength=Compressor.maxCodeLength(freqDict)
    compressedX,codeDict=Compressor.fixedHuffmanCoding(freqDict, maxCodeLength)
    Decompressor=Decompressor(compressedX, codeDict)
    orginalX=Decompressor.decompressor()

    # print('Orignal:',X)
    # print('compressed:',compressedX)
    # if(X==orginalX):
    #     print('Lossless Compression')

    Compressor.variableHuffmanCoding(freqDict)
    heap=Compressor.heap
    inorder=inorder(heap[0])
    print(inorder)
