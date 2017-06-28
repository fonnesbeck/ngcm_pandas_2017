import numpy as np
import dask.array as da

x = da.random.normal(10, 0.1, size=(20000, 20000),
                              chunks=(1000, 1000))
y = x.mean(axis=0)[::100]
