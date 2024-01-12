
# 2 Factorial fun times
# 5!= 5 *4*3*2*1 =120
#    res=i*num
#     add = add + res

def fact():
    num = int(input("enter a number:"))
    res = 1
    for i in range(1,num+1):
        res = i * res;

    print("Factorial of", num,"! is:", res)
