def print_stair(x):
    for i in range(1, x+1):
        sp = " "*(x-i)
        st = "*"*i
        print(sp + st + " " + st)
        
z=int(input("Enter size of the staircase:"))
print_stair(z)