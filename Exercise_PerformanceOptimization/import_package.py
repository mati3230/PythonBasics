# in your python file, import the package with the namespace of your choice
import time
import tqdm
import numpy as np

# and now you can use them
my_numpy_array = np.array([[1, 2, 3], [4, 5, 6]])

my_numpy_array_reshaped = np.reshape(my_numpy_array, [np.size(my_numpy_array)])

for element in tqdm.tqdm(my_numpy_array_reshaped, desc="Waiting"):
    time.sleep(element)
