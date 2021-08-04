#①

x = lambda :6

#xは関数なので実行するときは()をつける
print(x())

#②
def hello():
    print("hello")
#x2 = lambda : hello カッコ()なしだと実行されない
x2 = lambda : hello()
x2() 

listb = [[x*y for x in'abc'] for y in range(1,3)]
print(listb)