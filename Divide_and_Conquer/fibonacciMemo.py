def fibMemo(n,d = None):
    if d is None:
        d = {0:0,1:1}
    if n not in d:
        d[n] = fibMemo(n-2, d) + fibMemo(n-1, d)
    return d[n]

print fibMemo(100)