import os
from cv2.typing import MatLike
import cv2
import uuid
class file_interaction:

    def save_image(self,path: str,image, transormation_name: str) -> bool:
        ''' arguments : path : str : path of the image
                        image : MatLike : image to be saved
            returns a boolean value
        '''
        unique_file_name = self._create_unique_path_for_transformed_file(path, transormation_name)
        print(unique_file_name)
        print(type(image))

        file_saved = cv2.imwrite(unique_file_name, image)


        return file_saved

    def _create_unique_path_for_transformed_file(self, directory_path: str, transformation_name: str, image_format = "jpg") -> str:
        ''' arguments : directory_path : str : name of the original file
                        transformation_name : str : name of the transformation
            returns a string
            uses uuid to generate unique file in the base directory

        '''
        unique_file_name = directory_path + "_" + transformation_name + "_" + str(uuid.uuid4()) + "." + image_format

        return unique_file_name

    def save_multiple_images(self, path: str, images: list, transformation_name: str) -> bool:
        ''' arguments : path : str : path of the directory where the images will be saved
                        images : list : list of images to be saved
                        transformation_name : str : name of the transformation
            returns a boolean value
        '''
        for image in images:
            file_saved = self.save_image(path, image, transformation_name)

            if not file_saved:
                print("file not save")
                return False
        
        print("file saved")
        return True
    
    def get_file_path_within_directory(self,directory_path: str) -> list:
        ''' arguments : directory_path : str : path of the directory
            returns a list of full file path
        '''
        file_paths = []

        for entry in os.listdir(directory_path):
            full_path = os.path.join(directory_path, entry)
            file_paths.append(full_path)
        print(file_paths)
        return file_paths



        


