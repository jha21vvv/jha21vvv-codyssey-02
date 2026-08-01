class Quiz:
    def __init__(self, question, choices, answer,hint):
        """
        문제 카드 한 장을 만드는 설계도입니다.
        :param question: 문제 내용 (문자열)
        :param choices: 보기 4개 (리스트)
        :param answer: 정답 번호 (정수)
        """
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint # 힌트 저장

    def to_dict(self):
        """나중에 파일(JSON)에 저장하기 쉽게 사전 형태로 변환합니다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint 
            # 힌트 포함
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
               # print("\n[알림] 퀴즈 등록 기능을 준비 중입니다.") <- 이 줄을 아래로 교체
               self.add_quiz()
            elif choice == "3":
                self.show_quizzes() # 3번 메뉴 연결
            elif choice == "4":
                print("\n[알림] 최고 점수 확인 기능을 준비 중입니다.")
            elif choice == "5":
                print("\n게임을 종료합니다. 이용해 주셔서 감사합니다!")
                self.is_running = False
            else:
                print("\n[오류] 잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요.")
    def add_quiz(self):
        print("\n" + "-"*20)
        print("새로운 퀴즈를 등록합니다.")
        
        # 1. 문제 입력 받기
        question = input("문제 내용을 입력하세요: ")
        
        # 2. 보기 4개 입력 받기 (리스트 활용)
        choices = []
        for i in range(1, 5):
            choice = input(f"보기 {i}번을 입력하세요: ")
            choices.append(choice)
        hint = input("힌트를 입력하세요: ") 

        # 3. 정답 번호 입력 받기
        try:
            answer = int(input("정답 번호를 입력하세요 (1~4): "))
            if 1 <= answer <= 4:
                # 4. Quiz 객체 생성 및 리스트에 추가
                new_quiz = Quiz(question, choices, hint) 
                self.quizzes.append(new_quiz)
                print("\n[성공] 퀴즈가 등록되었습니다!")
            else:
                print("\n[오류] 정답은 1~4 사이의 숫자여야 합니다. 등록 실패.")
        except ValueError:
            print("\n[오류] 숫자를 입력해야 합니다. 등록 실패.")
        # 힌트 입력 단계 추가
    def show_quizzes(self):
        print("\n" + "-"*20)
        print("등록된 퀴즈 목록")
        
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 등록해 주세요!")
            return

        for i, quiz in enumerate(self.quizzes, 1):
            print(f"{i}. {quiz.question} (정답: {quiz.answer}번)")
            for j, choice in enumerate(quiz.choices, 1):
                print(f"   {j}) {choice}")
            print(f"   [힌트: {quiz.hint}]") # 힌트도 잘 들어갔는지 확인
        print("-"*20)        
# 프로그램의 시작점
#임포트가 아니라 python main.py라고 쳐서 이 파일을 주인공으로 실행했을 때 게임을 즉시 시작한다는 내용
if __name__ == "__main__":
    #QuizGame() 바탕으로 게임기 제작
    game = QuizGame()
    #게임기 실행    
    game.run()