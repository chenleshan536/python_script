# Definition for singly-linked list.
from tkinter import N
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node3=ListNode()
        node4=node3
        node1=list1
        node2=list2
        while(node1!=None and node2!=None):
            if node1.val<node2.val:
                node3.next=node1
               # print(node1.val)
                node3=node3.next
                node1=node1.next
                
            else:
                node3.next=node2
               # print(node2.val)
                node3=node3.next
                node2=node2.next
               
        if node1==None:
            node3.next=node2
        else:
            node3.next=node1

        return node4.next
    
    def mergeTwoArrays(self, list1, list2):
        # list1: [1,3,4]
        # list2: [1,2,4]
        # return [1,1,2,3,4,4]
        i=0
        j=0
        l=[]
        while(i<len(list1) and j<len(list2)):
            if list1[i]<list2[j]:
                l.append(list1[i])
                i =i +1
            else:
                l.append(list2[j])
                j =j +1
        if i > len(list1)-1:
            for x in range(j,len(list2)):
                print(list1[x])
                l.append(list2[x])
        elif j > len(list2)-1:
            for x in range(i,len(list1)):
                print(list2[x])
                l.append(list2[x])




        return l


def printNode(node3):
    tempNode = node3
    while tempNode != None:
        print(tempNode.val)
        tempNode = tempNode.next

calculator = Solution()
# node1 = ListNode(1,None)
# node1.next = ListNode(3, None)
# node1.next.next = ListNode(4,None)
# node2 = ListNode(1,None)
# node2.next = ListNode(2, None)
# node2.next.next = ListNode(4,None)
# node3 = calculator.mergeTwoLists(node1, node2)
# print("node 1")
# printNode(node1)
# print("node 2")
# printNode(node2)
# print('result')
# printNode(node3)
new_array = calculator.mergeTwoArrays([1,3,4], [1,2,4])
print(new_array)
