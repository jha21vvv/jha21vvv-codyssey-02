import json
import random

class Quiz:
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint
        }

class QuizGame:
    def __init__(self):
        self.is_running = True
        self.quizzes = []
        self.high_score = 0  # 변수명을 high_score로 통일
        self.load_data()      # 메서드명을 load_data로 통일

    def display_menu(self):
        print("\n" + "="*20)
        print("   파이썬 퀴즈 게임")
        print("="*20)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 관리 (등록/저장/불러오기)")
        print("3. 퀴즈 목록 보기")
        print("4. 최고 점수 확인")
        print("5. 퀴즈 삭제")
        print("6. 종료")
        print("="*20)

    def run(self):
        while self.is_running:
            self.display_menu()
            choice = input("원하는 메뉴 번호를 입력하세요: ")
            
            if choice == "1":
                self.play_quiz()
            elif choice == '2':
                self.manage_quizzes()
            elif choice == "3":
                self.show_quizzes()
            elif choice == "4":
                self.show_high_score()
            elif choice == "5":
                self.delete_quiz()
            elif choice == "6":
                print("\n게임을 종료합니다. 이용해 주셔서 감사합니다!")
                self.is_running = False
            else:
                print("\n[오류] 잘못된 입력입니다. 1~6 사이의 숫자를 입력해주세요.")

    def play_quiz(self):
        if not self.quizzes:
            print("\n[!] 등록된 퀴즈가 없습니다. 먼저 퀴즈를 등록해주세요.")
            return

        score = 0
        quiz_list = list(self.quizzes)
        random.shuffle(quiz_list)

        print("\n" + "="*20)
        print("🚀 퀴즈를 시작합니다! (기회는 총 2번!)")
        print("="*20)

        for quiz in quiz_list:
            print(f"\n[문제] {quiz.question}")
            for i, choice in enumerate(quiz.choices, 1):
                print(f"{i}. {choice}")

            try:
                user_ans = int(input("\n(1차 시도) 정답 번호: "))
                if user_ans == quiz.answer:
                    print("✅ 정답입니다! (+2점)")
                    score += 2
                else:
                    print(f"\n❌ 틀렸습니다! 힌트를 드릴게요.")
                    print(f"💡 힌트: {quiz.hint}")
                    user_ans = int(input("(2차 시도) 다시 입력: "))
                    
                    if user_ans == quiz.answer:
                        print("✅ 정답입니다! (+1점)")
                        score += 1
                    else:
                        print(f"❌ 아쉽네요. 정답은 {quiz.answer}번이었습니다.")
            except ValueError:
                print("⚠️ 숫자로만 입력해야 합니다. 다음 문제로 넘어갑니다.")

        print(f"\n🎊 게임 종료! 최종 점수: {score}점")
        if score > self.high_score:
            print(f"⭐ 최고 점수 갱신! ({self.high_score} -> {score})")
            self.high_score = score
            self.save_data()

    def manage_quizzes(self):
        while True:
            print("\n" + "-"*20)
            print("   퀴즈 관리 메뉴")
            print("1. 새로운 퀴즈 등록 (Add)")
            print("2. 파일에서 불러오기 (Load)")
            print("3. 파일에 저장하기 (Save)")
            print("4. 메인 메뉴로 돌아가기")
            print("-"*20)
            
            choice = input("선택: ")
            if choice == '1':
                self.add_quiz()
            elif choice == '2':
                self.load_data()
                print("\n[성공] 데이터를 불러왔습니다.")
            elif choice == '3':
                self.save_data()
                print("\n[성공] 데이터를 저장했습니다.")
            elif choice == '4':
                break

    def add_quiz(self):
        question = input("\n문제 내용: ")
        choices = [input(f"보기 {i}번: ") for i in range(1, 5)]
        hint = input("힌트 내용: ")
        try:
            answer = int(input("정답 번호 (1-4): "))
            self.quizzes.append(Quiz(question, choices, answer, hint))
            print("[알림] 메모리에 추가되었습니다. 저장하려면 Save를 눌러주세요.")
        except ValueError:
            print("[오류] 숫자를 입력하세요.")

    def show_quizzes(self):
        print("\n" + "="*20)
        print("   현재 등록된 퀴즈 목록")
        print("="*20)
        
        if not self.quizzes:
            print("[!] 등록된 퀴즈가 없습니다.")
            return

        for i, quiz in enumerate(self.quizzes, 1):
            # quiz 객체에서 question 속성을 가져와서 출력
            print(f"{i}. {quiz.question}")
        print("="*20)

    def delete_quiz(self):
        self.show_quizzes()
        if not self.quizzes: return
        try:
            idx = int(input("\n삭제할 번호: ")) - 1
            if 0 <= idx < len(self.quizzes):
                del self.quizzes[idx]
                print("[삭제 완료]")
            else:
                print("[오류] 범위를 벗어났습니다.")
        except ValueError:
            print("[오류] 숫자를 입력하세요.")

    def show_high_score(self):
        print(f"\n🏆 현재 최고 점수: {self.high_score}점")

    def save_data(self):
        data = {
            "high_score": self.high_score,
            "quizzes": [q.to_dict() for q in self.quizzes]
        }
        with open("quizzes.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_data(self):
        try:
            with open("quizzes.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                
                # 1. 데이터가 딕셔너리 형태인 경우 (새로운 형식: 점수 + 퀴즈)
                if isinstance(data, dict):
                    self.high_score = data.get("high_score", 0)
                    quiz_data = data.get("quizzes", [])
                    self.quizzes = [Quiz(**q) for q in quiz_data]
                
                # 2. 데이터가 리스트 형태인 경우 (예전 형식: 퀴즈만 있음)
                elif isinstance(data, list):
                    self.high_score = 0
                    self.quizzes = [Quiz(**q) for q in data]
                    
        except (FileNotFoundError, json.JSONDecodeError):
            # 파일이 없거나 내용이 비어있을 때 초기화
            self.quizzes = []
            self.high_score = 0

if __name__ == "__main__":
    game = QuizGame()
    game.run()