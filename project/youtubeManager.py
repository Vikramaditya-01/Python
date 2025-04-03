import json


def load_data():
    try:
        with open("youtube.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)


def list_of_videos(videos):
    print("\n")
    print("*" * 100)
    for index ,video in enumerate(videos , start=1):
        print(f"{index} . {video['name']} , {video['time']}")
    print("*" * 100)
    print("\n")

def add_video(videos):
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    videos.append({"name": name, "time": time})
    save_data(videos)

def update_video(videos):
    list_of_videos(videos)
    index = int(input("Enter the index of the video to update: ")) - 1
    if 0 <= index < len(videos):
        name = input("Enter the new name of the video: ")
        time = input("Enter the new time of the video: ")
        videos[index] = {"name": name, "time": time}
        save_data(videos)
    else:
        print("Invalid index. Please try again.")


def delete_video(videos):
    list_of_videos(videos)
    index = int(input("Enter the index of the video to delete: ")) - 1
    if 0 <= index < len(videos):
        videos.pop(index)
        save_data(videos)
    else:
        print("Invalid index. Please try again.")


def main():
    videos = load_data()

    while True:
        print(" YOUTUBE MANAGER || Choose an option:")
        print("1. See all Videos ")
        print("2. Add a Video")
        print("3. Update a Video")
        print("4. Delete a Video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_of_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Exiting the app.")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
