"""
Script to add extracted Mathematics questions to the HTML file
Filters out malformed questions and adds properly formatted ones
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
                    not any('Option not available' in str(opt) for opt in q.get('a', []))):
                    # Clean up question text - remove leading numbers and extra formatting
                    q['q'] = re.sub(r'^\d+[\.\)]\s*', '', q['q']).strip()
                    filtered.append(q)
            return filtered
        except:
            return []
    return []

grades = [8, 9, 10, 11, 12]
all_questions = {}

for grade in grades:
    questions = extract_grade_questions(content, grade)
    all_questions[grade] = questions
    print(f"Grade {grade}: {len(questions)} valid questions (from extracted file)")

# Generate JavaScript code for HTML insertion
print("\n" + "="*60)
print("JavaScript code to add to HTML:")
print("="*60 + "\n")

for grade in grades:
    print(f"// Grade {grade} Mathematics Questions")
    print(f"grade{grade}: [")
    for q in all_questions[grade]:
        # Convert to JavaScript format
        q_str = q['q'].replace("'", "\\'").replace("\n", " ")
        options = [opt.replace("'", "\\'").replace("\n", " ") for opt in q['a']]
        options_str = ", ".join([f"'{opt}'" for opt in options])
        print(f"    {{ q: '{q_str}', a: [{options_str}], correct: {q['correct']}, topic: '{q['topic']}', note: '{q['note']}' }},")
    print("],\n")

print(f"\nTotal questions by grade:")
for grade in grades:
    print(f"  Grade {grade}: {len(all_questions[grade])} questions")





