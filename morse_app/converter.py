from morse_code_dict import MORSE_CODE_DICT

def text_to_morse(text: str) -> str:
    text = text.upper()
    morse_chars = []
    
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_chars.append(MORSE_CODE_DICT[char])
        else:
            # Use a placeholder (like a slash) for unknown characters or spaces
            morse_chars.append('/')
    
    # Join the Morse code units with a space
    return ' '.join(morse_chars)

# Example usage:
if __name__ == "__main__":
    sample_text = "Hello World"
    print(text_to_morse(sample_text))
    # Output should be: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
