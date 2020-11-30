# exercise 1

a = int(input("Enter a value: "))
b = int(input("Enter a value: "))


def usr(a,b):
    add = "addition of 2 numbers" , a + b
    sub = "subtraction of 2 numbers" , a - b
    mul = "multiplication of 2 numbers" , a * b
    div = "division of 2 numbers " , (a / b)
    return add , sub, mul, div

result = usr(a,b)
print(result)

# exercise 2
patient_name = input("Enter patient's name: ")
body_temp = int(input("Enter body temp: "))

def covid(patient_name,body_temp):
        if body_temp > 98:
            print("patient body temp ", body_temp, "degrees. Covid patient")
        else:
            print(patient_name," is healthy.")


covid(patient_name,body_temp)







