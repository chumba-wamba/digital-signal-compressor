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
