
print "Find and Replace"
words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
words2 = words.replace("day","month", 1)
print words2

print "Min and Max"
x = [2,54,-2,7,12,98]
print "min is", min(x)
print "max is",max(x)

print "First and Last"
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x)-1]
newx = [x[0], x[len(x)-1]]
print newx

print "New List"
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x

xfirst = x[:len(x)/2]
xlast = x[len(x)/2:]
print xfirst
print xlast
xlast.insert(0,xfirst)
print xlast
