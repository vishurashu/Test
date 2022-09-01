print("1_add")
print("2_sub")
print("3_milti")
print("4_div")
print(" select correct ")
print("selectone")
selectone=int(input())
match selectone:
    case 1:
        print("enter two number")
        a,b=int(input()),int(input())
        c=a+b
        print(" sum of two number",c)
    case 2:
        print(" enter two number")
        a,b=int(input()),int(input()) 
        c=a-b
        print("differ two number",c)
    case 3:
        print(" enter two number")
        a,b=int(input()),int(input())
        c=a*b
        print(" multipal of two number is ",c)
    case 4:
        print("enter two number")
        a,b,=int(input()),int(input())
        c=a/b
        print("div of two number",c)
print()
  