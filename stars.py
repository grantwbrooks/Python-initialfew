

# def draw_stars(arr):
#     for i in range(0,len(arr)):
#         print arr[i]*"*"



# x = [4, 6, 1, 3, 5, 7, 25]

# draw_stars(x)



def draw_stars(arr):
    for i in range(0,len(arr)):
        if isinstance(arr[i],int):
            print arr[i]*"*"
        else:
            print (arr[i][0]).lower()*len(arr[i])

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(x)
