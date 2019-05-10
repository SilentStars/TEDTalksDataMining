from sklearn import datasets
from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(threshold=np.inf)

digits = datasets.load_digits()
clf = svm.SVC(gamma=0.001, C=100)
clf.fit(digits.data[:-1], digits.target[:-1])

# get one of the data.
def getResult(n):
    return digits.data[n]


# predict, then compare with the image and the target.
correct = 0
n = 0

for _ in [0, np.size(digits.data)/64]:
    result = getResult(n)
    if digits.target[n] == clf.predict([result])[0]:
        correct += 1
    n += 1

print("correct rate: " + str(correct/n*100) + "%")

# result = getResult(n)
# print(clf.predict([result])[0])
# print(digits.target[n])
# result = result.reshape((8, 8))
# plt.imshow(result)
# plt.show()