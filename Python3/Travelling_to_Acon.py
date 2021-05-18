# import codecademylib3
#import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Plot the histograms
plt.figure(1)
plt.subplot(211)
plt.hist(flights, range=(0,365), bins=365)
plt.title("Flowers in Bloom")
plt.xlabel("Days of Year")
plt.ylabel("Count")
plt.subplot(212)
plt.hist(flights, range=(0,365), bins=365)
plt.title("Flights to Acon")
plt.xlabel("Days of Year")
plt.ylabel("Count")
plt.tight_layout()
plt.show()