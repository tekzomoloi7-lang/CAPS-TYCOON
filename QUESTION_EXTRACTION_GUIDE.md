# Question Extraction Guide

## Current Status

- ✅ **Grade 11**: 140 questions extracted (needs manual review for correct answers)
- ✅ **Grade 12**: 54 questions extracted (needs manual review for correct answers)
- ❌ **Grade 9**: 0 questions extracted - document format needs manual extraction
- ❌ **Grade 10**: 0 questions extracted - document format needs manual extraction

## Issues with Extracted Questions

The automated extraction found questions but has some issues:
1. **Correct Answer Index**: All questions default to index 0 - needs manual verification
2. **Question Format**: Some questions have numbers at the start (e.g., "1 Two forces...") - should be cleaned
3. **Options**: Some questions have options embedded in question text (e.g., "A) linear. B) trigonal planar...")
4. **Placeholder Options**: Some questions have incorrect placeholder options

## Manual Extraction Process

### For Grade 9 and Grade 10:

1. Open the Word documents:
   - Grade 9: `Question Bank GRADE 9 NATURAL SCIENCES.docx`
   - Grade 10: `Question Bank of Grade 10 Physical Sciences MCQ's.docx`

2. For each question, extract:
   - **Question text** (remove question numbers)
   - **4 options** (A, B, C, D)
   - **Correct answer** (which option letter)
   - **Topic** (Mechanics, Electricity, Chemistry, etc.)

3. Format each question as:
```javascript
{
    q: 'Question text here',
    a: ['Option A', 'Option B', 'Option C', 'Option D'],
    correct: 0,  // 0 for A, 1 for B, 2 for C, 3 for D
    topic: 'Topic Name',
    note: 'CAPS Grade X: Topic Name'
}
```

### Example:
```javascript
{
    q: 'What is the unit of force?',
    a: ['Newton (N)', 'Joule (J)', 'Watt (W)', 'Pascal (Pa)'],
    correct: 0,  // A is correct
    topic: 'Mechanics',
    note: 'CAPS Grade 10: Mechanics'
}
```

## Adding Questions to HTML

1. Open `caps-tycoon.html`
2. Find the `questionBanks` object (around line 4578)
3. Add questions to the appropriate grade array:
   - `questionBanks.physicalSciences.grade9` for Grade 9
   - `questionBanks.physicalSciences.grade10` for Grade 10
   - `questionBanks.physicalSciences.grade11` for Grade 11
   - `questionBanks.physicalSciences.grade12` for Grade 12

## Topics to Use

Common Physical Sciences topics:
- Mechanics
- Electricity
- Magnetism
- Waves
- Light
- Atomic Structure
- Chemical Bonding
- Chemical Reactions
- Stoichiometry
- Acids and Bases
- Matter
- Energy
- Thermodynamics

## Next Steps

1. Review and fix Grade 11 and 12 extracted questions
2. Manually extract Grade 9 questions from Word document
3. Manually extract Grade 10 questions from Word document
4. Verify all correct answer indices
5. Clean up question text (remove leading numbers, fix formatting)

