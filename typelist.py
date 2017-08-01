
typelist = ['magical','unicorns']
newstring = ""
runningsum = 0

stringcount = 0
numbercount = 0
stringtype = ""

for item in typelist:
    #string
    if type(item) is str:
        newstring += item + " "
        stringcount += 1
    #number
    if type(item) is int or type(item) is float:
        runningsum += item
        numbercount += 1

#use a count to determine type of list        
if stringcount + numbercount == stringcount:
    stringtype = "string"
if stringcount + numbercount == numbercount:
    stringtype = "number"
else:
    stringtype = "mixed"



print "this is the new string:", newstring
print "this is the running sum:", runningsum
print "the list you entered is of "+ stringtype +"type"

