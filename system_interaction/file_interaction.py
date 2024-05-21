from cv2.typing import MatLike
import cv2

class file_interaction:

    def save_image(self,path: str,image: MatLike) -> bool:
        ''' arguments : path : str : path of the image
                        image : MatLike : image to be saved
            returns a boolean value
        '''
        file_saved = cv2.imwrite(path, image)


        return file_saved


