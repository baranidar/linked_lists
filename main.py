class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

    
class Linked_List:
  def __init__(self):
    self.head = None
  
    
  def insert_node_at_beginning(self, data):
    if self.head == None: 
      node = Node(data)
      self.head = node
      return
    node = Node(data)
    node.next = self.head
    self.head = node
  
  def insert_node_at_end(self, data):
    if self.head == None:
      node = Node(data)
      self.head = node
      return
    node = Node(data)
    current_node = self.head
    while current_node:
      last_node = current_node
      current_node = current_node.next
    last_node.next = node
    
  def insert_node_at_index(self, data, index):
    cur_pos = 1
    if self.head == None:
      if index == 1:
        node = Node(data)
        self.head = node
        return
    node = Node(data)
    current_node = self.head
    while current_node:
      if cur_pos == index - 1:
        # switch the pointers
        node.next = current_node.next
        current_node.next = node
        return
      current_node = current_node.next
      cur_pos = cur_pos + 1
  
  def find_position_of_data(self, item):
    current_node = self.head
    if self.head == None:
      print("Linked List is empty. Item not found.")
    cur_position = 0
    while current_node:
        cur_position = cur_position + 1
        if current_node.data == item:
          item_founud_at = cur_position
          print(item," was found at position ", cur_position)
          return
        current_node = current_node.next
  
  def delete_by_data(self, item):
    current_node = self.head
    if self.head == None:
      print("Linked List is empty. Cannot delete Item.")
    while current_node:
      if current_node.data == item:
        prev_node.next = current_node.next
        return
      prev_node = current_node
      current_node = current_node.next
  
  def delete_first_node(self):
    current_node = self.head
    if self.head == None:
      print("Linked List is empty. Cannot delete first node.")
    self.head = current_node.next

  def delete_last_node(self):
    current_node = self.head
    if self.head == None:
       print("Linked List is empty. Cannot delete last node.")
    if current_node.next == None:
      self.head = None
      return
    while current_node:
      if current_node.next.next == None:
        current_node.next = None
        return
    current_node = current_node.next

  def delete_node_at_index(self, index):
    cur_pos = 1
    if self.head == None:
      print("Linked List is empty. Cannot delete node by index.")
    current_node = self.head
    if current_node.next == None:
      self.head == None
    while current_node:
      if cur_pos == index - 1:
        current_node.next = current_node.next.next
        return
      current_node = current_node.next
      print(current_node.data)
      cur_pos = cur_pos + 1 
    
    
  def size_of_linked_list(self):
    current_node = self.head
    if self.head == None:
      print("Linked List is empty")
      return
    size = 0
    while current_node:
      size = size + 1
      current_node = current_node.next
    print("Size of Linked list is ", size)  
  
  def print_linked_list(self):
    current_node = self.head
    if self.head == None:
      print("Linked List is empty")
      return
    ll = ""
    while current_node:
      ll = ll + (current_node.data + "-->") if current_node.next is not None else ll + (current_node.data)
      current_node = current_node.next
    print(ll)
    
    
if __name__ == "__main__":
  linked_list = Linked_List()
  linked_list.insert_node_at_beginning("Banana")
  print("Added Banana at the beginning")
  linked_list.print_linked_list()
  linked_list.insert_node_at_beginning("Strawberry")
  print("Added Strawberry at the beginning")
  linked_list.print_linked_list()
  linked_list.insert_node_at_end("Mango")
  print("Added Mango at the end")
  linked_list.print_linked_list()
  linked_list.insert_node_at_index("Blueberry",2)
  print("Added Blueberry at index 2")
  linked_list.print_linked_list()
  linked_list.size_of_linked_list()
  linked_list.find_position_of_data("Banana")
  linked_list.delete_by_data("Blueberry")
  print("Deleted Blueberry")
  linked_list.print_linked_list()
  linked_list.size_of_linked_list()
  linked_list.delete_first_node()
  print("Deleted first node")
  linked_list.print_linked_list()
  linked_list.size_of_linked_list()
  print("Deleted last node")
  linked_list.delete_last_node()
  linked_list.print_linked_list()
  linked_list.size_of_linked_list()
  print("Insert Strawberry at the beginning")
  linked_list.insert_node_at_beginning("Strawberry")
  linked_list.print_linked_list()
  print("Insert Mango at the end")
  linked_list.insert_node_at_end("Mango")
  linked_list.print_linked_list()
  print("Insert Blueberry at index 2")
  linked_list.insert_node_at_index("Blueberry",2)
  linked_list.print_linked_list()
  linked_list.size_of_linked_list()
  print("Deleted index 2")
  linked_list.delete_node_at_index(2)
  linked_list.print_linked_list()
  linked_list.size_of_linked_list()
