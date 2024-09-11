import io

def fibonacci(value):
    if value <= 1:
        return value
    else:
        return (fibonacci(value-1) + fibonacci(value-2))
    

def TakeSomeSpace(value):
    with open("C:\\Users\\nages\\Downloads\\Python + SQL\\Python" + str(value) + ".txt", "w") as f:
        f.write(fibonacci(i) * '0')

value = 17567597987978967
for i in range(value):
    print(fibonacci(i))
    TakeSomeSpace(i)

print('Complete')