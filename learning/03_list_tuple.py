headline=["Government announce new policy","Celebrity discoverse magical medicine","Scientists discover new planet","Secret government announcement shocks world","New technology launched"]
label=["Real","Fake","Real","Fake","Real"]


print(f"Total News Article :{len(headline)}")

print(f"News 1: {headline[0]}")
print(f"News Label: {label[0]}")


news_tuple=("Politics","Technology","sports","Education")
print(news_tuple)
print(news_tuple[0])
print(len(news_tuple))

headline.append("new policy is fake")
print(headline)

headline.remove("new policy is fake")
print(headline)