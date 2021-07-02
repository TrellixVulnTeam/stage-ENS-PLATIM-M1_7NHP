from PIL import Image
import cv2
import sys

def histogram(str_img):
    print(str_img)
    img = Image.open(str_img)
    print(img.histogram()[0:256])
    print(len(img.histogram()))
    # img.show()

if __name__ == "__main__":
    # main(sys.argv[1:])

    for arg in sys.argv:
        print(arg)
    print(len(sys.argv))
    histogram(sys.argv[1])



