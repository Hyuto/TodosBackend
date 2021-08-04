import os, json, jwt, logging
import requests, argparse, pathlib
from urllib.parse import urlparse

URLS = {
    "dev": "http://127.0.0.1:8000/api/",
    "web": "https://django-todos-application.herokuapp.com/api/",
}

SECRET_KEY = 'SECRET-KEY'


class AUTH(object):
    auth_file_path = os.path.join(
        pathlib.Path(__file__).parent.resolve(), 'auth.auth')

    def __init__(self, url, status):
        parsing = urlparse(url)
        self.url = url
        self.regis_url = f'{parsing.scheme}://' + parsing.netloc + '/auth/register/'
        self.logout_url = f'{parsing.scheme}://' + parsing.netloc + '/auth/logout/'
        self.token_url = f'{parsing.scheme}://' + parsing.netloc + '/auth/login/'
        self.refresh_url = f'{parsing.scheme}://' + parsing.netloc + '/auth/login/refresh/'

        if status == 'register':
            self.register()
        elif status == 'logout':
            self.logout()
        elif os.path.isfile(self.auth_file_path) and status != 'login':
            logging.info('Using past auth config')
            with open(self.auth_file_path) as f:
                self.auth = json.load(f)

            try:
                jwt.decode(self.auth['access'],
                           SECRET_KEY,
                           algorithms=["HS256"])
            except jwt.ExpiredSignatureError:
                try:
                    jwt.decode(self.auth['refresh'],
                               SECRET_KEY,
                               algorithms=["HS256"])
                    self.refresh()
                except jwt.ExpiredSignatureError:
                    logging.warning('Token expired')
                    self.login()
        else:
            self.login()

    def _write_auth(self):
        with open(self.auth_file_path, "w") as outfile:
            json.dump(self.auth, outfile)

    def logout(self):
        logging.info('Logging out')
        if os.path.isfile(self.auth_file_path):
            with open(self.auth_file_path) as f:
                self.auth = json.load(f)

            post = requests.post(
                self.logout_url,
                data={'refresh': self.auth['refresh']},
                headers={'Authorization': f'Bearer {self.auth["access"]}'})
            print(f"STATUS     : {post.status_code}")
            print(f"RESPONSE   : {json.dumps(post.json(), indent=3)}")

            os.remove(self.auth_file_path)
        else:
            raise OSError('No auth file detected!')

    def register(self):
        data = {
            "username": None,
            "email": None,
            "password": None,
        }

        logging.info('REGISTER')
        for item in data:
            input_ = input(f'*  {item} : ')
            data[item] = input_

        post = requests.post(self.regis_url, data=data)

        print(f"STATUS     : {post.status_code}")
        print(f"RESPONSE   : {json.dumps(post.json(), indent=3)}")

    def login(self):
        data = {"username": None, "password": None}

        logging.info('LOGIN')
        for item in data:
            input_ = input(f'*  {item} : ')
            data[item] = input_

        post = requests.post(self.token_url, data=data)

        no_account_exception = "No active account found with the given credentials"
        if no_account_exception in post.json().values():
            logging.error(no_account_exception)
            raise requests.ConnectionError(no_account_exception)

        self.auth = post.json()
        self._write_auth()

    def refresh(self):
        logging.warning('Trying to refresh the token')
        post = requests.post(self.refresh_url,
                             data={'refresh': self.auth['refresh']})

        self.auth = post.json()
        self._write_auth()


def GET(url, token):
    logging.info(f'GET {url}')

    get = requests.get(url, headers={'Authorization': f'Bearer {token}'})

    print(f"STATUS     : {get.status_code}")
    print(f"TIME TAKEN : {get.elapsed.total_seconds()}s")
    print(f"RESPONSE   : {json.dumps(get.json(), indent=3)}")


def POST(url, token):
    logging.info(f'POST {url}')

    data = {
        "title": None,
        "description": None,
        "complete": None,
        "deadline": None,
    }

    print("Please enter following field :")
    required = ["title", "description"]
    for item in data:
        input_ = input(
            f'*  {item} [{"REQUIRED" if item in required else "OPTIONAL"}] : ')

        if input_ == "":
            input_ == None

        data[item] = input_

    data['user'] = jwt.decode(token,
                              options={"verify_signature": False},
                              algorithms=["HS256"])['user_id']

    post = requests.post(url,
                         data=data,
                         headers={'Authorization': f'Bearer {token}'})

    print(f"STATUS     : {post.status_code}")
    print(f"TIME TAKEN : {post.elapsed.total_seconds()}s")
    print(f"RESPONSE   : {json.dumps(post.json(), indent=3)}")


def PUT(url, id_, token):
    logging.info(f'PUT {url}')

    endpoint = f'{url}{id_}/'
    data = requests.get(endpoint, headers={
        'Authorization': f'Bearer {token}'
    }).json()

    if data == {"detail": 'Not found.'}:
        logging.error('Not found!')
        raise requests.ConnectionError('Not found!')

    print("Please enter following field :")
    required = ["title", "description"]
    for item in data:
        if item not in ['id', 'user']:
            input_ = input(
                f'*  {item} [{"REQUIRED" if item in required else "OPTIONAL"}] '
                + f'[BEFORE : {data[item]}] : ')

            if input_ == "":
                input_ = data[item]

            data[item] = input_

    put = requests.put(endpoint,
                       data=data,
                       headers={'Authorization': f'Bearer {token}'})
    print(f"STATUS     : {put.status_code}")
    print(f"TIME TAKEN : {put.elapsed.total_seconds()}s")
    print(f"RESPONSE   : {json.dumps(put.json(), indent=3)}")


def DELETE(url, id, token):
    logging.info(f'DELETE {url+ f"{id}/"}')

    delete = requests.delete(url + f"{id}/",
                             headers={'Authorization': f'Bearer {token}'})

    print(f"STATUS     : {delete.status_code}")
    print(f"TIME TAKEN : {delete.elapsed.total_seconds()}s")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Testing script for the backend")
    parser.add_argument("-u",
                        "--url",
                        help="Url / endpoint",
                        type=str,
                        required=True)
    parser.add_argument("-l", "--login", help="Login", action="store_true")
    parser.add_argument("-r",
                        "--register",
                        help="Register",
                        action="store_true")
    parser.add_argument("-q", "--logout", help="Logout", action="store_true")
    parser.add_argument("-g", "--get", help="GET", action="store_true")
    parser.add_argument("-p",
                        "--post",
                        help="Post to Endpoint",
                        action="store_true")
    parser.add_argument("-t", "--put", help="Put to Endpoint", type=str)
    parser.add_argument("-d", "--delete", help="Post to Endpoint", type=str)
    args = parser.parse_args()

    logging.basicConfig(format='[ %(levelname)s ] %(message)s',
                        level=logging.INFO)

    if args.url in URLS:
        args.url = URLS[args.url]

    if args.login:
        auth_type = 'login'
    elif args.register:
        auth_type = 'register'
    elif args.logout:
        auth_type = 'logout'
    else:
        auth_type = 'from file'

    auth = AUTH(args.url, auth_type)

    if args.get:
        GET(args.url, auth.auth['access'])

    if args.post:
        POST(args.url, auth.auth['access'])

    if args.put:
        PUT(args.url, args.put, auth.auth['access'])

    if args.delete:
        DELETE(args.url, args.delete, auth.auth['access'])

    logging.info('Done !')