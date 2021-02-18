title = input("Enter a title of your favorite Book :  ")

def favorite_book(title="Alice in Wonderland"):
    print(f"One of my favorite books is {title}")

while title == "" or title ==" ":
    print("You didnt type any title we will put our default")
    title = "Alice in Wonderland"

favorite_book(title)

