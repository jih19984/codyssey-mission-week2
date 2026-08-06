# Troubleshooting

미션 진행 중 겪은 개발 환경 이슈와 해결 방법을 기록합니다.

## 1. zsh에서 git 브랜치명 Tab 자동완성이 안 됨

**증상**

`git switch <브랜치명>` 등을 입력할 때 `Tab` 키를 눌러도 브랜치명이 자동완성되지 않음.

**원인**

- 기본 셸이 `zsh`인데 `oh-my-zsh` 등 프레임워크가 설치되어 있지 않았고, `~/.zshrc`에 zsh의 자동완성 시스템을 초기화하는 `compinit` 호출이 없었음.
- git 자체의 자동완성 스크립트(`_git`)는 시스템에 이미 존재했지만, `compinit`이 호출되지 않아 로드되지 않는 상태였음.

**해결**

`~/.zshrc` 파일 맨 아래에 아래 두 줄을 추가한다.

```zsh
autoload -Uz compinit
compinit
```

추가 후 아래 명령으로 설정을 적용한다.

```bash
source ~/.zshrc
```

적용 후 `git switch fea` + `Tab` 입력 시 브랜치명이 정상적으로 자동완성되는 것을 확인함.

## 2. 이미 push한 커밋 메시지에 컨벤션(`Docs:` 등) 접두사를 빠뜨림

**증상**

- README 작성 커밋을 `Docs:` 접두사 없이 `README 프로젝트 개요 및 사용 가이드 작성`으로 커밋하고 그대로 push함.
- 이후 커밋까지 쌓인 뒤에야 컨벤션이 빠진 걸 발견했고, 이미 origin에 올라간 과거 커밋이라 단순히 다시 커밋할 수 없는 상황이었음.

**원인**

- 커밋 전에 프로젝트 컨벤션(`Feat:`/`Fix:`/`Docs:`/`Refactor:`)을 확인하지 않고 커밋함.
- 가장 최근 커밋이 아니라 그 이전 커밋이었기 때문에 `git commit --amend`로는 고칠 수 없었음 (amend는 가장 최근 커밋에만 적용됨).

**해결**

- 고치려는 커밋의 부모 해시를 기준으로 interactive rebase 실행.

  ```bash
  git rebase -i <고칠 커밋의 부모 해시>
  ```

- todo list 편집기에서 해당 커밋 줄의 `pick`을 `reword`로 변경 후 저장/종료 (`Esc` → `:wq` → `Enter`).
- 이어서 열리는 커밋 메시지 편집기에서 메시지를 `Docs: README 프로젝트 개요 및 사용 가이드 작성`으로 수정 후 다시 저장/종료.
- 이미 origin에 push된 커밋이라 히스토리가 갈라지므로, 일반 `push` 대신 아래 명령으로 반영.

  ```bash
  git push --force-with-lease origin main
  ```

- `--force` 대신 `--force-with-lease`를 사용해, 그 사이 원격에 다른 변경이 생겼다면 강제 push가 막히도록 안전장치를 둠.
- 커밋 메시지 컨벤션은 이후부터 커밋 직전에 한 번 더 확인하는 습관으로 재발을 방지.

