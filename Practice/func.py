def my_function():
    print("hello a function")
my_function()

def far_to_cel(fahrenheit):
    celcius=(fahrenheit-32)*5/9
    return celcius

print(far_to_cel(77))
print(far_to_cel(95))
def function(*args):
    print(args)
    print("type",type(args))
function("ami","tumi","she")    

def summetion(*number):
    total=0
    for num in number:
        total+=num
    return total
print(summetion(1,3,5,6)) 

def maximum(*number):
    max=number[0]
    if len(number) == 0:
        return None
    for num in number:
        if num>max:
            max=num
    return max        
max_value=maximum(1,4,35,5,10,11,45)    
print(max_value)