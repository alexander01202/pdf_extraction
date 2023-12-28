import fitz
import string
from pypdf import PdfReader

reader = PdfReader('The Jungle book.pdf')
fitz.open('The Jungle book.pdf')

def extract_questions() -> list:
    questions = []

    for i in range(len(reader.pages)):
        page = reader.pages[i]
        pg_text = page.extract_text()

        for i,txt in enumerate(pg_text):
            question = ''

            if txt == '?':
                for num in range(i - 1, 1, -1):
                    if pg_text[num] in (string.punctuation):
                        questions.append(question + '?')
                        break
                    else:
                        # appends to the front
                        question = pg_text[num] + question
            
    return questions

text_questions = extract_questions()

file = open('The Jungle Book questions.txt', 'w')

for question in text_questions:
    question_without_break = question.replace('\n', ' ')
    question_without_leading_space = question_without_break.strip()
    file.write(question_without_leading_space + '\n')