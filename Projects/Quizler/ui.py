from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.high_score = 0

        self.window = Tk()
        self.window.title('Quizler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')

        self.score_text = Label(text=f'Score = {self.quiz.score}', bg=THEME_COLOR)
        self.card = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.card_text = self.card.create_text(150, 125,
                                               text='sample', fill=THEME_COLOR,
                                               width=280, font=FONT,
                                               justify=LEFT)
        self.true_button = Button(image=true_img, highlightbackground=THEME_COLOR, command=self.true_pressed)
        self.false_button = Button(image=false_img, highlightbackground=THEME_COLOR, command=self.false_pressed)

        self.score_text.grid(column=1, row=0)
        self.card.grid(column=0, row=1, sticky='e', columnspan=2, pady=50)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.card.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_text.config(text=f'Score = {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.card.itemconfig(self.card_text, text=q_text)
        else:
            self.card.itemconfig(self.card_text, text=f"You've reached the end of the quiz. "
                                                      f"Your guessed right {self.quiz.score} out of 10 questions")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.card.config(bg='green')
        else:
            self.card.config(bg='red')
        self.window.after(1000, self.get_next_question)
