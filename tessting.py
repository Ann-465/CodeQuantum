import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('LEA Characteristics.csv') 
categories = data['LEA_NAME']
values = data['LEA_ENR']

plt.bar(categories, values)
plt.xlabel('categories')
plt.ylabel('values')
plt.title('The number of students per school district')
plt.show()
