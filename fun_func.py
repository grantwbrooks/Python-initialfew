#Odd/Even
# def odd_even():
#     for i in range(1, 2001):
#         if i%2 == 0:
#             print "Number is", i ,"This is an even number."
#         elif i%2 == 1:
#             print "Number is",i, "This is an odd number."
#     return 

# odd_even()

#Multiply
# g = [2,4,10,16]
# h = 5


def multia(arr,a):
    arr2 = []
    for i in range(0,len(arr)):
        arr2.append(arr[i]*a)
    print arr2
    return arr2

# multia([2,4,10,16],5)


def layered(arr):
    arr3 = []
    for i in range(0,len(arr)):
        arr3.append([1]*arr[i])
    print arr3
layered(multia([2,4,5],3))






