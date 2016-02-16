def long_sub_seq(st1, st2):
    if len(st1) == 0 or len(st2) == 0:
        return
    c = {}
    max_num = 0
    for i in range(0, len(st1)+1):
        for j in range(0, len(st2)+1):
            if i == 0 or j == 0:
                c[i,j] = 0
            elif st1[i-1] == st2[j-1]:
                c[i,j] = c[i-1,j-1] +1
            else:
                c[i,j] = max(c[i-1,j], c[i,j-1])
            if c[i,j] > max_num:
                max_num = c[i,j]
    return max_num

if __name__ == "__main__":
    print long_sub_seq("acbcf" , "abcdaf")
