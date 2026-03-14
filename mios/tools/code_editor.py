import os

def replace_text_in_file(file_path, old_text, new_text):
    """
    Opens a file, replaces all occurrences of old_text with new_text,
    saves the file, and returns a success status.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = content.replace(old_text, new_text)

        if new_content == content:
            return False  # No changes were made

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True  # Changes were made and saved

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return False
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")
        return False
