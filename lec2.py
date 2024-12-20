# band = "Beatles"
# song = "Yesterday"
# song = "Let it be"
# print(song)
# print (5 + 3)
#print("Game Over")
# salary = 1000
# pay_raise = 100
# print(new_salary)
# new_salary = salary + pay_raise

# car_type = "sedan"
# print(sedan)
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a+b)
# a = int(input())
# b = int(input())
# if a < b :
#     print(a+b)
# elif a < b :
#     print(a-b)
# elif a < b :
#     print(a*b)
# else :
#     print('invailed again')

# str = "pynative"
# print(str[1:3])

# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add(1, "Vicki")
# print(sampleSet)

# var = "James Bond"
# print(var[2::-1])


# def calculate(num1, num2=4):
#     res = num1 * num2
#     print(res)
# calculate(5, 6)

# x = 0
# for i in range(10):
#     for j in range(-1, -10, -1):
#         x += 1
# print(x)


# numbers = [10,20]
# items = ["Chair","Table"]

# for x in numbers:
#     for y in items:
#         print(x, y)

# def outerFun(a, b):
#     def innerFun(c, d):
#         return c + d
#     return innerFun(a, b)
# result = outerFun(5,10)
# print(result)


# var = 10
# for i in range(10):
#     for j in range(2, 10, 1):
#         if var % 2 == 0:
#             continue
#             var += 1
#     var += 1
# else:
#     var += 1
# print(var)



# def f(x = 100, y = 100):
#     return(x+y, x-y)
# x, y = f(y = 200, x = 100)
# print(x, y)


# class stud:
#     def __init__(self, roll_no, grade):
#         self.roll_no = roll_no
#         self.grade = grade
#     def display (self):
#         print("Roll no : ", self.roll_no, ", Grade: ", self.grade)
# stud1 = stud(34, 'S')
# stud1.age=7
# print(hasattr(stud1, 'age'))



# check1 = ['Learn', 'Quiz', 'Practice', 'Contribute']
# check2 = check1
# check3 = check1[:]
# check2[0] = 'Code'
# check3[1] = 'Mcq'
# count = 0
# for c in (check1, check2, check3):
#     if c[0] == 'Code':
#         count += 1
#     if c[1] == 'Mcq':
#         count += 10
# print (count)


# def total(initial = 5, *num, **key):
#     count = initial
#     for n in num:
#         count+=n
#     for k in key:
#         count+=key[k]
#     return count
# print(total(100,2,3, clouds=50, stars=100))


class A:
    def __init__(self, i=100):
        self.i=i
class B(A):
    def __init__(self,j=0):
        self.j=j
def main():
    b= B()
    print(b.i)
    print(b.j)
main()