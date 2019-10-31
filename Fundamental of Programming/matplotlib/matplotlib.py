# Matplotlib.pyplot --- Mainly Used for Data Visualization

import matplotlib.pyplot as plt


# Working with list
plt.plot(list(range(0,4)),list(map(lambda x:x**2,list(range(0,4)))))
plt.grid()
plt.show()

# Give More Desine And Sense in list

plt.plot(list(range(0,4)),list(map(lambda x:x**2,list(range(0,4)))),label='x^2')
plt.plot(list(range(0,4)),list(map(lambda x:x**3,list(range(0,4)))),label='x^3')
plt.plot(list(range(0,4)),list(map(lambda x:x**4,list(range(0,4)))),label='x^4')
plt.legend()
plt.xlabel("X Value")
plt.ylabel("Y Value")
plt.title("Comparisons of Powers")
plt.show()


#Lets Enjoy With Numpy array beacuse it makes Computation fast
import numpy as np
a = np.arange(0,4)
plt.plot(a,a**2)
plt.grid()
plt.show()


# Lets Draw Multiple Diagrammes Using Figure and subplot Concept

plt.figure(1)
plt.subplot(311)
plt.plot(a,a**2,'b-')
plt.subplot(312)
plt.plot(a,a**3,'r--')
plt.subplot(313)
plt.plot(a,a**4)





