# from matplotlib import pyplot as plt
# plt.plot([1,2,3],[8,5,3])
# plt.show()

# from matplotlib import pyplot as plt
# x=[1.0, 2.0, 4.0, 6.5]
# y=[1.1, 2.3, 3.0, 5.5]
# plt.bar(x,y)
# plt.xlabel("x value")
# plt.ylabel("y value")
# plt.title('this is test')
# plt.show()

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
gender_values=np.random.choice(['male', 'female'],size=100)
print(gender_values)
data=pd.DataFrame({'gender':gender_values})
print(data)
count=data['gender'].value_counts()
print(count)
count.plot(kind='bar',color=['blue','pink'])
plt.xlabel('gender')
plt.ylabel('counter')
plt.title('GENDER DIFFERENCE')
plt.show()