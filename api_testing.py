import requests

APIKEY = "70c384bccb5dbf5eb51c6ac202b70c2c"
TOKEN = "ATTAb494b3bddfadd8aea4c289badb8743298913e7605db1f3a171212d57f51975a4F7DB3109"

URL = "https://api.trello.com/"

def get_user_boards():
    endpoint = "1/members/me/boards"
    params = {
        'key': APIKEY,
        'token': TOKEN
    }

    response = requests.get(url=URL+endpoint, params=params)

    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    return(response_json)

def get_board_id(name):
    id = None
    response = get_user_boards()
    for board in response:
        if board['name'] == name:
            id = board['id']
            break

    if  id is None:
        print("No board found with the name: {}".format(name))
    return id

def update_board(name, **kwargs):
    board_id = get_board_id(name)

    endpoint = "{}1/boards/{}".format(URL, board_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }
    for key, value in kwargs.items():
        params[key] = value

    response = requests.request(
        "PUT",
        endpoint,
        params=params
        )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)

def delete_board(name):
    board_id = get_board_id(name)
    endpoint = "{}1/boards/{}".format(URL, board_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }

    response = requests.request(
        "DELETE",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)

def create_new_board(name):
    endpoint =  "/1/boards/"
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }
    response = requests.post(url=URL+endpoint, json=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)

if __name__ == "__main__":
    #get_user_boards()
    #create_new_board("Test Automation")
    #update_board("Test Automation", desc="Add items to finish Automation")
    delete_board("Test Automation")
