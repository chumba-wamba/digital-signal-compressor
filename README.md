# Digital-Signal-Compressor
A python project for signal compression viz Huffman Coding which serves as a graded assignment for my Digital Signal and Image Processing course. The script supports both, fixed-length and variable-length (implemented via a min heap data structure) Huffman Coding. 

### Using the Script:
1) Create an object for the Compressor Class
``` 
Compressor=Compressor(orignalSignal) 
```
2) Compress the orignal signal
```
compressedSignal,codeDict=Compressor.fixedLengthHelper()
```
3) Decompress the compressed signal
```
Decompressor1=Decompressor(compressedSignal, codeDict)
decompressedSignal=Decompressor1.decompressor()
```
4) Compress (and then Decompress) the orignal signal using variable length Huffman Coding
```
compressedSignal,codeDictVar=Compressor.variableLengthHelper()
```
5) Huffman tree visualizer (support limited to in-terminal text) 
```
huffmanTree=Compressor.huffmanTreeVisualizer()
print('Tree:', huffmanTree)
```
