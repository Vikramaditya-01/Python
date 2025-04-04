import requests

def ramdom_user_data():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    Data = response.json()


    if Data["statusCode"] == 200 and "data" in Data:
        user_data = Data["data"]
        username = user_data["login"]["username"]
        location = user_data["location"]["country"]
        return username, location
    else:
        raise ValueError("Invalid response from API")
    

def main():
    try:
        username, location = ramdom_user_data()
        print(f"Username: {username}")
        print(f"Location: {location}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
