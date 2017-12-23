#coding=utf-8
"""二叉树"""
class Note(object):
    def __init__(self,item = None):
        self.item = item
        self.left_child = None
        self.right_child = None

class ForkTree(object):
    def __init__(self):
        self.root = None

    def add(self,item = None):
        """深度遍历 添加"""
        note = Note(item)
        if self.root is None:
            self.root = note
            return
        queue = [self.root]
        while queue:
            cur_note = queue.pop(0)
            if cur_note.left_child is None:
                cur_note.left_child = note
                return
            else:
                queue.append(cur_note.left_child)
                if cur_note.right_child is None:
                    cur_note.right_child = note
                    return
                else:
                    queue.append(cur_note.right_child)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_note = queue.pop(0)
            print(cur_note.item,end="")
            if cur_note.left_child is not None:
                queue.append(cur_note.left_child)
            if cur_note.right_child is not None:
                queue.append(cur_note.right_child)


    def preorder(self,node = None):
        """先序遍历"""
        if node is None:
            return
        print(node.item ,end="")
        self.preorder(node.left_child)
        self.preorder(node.right_child)

    def inorder(self,note = None):
        """先序遍历"""
        if note is None:
            return
        self.inorder(note.left_child)
        print(note.item ,end="")
        self.inorder(note.right_child)

    def postorder(self,note = None):
        """后序遍历"""
        if note is None:
            return
        self.postorder(note.left_child)
        self.postorder(note.right_child)
        print(note.item,end="")
        
if __name__ == "__main__":
    tree = ForkTree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print("\n"+"*"*50)
    tree.preorder(tree.root)
    print("\n"+"*"*50)
    tree.inorder(tree.root)
    print("\n"+"*"*50)
    tree.postorder(tree.root)




