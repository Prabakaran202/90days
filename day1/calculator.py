num_input1=float(input("enter number 1:-"))
num_input2=float(input("enter number 2 ):-"))
operator =str(input("Operators (+, -, *, /, %):-"))
List =[num_input1,num_input2]
def calculator(a,b):
   if operator == '+' :
       total = num_input1 + num_input2
       return f'{num_input1} + {num_input2}= {int(total)} '
   elif  operator == '-' :
       total = num_input1 - num_input2
       return f'{num_input1} - {num_input2}= {int(total)} '
   elif operator == '*' :
      total = num_input1 * num_input2
      return f'{num_input1}*{num_input2}= {int(total)} '
   elif operator == '/' : 
      total = num_input1 / num_input2
      return f'{num_input1} / {num_input2}= {int(total)} '
   elif operator == '%': 
      total = num_input1 %  num_input2
      return f'{num_input1} % { num_input2}= {int(total)} '
   else:
      print ('input wrong') 
a=calculator(num_input1,num_input2)
print(a)
