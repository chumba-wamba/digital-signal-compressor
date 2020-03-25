# Digital-Signal-Compressor
A python project for signal compression viz Huffman Coding which serves as a graded assignment for my Digital Signal and Image Processing course. The script supports both, fixed-length and variable-length (implemented via a min heap data structure) Huffman Coding. 

### Using the Script:
1) Create an object for the Compressor Class
``` 
Compressor=Compressor(orignalSignal) 
```
2) Calculate the frequencies for all signal elements  
```
freqDict=Compressor.freqCounter()
```
3) Calculate the maximum length of the code (only for fixed length Huffman Coding)
```
maxCodeLength=Compressor.maxCodeLength(freqDict)
```
4) Compress the orignal signal using fixed length Huffman Coding
```
compressedSignal,codeDict=Compressor.fixedHuffmanCoding(freqDict, maxCodeLength)
```
Alternatively, one can also use the helper method
```
compressedSignal,codeDict=Compressor.fixedLengthHelper()
```
5) Decompress the compressed signal :)
```
Decompressor1=Decompressor(compressedSignal, codeDict)
decompressedSignal=Decompressor1.decompressor()
```
6) Compress (and then Decompress) the orignal signal using variable length Huffman Coding
```
compressedSignal,codeDictVar=Compressor.variableHuffmanCoding(freqDict)
Decompressor2=Decompressor(compressedSignal, codeDictVar)
decompressedSignal=Decompressor2.decompressor()
```
Helper method
```
compressedSignal,codeDictVar=Compressor.variableLengthHelper()
```
7) Huffman tree visualizer (support only for text based terminal representation) 
```
huffmanTree=Compressor.huffmanTreeVisualizer()
print('Tree:', huffmanTree)
```
