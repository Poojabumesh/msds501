import numpy as np

def horizontal_flip(im):
    """
    Perform horizontal flipping on the input image.
    Args:
        im (numpy.ndarray): Input grayscale image represented as a 2D NumPy array.
    Returns:
        numpy.ndarray: Flipped image represented as a 2D NumPy array.
    Example:
        >>> image = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]
        >>> flipped_image = horizontal_flip(image)
        >>> flipped_image
        [[3, 2, 1],
         [6, 5, 4],
         [9, 8, 7]]
    """
    im_flipped = im.copy()
    width, height = im.shape
    im_flipped = im_flipped[:,::-1]
    return im_flipped


def region_avg(im, ic, jc, k=3):
    """
    Calculate the average pixel value within the kxk rectangular region
    centered at the specified coordinates.

    Args:
        im (numpy.ndarray): Input grayscale image represented as a 2D NumPy array.
        ic (int): Row index of the center of the region.
        jc (int): Column index of the center of the region.
        k: size of the region

    Returns:
        float: Average pixel value within the specified region.

    Example:
        >>> image = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]
        >>> region_avg(image, 1, 1)
        5.0
    """
    rows,cols = im.shape
    half_k = k // 2

    
    start_row = max(ic - half_k, 0)
    end_row = min(ic + half_k + 1, rows)
    start_col = max(jc - half_k, 0)
    end_col = min(jc + half_k + 1, cols)
    
    
    region = im[start_row:end_row, start_col:end_col]

    #average value
    mean_region = np.mean(region)
    return mean_region


def blur(im, k=3):
    """Apply a blur filter to the input image using a rectangular averaging.
    Use the region_avg function.

    Args:
        im (numpy.ndarray): Input grayscale image represented as a 2D NumPy array.
        k (int, optional): Size of the rectangular submatrix (default is 3).

    Returns:
        numpy.ndarray: Blurred image represented as a 2D NumPy array.

    """
    rows, cols = im.shape
    
    im_blurred = np.zeros((rows, cols))

    for ic in range(rows):
        for jc in range(cols):
            im_blurred[ic, jc] = region_avg(im, ic, jc, k)
    
    return im_blurred 


def region_median(im, ic, jc, k=3):
    """
    Calculate the median pixel value within the kxk rectangular region
    centered at the specified coordinates.

    Args:
        im (numpy.ndarray): Input grayscale image represented as a 2D NumPy array.
        ic (int): Row index of the center of the region.
        jc (int): Column index of the center of the region.
        k: size of the region

    Returns:
        float: Median pixel value within the specified region.

    Example:
        >>> image = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]
        >>> region_avg(image, 1, 1)
        5.0
    """
    half_k = k // 2
    rows, cols = im.shape

    start_row = max(ic - half_k, 0)
    end_row = min(ic + half_k + 1, rows)
    start_col = max(jc - half_k, 0)
    end_col = min(jc + half_k + 1, cols)

    # Extract the region
    region = im[start_row:end_row, start_col:end_col]
    
    return np.median(region)


def denoise(im, k=3):
    """Apply median filtering to denoise the input grayscale image.
    Apply region_median on each pixel.

    Args:
        im (numpy.ndarray): Input grayscale image represented as a 2D NumPy array.
        k (int, optional): Size of the rectangular region for median filtering (default is 3).

    Returns:
        numpy.ndarray: Denoised image represented as a 2D NumPy array.

    Example:
        >>> image = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]
        >>> denoise(image)
        array([[5, 5, 5],
               [5, 5, 5],
               [5, 5, 5]], dtype=uint8)
    """
    rows, cols = im.shape
    
    im_denoised = np.zeros((rows, cols), dtype=im.dtype)

    for ic in range(rows):
        for jc in range(cols):
            im_denoised[ic, jc] = region_median(im, ic, jc, k)
    
    return im_denoised


def thresholding(im, threshold=100):
    """Apply thresholding to convert the input grayscale image into a binary image.

    Args:
        im (numpy.ndarray): Input grayscale image represented as a 2D NumPy array.
        threshold (int, optional): Threshold value for pixel intensity (default is 100).

    Returns:
        numpy.ndarray: Binary image represented as a 2D NumPy array, where pixels
                       with intensity values above the threshold are set to 255 (white)
                       and pixels below the threshold are set to 0 (black).

    Example:
        >>> image = [[50, 120, 200],
                     [100, 150, 180],
                     [30, 170, 220]]
        >>> thresholding(image, threshold=100)
        array([[  0, 255, 255],
               [  0, 255, 255],
               [  0, 255, 255]], dtype=uint8)
    """
    im_th = im.copy()
    rows,cols = im.shape
    for row in im_th:
        for i in range(cols):
            if row[i] > threshold:
                row[i] = 255
            if row[i] <= threshold:
                row[i] = 0
    return im_th

# center crop changes
def center_crop(im, x_size, y_size):
    """ Perform a center crop on the input image.
    Args:
        im (numpy.ndarray): Input image represented as a 2D NumPy array.
        x_size (int): Desired width of the cropped region.
        y_size (int): Desired height of the cropped region.
    Returns:
        numpy.ndarray: Cropped image represented as a 2D NumPy array.
    Raises:
        ValueError: If the specified crop size is larger than the  dimensions of the image.
    Example:    
        >>> image = [[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],  
                     [11, 12, 13, 14, 15],
                     [16, 17, 18, 19, 20],
                     [21, 22, 23, 24, 25]]
        >>> center_crop(np.array(image), 3, 3)
        array([[ 7,  8,  9],
               [12, 13, 14],
               [17, 18, 19])
    """
        # Get the dimensions of the image
    height, width = im.shape
    
    # Check if the crop size is valid
    if x_size > width or y_size > height:
        raise ValueError("Crop size must be smaller than the dimensions of the image.")
    
    # starting and ending points for the crop
    start_x = (width - x_size) // 2
    end_x = start_x + x_size
    start_y = (height - y_size) // 2
    end_y = start_y + y_size
    
    im_cropped = im[start_y:end_y, start_x:end_x]
    
    return im_cropped
