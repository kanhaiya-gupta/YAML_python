import matplotlib.pyplot as plt
import numpy as np
from config import *
  


#print(config_yaml_data)  
if config_old['selection_options']["do_tZq"]:
    print("Hello, there is tZq selection")

if config_old['selection_options']["jet_pt_min"] > 30:
    print("Hello, pt of jet is more than 35 GeV")



# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# #plt.show()
# plt.savefig("test.pdf")


# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100

# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.show()