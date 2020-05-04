from huffman_coding.compressor import *
from huffman_coding.decompressor import *
from scipy.io import wavfile

if __name__ == '__main__':
    fs, orignal_signal = wavfile.read('./test.wav')
    orignal_signal = list(orignal_signal)
    CompressorObject = Compressor(orignal_signal)
    compressed_signal, code_dict = CompressorObject.fixed_length_helper()
    DecompressorObject = Decompressor(compressed_signal, code_dict)
    decompressed_signal = DecompressorObject.decompressor()

    print('\n---Fixed Length Huffman Coding---')
    print('Orignal:', orignal_signal)
    print('Compressed:', compressed_signal)
    print('Decompressed:', decompressed_signal)

    compressed_signal, code_dict_var = CompressorObject.variable_length_helper()
    huffmanTree = CompressorObject.huffman_tree_visualizer()
    print('\n---Variable Length Huffman Coding---')
    print('Compressed:', compressed_signal)
    print('Code Dict:', code_dict_var)
    print('Decompressed:', decompressed_signal)
