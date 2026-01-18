import matplotlib.pyplot as plt
from numpy.ma.core import append

fruits = ['Apple', 'Banana', 'Cherry', 'Date']
quantity = [10, 15, 7, 12]
plt.bar(fruits,quantity)
plt.xlabel("fruits")
plt.ylabel("quantity")
plt.title("Fruit quantity bar chart")
plt.show()

days = [1, 2, 3, 4, 5, 6, 7]
temperature = [22, 24, 19, 23, 25, 20, 21]
plt.plot(days,temperature, marker = 'o', color = 'red')
plt.xlabel("days")
plt.ylabel("temperature")
plt.title(" day v/s temperature line graph ")
plt.show()