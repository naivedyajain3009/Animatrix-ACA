from manim import *
import numpy as np

class FourierSeries(Scene):
    def construct(self):
        # 1. Display Title (using Text instead of Tex to avoid LaTeX dependencies)
        title = Text("Fourier Series Decomposition of a Square Wave", font_size=28)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))
        
        # 2. Build the Coordinate System 
        # Axes are centered at the ORIGIN (0,0) by default in Manim.
        axes = Axes(
            x_range=[-4 * np.pi, 4 * np.pi, np.pi],
            y_range=[-2, 2, 0.5],
            x_length=10,
            y_length=4.5,
            axis_config={"color": LIGHT_GRAY},
            tips=False
        )
        axes.center()
        
        # Explicitly create labels with standard Text objects to avoid LaTeX background calls
        x_label = Text("x", font_size=16).next_to(axes.x_axis.get_end(), DOWN + LEFT, buff=0.2)
        y_label = Text("f(x)", font_size=16).next_to(axes.y_axis.get_end(), UP + RIGHT, buff=0.2)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)
        
        # 3. Configure the Harmonics (First 5 terms of a square wave: n = 1, 3, 5, 7, 9)
        harmonics = [1, 3, 5, 7, 9]
        colors = [BLUE, GREEN, YELLOW, ORANGE, RED]
        
        # UI Tracking Text Layout
        list_header = Text("Active Harmonics:", font_size=18).to_corner(UL, buff=1.2)
        self.play(Write(list_header))
        
        previous_text_element = list_header
        cumulative_graph = None
        
        # 4. Step-by-Step Generation Loop
        for idx, n in enumerate(harmonics):
            current_color = colors[idx]
            
            # Text update for the active term
            term_text = Text(f"n = {n}  (Amp: 4/{n}π)", font_size=16, color=current_color)
            # FIXED: Chained .align_to() onto .next_to() properly
            term_text.next_to(previous_text_element, DOWN, buff=0.15).align_to(previous_text_element, LEFT)
            
            # Lambda function for individual sine wave component: (4 / n*pi) * sin(n * x)
            individual_wave_func = lambda x: (4 / (n * np.pi)) * np.sin(n * x)
            individual_graph = axes.plot(individual_wave_func, color=current_color, stroke_width=2, stroke_opacity=0.6)
            
            # Animate the introduction of the new harmonic term
            self.play(
                Write(term_text),
                Create(individual_graph),
                run_time=1.2
            )
            self.wait(0.3)
            
            # Define a lambda that computes the cumulative sum up to the current term index
            def make_cumulative_sum(max_term_idx):
                return lambda x: sum((4 / (harmonics[k] * np.pi)) * np.sin(harmonics[k] * x) for k in range(max_term_idx + 1))
            
            # Generate the new composite wave graph
            new_cumulative_graph = axes.plot(
                make_cumulative_sum(idx),
                color=PURPLE,
                stroke_width=4
            )
            
            # Morph the old cumulative sum graph into the new one (or create it on step 1)
            if cumulative_graph is None:
                self.play(Create(new_cumulative_graph), run_time=1.2)
                cumulative_graph = new_cumulative_graph
            else:
                self.play(Transform(cumulative_graph, new_cumulative_graph), run_time=1.2)
                self.remove(new_cumulative_graph) # Clean memory references after transform
                
            # Clean up the individual harmonic curve visualization to keep the layout legible
            self.play(FadeOut(individual_graph, run_time=0.4))
            
            previous_text_element = term_text
            
        # 5. Outro holding frame showing the final configuration
        conclusion_label = Text("Cumulative graph approaches an ideal square wave.", font_size=18, color=PURPLE)
        conclusion_label.to_edge(DOWN, buff=0.4)
        
        self.play(Write(conclusion_label))
        self.wait(3)