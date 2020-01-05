# Dammit, turnip!

A**dam**'s **mi**nimalist **t**ool **t**o p**u**t a ci**r**cle on Li**n**ked**I**n **p**rofile image, or **dammit-turnip** for short.

Python command line tool to place a circle on a LinkedIn profile image.

## Usage

First, clone the repository.
```
git clone https://github.com/adamlenart/dammit-turnip.git
```

Then from a terminal window run `make_circle.py`.

As a minimum, you will need to specify the input and output file paths, for example
`python3 make_circle.py img/my_input.jpg img/my_output.png` for an input image file saved `dammit-turnip\img`.

After this, the dammit-turnip will ask about what the coordinates for the center of the circle that you wish to draw, the diameter of the circle, the color of the circle and the width of the circle should be.

However, if you would like to skip the interactive questions, you can also run
```
python3 make_circle.py img/turnip.jpg img/fancy_turnip.png -x 600 -y 600 -d 1200 -R 56 -G 16 -B 77 -A 255 -width 30 --resize
```

which will render our original image ![old-turnip](img/turnip.jpg)
to
![new-turnip](img/fancy_turnip.png) 

For a complete list of options, run:
```
python3 make_circlepy --help
```


