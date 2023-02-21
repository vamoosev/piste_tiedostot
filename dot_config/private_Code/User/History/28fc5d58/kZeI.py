from manim import *

class lenghtofc(Scene):
    def construct(self):
        truangl = Polygon([-1, 2, 0], [-1, 0, 0], [2, 0, 0], fill_color=PINK, fill_opacity=0.5)
        sidea = Text("a").next_to(truangl, DOWN).shift(DOWN*.5)
        sideb = Text("b").next_to(truangl, RIGHT).shift(LEFT*.5)
        sidec = Text("c").next_to(truangl, LEFT).shift(RIGHT*.5)
        self.play(Write(truangl))
        self.wait(.25)
        self.play(truangl.animate.rotate(PI/2))
        self.wait(.25)
        self.play(Write(sidea), Write(sideb), Write(sidec))
        self.wait(.25)
        area_a = Square(side_length=5, fill_color=BLUE, fill_opacity=0.2).next_to(truangl, RIGHT).shift(LEFT*.5)
        area_b = Square(side_length=2, fill_color=BLUE, fill_opacity=0.2).next_to(truangl, DOWN).shift(UP*.5)
        area_c = Square(side_length=3, fill_color=BLUE, fill_opacity=0.2).rotate(PI/4).next_to(truangl, LEFT).shift(RIGHT*.5)
        self.play(Write(area_a), Write(area_b), Write(area_c))
        self.wait(2)