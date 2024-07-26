import string
from pypdf import PdfReader


def extract_questions(pages_num: int, reader: PdfReader) -> list:
    """
    Extracts questions and returns a list of questions
    """
    questions = []

    for pg_num in range(NUM_OF_PAGES):
        page = reader.pages[pg_num]
        pg_text = page.extract_text()

        for i, txt in enumerate(pg_text):
            question = ''

            # If a word is question mark, get previous words
            if txt != '?':
                continue

            # For Loop backward from current word index - 1
            for num in range(i - 1, 1, -1):

                # If a punctuation is met, it most likely isn't part of the question
                if pg_text[num] in string.punctuation:
                    questions.append(question + '?')
                    break

                # prepend text to question,
                question = pg_text[num] + question
            
    return questions


def save_questions(questions):
    with open('The Jungle Book questions.txt', 'w') as f:
        for question in questions:
            question_without_break = question.replace('\n', ' ')
            question_without_leading_space = question_without_break.strip()
            f.write(question_without_leading_space + '\n')


if __main__ == "__name__":
    reader = PdfReader('The Jungle book.pdf')
    pages_num = reader.pages
    text_questions = extract_questions(pages_num, reader)
    save_questions(text_questions)


