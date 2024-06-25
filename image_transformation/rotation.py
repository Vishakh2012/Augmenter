#opencv code for rotating a given object implement as class

import cv2
from cv2.typing import MatLike

from system_interaction.file_interaction import file_interaction
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

    def apply_selected_rotation_on_single_image(self, image_path: str, selected_angles: list) -> list:
        ''' arguments : image_path : str : path of the image
                        angle : list : list of angles by which image is to be rotated
            returns a list of rotated images
        '''
        rotated_images = []
        for i in selected_angles:
            rotated_images.append(self.rotateByAngle(image_path, int(i)))
        return rotated_images

    def apply_selected_rotation_on_multiple_images(self, directory_path: str, selected_angles: list) -> list:
        ''' arguments : directory_path : list : list of paths of the images
                        angle : list : list of angles by which image is to be rotated
            returns a list of rotated images
        '''
        rotated_images = []

        image_path = file_interaction().get_file_path_within_directory(directory_path)
        for i in range(len(image_path)):
            rotated_images.append(self.apply_selected_rotation_on_single_image(image_path[i], selected_angles))
        return rotated_images

    def get_all_rotations(self) -> list:
        ''' returns a list of all rotations
        '''
        return ['90', '180', '200', '270']
