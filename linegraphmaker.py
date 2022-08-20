from matplotlib import pyplot as plt
print("How many x-values does your plot have?")
numxvals=int(input())
datapoints = []
print("What would you like to label the Y-axis? ")
plt.ylabel(input())
print("What would you like to label the X-axis? ")
plt.xlabel(input())
print("What would you like to title the graph to be?")
plt.title(input())
nums = range(0,numxvals)
for i in range(numxvals):
    datapoints.append(int(input("Type the number (Must be an integer) that you would like to plot on the X value of "
                                + str(i+1))))
    print(datapoints)
plt.plot(nums, datapoints)
plt.show()
