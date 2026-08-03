# 퀴즈 게임 프로젝트

## 1. 프로젝트 개요
- 파이썬 OOP를 활용한 콘솔 기반 퀴즈 프로그램입니다.

## 2. 퀴즈 주제 선정 이유
- 아무 생각 없어서 고양고양하고 적어봄

## 3. 실행 방법
- python main.py

## 4. 기능 목록
- 퀴즈 풀기 / 추가 / 목록 보기 / 점수 확인

## 5. 파일 구조
- main.py: 메인 실행 파일
- state.json: 데이터 저장 파일
- quizzes.json (퀴즈 데이터 저장), scores.json (점수 기록 저장)


## 6. .gitignore 입력사항
``` bash
#Git이 추적하지 말아야 할 파일들을 적어주는 곳
__pycache__/
*.pyc
state.json
```

## 7. 커밋과 푸시 기본
``` bash
# 1. 현재 폴더의 모든 변경 사항을 스테이징(준비) 영역에 올립니다.
git add .
# 2. 첫 번째 기록을 남깁니다. (메시지는 요구사항 권장 형식을 따랐어요)
git commit -m "init: 프로젝트 초기 구조 설정 (.gitignore, README, main.py)"
# 3. 내 컴퓨터의 기록을 GitHub(원격 저장소)로 보냅니다.
git push origin main
```

2. GitHub 미션 해결하기 (이미지 3번 내용)
이미지에 있는 **"최소 1회 이상의 브랜치 생성 및 병합"**과 "10개 이상의 커밋" 조건을 충족해야 합니다. 지금이 딱 브랜치를 연습해볼 타이밍이에요!

[미션: 브랜치 만들고 '퀴즈 풀기' 기능 구현하기]

새 브랜치 만들기: 터미널에 입력하세요.

bash
📋 복사
git checkout -b feature/play-quiz
일단 main에서 나가는코드 -b 새로운 ㅡ랜치(포스트잇만듬)

기능 구현 후 커밋: 퀴즈 풀기 기능을 만들면서 커밋을 쪼개서 해보세요. (예: "문제 출력 기능 구현", "정답 체크 로직 구현" 등) 이렇게 하면 10개 커밋 채우기가 쉽습니다.

병합(Merge)하기: 기능이 완성되면 다시 main으로 돌아가서 합칩니다.

bash
📋 복사
git checkout main
메인으로 브랜치이동
git merge feature/play-quiz
메인에 포스트잇()에 붙은 내용 옮겨 적음

### 기존에 메인에서 나와서 새로운 브랜치 만듬
jha21vvv5332@c6r6s2 jha21vvv-codyssey-02 % git checkout -b feature/play-quiz
Switched to a new branch 'feature/play-quiz'
### 브랜치 상황확인
jha21vvv5332@c6r6s2 jha21vvv-codyssey-02 % git branch
* feature/play-quiz
  main
### 메인으로 이동
jha21vvv5332@c6r6s2 jha21vvv-codyssey-02 % git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
### 브랜치이동 확인
jha21vvv5332@c6r6s2 jha21vvv-codyssey-02 % git branch       
  feature/play-quiz
* main
### 메인에 feature/play-quiz의 내용 옮겨 적기
jha21vvv5332@c6r6s2 jha21vvv-codyssey-02 % git merge feature/play-quiz
Already up to date.
jha21vvv5332@c6r6s2 jha21vvv-codyssey-02 % git branch                 
  feature/play-quiz
* main
jha21vvv5332@c6r6s2 jha21vvv-codyssey-02 % 


