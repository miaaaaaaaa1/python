# 1

n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
n3 = int(input("Enter the third number:"))
n = int(input("Select an action: 1 - sum, 2 - product:"))
match n:
    case 1:
        print(n1+n2+n3)
    case 2:
        print(n1*n2*n3) 

# 2
        
c1 = int(input("Enter the first number:"))
c2 = int(input("Enter the second number:"))
c3 = int(input("Enter the third number:"))
c = int(input("Select an action: 1 - max, 2 - min, 3 - ariphmetic mean:"))
max_num = max(c1, c2, c3)
min_num = min(c1, c2, c3)
match c:
   case 1:
        print(max_num)
   case 2:
        print(min_num)
   case 3:
        print((c1+c2+c3)/3)

# 3
        
m = int(input("Enter the number of meters:"))    
s = int(input("Select an action: 1 - miles, 2 - inches, 3 - yards:"))
match s:
   case 1:
        print(m*0,00062137)
   case 2:
        print(m*39,37)
   case 3:
        print(m*1,0936133)


