Markdown# Manim GenAI Assignment: Automated Code Generation & Critical Evaluation

## Project Overview
This repository contains the implementation and critical analysis of automatically generated mathematical animations using the Google Generative AI (Gemini) API. The objective of this assignment is to prompt an LLM to generate Manim code for key mathematical visualizations, run the code locally to identify bugs or logical deficiencies, execute structural refactoring, and document the findings.

The project focuses on two core mathematical concepts:
1. **Visualisation of the Pythagorean Theorem ($a^2 + b^2 = c^2$)**: An animation showing a right-angled triangle, labels for its sides, filled square shapes built on each edge to prove area equivalence, and the algebraic identity.
2. **Visualisation of Fourier Series Decomposition**: A dynamic coordinate system demonstrating how a square wave is synthesized step-by-step by calculating and summing its individual sine wave harmonics ($n=1, 3, 5, 7, 9$) using distinct color palettes.

---

## Repository Structure
The project files are modularized and organized systematically into specific task directories rather than flattened into the root workspace:

```text
manim-genai-assignment/
├── .gitignore                  # Git ignore patterns for Python projects and virtual environments
├── requirements.txt            # System dependencies (manim, numpy, google-generativeai)
├── README.md                   # Project documentation and critical analysis findings
├── task1_pythagoras/
│   ├── generate_scene.py       # Python script containing prompt engineering & Gemini API configuration
│   └── pythagoras.py           # Final refactored, stable Manim scene code
└── task2_fourier/
    ├── generate_scene.py       # Python script containing prompt engineering & Gemini API configuration
    └── fourier_series.py       # Final refactored, stable Manim scene code
Setup Instructions1. PrerequisitesBefore running the animation scripts, ensure your system has the following core utilities installed:Python: python >= 3.8FFmpeg: Required by Manim for media processing and rendering output video codecs. Ensure it is appended to your environment's system PATH variables.(Optional) LaTeX Distribution: (e.g., MiKTeX on Windows or MacTeX on macOS). Note that the finalized code versions in this repository have been fully refactored to use standard text arrays to bypass local system LaTeX crashes (WinError 2).2. InstallationClone the repository and install the dependencies inside a dedicated virtual environment:Bash# Clone the repository
git clone [https://github.com/YOUR_USERNAME/manim-genai-assignment.git](https://github.com/YOUR_USERNAME/manim-genai-assignment.git)
cd manim-genai-assignment

# Create and activate a virtual environment
python -m venv venv

# On Windows (PowerShell):
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt
3. Environment ConfigurationTo run the automated script generators, configure your Gemini API token as an environment variable in your terminal session.On Windows (PowerShell):PowerShell$env:GEMINI_API_KEY="YOUR_ACTUAL_API_KEY_HERE"
On macOS/Linux:Bashexport GEMINI_API_KEY="YOUR_ACTUAL_API_KEY_HERE"
How to Run Each Manim SceneTo render the scenes with standard low quality (useful for rapid previewing and testing), execute the following commands inside your terminal:Rendering Task 1: Pythagorean TheoremBashmanim -pql task1_pythagoras/pythagoras.py PythagorasScene
Rendering Task 2: Fourier Series DecompositionBashmanim -pql task2_fourier/fourier_series.py FourierSeries
(Note: Replace -pql with -pqh to render a high-definition 1080p video once correctness is verified.)Critical Analysis FindingsTask 1: Visualisation of the Pythagorean TheoremRunning the raw code directly out of the initial generative prompt highlighted 5 specific shortcomings:System-Specific LaTeX Dependency Crashing: The AI default-constructed labels via MathTex(). On host machines lacking an external LaTeX compiler, this produced unhandled system terminal crashes (WinError 2). Impact: Code was completely un-renderable out-of-the-box. Correction: Substituted formatting using native standard Text() elements.Missing Geometric Shading: The AI generated empty line outlines for the squares built on the triangle edges rather than filling them. Impact: Defeated the visual proof concept, which relies on comparing square areas ($a^2 + b^2 = c^2$). Correction: Appended .set_fill(color, opacity=0.4) to give clear spatial context.Hardcoded Vector Positions: Layout coordinates were explicitly hardcoded as static arrays (e.g., [2, 1, 0]) rather than linked dynamically. Impact: Scalability modifications or scaling down objects caused text labels to decouple from their target lines. Correction: Refactored positioning using relative attachment hooks like .next_to(triangle, LEFT).Absence of Animation Timing Structure (wait()): The generated script chain context processed drawings concurrently without introducing static buffer stops. Impact: The rendering played through almost instantly, leaving viewers unable to process the proof steps. Correction: Integrated strategic self.wait(1.5) intervals following major draw sequences.Screen Layout Collision: The mathematical identity string overlapped the right-triangle drawing layer due to incorrect bounding box assessments. Impact: Obscured text information and impaired mathematical readability. Correction: Pushed formulas away from active graphics zones using bounds modifiers like .to_edge(UP, buff=0.5).Task 2: Visualisation of Fourier Series DecompositionRunning the generated Fourier scene exposed critical API syntax hallucinations and readability constraints:Hallucinated Layout Methods (Axes.to_center()): The AI attempted to center the drawing view using a non-existent .to_center() method on the coordinate object. Impact: Caused an instant compilation crash with an AttributeError. Correction: Stripped the invocation entirely since Manim natively centers new Axes objects around the origin matrix ([0,0,0]) automatically.Illegal Argument Chaining Syntax: The model incorrectly provided an alignment parameter straight inside a spacing declaration (term_text.next_to(..., align_to=LEFT)). Impact: Threw an unhandled TypeError stating that next_to() received an invalid keyword argument. Correction: Chained the instruction syntax cleanly into two distinct legal method calls: .next_to(...).align_to(..., LEFT).Implicit Axis Label LaTeX Requirements: Built-in axis utilities like axes.get_x_axis_label() were utilized, which silently deploy hidden LaTeX compilation pipelines under the hood. Impact: Triggered environment path failures when rendered on minimal Python environments. Correction: Explicitly manually configured standalone coordinate label assets using Text().Missing Legend Tracking Data: Although different colored curves were drawn for each harmonic frequency term, the AI omitted an explanatory legend or index tracking system. Impact: Viewers could not track which wave pattern corresponded to which harmonic frequency stage ($n=1,3,5...$). Correction: Assembled a tracking side-panel array (n = 1, Amp: 4/1π) whose active colors precisely index the corresponding curve markers.Visual Geometry Accumulation Bloat: The individual component graphs were continuously generated and left lingering on screen during iteration tracking loop updates. Impact: Cluttered the monitor layout and diluted the high-contrast presentation of the primary cumulative purple target wave. Correction: Implemented an explicit step cleanup loop using FadeOut(individual_graph) after animating each configuration shift.