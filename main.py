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


def main():
    while True:
        try:
            show_menu()
            choice = read_menu_choice()
            if choice is None:
                continue  # 잘못된 입력 -> 메뉴 다시 표시

            if choice == 1:
                print("[퀴즈 풀기] 아직 구현 전입니다.")
            elif choice == 2:
                print("[퀴즈 추가] 아직 구현 전입니다.")
            elif choice == 3:
                print("[퀴즈 목록] 아직 구현 전입니다.")
            elif choice == 4:
                print("[점수 확인] 아직 구현 전입니다.")
            elif choice == 5:
                print("게임을 종료합니다. 안녕하 가세여!")
                break
        except (KeyboardInterrupt, EOFError):
            print("\n프로그램을 종료합니다.")
            break


if __name__ == "__main__":
    main()
