""" linked_list.py

Student:Sepehr Mohammadi
Mail: sepehr.mohammadi.1613@student.uu.se
Reviewed by: Michelle Pap
Date reviewed: 04/10/2022
"""


from tkinter import S


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):             # Optional
        count = 1
        if self.first is None:
            return 0
        else:
            f = self.first
            while f.succ:
                count += 1
                f = f.succ
            return count

    def mean(self):               # Optional
        summ = 0
        counter = 0
        f = self.first
        while f:
            summ += f.data
            counter += 1
            f = f.succ 
        return (summ/counter)

    def remove_last(self):        # Optional
        if self.first is None:
            raise Exception('List is Empty')
        elif self.first.succ is None:
            last = self.first.data
            self.first = None
            return last
        else:
            f = self.first
            while f.succ.succ:
                f = f.succ
            last = f.succ.data
            f.succ = None
            return last

    def remove(self, x):          # Compulsory
        if self.__in__(x):
            f = self.first
            prev = None
            if self.first is None:
                raise Exception('List is Empty')
            
            elif self.first.data == x:
                self.first = f.succ 
                return True
            else:
                while f.data != x:
                    prev = f
                    f = f.succ
                    
                prev.succ = f.succ
                return True
        else:
            return False
            

    def count(self, x):           # Optional
        return self._count(self.first, x)
    def _count(self, f,x):           
        if f is None:
            return 0
        elif f.data == x:
            return 1 + self._count(f.succ, x)
        else:
            return self._count(f.succ, x)
        
       
    def to_list(self):            # Compulsory
        return self._to_list(self.first)
    def _to_list(self, f):
        if f is None:
            return []
        else:
            while f:
                return [f.data] + self._to_list(f.succ)
        

    def remove_all(self, x):      # Compulsory   
        self.first =  self._remove_all(self.first, x)
    def _remove_all(self, f,x):
        if f is None:
            return None
        elif f.data == x:
            f = self._remove_all(f.succ,x)
        else:
            f.succ = self._remove_all(f.succ,x)
        return f

    def __str__(self):            # Compulsary
       current = self.first
       if current is None:
           return '()'
       else:
           return '(' + ', '.join(str(x) for x in self) + ')'
           
        
        

    # def copy(self):               # Compulsary
    #     result = LinkedList()
    #     for x in self:
    #         result.insert(x)
    #     return result
        
        
    ''' Complexity for this implementation: 
            tethe (n**2)
    '''
    # def add_to_end(self, x):
    #     f = self.first
    #     #last = self.first
    #     if f:
    #         while f.succ != None:
    #             f = f.succ
    #         f.succ = LinkedList.Node(x, None)
    #         #f.succ = last
    #     else:
    #         self.first = LinkedList.Node(x, None)
    
    
    
    def copy(self):               # Compulsary
        result = LinkedList()                      # Should be more efficient
        lst = self.to_list()
        lst.reverse()
        for i in lst:
            result.insert(i)
        return result
                
    ''' 
    Complexity for this implementation:
        O(n)
    '''

    def __getitem__(self, ind):   # Compulsory
        if self.first is None:
            return None
        elif ind < 0 or ind > self.length():
            return None
        else:
            i = 0
            it = iter(self)
            while True:
                try:
                    val = next(it)
                    if i == ind:
                        return val
                    i += 1
                except StopIteration:
                    break

        
        
class Person:                     # Compulsory to complete
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"
    
    
    def __le__(self,p):
        if self.pnr <= p.pnr:
            return True
        return False
    
    def __lt__(self,p):
        if self.pnr < p.pnr:
            return True
        return False

    def __gt__(self,p):
        if self.pnr > p.pnr:
            return True
        return False

    def __ge__(self,p):
        if self.pnr >= p.pnr:
            return True
        return False

    def __eq__(self,p):
        if self.pnr == p.pnr:
            return True
        return False

    def __ne__(self,p):
        if self.pnr != p.pnr:
            return True
        return False


def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()
    
    # Test code:
    #lst.remove(2)
    #print(lst.remove(2))
    #lst.print()
    #lst.remove_last()
    #print(lst.remove_last())
    lst.remove(3)
    #lst.print()
    print(lst.copy())
    #lst.print()
    #print(lst.to_list())
    


if __name__ == '__main__':
    main()
