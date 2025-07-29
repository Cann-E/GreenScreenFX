import math
from dip import *
"""
Do not import cv2, numpy and other third party libs
"""


class Operation:

    def __init__(self):
        pass

    def flip(self, image, direction="horizontal"):
        """
          Perform image flipping along horizontal or vertical direction

          image: the input image to flip
          direction: direction along which to flip

          return: output_image
          """
          
        hei, wid = image.shape[:2]
        output_image = zeros(image.shape, uint8)

        for i in range(hei):
            for j in range(wid):
                if direction == "horizontal":
                    output_image[i][j] = image[i][wid - j - 1]
                elif direction == "vertical":
                    output_image[i][j] = image[hei - i - 1][j]


        #Solve The assignment

        return output_image

    def chroma_keying(self, foreground, background, target_color, threshold):
        """
        Perform chroma keying to create an image where the targeted green pixels is replaced with
        background

        foreground_img: the input image with green background
        background_img: the input image with normal background
        target_color: the target color to be extracted (green)
        threshold: value to threshold the pixel proximity to the target color

        return: output_image
        """

        hei, wid = foreground.shape[:2]
        for i in range(hei):
            for j in range(wid):
                r1, g1, b1 = foreground[i][j]
                r2, g2, b2 = background[i][j]
                dist = math.sqrt((int(r1) - target_color[0]) ** 2 +(int(g1) - target_color[1]) ** 2 +(int(b1) - target_color[2]) ** 2)

                if dist < threshold:
                    foreground[i][j] = [r2, g2, b2]

        # add your code here
        # Please do not change the structure
        return  foreground # Currently the input image is returned, please replace this with the color extracted image