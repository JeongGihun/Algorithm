def solution(data, ext, val_ext, sort_by):
    row = ["code", "date", "maximum", "remain"]
    answer = []
    idx = row.index(ext)
    
    for d in data :
        if val_ext >= int(d[idx]) :
            answer.append(d)
    idx2 = row.index(sort_by)
    answer.sort(key = lambda x : x[idx2])
    
    
    return answer