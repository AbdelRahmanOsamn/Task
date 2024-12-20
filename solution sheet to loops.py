# q1) Write a program to display only those numbers from a list that satisf the following conditions
# - The number must be divisible by five
# - if the number is greater than 150 , then skip it and move to the next number
# - if the number is greater than 500 , then stop the loop
# اكتب برنامجا لعرض تلك الأرقام فقط من القائمة التي تتوافر فيها الشروط التالية
# - يجب أن يكون العدد قابلاً للقسمة على خمسة
# - إذا كان الرقم أكبر من 150، فتخطاه وانتقل إلى الرقم التالي
# - إذا كان الرقم أكبر من 500، قم بإيقاف الحلقة
# given
# numbers = [12,75,150,180,145,525,50]
# Expected output:
# 75
# 150
# 145
# numbers = [12,75,150,180,145,525,50]
# Iterate through the list
# for num in numbers:
    # Stop the loop if the number is greater than 500
    # if num > 500:
    #     break
    # Skip the number if it is greater than 150
    # if num > 150:
    #     continue
    # Print the number if it is divisible by 5
    # if num % 5 == 0:
    #     print(num)


# Another solution
# Initialize x
# x = 0
# Iterate through the list using a while loop
# while x < len(numbers):
#     number = numbers[x]
    # Stop the loop if the number is greater than 500
    # if number > 500:
    #     break
    # Skip the number if it is greater than 150
    # if number > 150:
    #     x += 1
    #     continue
    # Print the number if it is divisible by 5
    # if number % 5 == 0:
    #     print(number)
    # x += 1

# ------------------------------------------------------------------------

# q2) Write a program to count the total number of digits in a number using a while loop.
# for example, the number is 75869, so the output should be 5
# اكتب برنامجًا لحساب إجمالي عدد الأرقام في رقم باستخدام حلقة while.
# على سبيل المثال، الرقم هو 75869، لذا يجب أن يكون الناتج 5

# Count the total number of digits in a given number
# number = 75869
# count = 0

# while number != 0:
#     number //= 10  # Remove the last digit
#     count += 1

# print("Total number of digits:", count)


# Another solution
# Count the total number of digits in a given number using a for loop
# number = 75869
# count = 0

# for digit in str(number):
#     count += 1

# print("Total number of digits:", count)

# ---------------------------------------------------------------------------
# q3) list = [10,20,30,40,50] 
# List أكتب برنامج لعرض هذه الأرقام من أخر رقم موجود فى ال
# Expected outouts:
# 50
# 40
# 30
# 20
# 10
# list = [10,20,30,40,50]
# for i in list[::-1] :
#     print(i)

# list = [10, 20, 30, 40, 50]
# i =  len(list) -1 #This ensures the index starts from the last valid position
# while i >= 0 :
#     print(list[i])
#     i -= 1
# ---------------------------------------------------------------------
# q4) Exercise 9 : Display numbers from -10 to -1 using for loop 
# for اكتب برنامج عرض الأرقام من -10 إلى -1 باستخدام حلقة 
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1

# for num in range(-10, 0):  
#     print (num)

# num = -10
# while num <= -1:
#     print(num)
#     num += 1  
# ------------------------------------------------------------------------------------
# q5) Excercsise 4 : Write a program to print multiplication table of a given number
# اكتب برنامج لطباعة جدول الضرب لعدد معين
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
# number = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(number * i)

# number = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(number * i)
#     i += 1

# ------------------------------------------------------------------------

# q6) Exercise 12 : Display Fibonacci series up to 10 terms
# The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1
# For example, 0,1,1,2,3,5,8,13,21 The next number in this serise above is 13+21=34.
#عرض سلسلة فيبوناتشي حتى 10 مصطلحات
# تسلسل فيبوناتشي عبارة عن سلسلة من الأرقام. يتم العثور على الرقم التالي عن طريق جمع الرقمين السابقين له. أول رقمين هما 0 و 1
# Expected output:
# Fibonacci sequence:
# 0 1 1 2 3 5 8 13 21 34
# num1, num2 = 0, 1 # These are the first two terms of the Fibonacci sequence. هذان هما أول فترتين من تسلسل فيبوناتشي.
# n_terms = 10 # Specifies the number of terms to generate. يحدد عدد القيم المطلوب إنشاؤها.
# count = 0 #  Counter to track the terms عداد لتتبع القيم
# print("Fibonacci sequence ")
# while count < n_terms: #Runs the loop until 10 terms are displayed. يقوم بتشغيل الحلقة حتى يتم عرض 10 القيم.
#     print(num1, end=", " if count < n_terms - 1 else "\n") # (end=", " or end="\n") Adds a comma after each term, except for the last one. إضافة فاصلة بعد كل مصطلح، باستثناء الأخير
#     nth = num1 + num2 # Calculates the next term in the series. حساب القيمة التالية في السلسلة.
#     num1, num2 = num2, nth # Updates the values for the next iteration. يقوم بتحديث القيم للتكرار التالي
#     count += 1 
