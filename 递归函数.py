def hanoi(n,a,b,c,d):
    print("n:",n,"a:",a,"b:",b,"c:",c,"d:",d)
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n-1,a,c,b,1) #先将A柱上的n-1个盘子移到B柱子上
        hanoi(1,a,b,c,2) #再将A柱上剩下的一个盘子移到C柱子上
        hanoi(n-1,b,a,c,3) #最后将B柱上的n-1个盘子移到C柱子上

hanoi(3,'A','B','C',0)