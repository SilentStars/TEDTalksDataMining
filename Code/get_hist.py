import matplotlib.pyplot as plt
import numpy as np


def get_hist(list, low_range, high_range, bins):
    average = np.mean(list)
    print('\n' + 'Average: ' + str(average))
    max = np.max(list)
    print('Maximum: ' + str(max))
    min = np.min(list)
    print('Minimum: ' + str(min) + '\n')
    plt.hist(list, range=(low_range, high_range), bins=bins, rwidth=1)
    plt.show()
