import random

'''Buggy Quick Sort which creates BST'''
def qSort(li):
    if li == []:
        return []
    p = random.choice(li)
    l = [x for x in li if x < p]
    r = [x for x in li if x > p]
    return [qSort(l)] + [p] + [qSort(r)]


if __name__ == "__main__":
    
    li = [4,2,6,3,5,7,1,9]
    liTree = qSort(li)
    print liTree

