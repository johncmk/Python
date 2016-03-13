def min_coin(coin, total):
    if len(coin) == 0 or total == 0:
        return
    cache={}
    for i in range(0,total+1):
        cache[0,i] = i
     
    for i in range(1, len(coin)+1): #row
        for j in range(0, total+1): #col
            if j >= coin[i-1]:
                cache[i,j] = min( cache[i-1,j], 1 + cache[i,j-coin[i-1]])
            else:
                cache[i,j] = cache[i-1,j]
            coin_min = cache[i,j]
    return coin_min
    
if __name__ == "__main__":
    
    coin = [1,5,6,8]
    total = 11
    
#     coin = [25,10,5]
#     total = 30
# 
#     coin = [9,6,5,1]
#     total = 11
    print min_coin(coin, total)