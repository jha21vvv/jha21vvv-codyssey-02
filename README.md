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