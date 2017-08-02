



start = [1,2,3,4,5,6,7,8,9,10,11,12]
print "x", " ".join(map(str,start))
for i in range(1,13):
    start = [1,2,3,4,5,6,7,8,9,10,11,12]
    for x in range(0,12):
        start[x] = start[x]*i
    print i, " ".join(map(str,start))





#just testing some stuff from the dict section here

# context = {
#   'questions': [
#    { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
#    { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
#    { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
#    { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
#   ]
#  }

# for key, data in context.items():
#     x = context.items()
#     # print x
#     print data
#     for value in data:
#         print "Question #", value["id"], ": ", value["content"]
        # print "----"
