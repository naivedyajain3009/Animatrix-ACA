import os
from google import genai

# Initialize the Gemini API Client
client = genai.Client()

# Detailed prompt matching assignment criteria
prompt = """
Write a complete, working Python script using the Manim Community library (`manim`).
The goal is to create a scene that visually proves the Pythagorean Theorem (a^2 + b^2 = c^2) using a clean, non-overlapping layout and a grid-based unit dissection animation (3-4-5 triangle).

Requirements:
1. Create a right-angled triangle with sides a=3, b=4, c=5. Scale the vertices by 0.6 and shift them to center the geometric figure to the right (e.g. A=(0, -0.9), B=(2.4, -0.9), C=(0, 0.9)) to leave room on the left. Label the sides 'a = 3', 'b = 4', and 'c = 5' and add a right angle indicator.
2. Build three squares on the three sides extending OUTWARDS from the triangle so they do not overlap. The square on the hypotenuse should be aligned and rotated correctly along the hypotenuse.
3. On the left side of the screen, display a formatted column of text: title, main equation a² + b² = c² (color-coded), step-by-step calculations showing the area of each square (Red Area = 9, Blue Area = 16, Green Area = 25), and the final proof equation (9 + 16 = 25).
4. Represent the squares using grids of unit squares (size 0.6x0.6): a 3x3 grid of red squares, a 4x4 grid of blue squares, and a 5x5 grid of green target slots.
5. Animate copies of the 9 red and 16 blue unit squares flying and rotating into the 25 target slots of the hypotenuse square to visually demonstrate that the sum of the small square areas perfectly equals the large square area.
6. Ensure appropriate timing with self.wait() to make the visual proof readable. Avoid LaTeX by using standard Text elements to prevent WinError path failures on environments without a LaTeX compiler.

Return ONLY the raw executable Python code inside a single standard markdown code block. Do not include any extra introductory or concluding text.
"""

print("Sending Pythagoras prompt to Gemini API...")

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
)

output_filename = "task1_pythagoras/pythagoras.py"

# Clean up markdown code block formatting if the model returns it
raw_text = response.text
if "```python" in raw_text:
    code = raw_text.split("```python")[1].split("```")[0].strip()
elif "```" in raw_text:
    code = raw_text.split("```")[1].split("```")[0].strip()
else:
    code = raw_text.strip()

with open(output_filename, "w", encoding="utf-8") as f:
    f.write(code)

print(f"Successfully saved generated code to {output_filename}!")