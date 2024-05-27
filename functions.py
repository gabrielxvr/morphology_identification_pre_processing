import numpy as np
import cv2
from skimage import io

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
    

def remove_background():
    """This function remove the background from a SEM image of a particle
    
    Input:
        cropped_image: image cropped of a specific particle
        
    Output:
        rmbg_cropped_image: image cropped of a specific particle without background
    """
    
def edge_finder():
    """This function will find the edges of a particle
    
    Input:
        rmbg_cropped_image: image cropped of a specific particle without background
        
    Output:
        particle_edges: image with just the edges of a particle
    """
    
