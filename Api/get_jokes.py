import requests


def get_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%252Cid%252Ccontent&page=1"

    response = requests.get(url)
    Data = response.json()
    

    if Data["statusCode"] == 200 and "data" in Data:

        return Data
    else:
        return None


def main():
    jokes = get_jokes()
    jokesarray = jokes["data"]["data"]
    print(jokesarray[2]["content"])
    # for joke in jokesarray:
    #     print("=====================================")
    #     print(joke["content"])
    #     print("\n")
    #     print("=====================================")


if __name__ == "__main__":
    main()