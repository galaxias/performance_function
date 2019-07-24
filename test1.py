from scipy.integrate import quad

import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

#----------------------------------------------------------------------------------------#
# Normal Distribution

x_min = 16.0
x_max = 21.0

mean = 18.0
std = 3.0


for num in range(0,9):


    std = 3.0 + 0.3 * num
    #nse = np.random.rand()

    x = np.linspace(x_min, x_max, 100)
    y = scipy.stats.norm.pdf(x, mean, std)

    x_min = x_max
    mean = x_max + 2.0
    x_max = mean + 3.0
    plt.plot(x, y, color='black')

    plt.grid()

    #plt.xlim(0.0, 36.0)

    plt.ylim(0, 0.25)




#----------------------------------------------------------------------------------------#
# integration between x1 and x1

# def normal_distribution_function(x):
#     value = scipy.stats.norm.pdf(x,mean,std)
#     return value
#
# x1 = mean + std
# x2 = mean + 2.0 * std
#
# res, err = quad(normal_distribution_function, x1, x2)
#
# print('Normal Distribution (mean,std):',mean,std)
# print('Integration bewteen {} and {} --> '.format(x1,x2),res)
#
# #----------------------------------------------------------------------------------------#
# # plot integration surface
#
# ptx = np.linspace(x1, x2, 10)
# pty = scipy.stats.norm.pdf(ptx,mean,std)
#
# plt.fill_between(ptx, pty, color='#0b559f', alpha='1.0')

#----------------------------------------------------------------------------------------#



plt.title('Performance Function',fontsize=10)

plt.xlabel('x')
plt.ylabel('Performance')

plt.savefig("performance_function.png")
plt.show()