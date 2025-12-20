import sys
input = sys.stdin.readline
# 로또는 6개의 수를 뽑는 게임
# 그러기 위해서 사용 리스트, 체크 리스트, 뽑은 갯수가 들어가야 할 듯
stack = []
def rep(board, n) :
    if n == 6 :
        tmp = ' '.join(stack)
        print(tmp)
    for i in range(len(board)) :
        stack.append(str(board[i]))
        rep(board[i+1:], n+1)
        stack.pop()

while True :
    l = list(map(int, input().split()))

    num = l[0]  # 리스트 갯수
    l = l[1:]  # 리스트 재정립
    if num == 0 :
        break
    else :
        rep(l, 0)
    print()