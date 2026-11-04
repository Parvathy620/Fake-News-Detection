def calculate_word_count(news):
    return len(news.split())

headline="Government announce new policy"
print(calculate_word_count(headline))


def classify_news(news):
    if news==1:
        return("Fake news")
    elif news==0:
        return("Real news")
    else:
        return("Invalid label")

print(classify_news(5))

news_labels = ["Real", "Fake", "Real", "Fake", "Real", "Real"]

def count_news(labels):
    real=0
    fake=1
    print(f"Total news article: {len(labels)}")
    for label in labels:
        if label=="Real":
            real=real+1
        else:
            fake=fake+1
    print(f"Number of real news: {real}")
    print(f"Number of fake new: {fake}")    

count_news(news_labels)

def clear_news(news):
    lower_case=news.lower()
    clean=lower_case.strip()
    return clean

print(clear_news("Government announce new policy  "))