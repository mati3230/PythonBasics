import matplotlib.pyplot as plt

# add a scatter plot
dataset_0 = [1, 10, 12, 0.5, 4, 3, 2, -3]
plt.scatter(
    list(range(len(dataset_0))), # values for x axis
    dataset_0 # values for y axis
)

# add a function plot
dataset_1 = []
for it in range(8):
    dataset_1 += [it ** 2]

plt.plot(dataset_1)

# show plot window
plt.show()
