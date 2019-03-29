import cv2
import msvcrt

if __name__=="__main__":
    error = True

    while error == True:
        name_template = input('Enter template image: ')
        try:
            f = open(name_template)
        except FileNotFoundError:
            print('File not found')
        else:
            error = False
            print('Image found')

    while error == True:
        name_input = input('Enter input image: ')
        try:
            f = open(name_template)
        except FileNotFoundError:
            print('File not found')
        else:
            error = False
            print('Image found')

    threshold = input('Enter threshold: ')






