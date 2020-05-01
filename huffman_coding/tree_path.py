import copy

class TreePath:  # Issues in this Class
    def __init__(self):
        self.temp_dict_var = {}

    def paths(self, root):
        path = []
        self.paths_rec(root, path, 0)

    def paths_rec(self, root, path, path_len):
        if root is None:
            return

        if(len(path) > path_len):
            path[path_len] = root.flag
        else:
            path.append(root.flag)

        path_len = path_len+1

        if root.left is None and root.right is None:
            self.temp_dict_var[root.key] = copy.deepcopy(
                ''.join(str(char) for char in path[1:]))
        else:
            self.paths_rec(root.left, path, path_len)
            self.paths_rec(root.right, path, path_len)


def inorder(root):
    solution = []

    current = root
    stack = []
    done = 0

    while(True):
        if current is not None:
            stack.append(current)
            current = current.left

        elif(stack):
            current = stack.pop()
            solution.append((current.key, current.value, current.flag))
            current = current.right

        else:
            break

    return solution
