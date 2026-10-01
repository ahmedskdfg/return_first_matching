def double(number):  # number is a parameter
    return number*2

result = double(7)       # 7 is an argument; 14 is the return value
print(result)


def calculate_total(price,quantity):
    return price*quantity

x=calculate_total(12,4)
print(x)

def count_above(numbers,threshold):
    y=0


    for number in numbers:
        
        if number>threshold:
            y+=number
    return(y)
ahmed=count_above([4, 10, 15], 10)
print(ahmed)

def sum_losses(amounts):
    z=0

    for number in amounts:
        
        if number<0:
            z+=number
    return(z)
rahaf=sum_losses([20, -10, -5, 0])
print(rahaf)

def contains_negative(negative):
    for number in negative:
        if number>0:
            print("false")
        elif number<0:
            print("True")
        else:
            print("false")
    return
paste=contains_negative([3, 0, -2])
print(paste)

def filter_above(numbers,threshold):
    selected=[] 
    for number in numbers:
        if number>threshold:
            selected.append(number)
    return(selected)
g=filter_above([7, 2, 7], 5)
print(g)      

