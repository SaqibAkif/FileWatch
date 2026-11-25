import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful and easy to learn programming language.",
    "Practice makes a man perfect and consistency is the key.",
    "Typing fast is a useful skill for programmers and writers.",
    "Stay focused and keep improving your speed every day."
]

def typing_test():
    print("=" * 50)
    print(" WELCOME TO TYPING SPEED TEST")
    print("=" * 50)
    input("Press ENTER to start...")

    sentence = random.choice(sentences)
    print("\nType this sentence:")
    print(f"\n>>> {sentence}\n")

    start_time = time.time()
    user_input = input("Your typing:")
    end_time = time.time()

    time_taken = round(end_time - start_time, 2)

    correct_chars = 0
    for i in range(min(len(sentence), len(user_input))):
        if sentence[i] == user_input[i]:
            correct_chars += 1

    accuracy = round((correct_chars / len(sentence)) * 100, 2)
    words = len(sentence.split())
    wpm = round((words / time_taken) * 60, 2)

    print("\n" + "=" * 50)
    print(" RESULTS")
    print("=" * 50)
    print(f"Time Taken : {time_taken} seconds")
    print(f"Speed : {wpm} WPM")
    print(f"Accuracy : {accuracy}%")
    print("=" * 50)

    if accuracy == 100 and wpm > 40:
        print("Amazing! You are a typing master!")
    elif accuracy > 80 and wpm > 25:
        print("Good job! Keep practice carry on!")
    else:
        print("Practice more to improve your speed and accuracy!")

if __name__ == "__main__":
    while True:
        typing_test()
        again = input("\n Do you want to try again? (y/n):").lower()
        if again!= 'y':
            print("Thanks for playing! Bye")
            break
































