import cv2
from cv2.typing import MatLike
import numpy as np
from system_interaction  import  file_interaction
class Blur():
    def gaussian_blur(self, image_path: str, kernel_size: int = 15) -> MatLike:
        ''' arguments : image_path : str : path of the image
                        kernel_size : int : size of the kernel
            returns a gaussian blurred image
        '''
        image = cv2.imread(image_path)
        gaussian_blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
        return gaussian_blurred_image

    def median_blur(self, image_path: str, kernel_size: int = 15) -> MatLike:
        ''' arguments : image_path : str : path of the image
                        kernel_size : int : size of the kernel
            returns a median blurred image
        '''
        image = cv2.imread(image_path)
        median_blurred_image = cv2.medianBlur(image, kernel_size)
        return median_blurred_image
    
    def average_blur(self, image_path: str, kernel_size: int = 15) -> MatLike:
        ''' arguments : image_path : str : path of the image
                        kernel_size : int : size of the kernel
            returns a average blurred image
        '''
        image = cv2.imread(image_path)
        average_blurred_image = cv2.blur(image, (kernel_size, kernel_size))
        return average_blurred_image 

    def bilateral_blur(self, image_path: str, d: int = 9, sigma_color: int = 75, sigma_space: int = 75) -> MatLike:
        ''' arguments : image_path : str : path of the image
                        d : int : Diameter of each pixel neighborhood that is used during filtering
                        sigma_color : int : Filter sigma in the color space
                        sigma_space : int : Filter sigma in the coordinate space
            returns a bilateral blurred image
        '''
        image = cv2.imread(image_path)
        bilateral_blurred_image = cv2.bilateralFilter(image, d, sigma_color, sigma_space)
        return bilateral_blurred_image

    def motion_blur(self, image_path: str, kernel_size: int = 15) -> MatLike:
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

    def mean_shift_blur(self, image_path: str, spatial_radius: int = 15, color_radius: int = 75) -> MatLike:
        ''' arguments : image_path : str : path of the image
                        spatial_radius : int : The spatial window radius
                        color_radius : int : The color window radius
            returns a mean shift blurred image
        '''
        image = cv2.imread(image_path)
        mean_shift_blurred_image = cv2.pyrMeanShiftFiltering(image, spatial_radius, color_radius)
        return mean_shift_blurred_image

    def apply_selected_blurs_on_single_image(self, image_path: str, selected_blurs: list) -> list:
        ''' arguments : image_path : str : path of the image
                        selected_blurs : list : list of blurs to be applied
            returns a list of images after applying selected blurs
        '''
        blurred_images = []
        for blur in selected_blurs:
            if blur == 'gaussian':
                blurred_images.append(self.gaussian_blur(image_path))
            elif blur == 'median':
                blurred_images.append(self.median_blur(image_path))
            elif blur == 'average':
                blurred_images.append(self.average_blur(image_path))
            elif blur == 'bilateral':
                blurred_images.append(self.bilateral_blur(image_path))
            elif blur == 'motion':
                blurred_images.append(self.motion_blur(image_path))
            elif blur == 'mean_shift':
                blurred_images.append(self.mean_shift_blur(image_path))
        return blurred_images 

    def apply_selected_blurs_on_multiple_images(self, directory_path: str, selected_blurs: list) -> list:
        ''' arguments : directory_path : list : list of paths of the images
                        selected_blurs : list : list of blurs to be applied
            returns a list of images after applying selected blurs
        '''
        blurred_images = []

        image_path = file_interaction().get_file_path_within_directory(directory_path)
        for i in range(len(image_path)):
            blurred_images.append(self.apply_selected_blurs_on_single_image(image_path[i], selected_blurs))
        return blurred_images
