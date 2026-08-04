class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self, number):
        # 문제 {number} 형식으로 question 출력
        # choices를 1~4번 선택지로 출력 (enumerate 활용)
        print(f"[문제 {number}]")
        print(self.question)
        print()
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def is_correct(self, user_answer):
        # user_answers와 self.answer를 비교해서 True/False 반환
        return user_answer == self.answer
