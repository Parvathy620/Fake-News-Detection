headline = input("Enter the headline: ")
confidence = int(input("Enter the confidence: "))

print(f"Headline : {headline}")
print(f"Confidence level :{confidence}%")

if confidence > 90:
    print("High Confidence")
elif confidence > 70:
    print("Moderate confidence")
elif confidence > 50:
    print("Low confidence")
elif confidence>0:
    print("Very low confidence")
else:
    print("Invalid confidence level")
