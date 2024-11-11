# Task: File Creation, Reading, Appending, and Error Handling

# Step 1: File Creation - Writing initial content to "my_file.txt"
try:
    with open("my_file.txt", 'w') as file:
        file.write("Line 1: This is the first line.\n")
        file.write("Line 2: Python file handling is useful.\n")
        file.write("Line 3: Here is a number: 12345.\n")
    print("File 'my_file.txt' created and initial content written.")
except Exception as e:
    print(f"An error occurred while creating the file: {e}")

# Step 2: File Reading and Display - Read contents of "my_file.txt"
try:
    with open("my_file.txt", 'r') as file:
        print("\nReading 'my_file.txt' contents:")
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# Step 3: File Appending - Append additional lines to "my_file.txt"
try:
    with open("my_file.txt", 'a') as file:
        file.write("Line 4: This line is appended to the file.\n")
        file.write("Line 5: More data is added here.\n")
        file.write("Line 6: The final appended line.\n")
    print("Additional lines appended to 'my_file.txt'.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

# Step 4: Final File Reading to Confirm Changes
try:
    with open("my_file.txt", 'r') as file:
        print("\nFinal contents of 'my_file.txt':")
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
finally:
    print("\nFile handling operations completed.")


# File Creation:
# The script opens my_file.txt in write mode ('w'), writing three initial lines to the file.
# Error handling is implemented with a try-except block to catch any issues during file creation.
  
# File Reading and Display:
# The script opens my_file.txt in read mode ('r'), reads the contents, and displays them on the console.
# Error handling includes a FileNotFoundError check in case the file is missing.
  
# File Appending:
# The script opens my_file.txt in append mode ('a') and writes three more lines to the end of the file.
# Additional error handling is implemented for this step.
  
# Final Reading with finally:
# After appending, the file is read again to confirm the final contents.
# A finally block ensures that the final print statement runs regardless of any errors, signifying the completion of all file operations.
