'''
파일명 : Ex-06-4-while4
'''

dan = 2
while dan <= 9:
    n = 1
    while n <= 9:
        print("{}x{}={}".format(dan, n, dan * n))
        n += 1
    dan += 1
    print()
