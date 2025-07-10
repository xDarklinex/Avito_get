import requests

CLIENT_ID = 'cVHYJOAvVXfVQqzwZ-TA'
CLIENT_SECRET = 'GQkhUeWk6d81hE8h0P4NTpcMU52YMHwAhw--h6_J'

def get_access_token():
    url = "https://api.avito.ru/token/"
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    resp = requests.post(url, data=data, headers=headers)
    resp.raise_for_status()
    return resp.json()["access_token"]

def get_accounts(access_token):
    url = "https://api.avito.ru/messenger/v1/accounts"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()

def main():
    token = get_access_token()
    accounts = get_accounts(token)
    print("Список аккаунтов и их ID:")
    for acc in accounts.get("accounts", []):
        print(f"ID: {acc['id']}, Name: {acc.get('name', 'No name')}")

if __name__ == "__main__":
    main()
