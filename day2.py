# def greet(name):
#     print(f"Hello,{name}")
# greet('Pritee')

# def addition(a, b):
#     sum = a + b
#     print(f"The sum is {sum}")
# addition(1,4)

# def add_numbers(num1, num2):
#     return num1 + num2

# result = add_numbers(5,7)
# print("The sum is:", result)

# add = lamda a,b : a+b
# multiply = lamda x,y : x*y
#  print(add(1,2))
# print(multiply(1,2))

# def test(*args):
#     print(args)
# test(1,2,3)

# def is_odd(number):
#     return number % 2 != 0
# result = is_odd(10)
# print(result)

# def elements(input_list):
#     result_list = []
#     for element in input_list:
#         result_list.append(element)
#     return result_list
# given_list = [1, 2, 3, 4, 5]
# output_list = elements(given_list)
# print(output_list)


# def list(num):
#     for i in num:
#         print(i**3)
# list([1,2,3,4,5,6,7])


# def cube_list(num):
#     return [i ** 3 for i in num]

# result = cube_list([1, 2, 3, 4, 5, 6, 7])
# print(result)


# class Calculation:
#     def add(self,a,b):
#         return a+b
#     def sub(self, a, b):
#         return a-b
#     def mul(self, a, b):
#         return a*b
# calculator = Calculation()
# result2 = calculator.add(1,2)
# result3 = calculator.sub(4,3 )
# result4 = calculator.mul(4,3 )
# print(result2)
# print(result3)
# print(result4)

# class Number:
   
#     def cube_list_with_power(num):
#         return [i ** 3 for i in num]
    
   
#     def cube_list_with_multiplication(cls, num):
#         return [i * i * i for i in num]

# def cube_list_with_power(num):
#     return [i ** 3 for i in num]

# def cube_list_with_multiplication(num):
#     return [i * i * i for i in num]

# # Example usage
# result1 = cube_list_with_power([1, 2, 3, 4, 5, 6, 7])
# print("Using power operator:", result1)

# result2 = cube_list_with_multiplication([1, 2, 3, 4, 5, 6, 7])
# print("Using multiplication:", result2)















def cube_elements(input_list):
    result_list = []
    for element in input_list:
        result_list.append(element ** 3)
    return result_list

# Example usage
input_list = [1, 2, 3, 4, 5, 6]
output_list = cube_elements(input_list)
print("Cubed list:", output_list)
