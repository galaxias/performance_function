from scipy.integrate import quad

import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

#----------------------------------------------------------------------------------------#
# Normal Distribution

x_min = 0.0
x_max = 36.0

mean = 18.0
std = 3.0


for num in range(0,2):

    x_min = 36 * num
    x_max = 26.0 + 36 * num
    mean = 18.0 + 36 * num
    std = 3.0 + 3.0 * num
    nse = np.random.rand()

    if num != 0:
        mean = mean - 8.0
        x_min = x_min - 10
    x = np.linspace(x_min, x_max, 100)
    y = scipy.stats.norm.pdf(x, mean, std + nse)

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

plt.savefig("integrate_normal_distribution.png")
plt.show()