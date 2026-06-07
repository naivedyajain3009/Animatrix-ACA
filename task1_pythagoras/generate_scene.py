import os
from google import genai

# Initialize the Gemini API Client
client = genai.Client()

# Detailed prompt matching assignment criteria
prompt = """
Write a complete, working Python script using the Manim Community library (`manim`).
The goal is to create a scene that visually proves the Pythagorean Theorem (a^2 + b^2 = c^2).

Requirements:
1. Create a right-angled triangle. Label its sides 'a', 'b', and 'c'.
2. Visually construct and shade three squares built on each of the three sides.
3. Clearly display the algebraic identity a^2 + b^2 = c^2 on screen.
4. Ensure appropriate use of self.play() and self.wait() calls to make the animation clean and readable.
5. Use proper color coding to link the side labels to their respective squares.

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