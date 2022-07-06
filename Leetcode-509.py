n = int(input())
if n>0:
    son1 = 0
    son2 = 1
    for i in range(n-2):
        son = son2
        son2 = son1+son2
        son1 = son
    print(son1+son2)
else: print(n)