# 파이썬을 활용한 프로그래밍 기초 실습 저장소

동덕여자대학교 2026학년도 2학기 「파이썬을 활용한 프로그래밍 기초」 실습용 저장소입니다.

## 여는 법 (GitHub Codespaces)

1. GitHub에 로그인합니다.
2. 이 페이지 위쪽의 초록색 **Code** 단추 → **Codespaces** 탭 → **Create codespace on main**을 누릅니다.
3. 2~3분 기다리면 브라우저 안에 VS Code가 열립니다. 파이썬 3.13과 pandas · openpyxl · matplotlib이 설치되어 있습니다.
4. 다음 수업부터는 <https://github.com/codespaces> 에서 만들어 둔 codespace를 눌러 엽니다. 새로 만들지 않습니다.

## 폴더

| 경로 | 내용 |
|---|---|
| `week09/` | 9주차 실습 파일 (`매출대장_9월.xlsx`, 예제 코드 `p01`~`p11`, `practice.py`) |
| `내작업/` | 여러분이 만든 파일을 두는 곳 |

## 실행

파일을 열고 오른쪽 위 실행 단추(▷)를 누르거나, 터미널에서 `cd week09` 뒤 `python p01_read.py`를 실행합니다.

## 설치된 도구 (codespace를 만들 때 자동 설치)

| 확장 | 하는 일 |
|---|---|
| Python · Pylance | 실행 단추, 자동 완성, 함수 설명 |
| Python Debugger | 멈출 곳을 찍고 한 줄씩 실행하며 변수 값 확인 |
| Ruff | 정의하지 않은 이름 같은 실수를 실행 전에 표시 |
| Error Lens | 오류 메시지를 줄 옆에 표시 |
| Jupyter · Data Wrangler | 노트북 실행, 데이터프레임 · CSV를 표로 보고 거르기 · 정렬을 pandas 코드로 |
| Spreadsheet Viewer | `.xlsx` 파일을 VS Code 안에서 보기 |
| Rainbow CSV | CSV 열 색 구분 |
| GitHub Copilot Chat · Codex | AI에게 질문, 코드 설명 · 작성 |

이미 만든 codespace에 새 확장이 없으면 `F1` → **Codespaces: Rebuild Container**를 실행합니다(내 파일은 남음).

## AI 도구

- **GitHub Copilot Chat**: GitHub 로그인만으로 바로 쓸 수 있습니다. 학생 인증을 하면 무료입니다.
- **Codex(OpenAI)**: 확장이 미리 설치되어 있습니다. 처음 한 번 **본인의 ChatGPT 계정**으로 로그인합니다(기기 코드 로그인 권장). 로그인 정보는 내 codespace 안에 남으므로 다음 수업에 다시 로그인하지 않아도 됩니다. 로그인 정보는 다른 사람과 공유하지 않습니다.

## 새 주차 파일 받기

터미널에서 `git pull`을 실행합니다. 여러분의 파일은 `내작업/` 폴더에 두면 새 파일을 받을 때 섞이지 않습니다.

## 데이터

`week09/매출대장_9월.xlsx`는 수업용으로 만든 가상 자료입니다.
