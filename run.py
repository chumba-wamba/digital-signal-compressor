from huffman_coding.compressor import *
from huffman_coding.decompressor import *

if __name__ == '__main__':
    orignal_signal = [1, 2, 2, 2, 2, 3, 3, 3, 4, 1, 1, 1, 1]
    CompressorObject = Compressor(orignal_signal)
    compressed_signal, code_dict = CompressorObject.fixed_length_helper()
    DecompressorObject = Decompressor(compressed_signal, code_dict)
    decompressed_signal = DecompressorObject.decompressor()

    print('\nFixed Length Huffman Coding')
    print('Orignal:', orignal_signal)
    print('Compressed:', compressed_signal)
    print('Decompressed:', decompressed_signal)

    compressed_signal, code_dict_var = CompressorObject.variable_length_helper()
    huffmanTree = CompressorObject.huffman_tree_visualizer()
    print('\nVariable Length Huffman Coding:')
    print('Compressed:', compressed_signal)
    print('Code Dict:', code_dict_var)
    print('Decompressed:', decompressed_signal)
