""" bst.py

Student:Sepehr Mohammadi
Mail: sepehr.mohammadi.1613@student.uu.se
Reviewed by: Michelle Pap
Date reviewed: 04/10/2022
"""


import math
import random
from tkinter import N
from linked_list import LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                             # Compulsory
        return self._height(self.root)
    def _height(self,r):
        if r is None:
            return 0
        else:
            return 1 + max(self._height(r.right), self._height(r.left))
        

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      # Compulsory
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)
            # r.left = left subtree with k removed
        elif k > r.key:
            r.right = self._remove(r.right, k)
            # r.right =  right subtree with k removed
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                # temp = r.right
                # r= None
                # return temp
                return r.right
            elif r.right is None:  # Also easy case
                # temp = r.left
                # r = None
                # return temp
                return r.left
            else:  # This is the tricky case.
                minright = r.right          # Find the smallest key in the right subtree
                while minright.left is not None:
                    minright = minright.left
                r.key = minright.key        # Put that key in this node
                r.right = self._remove(r.right, minright.key)                        # Remove that key from the right subtree
        return r   # Remember this! It applies to some of the cases above

    def __str__(self):                            # Compulsory
        if self.root is None:
            return '<>'
        else:
            return '<' + ', '.join(str(x) for x in self) + '>'
        
        # elif current.right is None and current.left:
        #     return '<' + ', '.join(str(x) for x in (current.left)) + ', ' + str(current.key) + '>'
        # elif current.left is None and current.right:
        #     return '<' + ', ' + str(current.key) + ', '.join(str(x) for x in (current.right)) + '>'
        # else:
        #     return '<' + ', '.join(str(x) for x in (current.left)) + ', ' + str(current.key) + ', ' + ', '.join(str(x) for x in (current.right)) + '>'
        

    def to_list(self):                            # Compulsory
        lst = []
        if self.root is None:
            return lst
        else:
            for x in self:
                lst.append(x)
            return lst
        # elif current.right is None and current.left:
        #     for x in current.left:
        #         lst.append(x)
        #     lst.append(current.key)
        #     return lst
        # elif current.left is None and current.right:
        #     lst.append(current.key)
        #     for x in current.right:
        #         lst.append(x)
        #     return lst
        # else:
        #     for x in current.left:
        #         lst.append(x)
        #     lst.append(current.key)
        #     for x in current.right:
        #         lst.append(x)
        #     return lst
    """
    complexity: tetha (n)
    """   

    def to_LinkedList(self):                      # Compulsory
        lst = LinkedList()
        for x in self:
            lst.insert(x)
        return lst


    def ipl(self):                                # Compulsory
        return self._ipl(self.root, 1)
    def _ipl(self, r, l):
        if r is None:
            return 0
        elif r.left is None and r.right is None:
            return l
        elif r.left is None and r.right:
            return l + self._ipl(r.right, l+1)
        elif r.right is None and r.left:
            return l + self._ipl(r.left, l+1)
        else:
            return l + self._ipl(r.right, l+1) + self._ipl(r.left, l+1)
        


def random_tree(n):                               # Useful
    randtree = BST()
    for x in range(0,n):
        randtree.insert(random.random())
    return randtree


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")
    #print(t.height())
    #t.remove(5)
    #t.__str__()
    #print(t.__str__())
    #t.print()
    
    bt = []
    for n in [10,10**2,10**3,10**4,10**5,10**6]:
        bt.append(random_tree(n))
    msg = (
        f'Tree\t' 
        f'size\t'   
        f'height\t'
        f'IPL\t     '    
        f'IPL/size\t'   
        f'1.39*log(n)')
    print(msg)    
    for i in range(len(bt)):
        msg = (
            f'{i+1}\t' 
            f'{bt[i].size()}\t'    
            f'{bt[i].height()}\t'
            f'{bt[i].ipl()}\t        '     
            f'{bt[i].ipl()/bt[i].size():4.2f}\t'    
            f'{1.39*math.log2(bt[i].size()):4.2f}')
        print(msg)

if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size? yes
2. computing height? No
3. contains? Yes
4. insert? No
5. remove? No




Results for ipl of random trees
===============================
Tree	size	height	IPL	     IPL/size	1.39*log(n)
1	    10	    6	    41	        4.10	4.62
2	    100	    14	    711	        7.11	9.23
3	    1000	20	    11908	    11.91	13.85
4	    10000	33	    162027	    16.20	18.47
5	    100000	46	    2102889	    21.03	23.09
6	    1000000	50	    26625331	26.63	27.70

Based on the chart above, it can be referred that IPL/n growas as 1.39*log(n). Therefore:
(IPL) grows as 1.39*n *  log2(n) + O(n)

height for a Binary Search Tree grows adjacent to the best case scenario which is O(log n)
"""
