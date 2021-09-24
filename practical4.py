class Stack():
    def __init__(self):
        self.items=[1,2,3,4,5]
    
    def enque(self,item):
        self.items.append(item)
        print(item)
    
    def deque(self):
        b=self.items
        b.pop()
        print(b)
    
    def traverse(self):
        a=[]
        l=self.items
        for i in l:
            a.append(i)
            print(a)




if __name__ == "__main__":
    s=Stack()
    print('adding element in the que')
    s.enque(6)
    print('initial queue')
    s.traverse()  
    print('after removing element from the queue')
    s.deque()
