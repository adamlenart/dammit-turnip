## dammit-turnip
## Version: 0.1
## Author: Adam Lenart

## Main file that interacts with the user

## standard imports
import argparse

## 3rd parth imports
from PIL import Image

## own modules
from src import dialog_action
from src import processor

###################################################################################
##                               Options                                         ##
###################################################################################

## ----------------------- Command line arguments ------------------------------ ##
parser = argparse.ArgumentParser(description='Create a circular image and draw ' +
                                 'a colored circle around its edge.' )
parser.add_argument('input', help='path to input file')
parser.add_argument('output', help='path to output file. The output format must be PNG.')
parser.add_argument('-x', type=int, help='integer,  x coordinate of the center of the circle. 0 is left.')
parser.add_argument('-y', type=int, help='integer,  y coordinate of the center of the circle. 0 is top.')
parser.add_argument('-d', type=int, help='integer,  diameter of the circle in pixels.')
parser.add_argument('-R', type=int,
                    help='integer, R in RGBA color specifications, e.g., 150 in "(150,0,100,255)".')
parser.add_argument('-G', type=int,
                    help='integer, G in RGBA color specifications, e.g., 0 in "(150,0,100,255)".')
parser.add_argument('-B', type=int,
                    help='integer, B in RGBA color specifications, e.g., 100 in "(150,0,100,255)".')
parser.add_argument('-A', type=int,
                    help='integer, A in RGBA color specifications, e.g., 255 in "(150,0,100,255)".')
parser.add_argument('-width', type=int, help='integer, width of circle line in pixels.')
parser.add_argument('--resize', action='store_true', help='Add to arguments to resize to 300 x 300 pixels.')

args = parser.parse_args()

## -------------------------- resize options ------------------------------------- ##
yes = {'yes','y', 'ye'}
no = {'no','n'}
allowed_responses = yes.union(no)
## continue loop below until yes or no arrives 
CONT = True

#####################################################################################
##                                   Run                                           ##
#####################################################################################

if __name__ == "__main__":
    print("dammit-turnip 0.1.\n\n")
    print("Make a circle from the input image and color the edge of it.\n")
    
    input_image = Image.open(args.input)
    print("Dimensions of the input image: {dim}".format(dim=input_image.size))
    if args.x is None:
        print("\nProvide input for the position of the circle on the original image.\n")
        x = int(input("X coordinate of the center of the circle (0 is left): "))
    else:
        x = args.x
    if args.y is None:
        y = int(input("Y coordinate of the center of the circle (0 is top): "))
    else:
        y= args.y
    if args.d is None:
        d = int(input("Diameter of the circle in pixels: "))
    else:
        d = args.d
    if args.R is None:
        print("\nNext, provide input for the color of the circle in RGBA format.\n")
        R = input('R channel color, integer between 0 and 255  (press ENTER for default): ')
        if R == '':
            R = 0
        else:
            R = int(R)
    else:
        R = args.R
    if args.G is None:
        G = input('G channel color, integer between 0 and 255  (press ENTER for default): ')
        if G == '':
            G = 0
        else:
            G = int(G)
    else:
        G = args.G
    if args.B is None:
        B = input('B channel color, integer between 0 and 255  (press ENTER for default): ')
        if B == '':
            B = 0
        else:
            B = int(B)
    else:
        B = args.B
    if args.A is None:
        A = input('A channel color, integer between 0 and 255  (press ENTER for default): ')
        if A == '':
            A = 255
        else:
            A = int(A)
    else:
        A = args.A
    if args.width is None:
        width = input("Width of the circle line in pixels (press ENTER for default): ")
        if width == '':
            width = int(d / 100)
        else:
            width = int(width)
    else:
        width = args.width
    ## Make circle
    circle = processor.circle_maker(input_image, (x,y), d, width, (R,G,B,A))
    ## Resize?
    print(args)
    if args.resize:
        dialog_action.yes_action(circle, args.output)
    else:
        while CONT:
            response = input("\nWe have now a circular shaped image.\n" +
                             "Resize it to LinkedIn size recommendation (300 x 300)? (yes/no): ").lower()
            if response in allowed_responses:
                dialog_action.response_action(response, yes, no, circle, args.output)
                break
            while response not in allowed_responses:
                response = input("Please respond with 'yes' or 'no': ")
                if response in allowed_responses:
                    dialog_action.response_action(response, yes, no, circle, args.output)
                    CONT = False
                    break
