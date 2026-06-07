from manim import *

class PythagorasProof(Scene):
    def construct(self):
        # --- 1. Define Vertices for a Right-Angled Triangle ---
        A = ORIGIN
        B = RIGHT * 4
        C = UP * 3

        # --- 2. Create Intersecting Line Segments ---
        line_ab = Line(A, B, color=BLUE)
        line_ac = Line(A, C, color=RED)
        line_cb = Line(C, B, color=GREEN)

        # --- 3. Create the Right-Angled Triangle Mobject ---
        triangle = Polygon(A, B, C, stroke_width=2, fill_opacity=0.1, fill_color=WHITE)

        # --- 4. Right Angle Indicator ---
        right_angle_mark = RightAngle(line_ab, line_ac, length=0.3, color=YELLOW)

        # --- 5. Labels for Sides (Using Text to completely bypass LaTeX dependency) ---
        label_a = Text("a", color=RED).next_to(line_ac, LEFT, buff=0.2)
        label_b = Text("b", color=BLUE).next_to(line_ab, DOWN, buff=0.2)
        label_c = Text("c", color=GREEN).next_to(line_cb, UR, buff=0.1)

        # --- 6. Construct Squares on Each Side ---
        # Square on side 'b' (extends downwards from AB)
        square_b = Square(side_length=4, stroke_color=BLUE, fill_color=BLUE, fill_opacity=0.3)
        square_b.next_to(line_ab, DOWN, buff=0)

        # Square on side 'a' (extends leftwards from AC)
        square_a = Square(side_length=3, stroke_color=RED, fill_color=RED, fill_opacity=0.3)
        square_a.next_to(line_ac, LEFT, buff=0)

        # Square on side 'c' (hypotenuse)
        square_c = Square(side_length=5, stroke_color=GREEN, fill_color=GREEN, fill_opacity=0.3)
        alpha = line_cb.get_angle()
        square_c.rotate(alpha)
        # Shifted alignment adjustment to snap to the hypotenuse
        square_c.move_to(line_cb.get_center()).shift(UP * 1.2 + RIGHT * 1.6)

        # --- 7. Algebraic Identity Text (Using unicode exponents and t2c for coloring) ---
        equation = Text("a² + b² = c²", t2c={"a²": RED, "b²": BLUE, "c²": GREEN})
        equation.to_corner(UL)

        # --- 8. Animation Sequence ---
        self.play(Write(equation))
        self.wait(0.5)

        self.play(Create(triangle), Create(right_angle_mark))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(1)

        self.play(FadeIn(square_a, shift=LEFT), run_time=1.5)
        self.play(FadeIn(square_b, shift=DOWN), run_time=1.5)
        self.play(FadeIn(square_c), run_time=1.5)
        
        self.wait(3)