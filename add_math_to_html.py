"""
Script to directly add extracted Mathematics questions to HTML file
"""

import json
import re
import os

# Read the extracted questions file
extracted_file = r"C:\Users\tekzo\OneDrive\Desktop\CAPS TYCOON GAME\extracted_math_questions.js"

with open(extracted_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract each grade's questions using regex
def extract_grade_questions(content, grade):
    pattern = rf'const mathGrade{grade}Questions = (\[.*?\]);'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        try:
            questions = json.loads(match.group(1))
            # Filter out malformed questions
            filtered = []
            for q in questions:
                # Check if question is valid
                if (q.get('q') and len(q.get('q', '')) > 5 and 
                    q.get('a') and len(q.get('a')) == 4 and
                    all(opt and len(str(opt)) > 0 and len(str(opt)) < 200 for opt in q.get('a', [])) and
                    not any('Option not available' in str(opt) for opt in q.get('a', [])) and
                    not any('B. C. D.' in str(opt) for opt in q.get('a', []))):  # Filter out obviously malformed
                    # Clean up question text - remove leading numbers and extra formatting
                    q_text = re.sub(r'^\d+[\.\)]\s*', '', q['q']).strip()
                    q_text = re.sub(r'^Patterns/Functions.*?\d+\.\s*', '', q_text)  # Remove section headers
                    q_text = re.sub(r'^\d+\.\s+', '', q_text)  # Remove leading numbers
                    if len(q_text) > 5:  # Valid question after cleaning
                        q['q'] = q_text
                        filtered.append(q)
            return filtered
        except Exception as e:
            print(f"Error parsing grade {grade}: {e}")
            return []
    return []

grades = [8, 9, 10, 11, 12]
all_questions = {}

for grade in grades:
    questions = extract_grade_questions(content, grade)
    all_questions[grade] = questions
    print(f"Grade {grade}: {len(questions)} valid questions")

# Read the HTML file
html_file = r"C:\Users\tekzo\OneDrive\Desktop\CAPS TYCOON GAME\caps-tycoon.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Generate the questions JavaScript code
questions_js = {}
for grade in grades:
    questions_js[grade] = []
    for q in all_questions[grade]:
        # Escape single quotes and newlines for JavaScript
        q_text = q['q'].replace('\\', '\\\\').replace("'", "\\'").replace('\n', ' ').replace('\r', ' ')
        options = [opt.replace('\\', '\\\\').replace("'", "\\'").replace('\n', ' ').replace('\r', ' ') if opt else '' for opt in q['a']]
        options_str = ', '.join([f"'{opt}'" for opt in options])
        questions_js[grade].append(
            f"                {{ q: '{q_text}', a: [{options_str}], correct: {q['correct']}, topic: '{q['topic']}', note: '{q['note']}' }}"
        )

# Find the mathematics section and replace grade arrays
for grade in grades:
    pattern = rf'(grade{grade}:\s*\[\s*)(//.*?\n\s*)?(\],)'
    replacement = f'grade{grade}: [\n                    // Grade {grade} Mathematics questions\n                    ' + ',\n                    '.join(questions_js[grade]) + '\n                ],'
    html_content = re.sub(pattern, replacement, html_content, flags=re.DOTALL)

# Write back to HTML file
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"\n✅ Added Mathematics questions to {html_file}")
print(f"\nSummary:")
for grade in grades:
    print(f"  Grade {grade}: {len(all_questions[grade])} questions added")





