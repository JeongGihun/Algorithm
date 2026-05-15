from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def chk(list_) :
            cnt = Counter(list_)
            for k, v in cnt.items() :
                if k != "." and v > 1 :
                    return False
            return True

        flag = True
        # X축 확인
        for i in range(9) :
            tmp = board[i]
            if chk(tmp) == False :
                flag = False
        # Y축 확인
        for i in range(9) :
            tmp = list(map(lambda x : x[i], board))
            if chk(tmp) == False :
                flag = False

        # Box 확인
        for i in range(3) :
            for j in range(3) :
                tmp = []
                for k in range(3) :
                    tmp.extend(board[i*3+k][j*3:j*3+3])
                if chk(tmp) == False :
                    flag = False

    
        return flag