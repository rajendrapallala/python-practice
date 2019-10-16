# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
from collections import deque

if __name__ == "__main__":
    n = 3 #int(input())
    for i in range(n):
        dq = deque()
        prt = 'Yes'
        nq = 431 #int(input())
        for x in map(int, input().split()):
            dq.append(x)
        if len(dq) != nq:
            print('No')
            break
        lq = dq.popleft() if dq else 0
        rq = dq.pop() if dq else 0
        prevmin = min(rq,lq)
        while len(dq) > 0 :
            #print(len(dq))
            #if len(dq) < 340:
            #   print("start debug")
            l1 = dq.popleft() if dq else 0
            while l1 != prevmin:
                11 = dq.popleft() if dq else 0
            r1 = dq.pop() if dq else 0
            while r1 != prevmin:
                r1 = dq.pop() if dq else 0
            if l1 > prevmin or r1 > prevmin:
                prt = 'No'
                break
            else:
                prevmin = min(l1,r1)
        print(prt)

'''
from collections import deque 
import sys
for _ in range(input()):
    n = input()
    arr = map(int,raw_input().split())
    for i in arr:
        assert i<=2**31 - 1
    lst = deque(arr)

    curr = 9999999999999999
    flag = 0
    if (len(lst)<=2):
        print "Yes"
        continue
    left = lst.popleft()
    right = lst.pop()
    latest = -1
    while (len(lst)>0):
        flag = 0
        if (left >= right and left <= curr):
            curr = left
            left = lst.popleft()
            latest = left
            flag = 1
        elif (right> left and right <= curr):
            curr = right
            right = lst.pop()
            latest = right
            flag = 1
        if flag == 0:
            break
    if len(lst)>0 or latest > curr:
        print "No"
    else:
        print "Yes"
