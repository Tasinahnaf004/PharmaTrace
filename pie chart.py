import matplotlib.pyplot as plt

# Data
labels = ['Apple', 'Banana', 'Cherry', 'Dates']
sizes = [30, 25, 20, 25]

# Plot
plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Fruit Distribution')
plt.axis('equal')  # makes the pie chart a perfect circle

plt.show()
i