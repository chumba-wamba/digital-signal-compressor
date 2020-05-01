class Decompressor:
    def __init__(self, compressed_signal, code_dict):
        self.compressed_signal=compressed_signal
        self.code_dict=code_dict

    def decompressor(self):
        orginal_signal=[]
        for value in self.compressed_signal:
            orginal_signal.append(self.code_dict[value])

        return orginal_signal