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
# for i in range(0, 101):
#     if i % 10 != 3 and i % 10 != 4:
#         print(i, end=' ')

# print("\n--------------------------------------------------------------\n")

#2. while
# i = 0
# while True:
#     if i % 10 != 3 and i % 10 != 4:
#         print(i, end=' ')
#     if i == 100:
#         break
#     i += 1
a, b = map(int, input().split())

class Cacul:
    def __init__(self): #클래스안에 있음 함수는 메소드임
        self.result = 0

    def add(self, num1, num2):
        self.result += num1 + num2 
        return self.result
        #def __str__(self)는 소멸자
car1 = Cacul()
car2 = Cacul()

car1.add(7, 1)
car1.add(8, 90)
car2.add(a, b)

print(car1.result, car2.result)