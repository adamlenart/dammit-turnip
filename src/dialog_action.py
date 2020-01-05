## dammit-turnip
## Version: 0.1
## Author: Adam Lenart

## Helper script for easier dialog parsing

def yes_action(circle, output):
    '''
    Resizes and saves the circle image.

    Args:
    -----
        circle: a PIL image file
        output: string, output path
    '''
    circle = circle.resize((300,300))
    circle.save(output)
    print("\nOutput is resized and saved.")

def no_action(circle, output):
    '''
    Saves the circle image.

    Args:
    -----
        circle: a PIL image file
        output: string, output path 
    '''
    circle.save(output)
    print("\nOutput is not resized. Output is saved.")

def response_action(response, yes_set, no_set, circle, output):
    '''
    Redirects the response either to yes or no resize action.

    Args:
    -----
        response: string, either in yes or no
        yes: set of yes responses
        no: set of no responses
        circle: a PIL image
        output: string, output path
    '''
    if response in yes_set:
        yes_action(circle, output)
    if response in no_set:
        no_action(circle, output)
