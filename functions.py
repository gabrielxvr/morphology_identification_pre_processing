import cv2
import numpy as np
from skimage import measure
from skimage.color import rgb2gray
from skimage.feature import canny
from skimage.filters import threshold_otsu
from skimage.io import imread, imsave
from skimage.util import img_as_ubyte

def particles_identification():
    """This function identify and mark the particles in a SEM image.
    
    Input:
        SEM_image: "png"
        
    Output:
        positions_dic: keys are the particles enumerated and the values are the position in (x, y)
    """
    

def crop_image():
    """This function crop the original SEM image into new images for each particle
    
    Input:
        SEM_image: "png"
        positions_dic: keys are the particles enumerated and the values are the position in (x, y)
        
    Output:
        cropped_images_list: list with new images cropped for each particle.
    """
    

def remove_background(cropped_image):
    """This function removes the background from a SEM image of a particle
    
    Input:
        cropped_image: np.array, image cropped of a specific particle
        
    Output:
        rmbg_cropped_image: np.array, image cropped of a specific particle without background
    """

def edge_finder(rmbg_cropped_image):
    """This function finds the edges of a particle
    
    Input:
        rmbg_cropped_image: np.array, image cropped of a specific particle without background
        
    Output:
        particle_edges: np.array, image with just the edges of a particle
    """
    gray_image = rgb2gray(rmbg_cropped_image)
    edges = canny(gray_image)
    
    return edges