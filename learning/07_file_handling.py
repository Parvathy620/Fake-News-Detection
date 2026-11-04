file = open("news.txt", "w")
file.write("Government announces new policy\n")
file.write("Scientists discover new planet\n")
file.write("New technology launched")
file.close()


file = open("news.txt", "r")
content = file.read()
print(content)
file.close()


file = open("news.txt", "r")
lines = file.readlines()
print(lines)
file.close()

file = open("news.txt", "a")
file.write("\nNew AI technology arrived")
file.close()

file = open("news.txt", "r")
news_lines = file.readlines()
count = len(news_lines)
print(f"Total news articles: {count}")
file.close()

keyword = input("Enter the keyword: ")
print("Matching headlines:\n")

with open("news.txt", "r") as file:
    for line in file:
        if keyword.lower() in line.lower():
            print(line.strip())
