import json
import random
import datetime # 날짜 기록을 위해 상단에 추가 필요

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
        self.history = [] # 점수 기록 히스토리 리스트 추가
        self.load_data()      # 메서드명을 load_data로 통일

    def get_safe_input(self, prompt, min_val=None, max_val=None):
        while True:
            try:
                user_input = input(prompt).strip() # 1. 앞뒤 공백 제거
                if not user_input: # 2. 빈 입력 처리
                    print("⚠️ 입력값이 없습니다. 다시 입력해주세요.")
                    continue
                
                val = int(user_input) # 3. 숫자 변환
                
                # 4. 허용 범위 밖 숫자 처리
                if min_val is not None and val < min_val:
                    print(f"⚠️ {min_val} 이상의 숫자를 입력하세요.")
                elif max_val is not None and val > max_val:
                    print(f"⚠️ {max_val} 이하의 숫자를 입력하세요.")
                else:
                    return val # 모든 조건 만족 시 반환
            except ValueError: # 5. 숫자 변환 실패 시 재입력
                print("⚠️ 숫자로만 입력해주세요.")
                
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
        try:
            while self.is_running:
                self.display_menu()
                choice = self.get_safe_input("원하는 메뉴 번호를 입력하세요 (1-6): ", 1, 6)     
                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.manage_quizzes()
                elif choice == 3:
                    self.show_quizzes()
                elif choice == 4:
                    self.show_high_score()
                elif choice == 5:
                    self.delete_quiz()
                elif choice == 6: 
                    self.exit_game()
                else: print("\n[오류] 1~6 사이의 숫자를 입력해주세요.")
                
        except (KeyboardInterrupt, EOFError): # Ctrl+C 또는 입력 종료 시
            self.exit_game()

    def exit_game(self):
        print("\n\n[알림] 프로그램을 안전하게 종료합니다. 데이터를 저장합니다...")
        self.save_data() # 종료 전 자동 저장
        self.is_running = False

    def play_quiz(self):
        if not self.quizzes:
            print("\n[!] 등록된 퀴즈가 없습니다. 먼저 퀴즈를 등록해주세요.")
            return
        # 1. 문제 수 선택 기능
        total_available = len(self.quizzes)
        print(f"\n현재 총 {total_available}개의 문제가 있습니다.")
        num_to_solve = self.get_safe_input(f"몇 문제를 푸시겠습니까? (1-{total_available}): ", 1, total_available)

        # 문제 섞기 및 선택
        quiz_list = random.sample(self.quizzes, num_to_solve)
        score = 0

        print("\n" + "="*30)
        print(f"🚀 퀴즈 시작! (총 {num_to_solve}문제)")
        print("💡 힌트(5번)를 쓰면 기회는 1번, 점수는 1점!")
        print("="*30)

        for idx, quiz in enumerate(quiz_list, 1):
            print(f"\n[Q{idx}] {quiz.question}")
            for i, choice in enumerate(quiz.choices, 1):
                print(f"{i}. {choice}")

            # 2 & 3. 힌트 기능 및 점수 차감 로직
            user_ans = self.get_safe_input("\n정답 번호 (1-4, 힌트는 5번): ", 1, 5)

            if user_ans == 5: # 힌트 사용
                print(f"🔍 [HINT] {quiz.hint}")
                # 힌트 사용 시 1회 시도만 가능
                user_ans = self.get_safe_input("정답 번호 (1-4): ", 1, 4)
                if user_ans == quiz.answer:
                    print("✅ 정답입니다! (힌트 사용: +1점)")
                    score += 1
                else:
                    print(f"❌ 틀렸습니다. 정답은 {quiz.answer}번이었습니다.")
            else: # 힌트 미사용 (바로 정답 입력)
                if user_ans == quiz.answer:
                    print("✅ 정답입니다! (+2점)")
                    score += 2
                else:
                    print(f"❌ 틀렸습니다. 정답은 {quiz.answer}번이었습니다.")

        # 게임 종료 및 결과 처리
        print("\n" + "="*30)
        print(f"🎊 게임 종료! 최종 점수: {score}점")
        
        # 최고 점수 갱신
        if score > self.high_score:
            print(f"⭐ 최고 점수 갱신! ({self.high_score} -> {score})")
            self.high_score = score

        # 5. 점수 기록 히스토리 저장
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = {
            "date": now,
            "num_questions": num_to_solve,
            "score": score
        }
        self.history.append(record)
        self.save_data() # 변경된 점수와 히스토리 저장
        print("💾 결과가 state.json에 기록되었습니다.")
    def delete_quiz(self):
        """퀴즈를 목록에서 삭제하고 state.json에 즉시 반영합니다."""
        # 1. 현재 등록된 퀴즈 목록을 먼저 보여줍니다.
        self.show_quizzes()
        
        # 2. 퀴즈가 하나도 없으면 삭제 과정을 진행하지 않습니다.
        if not self.quizzes:
            return

        # 3. 삭제할 번호 입력 받기 (get_safe_input 사용으로 안전함)
        # 0을 입력하면 삭제를 취소할 수 있도록 범위를 0부터 설정했습니다.
        print("\n[삭제 안내] 삭제할 문제의 번호를 입력해주세요.")
        choice = self.get_safe_input(f"삭제할 번호 (1-{len(self.quizzes)}, 취소는 0): ", 0, len(self.quizzes))

        if choice == 0:
            print("[알림] 삭제가 취소되었습니다.")
            return

        # 4. 선택한 퀴즈 삭제 (리스트 인덱스는 0부터 시작하므로 입력값에서 1을 뺍니다)
        removed_quiz = self.quizzes.pop(choice - 1)
        print(f"\n✅ [삭제 완료] 문제: '{removed_quiz.question}'")

        # 5. 중요: 삭제된 상태를 파일에 즉시 저장합니다.
        self.save_data()
        print("[시스템] 변경사항이 state.json에 안전하게 저장되었습니다.")

    def manage_quizzes(self):
        while True:
            print("\n" + "-"*20)
            print("   퀴즈 관리 메뉴")
            print("1. 새로운 퀴즈 등록 (Add)")
            print("2. 파일에서 불러오기 (Load)")
            print("3. 파일에 저장하기 (Save)")
            print("4. 메인 메뉴로 돌아가기")
            print("-"*20)
            
            choice = self.get_safe_input("선택 (1-4): ", 1, 4)
            if choice == 1:
                self.add_quiz()
            elif choice == 2:
                self.load_data()
                print("\n[성공] 데이터를 불러왔습니다.")
            elif choice == 3:
                self.save_data()
                print("\n[성공] 데이터를 저장했습니다.")
            elif choice == 4:
                break

    def add_quiz(self):
        question = input("\n문제 내용: ")
        choices = [input(f"보기 {i}번: ") for i in range(1, 5)]
        hint = input("힌트 내용: ")
        try:
            answer = self.get_safe_input("정답 번호 (1-4): ", 1, 4)
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

    # 파일 입출력 시 history도 포함하도록 수정
    def save_data(self):
        try:
            data = {
                "high_score": self.high_score,
                "history": self.history, # 히스토리 추가
                "quizzes": [q.to_dict() for q in self.quizzes]
            }
            with open("state.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                # dump는 저장하다-data는 저장할것-f는 객체용 그릇, 위에 "state.json"을 f라고 했음-"ASCII(영어 중심 문자 체계)만 고집할 것인가?" -> "아니오(False)"-들여쓰기를 4칸씩 해줘:이 옵션이 없으면 JSON 파일의 모든 내용이 한 줄로 길게 붙어서 저장(인간 읽기용)
            # print("\n[시스템] 데이터가 state.json에 안전하게 저장되었습니다.")
        except Exception as e:
            print(f"\n[오류] 파일 저장 중 문제가 발생했습니다: {e}")

    def show_high_score(self):
        print(f"\n🏆 현재 최고 점수: {self.high_score}점")

    def load_data(self):
        try:
            with open("state.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                
                # 1. 데이터가 딕셔너리 형태인 경우 (최신 형식)
                if isinstance(data, dict):
                    self.high_score = data.get("high_score", 0)
                    self.history = data.get("history", []) # 히스토리 불러오기
                    quiz_data = data.get("quizzes", [])
                    self.quizzes = [Quiz(**q) for q in quiz_data]
                    # **q: 만약 q가 {"question": "1+1?", "choices": ["2", "3"], "answer": "2"} 라면, **q는 question="1+1?", choices=["2", "3"], answer="2"로 변신합니다.
                    # Quiz(**q) (객체 생성)의미: "풀어헤쳐진 데이터를 재료로 삼아 Quiz 클래스의 인스턴스(객체)를 만들어라"는 뜻입니다.

                
                # 2. 데이터가 리스트 형태인 경우 (이전 버전 호환용)
                elif isinstance(data, list):
                    self.high_score = 0
                    self.history = []
                    self.quizzes = [Quiz(**q) for q in data]
                    
        except (FileNotFoundError, json.JSONDecodeError):
            # [요구사항 반영] 파일이 없거나 손상되었을 때의 복구 로직
            print("\n[! 데이터 복구] 파일이 없거나 손상되어 기본 퀴즈 데이터로 복구합니다.")
            self.high_score = 0
            self.history = []
            # 기본 퀴즈 데이터 1개 제공 (사용자가 바로 게임을 테스트해볼 수 있게 함)
            self.quizzes = [
                Quiz("파이썬의 창시자는?", ["귀도 반 로섬", "제임스 고슬링", "데니스 리치", "빌 게이츠"], 1, "네덜란드 출신 프로그래머")
            ]
            # 복구된 데이터를 파일로 즉시 저장하여 다음 실행 시 오류 방지
            self.save_data()

if __name__ == "__main__":  #임포트되지 않은 상황에서
    game = QuizGame() #퀴즈 게임기를 만들어서
    game.run() # 실행한다는 내용