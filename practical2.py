class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        itr=self.head
        llstr=''
        while itr :
            suffix=''
            if itr.next :
                suffix='-->'
            llstr +=str(itr.data)+suffix
            itr=itr.next
        print(llstr)
    def get_length(self):
        count=0
        itr=self.head
        while itr :
            count +=1
            itr=itr.next
        return  count


    def insert_at_end(self,data):
        if self.head is None :
            self.head=Node(data)

        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data)


    def insert_at(self,index,data):
        if index <0 or index > self.get_length():
            raise Exception ("invalid index")
        elif  index==0 :
            self.insert_at_begining(data)

            return
        elif  index ==self.get_length():

            self.insert_at_end(data)
            return

        else:
            itr=self.head
            print("logic")
            count=0
            while itr :
                if count==index-1:
                    node=Node(data,itr.next)
                    itr.next=node
                    break
                itr=itr.next
                count +=1
    def remove_at(self,index):
        if index <0 or index > self.get_length():
            raise Exception ("invalid index")
        if index==0:
            self.head=self.head.next
            return
        itr = self.head
        print("my")
        count = 0
        while itr:
            if count == index - 1:

                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1
    def insert_many(self,data_list):
        self.head=None
        for data in data_list :
            self.head=Node(data,self.head)
    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            return
        if self.head.data==data_after:
            self.head.next=Node(data_to_insert,self.head.next)
            return

        itr=self.head
        while itr :
            if itr.data==data_after:
                itr.next=Node(data_to_insert,itr.next)
                break
            itr=itr.next

    def remove_by_value(self,value):
        if self.head is Node:
            return
        if self.head.data==value:
            self.head=self.head.next
            return

        itr=self.head
        while itr.data.next==value:
            itr.next=itr




if __name__ == '__main__':
    t=LinkedList()
    t.insert_at_begining(5)
    t.insert_at_begining(1)
    t.insert_at_begining(52)
    t.print()
    
    t.insert_at(3,3124)
    t.print()
    
    t.remove_at(2)
    t.print()
    t.insert_many(['tonu','monu','sonu',1,4,6])
    print(t.get_length())
    t.print()
    t.insert_at(2,'bruh')
    t.insert_after_value(4,'noob')
    t.print()

