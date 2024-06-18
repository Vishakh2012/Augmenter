#opencv code for rotating a given object implement as class

import cv2
from cv2.typing import MatLike
print (cv2.__version__)
class Rotation:
    def rotateByAngle(self, image_path: str, angle: int) -> MatLike:
        ''' arguments : image_path : str : path of the image
                        angle : int : angle by which image is to be rotated
            returns a rotated image
        '''
        image = cv2.imread(image_path)
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated_image = cv2.warpAffine(image, M, (w, h))
        return rotated_image

    def multipleRotationForSingleImage(self, image_path: str, angle: list) -> list:
        ''' arguments : image_path : str : path of the image
                        angle : list : list of angles by which image is to be rotated
            returns a list of rotated images
        '''
        rotated_images = []
        for i in angle:
            rotated_images.append(self.rotateByAngle(image_path, i))
        return rotated_images

    def multipleRotationForMultipleImages(self, image_path: list, angle: list) -> list:
        ''' arguments : image_path : list : list of paths of the images
                        angle : list : list of angles by which image is to be rotated
            returns a list of rotated images
        '''
        rotated_images = []
        for i in range(len(image_path)):
            rotated_images.append(self.multipleRotationForSingleImage(image_path[i], angle))
        return rotated_images
