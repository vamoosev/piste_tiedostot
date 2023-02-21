from manim import *

class lenghtofc(Scene):
    def construct(self):
        truangl = Polygon([-1, 2, 0], [-1, 0, 0], [2, 0, 0], fill_color=PINK, fill_opacity=0.5)
        sidea = Text("a").next_to(truangl, DOWN).shift(DOWN*.5)
        sideb = Text("b").next_to(truangl, RIGHT).shift(LEFT*.5)
        self.play(Write(truangl))
        self.wait(.25)
        self.play(truangl.animate.rotate(PI/2))
        self.wait(.25)
        self.play(Write(sidea), Write(sideb))
        self.wait(2)