import random
# random_num = random.random()
# # the random function will return a floating point number, that is 0.0 <= random_num < 1.0
# #or use...
# random_num = random.randint()

def grade():

    print "Scores and Grades"
    for i in range(0,10):
        random_num = random.randint(60, 100)
        if random_num < 70:
            print "Score: {}; Your grade is D".format(random_num)
        elif random_num < 80:
            print "Score: {}; Your grade is C".format(random_num)
        elif random_num < 90:
            print "Score: {}; Your grade is B".format(random_num)
        else:
            print "Score: {}; Your grade is A".format(random_num)
    print "End of the program. Bye!"


grade()




