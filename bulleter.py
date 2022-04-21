import pyperclip


def bulleter_function(lines: list) -> str:
    """
    This functiontakes in a list of lines and
    capitalizes the first character of each line
    adds * to the beginning at the beginning of the same line
    Also adds a space in between the lines for readability

    Args:
        line (string): This is the string that represents a line of the document

    Returns:
        str: returns the formatted string
    """
    newfile = ""
    for line in lines:
        newfile += f"* {line.capitalize()} \n"

    return newfile


def exporter_clipboarder(txt_file: str, file_name: str) -> None:
    """
    Creates a file with the name  `file_name`
    Writes some text file into the created file.
    Copies the contents of the file onto a clipboard.
    
    Args:
        txt_file (str): The file that has to be written
        file_name (str): The name of the destination file to be written
    """
    with open(f'{file_name}.txt', 'w') as file_name:
        print(txt_file, file=file_name)
    pyperclip.copy(file_name)


# Test Case
with open('text.txt', 'r') as text:
    lines = text.readlines()
    new_file = bulleter_function(lines)
    exporter_clipboarder(new_file, "beauty")
