from collections import Counter
from math import log, ceil
import heapq
import copy

class HeapNode:
    def __init__(self, key, value):
        self.left=None
        self.right=None
        self.key=key
        self.value=value
        self.flag=None

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
            solution.append((current.key,current.value,current.flag))
            current=current.right

        else:
            break

    return solution

class TreePath:
    def __init__(self):
        self.codeDictVar={}

    def paths(self, root):
        path = []
        self.pathsRec(root,path,0)

    def pathsRec(self, root, path, pathLen):
        if root is None:
            return

        if(len(path)>pathLen):
            path[pathLen]=root.flag
        else:
            path.append(root.flag)

        pathLen=pathLen+1

        if root.left is None and root.right is None:

            self.codeDictVar[root.key]=copy.deepcopy(''.join(str(char) for char in path[1:]))
        else:
            self.pathsRec(root.left,path,pathLen)
            self.pathsRec(root.right,path,pathLen)

class Compressor:
    def __init__(self, orignalSignal):
        self.orignalSignal=orignalSignal

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
        heap=[]

        for key in freqDict:
            node=HeapNode(key, freqDict[key],)
            heapq.heappush(heap, node)

        counter=0
        while(len(heap)>1):
            node1=heapq.heappop(heap)
            node2=heapq.heappop(heap)
            node1.flag=0
            node2.flag=1

            merged=HeapNode(None, node1.value+node2.value)
            merged.flag=(counter%2)
            counter+=1

            merged.left=node1
            merged.right=node2

            heapq.heappush(heap, merged)

            treePath=TreePath()
            treePath.paths(heap[0])

        return treePath.codeDictVar

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
    X=[1,1,2,2,2,3,4,-1]
    Compressor=Compressor(X)
    freqDict=Compressor.freqCounter()
    maxCodeLength=Compressor.maxCodeLength(freqDict)
    compressedX,codeDict=Compressor.fixedHuffmanCoding(freqDict, maxCodeLength)
    Decompressor=Decompressor(compressedX, codeDict)
    orginalX=Decompressor.decompressor()

    print('Fixed Length Huffman Coding:')
    print('Orignal:',X)
    print('Compressed:',compressedX)
    # if(X==orginalX):
    #     print('Lossless Compression')

    print('Variable Length Huffman Coding:')
    codeDictVar=Compressor.variableHuffmanCoding(freqDict)
    # inorder=inorder(heap[0])
    # print(heap[0].value)
    # print(heap[0].left.key, heap[0].left.value)
    # print(heap[0].right.key, heap[0].right.value)
    # print(heap[0].right.right.key, heap[0].right.right.value)
    # print(heap[0].right.left.key, heap[0].left.right.value)
    # print(heap[0].right.left.left.key, heap[0].right.left.left.value)
    # print(heap[0].right.left.right.key, heap[0].right.left.left.value)
    # print(inorder)

    # TreePath=TreePath()
    # TreePath.paths(heap[0])
    # print(TreePath.codeDictVar)
    print(codeDictVar)
