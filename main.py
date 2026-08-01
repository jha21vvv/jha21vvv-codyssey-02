class Quiz:
    def __init__(self, question, choices, answer):
        """
        문제 카드 한 장을 만드는 설계도입니다.
        :param question: 문제 내용 (문자열)
        :param choices: 보기 4개 (리스트)
        :param answer: 정답 번호 (정수)
        """
        self.question = question
        self.choices = choices
        self.answer = answer

    def to_dict(self):
        """나중에 파일(JSON)에 저장하기 쉽게 사전 형태로 변환합니다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

class QuizGame:
    def __init__(self):
        # 게임이 계속 실행될지 결정하는 변수입니다.
        # 1. 이 게임 객체가 만들어지는 순간 자동으로 실행된다.
        # 2. 'self'라는 내 주머니 안에 'is_running'이라는 스위치를 넣는다.
        # 3. 그 스위치의 초기 상태를 'True(켜짐)'로 설정한다
        self.is_running = True
        # 퀴즈 객체들을 담을 리스트
        self.quizzes = []
        # 최고 점수 기록
        self.best_score = 0

    def display_menu(self):
        print("\n" + "="*20)
        print("   파이썬 퀴즈 게임")
        print("="*20)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 등록")
        print("3. 퀴즈 목록 보기")
        print("4. 최고 점수 확인")
        print("5. 종료")
        print("="*20)

    def run(self):
        while self.is_running:
            self.display_menu()
            choice = input("원하는 메뉴 번호를 입력하세요: ")
            
            if choice == "1":
                print("\n[알림] 퀴즈 풀기 기능을 준비 중입니다.")
            elif choice == "2":
                print("\n[알림] 퀴즈 등록 기능을 준비 중입니다.")
            elif choice == "3":
                print("\n[알림] 퀴즈 목록 보기 기능을 준비 중입니다.")
            elif choice == "4":
                print("\n[알림] 최고 점수 확인 기능을 준비 중입니다.")
            elif choice == "5":
                print("\n게임을 종료합니다. 이용해 주셔서 감사합니다!")
                self.is_running = False
            else:
                print("\n[오류] 잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요.")
# 프로그램의 시작점
#임포트가 아니라 python main.py라고 쳐서 이 파일을 주인공으로 실행했을 때 게임을 즉시 시작한다는 내용
if __name__ == "__main__":
    #QuizGame() 바탕으로 게임기 제작
    game = QuizGame()
    #게임기 실행    
    game.run()