import cv2
import numpy as np
class noise:

    def add_salt_and_pepper_noise(self, image_path: str, amount):
        image = cv2.imread(image_path)
        row, col, _ = image.shape
        s_vs_p = 0.5
        out = image.copy()
        num_salt = int(amount * row * col * s_vs_p)
        coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
        out[coords[0], coords[1], :] = 1

        num_pepper = int(amount * row * col * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
        out[coords[0], coords[1], :] = 0
        return out

    def add_gaussian_noise(self, image_path: str, mean, sigma):
        image = cv2.imread(image_path)
        row, col, ch = image.shape
        gauss = np.random.normal(mean, sigma, (row, col, ch))
        noisy = cv2.add(image, gauss)
        return noisy
