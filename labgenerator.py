def my_generator(number):
    value=1
    result=1
    for i in range(number):
     yield result
     value=value+1 
     result=value*value    
     
number=int(input())
value= my_generator(number)
print(list(value))
