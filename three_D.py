import numpy as np 
import rasterio
import mayavi.mlab as mlab
mlab.figure('welcome')
with rasterio.open("tufa-rock-formations-landscape-1.tif") as src:
    elev = src.read(1)
nrows, ncols = elev.shape
x, y = np.meshgrid(np.arange(ncols), np.arange(nrows))
z = elev
mesh = mlab.mesh(x, y, z)
mlab.show()
