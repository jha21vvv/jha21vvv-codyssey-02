class QuizGame:
    def __init__(self):
        # 게임이 계속 실행될지 결정하는 변수입니다.
        # 1. 이 게임 객체가 만들어지는 순간 자동으로 실행된다.
        # 2. 'self'라는 내 주머니 안에 'is_running'이라는 스위치를 넣는다.
        # 3. 그 스위치의 초기 상태를 'True(켜짐)'로 설정한다
        self.is_running = True

    def display_menu(self):
        """메뉴를 화면에 출력하는 함수"""
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
        """게임을 실행하고 사용자의 입력을 받는 메인 루프"""
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
                self.is_running = False  # 루프를 빠져나가 게임을 종료합니다.
            else:
                # 요구사항: 잘못된 입력에 대한 처리
                print("\n[오류] 잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요.")

# 프로그램의 시작점
#임포트가 아니라 직접 실행일때 게임을 즉시 시작한다는 내용
if __name__ == "__main__":
    game = QuizGame()
    game.run()