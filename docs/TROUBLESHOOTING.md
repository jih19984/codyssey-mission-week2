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
