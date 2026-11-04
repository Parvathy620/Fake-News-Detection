try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Enter valid input")


def file_content(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found!")

file_content("news.txt")


def validate_confidence(num):
    if num < 0 or num > 100:
        raise ValueError("Confidence must be within 0 to 100")
    else:
        print("High confidence")

try:
    validate_confidence(110)
except ValueError as e:
    print(f"Caught expected error: {e}")


# ==========================================
# News Statistics Program
# ==========================================

def calculate_news_stats(labels):
    try:
        if not isinstance(labels, list):
            raise TypeError("Labels must be provided as a list.")

        real_count = 0
        fake_count = 0

        for item in labels:
            if not isinstance(item, str):
                raise ValueError(f"Invalid label type found: {item}")

            label = item.strip().capitalize()
            if label == "Real":
                real_count += 1
            elif label == "Fake":
                fake_count += 1
            else:
                raise ValueError(f"Unexpected label found: '{item}'")

        total_articles = len(labels)
        fake_percentage = (fake_count / total_articles) * 100

        print(f"Total Articles: {total_articles}")
        print(f"Real News: {real_count}")
        print(f"Fake News: {fake_count}")
        print(f"Fake News Percentage: {fake_percentage:.0f}%")

    except ZeroDivisionError:
        print("Error: List is empty, cannot calculate percentage.")
    except (ValueError, TypeError) as e:
        print(f"Error handling data: {e}")


news_labels = ["Real", "Fake", "Real", "Fake", "Real"]
calculate_news_stats(news_labels)
