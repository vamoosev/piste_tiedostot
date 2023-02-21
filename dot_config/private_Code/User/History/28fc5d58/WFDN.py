from manim import *
from manim_slides import Slide

class lenghtofc(Slide):
    def construct(self):
        truangl = Polygon([-1, 2, 0], [-1, 0, 0], [1, 0, 0], fill_color=PINK, fill_opacity=0.5)
        self.play(Write(truangl))
        self.pause()
