# Digital-Signal-Compressor
A python project for signal compression viz Huffman Coding which serves as a graded assignment for my Digital Signal and Image Processing course. The script supports both, fixed-length and variable-length (implemented via a min heap data structure) Huffman Coding. 

### Using the Script:
1) Create an object of the Compressor Class
``` 
compressor = Compressor(orignal_signal) 
```
2) Compress the orignal signal
```
compressed_signal, code_dict = compressor.fixed_length_helper()
```
3) Decompress the compressed signal
```
decompressor = Decompressor(compressed_signal, code_dict)
decompressed_signal = decompressor.decompressor()
```
4) Compress (and then decompress) the orignal signal using variable length Huffman Coding
```
compressed_signal, code_dict_var = compressor.variable_length_helper()
```
5) Huffman tree visualizer (support limited to in-terminal text) 
```
huffman_tree = compressor.huffman_tree_visualizer()
print('Tree:', huffman_tree)
```
