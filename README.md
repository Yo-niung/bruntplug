# bruntplug
Remote and refresh status from BRUNT plug
BruntOn.py
BruntOn은 Brunt 서비스로부터 정보를 받아오는 파이썬 코드입니다. 이 코드를 사용하여 Brunt 장치의 상태를 확인하고 제어할 수 있습니다.

실행 환경
Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug 1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
필요한 라이브러리
requests
json
사용 방법
config 딕셔너리를 설정합니다. 아이디와 비밀번호를 입력해야 합니다.
python
Copy code
config = {
    "user": "아이디",
    "password": "비밀번호",
}
Brunt 클래스를 인스턴스화합니다.
python
Copy code
brunt = Brunt(config)
get_things() 메서드를 사용하여 Brunt 장치 목록을 가져옵니다.
python
Copy code
things = brunt.get_things()
print(things)
필요에 따라 change_state() 메서드를 사용하여 Brunt 장치의 상태를 변경할 수 있습니다.
python
Copy code
# 예시: 서버 장치의 전원을 끄는 경우
brunt.change_state("/hub/b3920d68a6374fb2", 0)
참고 사항
코드 실행 전에 Python 3.10.6 버전을 설치해야 합니다.
필요한 라이브러리를 설치해야 합니다. 아래 명령을 사용하세요.
Copy code
pip install requests
