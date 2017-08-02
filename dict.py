hello={
    'name':'Grant',
    'age':36,
    'country': 'USA',
    'favlang': 'python'
}


def myself(dict):
    for key, val in dict.items():
        print "{}: {}".format(key,val)



myself(hello)

