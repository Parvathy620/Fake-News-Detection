news={"news_id":"101","headline":"Government announce new education policy",
"category":"Education","lebel":"Real","source":"News Website"}

print(news["headline"])
print(news["lebel"])

news["category"]="Politics"
print(news["category"])

print(news.keys())


news_article={
    1: {
        "headline":"Government announce new education policy",
        "cetegory":"Education",
        "label":"Real"
    },
    2: {
        "headline":"Celebrity discoverse magical medicine",
        "cetegory":"Medical",
        "label":"Fake"
    },
    3: {
        "headline":"Scientists discover new planet",
        "category":"Science",
        "label":"Real"    
        }
}

print(news_article[2]["headline"])

set1={"Politics","Sports","Technology"}
set2={"Politics","Education","Entertainment"}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

unique_category=set1.union(set2)

print(len(unique_category))