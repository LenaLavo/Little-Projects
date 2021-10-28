from itertools import cycle
import tkinter as tk
#root = tk.Tk()
#root.mainloop()

class App(tk.Tk):
    '''Tk window/label adjusts to size of image'''
    def __init__(self, a, x, y, delay):
        # the root will be self
        tk.Tk.__init__(self)
        # set x, y position only
        self.geometry('+{}+{}'.format(x, y))
        self.delay = delay
        # allows repeat cycling through the pictures
        # store as (img_object, img_name) tuple
        self.pictures = cycle((tk.PhotoImage(file=image), image)
                              for image in a)
        self.picture_display = tk.Label(self)
        self.picture_display.pack()

    def show_slides(self):
        '''cycle through the images and show them'''
        # next works with Python26 or higher
        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)
        # shows the image filename, but could be expanded
        # to show an associated description of the image
        self.title(img_name)
        self.after(self.delay, self.show_slides)

    def run(self):
        self.mainloop()


# set milliseconds time between slides
delay = 2000

# get a series of gif images you have in the working folder
# or use full path, or set directory to where the images are
image_files = [
'/Users/lena/Python/projects/Slide_Farm.gif',
'/Users/lena/Python/projects/Slide_House.gif',
'/Users/lena/Python/projects/Slide_Sunset.gif',
'/Users/lena/Python/projects/Slide_Pond.gif',
'/Users/lena/Python/projects/Slide_Python.gif'
]

images2 = ['/Users/lena/Python/projects/Slide_House.gif']

# upper left corner coordinates of app window
x = 200
y = 100

app = App(image_files, x, y, delay)
app.show_slides()
app.run()

x = App(images2, x, y, delay)
x.show_slides()
x.run()
