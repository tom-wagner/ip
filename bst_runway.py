import random


def new_node(time):
    return dict(val=time, left=None, right=None)


class BST:
    def __init__(self):
        self.bst = None

    def can_land(self, time, k):
        if not self.bst:
            return True

        # traverse tree
        # find largest node smaller than time and smallest node larger than time
        # make sure both are at least k away from time
        # if they are return True --> else return False

    def add_time(self, time):
        if not self.bst:
            self.bst = new_node(time)

        node_to_eval = self.bst

        while node_to_eval:
            print(node_to_eval)
            if time < node_to_eval['val']:
                if not node_to_eval['left']:
                    node_to_eval['left'] = new_node(time)
                else:
                    print(node_to_eval)
                    node_to_eval = node_to_eval['left']
            elif time > node_to_eval['val']:
                if not node_to_eval['right']:
                    node_to_eval['right'] = new_node(time)
                else:
                    node_to_eval = node_to_eval['right']
            else:
                return


bst = BST()

for _ in range(100):
    bst.add_time(random.randint(1, 100))


print(bst.bst)


















