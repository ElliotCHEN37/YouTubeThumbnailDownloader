import webbrowser
import requests

print("Welcome")
while True:
    Cho = input("Please choose (1)Enter Video ID (2)Exit: ")
    if Cho in ("1", "2"):
        if Cho == "1":
            q = input("Enter Video ID: ")
            url = f'https://img.youtube.com/vi/{q}/maxresdefault.jpg'
            file_name = 'maxresdefault.jpg'
            res = requests.get(url)
            with open(file_name, 'wb') as f:
                f.write(res.content)
            print("Image downloaded successfully!")
        elif Cho == "2":
            print("Goodbye~")
            break
    else:
        print("Invalid choice. Please choose (1)Enter Video ID (2)Exit.")
