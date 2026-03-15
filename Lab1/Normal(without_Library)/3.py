# Implement y = 2x12 + 3x1 + 4 and plot x1,# y in the range [start=--10, stop=10, num=100]

start = -10
end = 10
num= 100
step = (end - start) / num

x=[]
for i in range(50,-51, -1):
    x.append(i*step)
y=[]
for xi in x :
    y.append(2*xi**2 + 3*xi +4)

for i in range(num):
    print(f"x= {x[i]:.2f} y= {y[i]:.2f}")

# plot using matplotlib only
import matplotlib.pyplot as plt

plt.plot(x, y)
plt.title(' y = 2x^2 + 3x + 4')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
