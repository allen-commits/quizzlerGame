from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    """
    This class represents the UI. It is to help compartmentalize the code.
    ...

    Attributes
    ----------
    Because tkinter has extensive documentation, the individual attributes can read about at
    https://docs.python.org/3/library/tkinter.html
    """

    def __init__(self,
                 quiz_brain: QuizBrain):  # this ensures the proper data type is passed. In this case, its QuizBrain
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, highlightcolor=THEME_COLOR, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic"))

        self.score_label = Label(text="score = 0", fg="WHITE", bg=THEME_COLOR, font=("Ariel", 15, "italic"))
        self.score_label.grid(column=1, row=0)
        """This is the score label"""

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(column=1, row=2)
        """This is the false image and button"""

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_answer_true)
        self.true_button.grid(column=0, row=2)
        """This is the false image and button"""

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """
        Sets the canvas white, checks to see if there are still questions;
        if true, set the letter color to THEME_COLOR,  update the score, display the next question.
        if false, set the text to congratulate the player, and disable the 2 buttons.
        """
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
            self.score_label.config(text=f"Score = {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Congratulations! you made it to the end of the game!",
                                   fill="black")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer_true(self):
        """
        Calls the quiz.check_answer method. A value of true is passed when the player hits the true_button.
        check_answer() selects the current questions answer, and compares the answer. If the user is correct, then a
        "False" is passed into the variable is_correct. This value is then passed into give_feedback().
        """
        is_correct = self.quiz.check_answer("true")
        self.give_feedback(is_correct)

    def check_answer_false(self):
        """
        Calls the quiz.check_answer method. A value of true is passed when the player hits the true_button.
        check_answer() selects the current questions answer, and compares the answer. If the user is correct, then a
        "False" is passed into the variable is_correct. This value is then passed into give_feedback().
        """
        is_correct = self.quiz.check_answer("false")
        self.give_feedback(is_correct)

    def give_feedback(self, is_user_correct):
        """if True is passed into give_feedback(), set the canvas to green and set the letter color to white for half a
        second. After, call get_next_question()"""
        if is_user_correct:
            print("User got it right")
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
            print("User got it wrong")
        self.window.after(500, self.get_next_question)
