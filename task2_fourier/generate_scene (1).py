import os
from google import genai

# Initialize the Gemini API Client
client = genai.Client()

# Detailed prompt matching assignment criteria
prompt = """
Write a complete, working Python script using the Manim Community library (`manim`).
The goal is to create a scene that visualizes Fourier Series Decomposition.

Requirements:
1. Demonstrate how a square wave is built up by summing sine harmonics.
2. Show at least the first 5 terms of the Fourier series.
3. Draw each individual wave component in a different color.
4. Show the cumulative sum updating step-by-step on screen.
5. Ensure appropriate use of axes, labels, a legend, and an on-screen title.

Return ONLY the raw executable Python code inside a single standard markdown code block. Do not include any extra introductory or concluding text.
"""

print("Sending Fourier Series prompt to Gemini API...")

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
)

output_filename = "task2_fourier/fourier_series.py"

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