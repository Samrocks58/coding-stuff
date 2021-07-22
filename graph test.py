import matplotlib,math
from matplotlib import pyplot, scale


x=0
xlist=[]
ylist=[]
equation=input("What equation do you want to graph? Please use y=mx+b format. No Spaces. ")
points=input("How many points do you want? ")
points=points + "+1"
equation=equation.split("y=")
equation=equation[-1].split("x")
if equation[0] != "":
    equation.insert(1, "*")
    equation.insert(2, "x")
else:
    equation.remove("")
    equation.insert(0, "x")
equation2=""
for i in equation:
    equation2 += i
#equation2="x*x"
#for number in range(1, eval(points)):
i=-1
x=-1
#while eval(equation2) >= 0:
#    ylist.append(eval(equation2))
#    xlist.append(i)
#    x -= 1
#    i -= 1
x=0
i=0
while eval(equation2) < 20:
    ylist.append(eval(equation2))
    xlist.append(i)
    x += 1
    i += 1
print(eval(equation2))
scale=1
scale=int(max(len(ylist), len(xlist)) /8)
if scale == 0:
    scale=1
xticks=[]
yticks=[]

pyplot.plot(ylist, scalex=False, scaley=False, data=None)
pyplot.axis([xlist[0]-2, xlist[-1]+2, ylist[0]-2, ylist[-1]+2])
pyplot.xticks(ticks=[i for i in range(0, 21, 2)])
pyplot.yticks(ticks=[i for i in range(0, 21, 2)])
xlim = pyplot.xlim()
pyplot.ylim(top=xlim[1])
pyplot.show()