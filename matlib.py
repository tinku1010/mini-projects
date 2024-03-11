import matplotlib.pyplot as plt
import numpy as np
# Generate some random data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = np.random.randint(1, 100, size=len(categories))

# Bar chart
plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Pie chart
plt.figure(figsize=(8, 6))
plt.pie(values, labels=categories, autopct='%1.1f%%', colors=['lightcoral', 'lightgreen', 'lightskyblue', 'lightpink'])
plt.title('Pie Chart Example')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()