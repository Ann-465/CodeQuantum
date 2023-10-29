import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('LEA Characteristics.csv') 
categories = data['LEA_NAME']
values = data['LEA_ENR']

plt.bar(categories, values)
plt.xlabel('School Districts')
plt.ylabel('Number of Students')
plt.title('Number of Students per School District')

plt.show()
