# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def toList(a, l1):
            # a.append(str(l1.val))
            if l1.next:
                a.append(str(l1.val))
                toList(a, l1.next)
            else:
                a.append(str(l1.val))
                # print(a)
            return a       
        
        def toListNode(i, re):
            r = ListNode(i)
            r.next = re
            return r
            
        s1 = ''.join(toList([], l1)[:: -1])
        s2 = ''.join(toList([], l2)[:: -1])
        # print(s1,s2)
        sum = str(int(s1) + int(s2))
        # print(type(sum))
        
        re = None
        for i in sum:
            re = toListNode(i, re)
        return re