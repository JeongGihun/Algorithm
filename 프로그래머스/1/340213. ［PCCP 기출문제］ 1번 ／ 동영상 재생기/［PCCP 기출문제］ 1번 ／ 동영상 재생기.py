def ref(time) :
    return int(time[:2]) * 60 + int(time[3:])

def solution(video_len, pos, op_start, op_end, commands):
    ans = ''
    # 시간 단위로 작성
    ivideo_len = ref(video_len)
    ipos = ref(pos)
    iop_start = ref(op_start)
    iop_end = ref(op_end)
    now = ipos
    if iop_start <= now <= iop_end :
        now = iop_end
    for command in commands :
        if command == "prev" :
            now -= 10     
            now = now if now > 0 else 0
        if command == "next" :
            now += 10
            now = now if now <= ivideo_len else ivideo_len
        if iop_start <= now <= iop_end :
            now = iop_end
            
    ans = f"{now//60:02}"+":"+f"{now%60:02}"
    return ans