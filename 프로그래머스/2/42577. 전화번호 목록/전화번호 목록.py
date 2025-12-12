def solution(phone_book):
    ans = True
    phone_book.sort()
    l = len(phone_book)
    for i in range(l) :
        if i == 0 :
            continue
        tmp = len(phone_book[i-1])
        if phone_book[i-1] == phone_book[i][:tmp] :
            ans = False
            break
    return ans