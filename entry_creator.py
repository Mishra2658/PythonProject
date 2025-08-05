import pyttsx3

# Store candidate entries
candidates = []

# Initialize text-to-speech engine
engine = pyttsx3.init()

def get_user_input():
    print("\n--- Enter Candidate Details ---")
    name = input("Name: ")
    age = input("Age: ")
    profession = input("Profession: ")
    city = input("City: ")
    hobby = input("Hobby: ")
    
    candidate = {
        "name": name,
        "age": age,
        "profession": profession,
        "city": city,
        "hobby": hobby
    }

    candidates.append(candidate)
    print("✅ Candidate added successfully!\n")

def list_candidates():
    print("\n--- List of Candidates ---")
    for index, candidate in enumerate(candidates):
        print(f"{index + 1}. {candidate['name']}")

def speak_intro(index):
    try:
        candidate = candidates[index]
        intro = (
            f"Meet {candidate['name']}, who is {candidate['age']} years old. "
            f"They work as a {candidate['profession']} in {candidate['city']}. "
            f"In their free time, they enjoy {candidate['hobby']}."
        )
        print("\n🗣 Speaking Introduction...")
        print(intro)
        engine.say(intro)
        engine.runAndWait()
    except IndexError:
        print("❌ Invalid candidate selection.")

def main():
    while True:
        print("\n--- Candidate Entry System ---")
        print("1. Add new candidate")
        print("2. List candidates")
        print("3. Introduce a candidate")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            get_user_input()
        elif choice == '2':
            list_candidates()
        elif choice == '3':
            list_candidates()
            try:
                idx = int(input("Enter candidate number to introduce: ")) - 1
                speak_intro(idx)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == '4':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
