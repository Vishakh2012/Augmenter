import cv2
from cv2.typing import MatLike
import numpy as np
class Blur():
    def gaussianBlur(self, image_path: str, kernel_size: int = 15) -> MatLike:
        ''' arguments : image_path : str : path of the image
                        kernel_size : int : size of the kernel
            returns a gaussian blurred image
        '''
        image = cv2.imread(image_path)
        gaussian_blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
        return gaussian_blurred_image

    def medianBlur(self, image_path: str, kernel_size: int = 15) -> MatLike:
        ''' arguments : image_path : str : path of the image
                        kernel_size : int : size of the kernel
            returns a median blurred image
        '''
        image = cv2.imread(image_path)
        median_blurred_image = cv2.medianBlur(image, kernel_size)
        return median_blurred_image
    
    def averageBlur(self, image_path: str, kernel_size: int = 15) -> MatLike:
        ''' arguments : image_path : str : path of the image
                        kernel_size : int : size of the kernel
            returns a average blurred image
        '''
        image = cv2.imread(image_path)
        average_blurred_image = cv2.blur(image, (kernel_size, kernel_size))
        return average_blurred_image 

    def bilateralBlur(self, image_path: str, d: int = 9, sigmaColor: int = 75, sigmaSpace: int = 75) -> MatLike:
        ''' arguments : image_path : str : path of the image
                        d : int : Diameter of each pixel neighborhood that is used during filtering
                        sigmaColor : int : Filter sigma in the color space
                        sigmaSpace : int : Filter sigma in the coordinate space
            returns a bilateral blurred image
        '''
        image = cv2.imread(image_path)
        bilateral_blurred_image = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)
        return bilateral_blurred_image

    def motionBlur(self, image_path: str, kernel_size: int = 15) -> MatLike:
        ''' arguments : image_path : str : path of the image
                        kernel_size : int : size of the kernel
            returns a motion blurred image
        '''
        image = cv2.imread(image_path)
        motion_blur_kernel = np.zeros((kernel_size, kernel_size))
        motion_blur_kernel[int((kernel_size-1)/2), :] = np.ones(kernel_size)
        motion_blur_kernel = motion_blur_kernel / kernel_size
        motion_blurred_image = cv2.filter2D(image, -1, motion_blur_kernel)
        return motion_blurred_image

    def meanShiftBlur(self, image_path: str, spatial_radius: int = 15, color_radius: int = 75) -> MatLike:
        ''' arguments : image_path : str : path of the image
                        spatial_radius : int : The spatial window radius
                        color_radius : int : The color window radius
            returns a mean shift blurred image
        '''
        image = cv2.imread(image_path)
        mean_shift_blurred_image = cv2.pyrMeanShiftFiltering(image, spatial_radius, color_radius)
        return mean_shift_blurred_image


