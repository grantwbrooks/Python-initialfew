import random
# random_num = random.random()

def coins():
    toss = round(random.random())
    print toss

    tails = 0
    heads = 0
    
    print "Starting the program..."
    for i in range(0,5000):
        if round(random.random()) == 1:
            tails += 1
            print "Attempt #{}: Throwing a coin... It's a tails! ... Got {} head(s) so far and {} tail(s) so far".format(i+1,heads,tails)
            "Tails", tails
        elif round(random.random()) == 0:
            heads += 1
            print "Attempt #{}: Throwing a coin... It's a heads! ... Got {} head(s) so far and {} tail(s) so far".format(i+1,tails,heads)
    print "Ending the program, thank you!"


coins()

