from collections import Counter
from math import log, ceil
import heapq
import copy
from graphviz import Digraph

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
        self.tempDictVar={}

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
            self.tempDictVar[root.key]=copy.deepcopy(''.join(str(char) for char in path[1:]))
        else:
            self.pathsRec(root.left,path,pathLen)
            self.pathsRec(root.right,path,pathLen)

class Compressor:
    def __init__(self, orignalSignal):
        self.orignalSignal=orignalSignal

        huffmanTree=Digraph()
        self.huffmanTree=huffmanTree

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

        compressedSignal=[]
        for value in orignalSignal:
            compressedSignal.append(tempDict[value])

        return compressedSignal, codeDict

    def variableHuffmanCoding(self, freqDict):
        freqDict={key: value for key, value in sorted(freqDict.items(), key=lambda item: item[1])}
        heap=[]

        for key in freqDict:
            node=HeapNode(key, freqDict[key])
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

            self.huffmanTree.node(f'{node1.key}, {node1.value}', f'{node1.key}, {node1.value}') # Graphviz
            self.huffmanTree.node(f'{node2.key}, {node2.value}', f'{node2.key}, {node2.value}') # Graphviz
            self.huffmanTree.node(f'None, {node1.value+node2.value}', f'None, {node1.value+node2.value}') # Graphviz

            self.huffmanTree.edge(f'None, {node1.value+node2.value}', f'{node1.key}, {node1.value}') # Graphviz
            self.huffmanTree.edge(f'None, {node1.value+node2.value}', f'{node2.key}, {node2.value}') # Graphviz

            merged.left=node1
            merged.right=node2

            heapq.heappush(heap, merged)

        treePath=TreePath()
        treePath.paths(heap[0])

        tempDict=treePath.tempDictVar
        compressedSignal=[]
        for elem in self.orignalSignal:
            compressedSignal.append(tempDict[elem])

        codeDictVar={}
        for key in tempDict:
            codeDictVar[tempDict[key]]=key

        return compressedSignal, codeDictVar

    def huffmanTreeVisualizer(self):
        return self.huffmanTree.source
        # self.huffmanTree.render('test.gv', view=True) # Graphviz

    def fixedLengthHelper(self):
        freqDict=self.freqCounter()
        maxCodeLength=self.maxCodeLength(freqDict)
        compressedSignal,codeDict=self.fixedHuffmanCoding(freqDict, maxCodeLength)

        return compressedSignal, codeDict

    def variableLengthHelper(self):
        freqDict=self.freqCounter()
        compressedSignal,codeDictVar=self.variableHuffmanCoding(freqDict)

        return compressedSignal, codeDictVar

class Decompressor:
    def __init__(self, compressedSignal, codeDict):
        self.compressedSignal=compressedSignal
        self.codeDict=codeDict

    def decompressor(self):
        orginalX=[]
        for value in self.compressedSignal:
            orginalX.append(self.codeDict[value])

        return orginalX

if __name__ == '__main__':
    orignalSignal=[1,2,2,2,2,3,3,3,4,1,1,1,1]
    Compressor=Compressor(orignalSignal)
    compressedSignal,codeDict=Compressor.fixedLengthHelper()
    Decompressor1=Decompressor(compressedSignal, codeDict)
    decompressedSignal=Decompressor1.decompressor()

    print('\nFixed Length Huffman Coding')
    print('Orignal:',orignalSignal)
    print('Compressed:',compressedSignal)
    print('Decompressed:',decompressedSignal)

    compressedSignal,codeDictVar=Compressor.variableLengthHelper()
    huffmanTree=Compressor.huffmanTreeVisualizer()
    print('\nVariable Length Huffman Coding:')
    print('Compressed:',compressedSignal)
    print('Code Dict:',codeDictVar)
    print('Decompressed:',decompressedSignal)
    print('Tree:', huffmanTree)
