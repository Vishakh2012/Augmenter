from cv2.typing import MatLike
import cv2
import uuid
class file_interaction:

    def save_image(self,path: str,image: MatLike, transormation_name: str) -> bool:
        ''' arguments : path : str : path of the image
                        image : MatLike : image to be saved
            returns a boolean value
        '''
        unique_file_name = self.__create_unique_path_for_transformed_file(path, transormation_name)
        print(unique_file_name)
        file_saved = cv2.imwrite(unique_file_name, image)


        return file_saved

    def __create_unique_path_for_transformed_file(self, original_file_name: str, transformation_name: str) -> str:
        ''' arguments : original_file_name : str : name of the original file
                        transformation_name : str : name of the transformation
            returns a string
            uses uuid to generate unique file in the base directory

        '''
        unique_file_name = original_file_name.split(".")[0] + "_" + transformation_name + "_" + str(uuid.uuid4()) + "." + original_file_name.split(".")[1]

        return unique_file_name

