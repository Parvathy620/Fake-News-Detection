headline=input("Enter the headline: ")
category="Education"
word_count=len(headline.split())
is_fake_news=False

print("=====NEWS INFORMATION=====")
print("Headline :",headline.upper())
print("Category :",category)
print("Word Count :",word_count)
print("Is Fake News : ",is_fake_news)

print(type(headline))
print(type(category))
print(type(word_count))
print(type(is_fake_news))