import queue
import image_resize as b
str_bits = b.img_to_bits('test.jpg')
freq = b.countLetters(str_bits).items()

ascii_list = [
    '!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ':', ';', '<', '=', '>', '?', '@',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '[', ']', '^', '_', '``',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '{', '|', '}', '~']
print(len)


class HuffmanNode(object):
    def __init__(self, branches=None, root=None):
        self.branches = {}
        self.root = root     # Why?  Not needed for anything.
    def children(self):
        return((self.branches))

def create_tree(frequencies):
    p = queue.PriorityQueue()
    for value in frequencies:  # 1. Create a leaf node for each symbol
        p.put((value[1],value[0]))
                    #    and add it to the priority queue
    while p.qsize() > 2:         # 2. While there is more than one node
        current = []
        i = 0
        curr_freq = 0.0
        while i < len(ascii_list) and p.qsize() > 1:
            c = p.get()
            curr_freq += c[0]
            current.append(c) # 2a. remove two highest nodes
            i += 1
        ''' ThIS IS WHERE I ALTER THE ALGORITHM '''
        node = HuffmanNode(current) # 2b. create internal node with children
        p.put(c, node)
    return p.get()               # 3. tree is complete - return root node

node = create_tree(freq)
print(node)

# Recursively walk the tree down to the leaves,
#   assigning a code value to each symbol
def walk_tree(node, prefix="", code={}):
    return(code)

code = walk_tree(node)
for i in sorted(freq, reverse=True):
    print(i[1], '{:6.2f}'.format(i[0]), code[i[1]])
