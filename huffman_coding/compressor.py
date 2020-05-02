from collections import Counter
from math import log, ceil
import heapq
import copy
from graphviz import Digraph
from huffman_coding.heap_node import HeapNode
from huffman_coding.tree_path import TreePath


class Compressor:
    def __init__(self, orignal_signal):
        self.orignal_signal = orignal_signal

        huffman_tree = Digraph()
        self.huffman_tree = huffman_tree

    def freq_counter(self):
        freq_dict = {}
        for value in self.orignal_signal:
            if value not in freq_dict:
                freq_dict[value] = 0
            freq_dict[value] + = 1

        return freq_dict

    def freq_counter_inbuilt(self):
        return(dict(Counter(self.orignal_signal)))

    def max_code_length(self, freq_dict):
        return(ceil(log(len(freq_dict), 2)))

    def fixed_huffman_coding(self, freq_dict, length):
        orignal_signal = self.orignal_signal
        temp_dict, code_dict = {}, {}

        counter = 0
        for key in freq_dict:
            temp_dict[key] = bin(counter)[2:].zfill(length)
            code_dict[bin(counter)[2:].zfill(length)] = key
            counter + = 1

        compressed_signal = []
        for value in orignal_signal:
            compressed_signal.append(temp_dict[value])

        return compressed_signal, code_dict

    def variable_huffman_coding(self, freq_dict):
        freq_dict = {key: value for key, value in sorted(
            freq_dict.items(), key=lambda item: item[1])}
        heap = []

        for key in freq_dict:
            node = HeapNode(key, freq_dict[key])
            heapq.heappush(heap, node)

        counter = 0
        while(len(heap) > 1):
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)
            node1.flag = 0
            node2.flag = 1

            merged = HeapNode(None, node1.value + node2.value)
            merged.flag = (counter % 2)
            counter + = 1

            self.huffman_tree.node(
                f'{node1.key}, {node1.value}', f'{node1.key}, {node1.value}')  # Graphviz
            self.huffman_tree.node(
                f'{node2.key}, {node2.value}', f'{node2.key}, {node2.value}')  # Graphviz
            self.huffman_tree.node(
                f'None, {node1.value + node2.value}', f'None, {node1.value + node2.value}')  # Graphviz

            self.huffman_tree.edge(
                f'None, {node1.value + node2.value}', f'{node1.key}, {node1.value}')  # Graphviz
            self.huffman_tree.edge(
                f'None, {node1.value + node2.value}', f'{node2.key}, {node2.value}')  # Graphviz

            merged.left, merged.right = node1, node2
            heapq.heappush(heap, merged)

        treePath = TreePath()
        treePath.paths(heap[0])

        temp_dict = treePath.temp_dict_var
        compressed_signal = []
        for elem in self.orignal_signal:
            compressed_signal.append(temp_dict[elem])

        code_dictVar = {}
        for key in temp_dict:
            code_dictVar[temp_dict[key]] = key

        return compressed_signal, code_dictVar

    def huffman_tree_visualizer(self):
        return self.huffman_tree.source
        # self.huffman_tree.render('test.gv', view=True) # Graphviz

    def fixed_length_helper(self):
        freq_dict = self.freq_counter()
        max_code_length = self.max_code_length(freq_dict)
        compressed_signal, code_dict = self.fixed_huffman_coding(
            freq_dict, max_code_length)

        return compressed_signal, code_dict

    def variable_length_helper(self):
        freq_dict = self.freq_counter()
        compressed_signal, code_dictVar = self.variable_huffman_coding(
            freq_dict)

        return compressed_signal, code_dictVar
