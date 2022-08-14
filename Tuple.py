# 튜플
# : 읽기전용 리스트
a = (3,4,5)
b= 3,4,5

c = 10,

e = tuple([3,4,5])
f = list(range(10))
g = tuple(f)

h = 3,4,5
i = list(h)

# 튜플 관련 함수
x = 3,4,6,7
print(max(x))
print(min(x))
print(sum(x))
print(x.count(6))
print(x.index(7))