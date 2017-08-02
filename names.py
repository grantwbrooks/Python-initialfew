students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]





def names(list):
    for i in list:
        print "{} {}".format(i["first_name"],i["last_name"]) 



# names(students)



users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def both(dict):
    for key, data in dict.items():
        print key
        print data
        count = 0
        print key
        for value in data:
            count += 1
            print count,"-", value["first_name"], value["last_name"],"-", len(value["first_name"]+value["last_name"])



both(users) 