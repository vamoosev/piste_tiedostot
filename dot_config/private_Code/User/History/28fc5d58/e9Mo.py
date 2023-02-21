from manim import *
from manim_slides import Slide

class lenghtofc(Slide):
    def construct(self):
        truangl = Polygon([0,0,0],[0,1,0],[2,0,0]).set_fill(pink)
        self.play(Write(truangl))
        self.pause()
