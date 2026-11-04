news_article = [
    "Govvernment announce new policy",
    "Scientists discover new planet",
    "New technology launched",
    "New education scheme introduced",
    "Space research advances",
]

for index, news in enumerate(news_article, start=1):
    print(f"{index}. {news}")

news_label = ["Real", "Fake", "Real", "Fake", "Real", "Fake"]

print(f"Total number of news article: {len(news_label)}")
real = 0
fake = 0

for label in news_label:
    if label == "Real":
        real = real + 1
    else:
        fake = fake + 1

print(f"Number of real news : {real}")
print(f"Number of fake news : {fake}")


news_article = [
    "Govvernment announce new policy",
    "Scientists discover new planet",
    "New technology launched",
]

for news in news_article:
    print(f"News :{news}")
    print(f"Word count : {len(news.split())}")
    print("*******************************")


news_label = ["Real", "Real", "Real", "Fake", "Real", "Fake"]

# Find the first occurrence of "Fake" and break
for index, label in enumerate(news_label):
    if label == "Fake":
        print(f"First fake news detected at index {index}.")
        break
