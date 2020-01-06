## dammit-turnip
## Version: 0.1
## Author: Adam Lenart

## Process image file

## 3rd party imports
from PIL import Image, ImageDraw

def square_coordinates_getter(image, center, diameter):
    """
    Returns the coordinates of the outer square of the required circle.

    Args:
    -----
        image: an image file read in by Pillow
        center: tuple, coordinates of the required center of the
                circle output
        diameter: int, diameter of the circle.

    Returns:
    --------
        Coordinates of the outer square of the required circle as (left, upper, right, lower)
        tuple.
    """
    ## diameter validity checks
    if not isinstance(diameter, int):
        raise TypeError('Diameter must  be an integer.')
    if diameter > min(image.size):
        raise ValueError('Diameter cannot be larger than {0} which is the shorter ' \
                          'side of your image.'.format(min(image.size)))
    ## calculate coordinates
    radius = diameter / 2
    ## if diameter is an odd number, we have to force
    ## coordinates to be integers
    left = int(center[0] - radius)
    upper = int(center[1] - radius)
    right = int(center[0] + radius)
    lower = int(center[1] + radius)
    return (left, upper, right, lower)

def circle_cutter(outer_square_image):
    """
    Returns inner circle image from square.

    Args:
    -----
        outer_square_image: a square-shaped PIL image file
    Returns:
        circle-shaped PIL image file (pixels out of the circle are colored transparent)
    --------
    """
    ## from https://stackoverflow.com/questions/890051/how-do-i-generate-circular-thumbnails-with-pil
    ## create a bigger mask and then scale it down with antialias filter
    big_square_size = (outer_square_image.size[0] * 3, outer_square_image.size[0] * 3)
    mask = Image.new('L', big_square_size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + big_square_size, fill=255)
    mask = mask.resize(outer_square_image.size, Image.ANTIALIAS)
    outer_square_image.putalpha(mask)
    return outer_square_image

def circle_maker(image, center, diameter, width="auto", color=(0,0,0,255)):
    """
    Returns a circular image file with transparent pixels in the area of the outer square
    from original image.

    Args:
    -----
        image: an image file read in by Pillow
        center: two-tuple, coordinates of the required center of the
                circle output
        diameter: int, diameter of the circle.
        width: width of the circle in pixels. Can be left "auto" to take diameter / 100
               pixels
        color: color of the circle in RGBA format.
    """
    if width == "auto":
        width = int(diameter / 100)
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    ## create outer square for the circle
    outer_square_coords = square_coordinates_getter(image, center, diameter)
    outer_square = image.crop(outer_square_coords)
    ## cut the circle from the square
    circular_image = circle_cutter(outer_square)
    ## draw the outline of the circle
    circle = ImageDraw.Draw(outer_square)
    circle.ellipse((0,0) + outer_square.size, width=width, outline=color)
    return circular_image
