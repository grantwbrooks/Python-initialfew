#check types first
x = ['name','address','phone number','social security number']



#if integer do this
if type(x) == int:
    if x >= 100:
        print "That's a big number!"
    else:
        print "That's a small number"

#if string do this
elif type(x) == str:
    if len(x) >= 50:
        print "Long sentence."
    else:
        print "Short sentence."

#if list do this
elif type(x) == list:
    if len(x) >= 10:
        print "Big list!"
    else: 
        print "Short list."


#you can also check type like this:
if isinstance(x,int) == True:
    print "yup"