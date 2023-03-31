import html


class QuizBrain:
    """
    A class to control the quiz functions.
    ...
    Attributes
    ----------
    question_number: int
        The current question number
    score: int
        The current score
    question_list: list
        A list of questions (10). Each element is of Question type, defined in the question_model class
    current_question: Question
        The current question, derived from the question class, selected using the question_number

    Methods
    -------
    still_has_questions():
        Checks if there is still questions left in the question_list. Returns True or False.
    next_question():
        Selects the current question, adds 1 to the question_number, escapes the question text, and returns the question
        number and text.
    check_answer(user_answer):
        Receives the parameter of the user answer (which is "true" or "false"), selects the current questions answer,
        and compares the answer. If the user is wrong, return False, else, return True.
    """

    def __init__(self, q_list: list):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
        q_list: list
            The list of questions that is constructed in main.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Checks if there is still questions left in the question_list. Returns True or False"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Selects the current question, adds 1 to the question_number, escapes the question text, and returns the
        question number and text."""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text} (True/False): "
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        """Receives the parameter of the user answer (which is "true" or "false"), selects the current questions answer,
        and compares the answer. If the user is wrong, return False, else, return True."""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
