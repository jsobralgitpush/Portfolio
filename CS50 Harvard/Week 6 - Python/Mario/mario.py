import cs50

while True:
    height = cs50.get_int("Height: ")
    if height > 0 and height < 9:
        break

for i in range(height):
    if i == 0:
        print(" " * (height-1), end="")
        print("#" * (i+1), end="")
        print("  ", end="")
        print("#" * (i+1))
        #print(" " * (height))
    else:
        print(" " * (height-i-1), end="")
        print("#" * (i+1), end="")
        print("  ", end="")
        print("#" * (i+1))
        #print(" " * (height-i))
        

# for i in range(height):
#     print("#" * height)