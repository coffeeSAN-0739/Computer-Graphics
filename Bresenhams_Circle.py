import matplotlib.pyplot as plt
r = int(input("Enter radius: "))
x = 0
y = r
p = 3 - 2 * r
while x <= y:
    if p < 0:
        p = p + 4 * x + 6
    else:
        p = p + 4 * (x - y) + 10
        y = y - 1
    x = x + 1
    plt.plot(x, y, marker='o', color='black')
    plt.plot(-x, y, marker='o', color='black')
    plt.plot(x, -y, marker='o', color='black')
    plt.plot(-x, -y, marker='o', color='black')
    plt.plot(y, x, marker='o', color='black')
    plt.plot(-y, x, marker='o', color='black')
    plt.plot(y, -x, marker='o', color='black')
    plt.plot(-y, -x, marker='o', color='black')
    plt.title("Bresenham's Circle Drawing Algorithm")
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
plt.show()
