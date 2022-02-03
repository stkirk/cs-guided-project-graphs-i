# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None
# helper to print:
def print_list(start_node):
    current_node = start_node
    while current_node:
        print(current_node.value)
        current_node = current_node.next

# Given a linked list of integers(node), remove and nodes from the linked list that have values that have already occurred in the list
# return the head node of the revised list

def remove_recurring_values(node):
  # create a dictionary of stored node values to add to
  values = {}
  # init current_node starting at head node
  current_node = node
  # init previous_node as None
  previous_node = None
  # while loop through linked list as long as current_node exists
  while current_node:
    # if current_node value is not in values
    if current_node.value not in values:
      # add it to values
      values[current_node.value] = True
      previous_node = current_node
      # keep the node in the list and move current_node to next
      current_node = current_node.next
    # else the current_node value is already in the list
    else:
      # juggle pointers to remove the node
      previous_node.next = current_node.next
      current_node = previous_node.next
  # return new head node
  return node

# test case (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
head = ListNode(3)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(6)
head.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next.next = ListNode(6)

remove_recurring_values(head)
print_list(head) #(3) -> (4) -> (2) -> (6) -> (1) -> N
