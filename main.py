from quiz import Quiz


def get_default_quizzes():
    return [
        Quiz(
            "실행 중인 컨테이너 목록을 확인하는 도커 명령어는?",
            ["docker images", "docker ps", "docker exec", "docker build"],
            2,
        ),
        Quiz(
            "Docker Hub 등 레지스트리에서 이미지를 내려받는 명령어는?",
            ["docker pull", "docker push", "docker run", "docker commit"],
            1,
        ),
        Quiz(
            "Dockerfile을 기반으로 이미지를 빌드하는 명령어는?",
            ["docker create", "docker start", "docker build", "docker load"],
            3,
        ),
        Quiz(
            "이미지를 컨테이너로 실행하는 명령어는?",
            ["docker run", "docker stop", "docker rm", "docker rmi"],
            1,
        ),
        Quiz(
            "실행 중인 컨테이너 내부에 셸로 접속할 때 사용하는 명령어는?",
            ["docker logs", "docker inspect", "docker exec", "docker attach"],
            3,
        ),
        Quiz(
            "컨테이너를 완전히 삭제하는 명령어는?",
            ["docker stop", "docker rm", "docker rmi", "docker kill"],
            2,
        ),
    ]


def show_menu():
    print("=" * 40)
    print("      🎯 나만의 퀴즈 게임 🎯")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)


def read_menu_choice():
    """사용자에게 1~5 사이 숫자를 입력받습니다. 잘못된 입력이면 None을 반환합니다."""
    raw = input("선택 : ")
    # TODO 1: raw.strip()으로 앞뒤 공백 제거
    raw = raw.strip()
    # TODO 2: 빈 문자열이면 안내 메시지 출력하고 None 반환
    if raw == "":
        print("빈 문자열 입니다.")
        return None

    # TODO 3: int(...)로 변환 시도, 실패하면(ValueError) 안내 메시지 출력하고 None 반환
    try:
        choice = int(raw)
    except ValueError:
        print("숫자만 입력해주세요.")
        return None
    # TODO 4: 변환은 됐는데 1~5 범위 밖이면 안내 메시지 출력하고 None 반환
    if not (1 <= choice <= 5):
        print("입력된 숫자가 1이상 5이하의 자연수가 아닙니다.")
        return None
    # TODO 5: 다 통과하면 정수값 반환
    return choice

def read_answer_choice():
    """사용자에게 1~4 사이 숫자를 입력받습니다. 잘못된 입력이면 None을 반환합니다."""
    raw = input("선택 : ")
    raw = raw.strip()
    if raw == "":
        print("빈 문자열입니다.")
        return None
    try:
        choice = int(raw)
    except ValueError:
        print("숫자만 입력해주세요.")
        return None
    if not (1 <= choice <= 4):
        print("입력된 숫자가 1이상 4이하의 자연수가 아닙니다.")
        return None
    return choice



def main():
    quizzes = get_default_quizzes()

    while True:
        try:
            show_menu()
            choice = read_menu_choice()
            if choice is None:
                continue  # 잘못된 입력 -> 메뉴 다시 표시

            if choice == 1:
                play_quiz(quizzes)
            elif choice == 2:
                add_quiz(quizzes)
            elif choice == 3:
                list_quizzes(quizzes)
            elif choice == 4:
                print("[점수 확인] 아직 구현 전입니다.")
            elif choice == 5:
                print("게임을 종료합니다. 안녕하 가세여!")
                break
        except (KeyboardInterrupt, EOFError):
            print("\n프로그램을 종료합니다.")
            break

def play_quiz(quizzes):
    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return

    print(f"퀴즈를 시작합니다! (총 {len(quizzes)}문제)")
    score = 0
    for i, quiz in enumerate(quizzes, start=1):
        quiz.show(i)
        while True:
            answer = read_answer_choice() # 1~4를 검증하는 별도 함수
            if answer is not None:
                break
        if quiz.is_correct(answer):
            print("정답입니다!")
            score += 1
        else:
            print("오답입니다!")

    print(f"결과 : {len(quizzes)} 문제 중 {score}문제 정답!")

def add_quiz(quizzes):
    print("새로운 퀴즈를 추가합니다.")
    question=read_non_empty_text("문제를 입력하세요 : ")
    choices=[]

    for i in range(1, 5):
        choice = read_non_empty_text(f"선택지 {i} : ")
        choices.append(choice)

    while True:
        answer = read_answer_choice() # 이미 만들어둔 함수 재사용
        if answer is not None:
            break

    quizzes.append(Quiz(question, choices, answer))
    print("퀴즈가 추가되었습니다.")

def read_non_empty_text(prompt):
    while True:
        text = input(prompt).strip()
        if text == "":
            print("빈 값을 입력할 수 없습니다. 다시 입력해주세요.")
            continue
        return text

def list_quizzes(quizzes):
    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return
    print(f"등록된 퀴즈 목록 (총 {len(quizzes)}개)")
    print("-" * 40)
    for i, quiz in enumerate(quizzes, start=1):
        print(f"[{i}] {quiz.question}")
    print("-" * 40)


if __name__ == "__main__":
    main()
