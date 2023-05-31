import requests
import json

SKY = 'https://sky.brunt.co:443/'
THING = 'https://thing.brunt.co:8080/'

class Brunt:
    def __init__(self, config):
        self.config = config
        self.sessionId = None

    def set_session_id(self, cookie_str):
        cookies = requests.utils.dict_from_cookiejar(cookie_str)
        self.sessionId = cookies.get('skySSEIONID')

    def login(self, user, password):
        data = {
            "ID": user,
            "PASS": password,
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f'{SKY}/session', headers=headers, data=json.dumps(data))
        self.set_session_id(response.cookies)
        response_data = response.json()
        if response_data.get('status') != 'activate':
            raise Exception('The account not activated.')
        return response_data

    def get_things(self):
        if not self.sessionId:
            user_data = self.login(self.config['user'], self.config['password'])
            print(f"Hello {user_data['nickname']}! {self.config['user']} is logged.")
        headers = {'Cookie': f'skySSEIONID={self.sessionId}'}
        response = requests.get(f'{SKY}/thing', headers=headers)
        return response.json()

    def change_state(self, thingUri, state):
        if not self.sessionId:
            user_data = self.login(self.config['user'], self.config['password'])
            print(f"Hello {user_data['nickname']}! {self.config['user']} is logged.")
        data = {"power": state}
        headers = {'Content-Type': 'application/json', 'Cookie': f'skySSEIONID={self.sessionId}'}
        response = requests.put(f'{THING}/thing{thingUri}', headers=headers, data=json.dumps(data))
        if response.text != 'string':
            raise Exception(response.text)
        return True

config = {
    "user": "아이디",
    "password": "비밀번호",
}

brunt = Brunt(config)
things = brunt.get_things()
print(things)
