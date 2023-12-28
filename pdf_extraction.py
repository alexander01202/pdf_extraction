import fitz
import string
from pypdf import PdfReader

reader = PdfReader('The Jungle book.pdf')
fitz.open('The Jungle book.pdf')

def extract_questions() -> list:
    """
    Extracts questions and returns a list of questions
    """
    questions = []

    for i in range(len(reader.pages)):
        page = reader.pages[i]
        pg_text = page.extract_text()

        for i,txt in enumerate(pg_text):
            question = ''

            # If a word is question mark, get previous words
            if txt == '?':
                # For Loop backward from current word index - 1
                for num in range(i - 1, 1, -1):

                    # If a punctuation is met, it most likely isn't part of the question
                    if pg_text[num] in (string.punctuation):
                        questions.append(question + '?')
                        break
                    else:
                        # prepend text to question, 
                        question = pg_text[num] + question
            
    return questions

text_questions = extract_questions()

file = open('The Jungle Book questions.txt', 'w')
for question in text_questions:
    question_without_break = question.replace('\n', ' ')
    question_without_leading_space = question_without_break.strip()
    file.write(question_without_leading_space + '\n')
