import matplotlib.pyplot as plt

points = []

for i in range(4):
    points.append(int(input("Enter coordinate: ")))

x1, y1, x2, y2 = points

dx = x2 - x1
dy = y2 - y1

p = (2 * dy) - dx

x, y = x1, y1

points = []

while x <= x2:

    points.append((x, y))

    if p > 0:
        y = y + 1
        p = p + 2 * (dy - dx)
    else:
        p = p + (2 * dy)

    x = x + 1

for x, y in points:
    plt.plot(x, y, marker='o', color='black')

plt.grid(True)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Bresenham's Line Drawing Algorithm")
plt.show()
