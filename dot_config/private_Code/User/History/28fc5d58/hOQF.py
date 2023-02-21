from manim import *
from manim_slides import Slide

class lenghtofc(Slide):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.flip(RIGHT)  # flip horizontally
        square.rotate(-3 * TAU / 8)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.pause()
        self.play(Transform(square, circle))
        self.pause()  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation
