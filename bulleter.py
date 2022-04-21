
import pyperclip


def bulleter_function(lines:list)->str:
    """
    This functiontakes in a list of lines andd
    capitalizes the first character of each line
    adds * to the beginning at the beginning of the same line

    Args:
        line (string): This is the string that represents a line of the document

    Returns:
        str: returns the formatted string
    """
    newfile = ""
    for line in lines:
        newfile += f"* {line.capitalize()} \n"
    
    return newfile


def exporter_clipboarder(txt_file:str,file_name:str)->None:
    """
    Writes a file into a new file which has been named by
    the file name

    Args:
        txt_file (str): The file that has to be written
        file_name (str): The name of the destination file to be written
    """
    with open(f'{file_name}.txt','w') as file_name:
        print(txt_file,file=file_name)
    pyperclip.copy(file_name)
    


with open('text.txt','r') as text:
    lines = text.readlines()
    new_file = bulleter_function(lines)
    exporter_clipboarder(new_file,"beauty")
    
    