# Phishing URL Detector - With Repeat Loop

print("===== PHISHING URL DETECTOR =====")

# While loop - Program repeat hoga
while True:
    # 1. URL input
    url = input("\nEnter URL to check: ")
    url = url.lower()

    suspicious_words = ["login", "verify", "free", "prize", "urgent", "account", "suspended", "update", "secure", "bank"]
    score = 0

    # Condition 1 - https check
    if url.startswith("https"):
        print("[SAFE] It has https")
    else:
        print("[DANGER] No https, only http")
        score = score + 1

    # Condition 2 - Length check
    if len(url) > 75:
        print("[DANGER] URL is too long")
        score = score + 1
    else:
        print("[SAFE] URL length is normal")

    # Condition 3 - @ check
    if "@" in url:
        print("[DANGER] @ found in URL")
        score = score + 1
    else:
        print("[SAFE] No @ found")

    # Condition 4 - Dash check
    if url.count("-") > 3:
        print("[DANGER] Too many - in URL")
        score = score + 1
    else:
        print("[SAFE] Dashes are normal")

    # Loop - Suspicious words check
    for word in suspicious_words:
        if word in url:
            print(f"[DANGER] Suspicious word found: {word}")
            score = score + 1

    # Final Result
    print("\n===== RESULT =====")
    print(f"Total Danger Score: {score}")

    if score >= 3:
        print("⚠️ THIS IS PHISHING! Do not open it!")
    elif score >= 1:
        print("⚠️ SLIGHTLY SUSPICIOUS! Open carefully!")
    else:
        print("✅ THIS IS SAFE!")

    # Repeat karna hai ya nahi? - Yehi asal loop hai
    choice = input("\nDo you want to check another URL? (y/n): ")
    if choice.lower() == "n":
        print("Thank you! Program Closed.")
        break