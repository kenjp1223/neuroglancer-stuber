import neuroglancer
import numpy as np
import tifffile # package for reading tiff images


imgpath = r"\\10.159.50.7\LabCommon\Ken\data\OPTRAP\result\AcM-AcM_mean_heatmap.tif"  # path to your tiff image
imgname = "AcM-AcM_mean_heatmap"  # get the image name from the path
img = tifffile.imread(imgpath)
print(img.shape, img.dtype)   # check this first: usually (z, y, x)

dims = neuroglancer.CoordinateSpace(
    names=['x', 'y', 'z'], units='um', scales=[20, 20, 50])  # set your voxel size

viewer = neuroglancer.Viewer()
with viewer.txn() as s:
    s.dimensions = dims
    s.layers[imgname] = neuroglancer.ImageLayer(
        source=neuroglancer.LocalVolume(img.transpose(2, 1, 0), dimensions=dims))

print(viewer)