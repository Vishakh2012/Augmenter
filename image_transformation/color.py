import cv2

class color:
    def convert_to_gray(self, image_path: str):
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray_image

    def convert_to_hsv(self, image_path: str):
        image = cv2.imread(image_path)
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        return hsv_image

    def multiply_saturation(self, image_path: str, factor):
        image = cv2.imread(image_path)
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_image)
        s = s * factor
        hsv_image = cv2.merge([h, s, v])
        return cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    def multiply_hue(self, image_path: str, factor):
        image = cv2.imread(image_path)
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_image)
        h = h * factor
        hsv_image = cv2.merge([h, s, v])
        return cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    def change_brightness(self, image_path: str, factor):
        image = cv2.imread(image_path)
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_image)
        v = v * factor
        hsv_image = cv2.merge([h, s, v])
        return cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)


        


