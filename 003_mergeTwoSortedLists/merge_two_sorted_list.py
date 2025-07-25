class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = Node(0)
    merge = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            merge.next = list1
            list1 = list1.next
        else:
            merge.next = list2
            list2 = list2.next
        merge = merge.next

    if list1:
        merge.next = list1
    elif list2:
        merge.next = list2
    
    return dummy.next



        