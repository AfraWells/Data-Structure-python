def cutdown(i):
    print(i)
    if i<=0:
        return
    else:
        cutdown(i-1)

cutdown(5)
