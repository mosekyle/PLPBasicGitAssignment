import json
import difflib

# Load dictionary data from JSON file
def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to find the closest match if the word is not found
def get_closest_match(word, dictionary_data):
    suggestions = difflib.get_close_matches(word, dictionary_data.keys())
    return suggestions[0] if suggestions else None

# Function to get the definition of a word
def get_definition(word, dictionary_data):
    word = word.lower()  # Normalize word to lowercase for consistency
    if word in dictionary_data:
        return dictionary_data[word]
    else:
        suggestion = get_closest_match(word, dictionary_data)
        if suggestion:
            user_input = input(f"Did you mean '{suggestion}' instead? (Y/N): ")
            if user_input.lower() == 'y':
                return dictionary_data[suggestion]
        return "Word not found in the dictionary."

# Main function to interact with the user
def main():
    # Load dictionary data
    dictionary_data = load_dictionary("dictionary.json")

    # Prompt the user to enter a word
    word = input("Enter a word to find its definition: ")
    definition = get_definition(word, dictionary_data)

    # Display the definition or message if not found
    if isinstance(definition, list):
        print("Definition(s):")
        for item in definition:
            print(f"- {item}")
    else:
        print(definition)

if __name__ == "__main__":
    main()



# Loading the Dictionary:
# The load_dictionary function reads data from a JSON file and loads it into a Python dictionary.
  
# Handling Case Sensitivity:
# The get_definition function converts the input word to lowercase to standardize the search.
  
# Suggesting Closest Matches:
# The get_closest_match function uses difflib.get_close_matches to find the closest word if the word isn’t found.
# If a match is suggested, the user is prompted to confirm it.
  
# Running the Program:
# The main function serves as the program’s entry point, where it loads the dictionary and prompts the user for a word. It then displays either the definition or an appropriate message.

# Additional Notes
# Requirements: Ensure the JSON file (e.g., dictionary.json) is downloaded and in the same directory as the script.
# Error Handling: This code assumes that the JSON file is well-formed and has the correct structure (i.e., words as keys and definitions as values).
