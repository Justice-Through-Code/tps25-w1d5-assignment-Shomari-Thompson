import requests

def get_all_breeds():
    """GET request to fetch all dog breeds."""
    try:
        response = requests.get("https://dog.ceo/api/breeds/list/all")
        response.raise_for_status()
        data = response.json()
        return data["message"]
    except requests.exceptions.RequestException:
        print("Error: Could not fetch breed list from API.")
        return {}

def get_random_image(breed):
    """GET request to fetch a random image from a breed."""
    try:
        response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
        response.raise_for_status()
        data = response.json()
        return data["message"]
    except requests.exceptions.RequestException:
        print(f"Error: Could not fetch image for breed '{breed}'.")
        return None

def get_random_sub_breed_image(breed, sub_breed):
    """GET request to fetch a random image from a sub-breed."""
    try:
        response = requests.get(f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random")
        response.raise_for_status()
        data = response.json()
        return data["message"]
    except requests.exceptions.RequestException:
        print(f"Error: Could not fetch image for sub-breed '{sub_breed}' of breed '{breed}'.")
        return None

def show_breeds(breeds_dict):
    """Prints all available breeds 5 per line."""
    breed_names = sorted(breeds_dict.keys())
    for i in range(0, len(breed_names), 5):
        print(", ".join(breed_names[i:i+5]))

def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Show all breeds")
        print("2. Get a random image from a breed")
        print("3. Get a random image from a sub-breed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            breeds = get_all_breeds()
            show_breeds(breeds)

        elif choice == "2":
            breeds = get_all_breeds()
            breed = input("Enter breed name: ").strip().lower()
            if breed in breeds:
                image_url = get_random_image(breed)
                if image_url:
                    print(f"Here's your image: {image_url}")
            else:
                print(f"Error: '{breed}' is not a valid breed.")

        elif choice == "3":
            breeds = get_all_breeds()
            breed = input("Enter breed name: ").strip().lower()
            if breed in breeds and breeds[breed]:
                print("Available sub-breeds:", ", ".join(breeds[breed]))
                sub_breed = input("Enter sub-breed name: ").strip().lower()
                if sub_breed in breeds[breed]:
                    image_url = get_random_sub_breed_image(breed, sub_breed)
                    if image_url:
                        print(f"Here's your image: {image_url}")
                else:
                    print(f"Error: '{sub_breed}' is not a valid sub-breed of '{breed}'.")
            elif breed in breeds:
                print(f"Error: '{breed}' has no sub-breeds.")
            else:
                print(f"Error: '{breed}' is not a valid breed.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
