from manim import *

class lenghtofc(Scene):
    def construct(self):
        truangl = Polygon([-1, 2, 0], [-1, 0, 0], [2, 0, 0], fill_color=PINK, fill_opacity=0.5).rotate(PI/2)
        self.play(Write(truangl))
        self.pause()
