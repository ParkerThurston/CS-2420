# # # Python program to insert in a sorted list
 
# # # Node class
# # class Node:
 
# #     # Constructor to initialize the node object
# #     def __init__(self, data):
# #         self.data = data
# #         # self.next = None
# #         pass
 
# # class LinkedList:
 
# #     # Function to initialize head
# #     def __init__(self):
# #         self.head = None
 
# #     def sortedInsert(self, new_node):
         
# #         # Special case for the empty linked list
# #         if self.head is None:
# #             new_node.next = self.head
# #             self.head = new_node
 
# #         # Special case for head at end
# #         elif self.head.data >= new_node.data:
# #             new_node.next = self.head
# #             self.head = new_node
 
# #         else :
 
# #             # Locate the node before the point of insertion
# #             current = self.head
# #             while(current.next is not None and
# #                  current.next.data < new_node.data):
# #                 current = current.next
             
# #             new_node.next = current.next
# #             current.next = new_node
 
# #     # Function to insert a new node at the beginning
# #     # def push(self, new_data):
# #     #     new_node = Node(new_data)
# #     #     new_node.next = self.head
# #     #     self.head = new_node
 
# #     # Utility function to print it the linked LinkedList
# #     def printList(self):
# #         temp = self.head
# #         while(temp):
# #             print( temp.data)
# #             temp = temp.next
 
 
# # # Driver program
# # llist = LinkedList()
# # new_node = Node(5)
# # llist.sortedInsert(new_node)
# # new_node = Node(10)
# # llist.sortedInsert(new_node)
# # new_node = Node(7)
# # llist.sortedInsert(new_node)
# # new_node = Node(3)
# # llist.sortedInsert(new_node)
# # new_node = Node(1)
# # llist.sortedInsert(new_node)
# # new_node = Node(9)
# # llist.sortedInsert(new_node)
# # print( "Create Linked List")
# # llist.printList()
 
# # # This code is contributed by Nikhil Kumar Singh(nickzuck_007)


# # Pyhton implementation of above algorithm
 
# # Node class
# class Node:
     
#     # Constructor to initialize the node object
#     def __init__(self, data):
#         self.data = data
#         self.next = None
 
# # function to sort a singly linked list using insertion sort
# def insertionSort(head_ref):
 
#     # Initialize sorted linked list
#     sorted = None
 
#     # Traverse the given linked list and insert every
#     # node to sorted
#     current = head_ref
#     while (current != None):
     
#         # Store next for next iteration
#         next = current.next
 
#         # insert current in sorted linked list
#         sorted = sortedInsert(sorted, current)
 
#         # Update current
#         current = next
     
#     # Update head_ref to point to sorted linked list
#     head_ref = sorted
#     return head_ref
 
# # function to insert a new_node in a list. Note that this
# # function expects a pointer to head_ref as this can modify the
# # head of the input linked list (similar to push())
# def sortedInsert(head_ref, new_node):
 
#     current = None
     
#     # Special case for the head end */
#     if (head_ref == None or (head_ref).data >= new_node.data):
     
#         new_node.next = head_ref
#         head_ref = new_node
     
#     else:
     
#         # Locate the node before the point of insertion
#         current = head_ref
#         while (current.next != None and
#             current.next.data < new_node.data):
         
#             current = current.next
         
#         new_node.next = current.next
#         current.next = new_node
         
#     return head_ref
 
# # BELOW FUNCTIONS ARE JUST UTILITY TO TEST sortedInsert
 
# # Function to print linked list */
# def printList(head):
 
#     temp = head
#     while(temp != None):
     
#         print( temp.data, end = " ")
#         temp = temp.next
     
# # A utility function to insert a node
# # at the beginning of linked list
# def push( head_ref, new_data):
 
#     # allocate node
#     new_node = Node(0)
 
#     # put in the data
#     new_node.data = new_data
 
#     # link the old list off the new node
#     new_node.next = (head_ref)
 
#     # move the head to point to the new node
#     (head_ref) = new_node
#     return head_ref
 
# # Driver program to test above functions
 
# a = None
# a = push(a, 5)
# a = push(a, 20)
# a = push(a, 4)
# a = push(a, 3)
# a = push(a, 30)
 
# print("Linked List before sorting ")
# printList(a)
 
# a = insertionSort(a)
 
# print("\nLinked List after sorting ")
# printList(a)
 
# # This code is contributed by Arnab Kundu

# import datetime
# x = datetime.datetime.now()
# print(x.strftime("%c"))