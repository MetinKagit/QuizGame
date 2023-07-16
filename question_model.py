class Question():
    """ This creates a question object."""

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def get_text(self):
        ":return: question text"
        return self.text

    def get_answer(self):
        ":return: question answer"
        return self.answer
