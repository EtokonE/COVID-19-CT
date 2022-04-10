import numpy as np
import matplotlib.pyplot as plt 

import nibabel as nib


def get_single_slice(nimage, slice_number: int):
    """
    Extract single slice from Nifti1Image 
    
    Parameters
    ----------
    nimage : Nifti1Image
            3D image of the lung in nifti1 format
    slice_number : int
            Required slice number
    
    Returns
    -------
    single_slice
        Single slice (m * n)
    """
    raw_slice = nimage.slicer[...,slice_number-1:slice_number].get_fdata()
    single_slice = np.reshape(raw_slice, (np.shape(raw_slice)[0], np.shape(raw_slice)[1]))
    
    return single_slice


def plot_slice_subsample(nimage, grid_shape: int, start: int, step: int) -> None:
    """ 
    Plot subsample of 3D nifti image slices
    
    Parameters
    ----------
    nimage : Nifti1Image
            3D image of the lung in nifti1 format
    grid_shape : int
            Axes grid shape (grid_shape * grid_shape) 
    start : int
            First slice number
    step : int
            Step of rendering slices
            
    Returns
    -------
    None
    """
    fig, ax = plt.subplots(grid_shape, grid_shape, figsize=[12, 12])
    for i in range(grid_shape**2):
        ind = start + i * step
        image_data = get_single_slice(nimage, slice_number=ind+1)

        ax[int(i / grid_shape), int(i % grid_shape)].set_title('slice %d' % ind)
        ax[int(i / grid_shape), int(i % grid_shape)].imshow(image_data, cmap='gray')
        ax[int(i / grid_shape), int(i % grid_shape)].axis('off')
    plt.show()
    

def clip_housenfield_range(ct_slice, level: int, window: int):
    """
    Clip the Housenfield range by choosing a central intensity. 
    
    The Hounsfield scale measures absorption degree of X-ray radiation, 
    where: 
            ---> Air == -1000 intensity
            ---> Water == 0 intensity
            ---> Cortical bones == 1000 intensity
    
    Parameters
    ----------
    ct_slice : numpy.ndarray
            Single slice of the lung in nifti1 format (m*n*1)
    level : int
            Middle intencity level
    window : int
            Window width
    
    Returns
    -------
    clipped_slice
        Slice clipped by window
    """
    
    max = level + window / 2
    min = level - window / 2
    clipped_slice = ct_slice.clip(min, max)
    
    return clipped_slice


