from pymongo import MongoClient
from bson.objectid import ObjectId

pymongo_client = MongoClient("mongodb://localhost:27017/")
db = pymongo_client["youtubeManager"]
videos_collection = db["videos"]

# print(videos_collection)

def list_of_videos():
    for video in videos_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video(name, time):
    videos_collection.insert_one({"name": name, "time": time})
    print(f"Video '{name}' added successfully.")

def update_video(video_id, name, time):
    videos_collection.update_one({"_id": ObjectId(video_id)}, {"$set": {"name": name, "time": time}})
    print(f"Video with ID '{video_id}' updated successfully.")

def delete_video(video_id):
    videos_collection.delete_one({"_id": ObjectId(video_id)})
    print(f"Video with ID '{video_id}' deleted successfully.")


def main():
    while True:
        print("\n YOUTUBE MANAGER || Choose an option:")
        print("1. See all Videos ")
        print("2. Add a Video")
        print("3. Update a Video")
        print("4. Delete a Video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_of_videos()
            case "2":
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name, time)
            case "3":
                list_of_videos()
                video_id = input("Enter the video ID to update: ")
                name = input("Enter the new video name: ")
                time = input("Enter the new video time: ")
                update_video(video_id, name, time)
            case "4":
                list_of_videos()
                video_id = input("Enter the video ID to delete: ")
                delete_video(video_id)
            case "5":
                print("Exiting the app.")
                break
            case _:
                print("Invalid choice. Please try again.")




if __name__ == "__main__":
    main()

