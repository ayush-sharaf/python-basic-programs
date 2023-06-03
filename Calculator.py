
while True:
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Remainder\n")
    c = int(input("Enter your choice:"))
    match c:
        case 1:
            sum=a+b
            print("The sum is: ",sum)
        case 2:
            diff=a-b
            print("The difference is: ",diff)
        case 3:
            mul=a*b
            print("The multiplication is : ",mul)
        case 4:
            div=a/b
            print("The division is : ",div)
        case 5:
            rem=a%b
            print("The remainer is : ",rem)



