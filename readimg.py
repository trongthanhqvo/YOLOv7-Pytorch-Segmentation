import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import cv2
import matplotlib.image as img

from PIL import Image
import PIL
 
import numpy
 
def fig2data ( fig ):
    """
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    # draw the renderer
    fig.canvas.draw ( )
 
    # Get the RGBA buffer from the figure
    w,h = fig.canvas.get_width_height()
    buf = numpy.frombuffer( fig.canvas.tostring_rgb(), dtype=numpy.uint8 )
    buf.shape = ( w, h, 3)
 
    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = numpy.roll ( buf, 3, axis = 2 )
    return buf

def fig2img ( fig ):
    """
    @brief Convert a Matplotlib figure to a PIL Image in RGBA format and return it
    @param fig a matplotlib figure
    @return a Python Imaging Library ( PIL ) image
    """
    # put the figure pixmap into a numpy array
    buf = fig2data ( fig )
    # print(buf)
    w, h, d = buf.shape
    print("w:", w)
    print("h:", h)
    print("d:", d)

    return PIL.Image.frombytes( "RGB", ( w ,h ), buf.tobytes() )

def getdata():
#get data
    data = np.array(pd.read_csv("./test.csv"))
    # print(len(data[0]))

    # data /= data.max()/255.0
    print("data= ",data.shape)

    fig = plt.figure()
    ax = fig.add_axes((0, 0, 1, 1))
    ax.get_xaxis().set_visible(False) 
    ax.get_yaxis().set_visible(False)
    ax.imshow(data)
    # fig = plt.imshow(data)

    im = fig2img (fig) 
    opencvImage = cv2.cvtColor(numpy.array(im), cv2.COLOR_RGB2BGR)
    # return opencvImage
    im.show()

getdata()


# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# img = mpimg.imread('your_image.png')
# imgplot = plt.imshow(img)
# plt.show()