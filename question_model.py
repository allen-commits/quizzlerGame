class Question:
    """
    A class to represent a given question text and its respective answer text.
    ...
    Attributes
    __________
    text: The question text
    answer: The Questions answer text
    """

    def __init__(self, q_text: str, q_answer: str):
        """
        Constructs all the necessary attributes for the question object
        :param q_text: Receives the question text.
        :param q_answer: Receives the answer text.
        """
        self.text = q_text
        self.answer = q_answer
