import sys
input = sys.stdin.readline

num = int(input())
list1 = []
list_ans = []

for i in range(num) :
    list1 = list(map(str, input().split()))
    if list1[0] == "push" :
        list_ans.append(list1[1])
    elif list1[0] == "pop" :
        if list_ans :
            print(list_ans.pop())
        else :
            print("-1")
    elif list1[0] == "size" :
        print(len(list_ans))
    elif list1[0] == "empty" :
        if len(list_ans)== 0 :
            print("1")
        else :
            print("0")
    elif list1[0] == "top" :
        if list_ans :
            print(list_ans[len(list_ans)-1])
        else :
            print("-1")