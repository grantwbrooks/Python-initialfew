#Multiples
#this prints odd numbers from 1 to 1000
for i in range(1, 1001):
    if i%2 == 1:
        print i
#or do it like this
for i in range(1,1001,2):
    print i

#this prints all multiples of 5 from 5 to 1,000,000
for i in range(5,1000001):
    if i%5 == 0:
        print i
# or do it like this
for i in range(5,1000001,5):
    print i



#Sum List
#this code sums a list
a = [1, 2, 5, 10, 255, 3]
asum = 0
for numbers in a:
    asum += numbers
print asum
# or use sum function
print "this is the sum:", sum(a)


#Average List
#this code finds the average of a list

avg = asum/len(a)
print "this is the average:", avg




