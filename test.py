import requests, argparse

URLS = {
    "dev": "http://127.0.0.1:8000/api/",
    "web": "https://django-todos-application.herokuapp.com/api/",
}


def POST(url):
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
            f'*  {item} [{"REQUIRED" if item in required else "OPTIONAL"}] : '
        )

        if input_ == "":
            input_ == None

        data[item] = input_
    post = requests.post(url, data=data)

    print(f"STATUS     : {post.status_code}")
    print(f"TIME TAKEN : {post.elapsed.total_seconds()}s")
    print(f"RESPONSE   : {post.json()}")


def PUT(url, id_):
    endpoint = f'{url}{id_}/'
    data = requests.get(endpoint).json()

    print("Please enter following field :")
    required = ["title", "description"]
    for item in data:
        if item != 'id':
            input_ = input(
                f'*  {item} [{"REQUIRED" if item in required else "OPTIONAL"}] '
                + f'[BEFORE : {data[item]}] : '
            )

            if input_ == "":
                input_ == None

            data[item] = input_

    put = requests.put(endpoint, data=data)
    print(f"STATUS     : {put.status_code}")
    print(f"TIME TAKEN : {put.elapsed.total_seconds()}s")
    print(f"RESPONSE   : {put.json()}")


def DELETE(url, id):
    delete = requests.delete(url + f"{id}/")

    print(f"STATUS     : {delete.status_code}")
    print(f"TIME TAKEN : {delete.elapsed.total_seconds()}s")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Testing script for the backend"
    )
    parser.add_argument(
        "-u", "--url", help="Url / endpoint", type=str, required=True
    )
    parser.add_argument(
        "-p", "--post", help="Post to Endpoint", action="store_true"
    )
    parser.add_argument("-t", "--put", help="Put to Endpoint", type=str)
    parser.add_argument("-d", "--delete", help="Post to Endpoint", type=str)
    args = parser.parse_args()

    if args.url in URLS:
        args.url = URLS[args.url]

    if args.post:
        POST(args.url)

    if args.put:
        PUT(args.url, args.put)

    if args.delete:
        DELETE(args.url, args.delete)
