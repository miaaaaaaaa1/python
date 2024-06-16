# 1

a = int(input("Enter the number from 1-7:"))
match a:
    case 1:
        print("monday")
    case 2:
        print("tuesday")    
    case 3:
        print("wednesday")       
    case 4:
        print("tuersday")   
    case 5:
        print("friday") 
    case 6:
        print("saturday")  
    case 7:
        print("sunday") 

# 2
        
b = int(input("Enter the number from 1-12:"))
match b:
    case 1:
        print("january")
    case 2:
        print("february")    
    case 3:
        print("march")       
    case 4:
        print("april")   
    case 5:
        print("may") 
    case 6:
        print("june")  
    case 7:
        print("july") 
    case 8:
        print("august")
    case 9:
        print("september")    
    case 10:
        print("october")       
    case 11:
        print("november")   
    case 12:
        print("december")    

# 3
        
c = int(input("Enter the number:"))
if(c>0):
    print("number is positive")  
elif(c<0):
    print("number is negative")   
else:
    print("number is equal to zero")  

# 4
    
d = int(input("Enter the first number:"))
e = int(input("Enter the second number:"))
if(d==e):
    print("numbers are equal")  
elif(d>e):
    print(d,e)  
else:
    print(e,d)  
