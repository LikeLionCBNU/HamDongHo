#a = [1,2,3,4]
#b = "아아아아"
#c = 0
#d = "hello"

#print(b+d)
#print(a, c)
#print(a[0],c)


#1. 아아아아hello
#2. [1, 2, 3, 4,] 0
#3. 10

# 0 ~ 100 까지의 숫자 중에서 3과 4로 끝나지 않는 숫자가 출력되도록 하시오.
#1. for
for i in range(0, 101):
    if i % 10 != 3 and i % 10 != 4:
        print(i, end=' ')

print("\n--------------------------------------------------------------\n")

#2. while
i = 0
while True:
    if i % 10 != 3 and i % 10 != 4:
        print(i, end=' ')
    if i == 100:
        break
    i += 1