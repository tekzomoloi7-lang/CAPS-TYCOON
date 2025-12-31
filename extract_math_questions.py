"""
Mathematics Question Extraction Script for CAPS Tycoon Game
Extracts MCQ questions from Word documents and converts them to JavaScript format

Requirements:
    pip install python-docx

Usage:
    python extract_math_questions.py
"""

try:
    from docx import Document
    import re
    import json
    import os
except ImportError:
    print("Installing required package...")
    import subprocess
    subprocess.check_call(["pip", "install", "python-docx"])
    from docx import Document
    import re
    import json
    import os

def extract_questions_from_docx(file_path, grade):
    """Extract questions from a Word document"""
    try:
        doc = Document(file_path)
        questions = []
        
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        
        text = "\n".join(full_text)
        
        # Split by lines
        lines = text.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip headers and section titles
            if any(keyword in line.lower() for keyword in ['paper', 'section', 'grade', 'compilation', 'mcq']):
                if len(line.split()) < 5:  # Likely a header
                    i += 1
                    continue
            
            # Check if line looks like a question with embedded options
            # Pattern: "Question text ... A. option1 B. option2 C. option3 D. option4"
            # Or: "Number. Question text A. option1 B. option2 C. option3 D. option4"
            question_match = None
            
            # Try pattern: options embedded in same line with "A. ... B. ... C. ... D. ..."
            embedded_pattern = r'(.+?)(?:\.\.\.|\.|:|\?)\s*([A-Da-d]\.\s*[^A-D]+?)\s+([A-Da-d]\.\s*[^A-D]+?)\s+([A-Da-d]\.\s*[^A-D]+?)\s+([A-Da-d]\.\s*[^A-D]+?)(?:\s|$)'
            embedded_match = re.search(embedded_pattern, line, re.IGNORECASE)
            
            if embedded_match:
                # Extract question and options from embedded format
                question_text = embedded_match.group(1).strip()
                options = [
                    embedded_match.group(2).strip(),
                    embedded_match.group(3).strip(),
                    embedded_match.group(4).strip(),
                    embedded_match.group(5).strip()
                ]
                
                # Clean up question text (remove leading numbers)
                question_text = re.sub(r'^\d+[\.\)]\s*', '', question_text)
                question_text = re.sub(r'^\d+\.\s*', '', question_text)
                
                # Clean up options (remove "A. ", "B. ", etc.)
                cleaned_options = []
                for opt in options:
                    opt_clean = re.sub(r'^[A-Da-d][\.\)]\s*', '', opt).strip()
                    cleaned_options.append(opt_clean)
                options = cleaned_options
                
                correct_index = 0  # Default, needs manual verification
                topic = "General"
                
                # Determine topic from question text
                topic_keywords = {
                    'Algebra': ['algebra', 'equation', 'solve', 'factor', 'expand', 'simplify', 'quadratic', 'linear', 'polynomial', 'x =', 'x^'],
                    'Geometry': ['triangle', 'circle', 'angle', 'area', 'perimeter', 'volume', 'similar', 'congruent', 'parallel', 'perpendicular', 'shape'],
                    'Trigonometry': ['trig', 'sin', 'cos', 'tan', 'angle', 'sine', 'cosine', 'tangent'],
                    'Financial Maths': ['interest', 'compound', 'loan', 'investment', 'deposit', 'annuity', 'present value', 'future value', 'simple interest', 'finance'],
                    'Statistics': ['mean', 'median', 'mode', 'average', 'data', 'graph', 'chart', 'probability', 'standard deviation'],
                    'Functions': ['function', 'graph', 'domain', 'range', 'inverse', 'exponential', 'logarithm', 'y =', 'asymptote', 'intercept', 'gradient'],
                    'Calculus': ['derivative', 'integral', 'differentiate', 'integrate', 'limit', 'calculus'],
                    'Number Patterns': ['sequence', 'pattern', 'series', 'arithmetic', 'geometric', 'term', 'lcm', 'hcf', 'next term', 'common ratio'],
                    'Exponents': ['exponent', 'power', 'index', 'indices', 'base', '^', 'square root', 'cube root'],
                    'Analytical Geometry': ['coordinate', 'gradient', 'distance', 'midpoint', 'line', 'slope']
                }
                
                for topic_name, keywords in topic_keywords.items():
                    if any(keyword in question_text.lower() for keyword in keywords):
                        topic = topic_name
                        break
                
                if len(question_text) > 10 and len(options) == 4:
                    questions.append({
                        'q': question_text,
                        'a': options,
                        'correct': correct_index,
                        'topic': topic,
                        'note': f'CAPS Grade {grade}: {topic}'
                    })
            else:
                # Try pattern: question on one line, options on next lines
                if re.match(r'^\d+[\.\)]', line) or (len(line) > 20 and ('?' in line or '...' in line)):
                    # Extract question text
                    question_text = re.sub(r'^\d+[\.\)]\s*', '', line)
                    question_text = re.sub(r'^Question\s+\d+[\.:]?\s*', '', question_text, flags=re.IGNORECASE)
                    question_text = question_text.strip()
                    
                    if len(question_text) > 10:  # Valid question
                        options = []
                        correct_index = 0
                        topic = "General"
                        
                        # Look for options in next lines
                        j = i + 1
                        max_lines_to_check = 10
                        lines_checked = 0
                        
                        while j < len(lines) and len(options) < 4 and lines_checked < max_lines_to_check:
                            opt_line = lines[j].strip()
                            lines_checked += 1
                            
                            # Skip empty lines
                            if not opt_line:
                                j += 1
                                continue
                            
                            # Check if line is an option (A, B, C, D)
                            option_match = re.match(r'^([A-Da-d])[\.\)]\s+(.+)$', opt_line)
                            if option_match:
                                option_text = option_match.group(2).strip()
                                
                                # Only add if it looks like a real option
                                if len(option_text) > 1 and not re.match(r'^\d+[\.\)]', option_text):
                                    options.append(option_text)
                                    
                                    # Check if marked as correct
                                    if '*' in opt_line or 'correct' in opt_line.lower():
                                        correct_index = len(options) - 1
                                    
                                    if len(options) == 4:
                                        break
                            
                            j += 1
                        
                        # If we found a question with options
                        if len(options) >= 2:
                            # Pad to 4 options if we have fewer
                            while len(options) < 4:
                                options.append("Option not available")
                            
                            # Try to determine topic from question text
                            topic_keywords = {
                                'Algebra': ['algebra', 'equation', 'solve', 'factor', 'expand', 'simplify', 'quadratic', 'linear', 'polynomial'],
                                'Geometry': ['triangle', 'circle', 'angle', 'area', 'perimeter', 'volume', 'similar', 'congruent', 'parallel', 'perpendicular'],
                                'Trigonometry': ['trig', 'sin', 'cos', 'tan', 'angle', 'triangle', 'sine', 'cosine', 'tangent'],
                                'Financial Maths': ['interest', 'compound', 'loan', 'investment', 'deposit', 'annuity', 'present value', 'future value'],
                                'Statistics': ['mean', 'median', 'mode', 'average', 'data', 'graph', 'chart', 'probability', 'standard deviation'],
                                'Functions': ['function', 'graph', 'domain', 'range', 'inverse', 'exponential', 'logarithm'],
                                'Calculus': ['derivative', 'integral', 'differentiate', 'integrate', 'limit', 'calculus'],
                                'Number Patterns': ['sequence', 'pattern', 'series', 'arithmetic', 'geometric', 'term'],
                                'Exponents': ['exponent', 'power', 'index', 'indices', 'base'],
                                'Analytical Geometry': ['coordinate', 'gradient', 'distance', 'midpoint', 'line', 'slope']
                            }
                            
                            for topic_name, keywords in topic_keywords.items():
                                if any(keyword in question_text.lower() for keyword in keywords):
                                    topic = topic_name
                                    break
                            
                            questions.append({
                                'q': question_text,
                                'a': options[:4],  # Ensure exactly 4 options
                                'correct': correct_index,
                                'topic': topic,
                                'note': f'CAPS Grade {grade}: {topic}'
                            })
            
            i += 1
        
        return questions
    
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        import traceback
        traceback.print_exc()
        return []

def main():
    """Main function to extract questions from all Mathematics Word documents"""
    base_path = r"C:\Users\tekzo\Downloads\MCQ Question Bank Mathematics"
    
    grade_files = {
        8: "Question Bank Grade 8 Mathematics MCQ Compilation.docx",
        9: "Question Bank Mathematics Grade 9 MCQ's.docx",
        10: "Question Bank Grade 10 Mathematics MCQ.docx",
        11: "Question Bank Grade 11 Mathematics MCQ.docx",
        12: "Question Bank of Grade 12 Mathematics MCQs.docx"
    }
    
    all_questions = {}
    
    for grade, filename in grade_files.items():
        file_path = os.path.join(base_path, filename)
        if os.path.exists(file_path):
            print(f"\nExtracting questions from Grade {grade} Mathematics...")
            questions = extract_questions_from_docx(file_path, grade)
            all_questions[grade] = questions
            print(f"Found {len(questions)} questions for Grade {grade}")
        else:
            print(f"File not found: {file_path}")
            all_questions[grade] = []
    
    # Generate JavaScript code
    js_output = "// Grade-specific Mathematics Questions\n\n"
    for grade in [8, 9, 10, 11, 12]:
        js_output += f"// Grade {grade} Questions\n"
        js_output += f"const mathGrade{grade}Questions = {json.dumps(all_questions[grade], indent=4, ensure_ascii=False)};\n\n"
    
    # Save to file
    output_file = os.path.join(r"C:\Users\tekzo\OneDrive\Desktop\CAPS TYCOON GAME", "extracted_math_questions.js")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_output)
    
    print(f"\n✅ Questions extracted and saved to: {output_file}")
    print(f"\nTotal questions extracted:")
    for grade in [8, 9, 10, 11, 12]:
        print(f"  Grade {grade}: {len(all_questions[grade])} questions")
    
    # Also create a formatted version for manual review
    formatted_file = os.path.join(r"C:\Users\tekzo\OneDrive\Desktop\CAPS TYCOON GAME", "math_questions_formatted.txt")
    with open(formatted_file, 'w', encoding='utf-8') as f:
        for grade in [8, 9, 10, 11, 12]:
            f.write(f"\n{'='*60}\n")
            f.write(f"GRADE {grade} MATHEMATICS QUESTIONS ({len(all_questions[grade])} questions)\n")
            f.write(f"{'='*60}\n\n")
            for i, q in enumerate(all_questions[grade], 1):
                f.write(f"Question {i}:\n")
                f.write(f"  Q: {q['q']}\n")
                f.write(f"  Options:\n")
                for j, opt in enumerate(q['a']):
                    marker = "✓" if j == q['correct'] else " "
                    f.write(f"    {marker} {chr(65+j)}. {opt}\n")
                f.write(f"  Topic: {q['topic']}\n")
                f.write(f"  Note: {q['note']}\n\n")
    
    print(f"\n📄 Formatted questions saved to: {formatted_file}")
    print("\n⚠️  Please review the extracted questions and manually verify:")
    print("   1. Question text is correct")
    print("   2. Options are in the right order")
    print("   3. Correct answer index is accurate")
    print("   4. Topics are assigned correctly")

if __name__ == "__main__":
    main()

