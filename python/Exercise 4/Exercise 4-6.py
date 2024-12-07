from random import uniform

#main
i = n = 0
sample = int(input("please enter the number of random points: "))
while i < sample:
    x = uniform( -1,1)
    y = uniform( -1,1)
    if x*x + y*y < 1:
        n+=1
    i+=1
print("Approximation of pi calculated by", sample,"random points is:", n*4/sample)