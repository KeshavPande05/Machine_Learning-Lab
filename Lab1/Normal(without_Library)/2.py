# Implement y = 2x1 + 3 and plot x1, y [start=-100, stop=100, num=100]

start = -100
stop = 100
num = 100

step = (stop - start) / num - 1

x1 =[]
for i in range(num):
    x1.append(start + i * step)

y = []
for i in range(num):
    y.append(2*x1[i] +3 )

for i in range(num):
    print(f"x1= {x1[i]:.2f} y= {y[i]:.2f}")

# for plot we have to use matplot 