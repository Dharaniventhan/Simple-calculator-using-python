'''
SIMPLE CALCULATOR

1)input 
2)operation
3)


'''

#operation 

def add(a,b):
    return a+b 

def minus(a,b):
    return a-b

def multi(a,b):
    return a*b

def divi(a,b):
    if a==0 or b==0:
        return "Error: Division by zero is not allowed."
       # print("ERROR SINCE ZER0 DIVISION ")
    return a/b
 
#input 

#values of two variables

print("______________________________________________________________________")

try:

    a=int(input("Enter a Number        : "))
    b=int(input("Enter another Number  : "))

except valueError:
    print("enter a valid number")


#operation

operator=input("enter a operator      : ")

#TO VERIFY THE OPERATOR VALID OR NOT

if operator not in ('+','-','*','/'):
    print("....ENTER A VALID OPERATOR....")



#defining an operator and operation


if operator == '+':
    ans=add(a,b)
    print("The Answer is         :", ans)
    
elif operator == '-':
    ans=minus(a,b)
    print("The Answer is          : ", ans)
     
elif operator == '*':
     ans=multi(a,b)
     print("The Answer is          : ",ans)
    
elif operator == '/':
    ans=divi(a,b)
    print("The Answer is          : ",ans)
        
'''

terms used :
    
    operators
    function
    exception handling
    conditional statement

'''

    
    
    
print("________________________________________________________________________")