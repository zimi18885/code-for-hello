def generate_response(button_text):
    if button_text:
        return "don't touch"
    else:
        return "Please type a button text."

# Example usage
user_input = input("Enter a button text: ")
response = generate_response(user_input)
print(response)
