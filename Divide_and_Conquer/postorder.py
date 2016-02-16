def postorder(preli,inli,root = [],l = [],r = [],i = 0,j = 0):
    if ((preli and inli) != []) and (len(preli) == len(inli)):
        if root == []:
            root.append(preli[0])
            return postorder(preli,inli,root)
        if root != []:
            if j == len(inli):
                return l+r+root #postorder
            if j > 0:
                r.insert(0,inli[j])
                j += 1
                return postorder(preli,inli,root,l,r,i,j)
            if inli[i] != root[0]:
                l.append(inli[i])
                i += 1
                return postorder(preli,inli,root,l,r,i)
            if inli[i] == root[0]:
                j = i+1
                return postorder(preli,inli,root,l,r,i,j)
    
preli = [1,2,3,5]
inli = [2,1,3,5]

print(postorder(preli,inli))
                
        