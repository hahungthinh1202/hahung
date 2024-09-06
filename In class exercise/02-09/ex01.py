
def draw_spruce(height):
    print("a spruce is coming")
    for i in range(1,height):
        print(" "*(height-i-1)+"*"*(i*2-1))
    print(" "*(height-2)+"*")
#main
draw_spruce(6)


