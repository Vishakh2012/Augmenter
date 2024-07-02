import  cv2
from cv2.typing import MatLike
from system_interaction.file_interaction import file_interaction

class Pooling():
    """functions for various pooling but the size of the image remains consistent"""
    def __init__(self) -> None:
        pass
    
    def max_pooling(self, img_path: str, kernel_size: int) -> MatLike:
        """max pooling of an image
        arguments : img_path : str : path of the image
                    kernel_size : int : size of the kernel
        returns : np.ndarray : max pooled image
        """
        img = cv2.imread(img_path)
        max_pooled_img = cv2.resize(img, (img.shape[1]//kernel_size, img.shape[0]//kernel_size), interpolation=cv2.INTER_AREA)
        max_pooled_img = cv2.resize(max_pooled_img, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)
        return max_pooled_img
    
    def mean_pooling(self, img_path: str, kernel_size: int = 15) -> MatLike:
        """mean pooling of an image
        arguments : img_path : str : path of the image
                    kernel_size : int : size of the kernel
        returns : np.ndarray : mean pooled image
        """

        img = cv2.imread(img_path)
        mean_pooled_img = cv2.resize(img, (img.shape[1]//kernel_size, img.shape[0]//kernel_size), interpolation=cv2.INTER_LINEAR)
        mean_pooled_img = cv2.resize(mean_pooled_img, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)
        return mean_pooled_img
 
    def apply_pooling_on_single_image(self, img_path: str, pooling_list: list, kernel_size: int = 15) -> list:
        """apply pooling on a single image
        arguments : img_path : str : path of the image
                    kernel_size : int : size of the kernel
                    pooling_list : list : list of pooling functions
        returns : list : list of pooled images
        """
        pooled_images = []
        for i in pooling_list:
            if i == "max":
                pooled_images.append(self.max_pooling(img_path, kernel_size))
            elif i == "mean":
                pooled_images.append(self.mean_pooling(img_path, kernel_size))
        return pooled_images

    def apply_selected_pooling_on_multiple_images(self, directory_path: str, pooling_list: list, kernel_size: int = 15) -> list:
        """apply pooling on multiple images
        arguments : directory_path : str : path of the directory
                    kernel_size : int : size of the kernel
                    pooling_list : list : list of pooling functions
        returns : list : list of pooled images
        """
        pooled_images = []
        image_path = file_interaction().get_file_path_within_directory(directory_path)
        for i in range(len(image_path)):
            pooled_images.extend(self.apply_pooling_on_single_image(image_path[i], pooling_list, kernel_size))
        return pooled_images

    def get_all_pooling(self) -> list:
        """returns a list of all pooling functions"""
        return ["max", "mean"]

