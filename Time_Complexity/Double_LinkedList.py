#Doubly Linked List Programme

class Node:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next 
        self.prev = prev

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        """Append a new node at the end of doubly linked list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return 

        last = self.head
        while last.next: # Traverse the last node
            last = last.next

        last.next = new_node
        new_node.prev = last
        
    def print_forward(self):
        """Print forward node in the linked list. node.next"""
        current = self.head 

        while current:
            print(current.data, end='-->')
            current = current.next
        return 
    
    def print_backward(self):
        """Print the linked list in the previous node. node.prev"""
        if not self.head:
            print("Linked list is empty!")
            return 
        
        current = self.head
        #Move to the last node
        while current.next:
            current = current.next
        
        #Traverser back from the last node
        while current:
            print(current.data, end="-->")
            current = current.prev

        return 
    
    def get_last_node(self):
        """Retrieve the last node"""
        current = self.head
        while current.next:
            current = current.next

        #print(f'last node data is: {current.data}')
        #return current # return last node reference 
        return current.data
    
    def get_first_node(self):
        """Retrieve first node"""
        if not self.head:
            print("Doubly Linked List is empty!")
        
        Current = self.head
        print('First node data in the linked list is:', Current.data)
        
    def get_length(self):
        """Get Linked List Length"""
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next
        
        return count
    
   

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.append('Apple')
    dll.append('Orange')
    dll.append('Carrote')
    dll.append('pear')
    dll.get_last_node()
    print("length of Linked List is:", dll.get_length())
    print('Last node is:', dll.get_last_node())
    dll.get_first_node()
    print("List printed forward:")
    #print("List printed backward:")
    #dll.print_backward()
    dll.print_forward()
    
    
   