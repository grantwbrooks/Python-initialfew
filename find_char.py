word_list = ['hello','world','my','name','is','Anna']
char = 'o'

#created function to be put in map function that checks each word for character if it finds it return the word otherwise None is returned
def checkchar(word):
    for letters in word:
        if letters == char:
            return word


#use that function in map then filter out the None vaues
new_list = filter(None,map(checkchar, word_list))
print new_list
# print filter(None,new_list)

