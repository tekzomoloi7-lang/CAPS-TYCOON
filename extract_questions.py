"""
Question Extraction Script for CAPS Tycoon Game
Extracts MCQ questions from Word documents and converts them to JavaScript format

Requirements:
    pip install python-docx

Usage:
    python extract_questions.py
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
        current_question = None
        current_options = []
        current_correct = None
        current_topic = "General"
        
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        
        text = "\n".join(full_text)
        
        # Try to identify question patterns
        # Common patterns:
        # 1. Question number followed by question text
        # 2. Options labeled A, B, C, D or 1, 2, 3, 4
        # 3. Correct answer indicated
        
        # Split by common question markers
        question_patterns = [
            r'(\d+[\.\)]\s*)(.+?)(?=\d+[\.\)]|$)',
            r'(Question\s+\d+[\.:]?\s*)(.+?)(?=Question\s+\d+|$)',
        ]
        
        # Simple extraction: look for numbered items
        lines = text.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Check if line looks like a question (starts with number or "Question")
            if re.match(r'^\d+[\.\)]', line) or line.lower().startswith('question'):
                # Extract question text
                question_text = re.sub(r'^\d+[\.\)]\s*', '', line)
                question_text = re.sub(r'^Question\s+\d+[\.:]?\s*', '', question_text, flags=re.IGNORECASE)
                
                if len(question_text) > 10:  # Valid question
                    options = []
                    correct_index = 0
                    topic = "General"
                    
                    # Look for options in next lines
                    j = i + 1
                    option_labels = ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd', '1', '2', '3', '4']
                    
                    while j < len(lines) and len(options) < 4:
                        opt_line = lines[j].strip()
                        # Check if line is an option
                        if re.match(r'^[A-Da-d1-4][\.\)]\s+', opt_line):
                            option_text = re.sub(r'^[A-Da-d1-4][\.\)]\s+', '', opt_line)
                            options.append(option_text)
                            
                            # Check if marked as correct (common indicators)
                            if '*' in opt_line or 'correct' in opt_line.lower() or 'answer' in opt_line.lower():
                                correct_index = len(options) - 1
                        j += 1
                    
                    # If we found a question with options
                    if len(options) >= 2:
                        # Try to determine topic from question text
                        topic_keywords = {
                            'Mechanics': ['force', 'acceleration', 'velocity', 'momentum', 'newton', 'motion'],
                            'Electricity': ['current', 'voltage', 'resistance', 'circuit', 'ohm', 'ampere'],
                            'Waves': ['wave', 'frequency', 'wavelength', 'sound', 'light'],
                            'Chemistry': ['atom', 'molecule', 'reaction', 'compound', 'element'],
                            'Atomic Structure': ['proton', 'neutron', 'electron', 'atomic number'],
                            'Chemical Bonding': ['bond', 'ionic', 'covalent', 'valency'],
                            'Acids and Bases': ['acid', 'base', 'pH', 'neutral'],
                            'Energy': ['energy', 'joule', 'work', 'power'],
                            'Matter': ['solid', 'liquid', 'gas', 'state', 'particle']
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
        return []

def main():
    """Main function to extract questions from all Word documents"""
    base_path = r"C:\Users\tekzo\Downloads\MCQ Question Bank Physical Sciences"
    
    grade_files = {
        9: "Question Bank GRADE 9 NATURAL SCIENCES.docx",
        10: "Question Bank of Grade 10 Physical Sciences MCQ's.docx",
        11: "Question Bank Physical Sciences Grade 11.docx",
        12: "Question Bank of Grade 12 Physical Sciences MCQ.docx"
    }
    
    all_questions = {}
    
    for grade, filename in grade_files.items():
        file_path = os.path.join(base_path, filename)
        if os.path.exists(file_path):
            print(f"\nExtracting questions from Grade {grade}...")
            questions = extract_questions_from_docx(file_path, grade)
            all_questions[grade] = questions
            print(f"Found {len(questions)} questions for Grade {grade}")
        else:
            print(f"File not found: {file_path}")
            all_questions[grade] = []
    
    # Generate JavaScript code
    js_output = "// Grade-specific Physical Sciences Questions\n\n"
    js_output += "// Grade 9 Questions\n"
    js_output += f"const grade9Questions = {json.dumps(all_questions[9], indent=4, ensure_ascii=False)};\n\n"
    js_output += "// Grade 10 Questions\n"
    js_output += f"const grade10Questions = {json.dumps(all_questions[10], indent=4, ensure_ascii=False)};\n\n"
    js_output += "// Grade 11 Questions\n"
    js_output += f"const grade11Questions = {json.dumps(all_questions[11], indent=4, ensure_ascii=False)};\n\n"
    js_output += "// Grade 12 Questions\n"
    js_output += f"const grade12Questions = {json.dumps(all_questions[12], indent=4, ensure_ascii=False)};\n"
    
    # Save to file
    output_file = os.path.join(r"C:\Users\tekzo\OneDrive\Desktop\CAPS TYCOON GAME", "extracted_questions.js")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_output)
    
    print(f"\n✅ Questions extracted and saved to: {output_file}")
    print(f"\nTotal questions extracted:")
    for grade in [9, 10, 11, 12]:
        print(f"  Grade {grade}: {len(all_questions[grade])} questions")
    
    # Also create a formatted version for manual review
    formatted_file = os.path.join(r"C:\Users\tekzo\OneDrive\Desktop\CAPS TYCOON GAME", "questions_formatted.txt")
    with open(formatted_file, 'w', encoding='utf-8') as f:
        for grade in [9, 10, 11, 12]:
            f.write(f"\n{'='*60}\n")
            f.write(f"GRADE {grade} QUESTIONS ({len(all_questions[grade])} questions)\n")
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





