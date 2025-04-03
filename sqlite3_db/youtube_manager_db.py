import sqlite3

# Connect to the database
con = sqlite3.connect("youtube_manager.db")
cursor = con.cursor()

# Create a table to store video information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

def list_of_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()  # Store result before iterating
    print("\n" + "*" * 50)
    if not rows:
        print("No videos found.")
    else:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Time: {row[2]}")
    print("*" * 50 + "\n")

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()
    print(f"Video '{name}' added successfully.")

def update_video(video_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, int(video_id)))
    con.commit()
    print(f"Video with ID '{video_id}' updated successfully.")

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (int(video_id),))
    con.commit()
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
    con.commit()
    con.close()  # Close database connection properly
