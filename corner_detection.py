from pylab import *
from numpy import *
from PIL import Image

from PCV.localdescriptors import harris

"""
detecting Harris corner points.
"""


def plot_harris_points(image,filtered_coords):
    """ Plots corners found in image. """
    
    figure()
    gray()
    imshow(image)
    plot([p[1] for p in filtered_coords],
                [p[0] for p in filtered_coords],'.')
    axis('off')
    show()

# open image
# im = array(Image.open("/Users/manish/Desktop/CurrentStudy/drone_doc/thesis3_uav_landing/data_collection/2 landing zone pics May 8 2018/image_16.51.jpg").convert('L'))
# x0 = 140
# y0 = 100
# width = 120
# height = 120
# im = im[y0:y0+height , x0:x0+width]

# im = array(Image.open("/Users/manish/Desktop/CurrentStudy/drone_doc/thesis3_uav_landing/data_collection/2 landing zone pics May 8 2018/image_34.59.jpg").convert('L'))
# x0 = 180
# y0 = 70
# width = 80
# height = 80
# im = im[y0:y0+height , x0:x0+width]



im = array(Image.open("/Users/manish/Desktop/CurrentStudy/drone_doc/thesis3_uav_landing/codes/training/raspberryPiCam/raspCamDiffHeight/m_lspot_obs/at_home2/lspot1/4th/spot3_h1085_x360_y230/pose_test_640_480_p0.159_r0.001_y2.933_a6.920_18_corr.jpg").convert('L'))
x0 = 510
y0 = 256
width = 75
height = 50
im = im[y0:y0+height , x0:x0+width]



# extra_search_factor=1.25
# #obj_detection_result = [0.707006, 0.858284, 0.258291, 0.271830] # for sw1_110.jpg
# obj_detection_result = [0.634343, 0.529298, 0.162226, 0.287609]
# im = array(Image.open("/Users/manish/Desktop/CurrentStudy/drone_doc/thesis3_uav_landing/codes/practise/mav_landing/data/sw1_120.jpg").convert('L'))
# x0 = im.shape[1] * obj_detection_result[0] # shape => row, column
# y0 = im.shape[0] * obj_detection_result[1]
# width = (im.shape[1] * obj_detection_result[2])*extra_search_factor
# height = (im.shape[0] * obj_detection_result[3])*extra_search_factor
# #im = im[y0:y0+height , x0:x0+width]
# im = im[int(y0-height/2):int(y0+height/2) , int(x0-width/2):int(x0+width/2)]



# im = array(Image.open("/Users/manish/Desktop/CurrentStudy/drone_doc/thesis3_uav_landing/codes/training/raspberryPiCam/raspCamDiffHeight/m_lspot_obs/at_home/r0_p0_y0_640_480_h410cm_2.jpg").convert('L'))
# x0 = 337
# y0 = 229
# width = 110
# height = 100
# im = im[y0:y0+height , x0:x0+width]




# detect corners and plot
harrisim = harris.compute_harris_response(im)
#filtered_coords = harris.get_harris_points(harrisim, 20, threshold=0.01) # for  image_16
filtered_coords = harris.get_harris_points(harrisim, 8, threshold=0.01) # for image_34
harris.plot_harris_points(im, filtered_coords)

# plot only 9 strongest
#harris.plot_harris_points(im, filtered_coords[:9])

plot_harris_points(im, filtered_coords[:14])

print (filtered_coords[:9])