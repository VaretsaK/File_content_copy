def copy_file(file_copy_from: str, file_copy_into: str = "copy_here.txt") -> None:
    """
    This function copies the file's content into another file.
    :param file_copy_from:
    :param file_copy_into:
    :return:
    """
    # opening a file to copy from, reading its content and saving it into a new variable
    with open(file_copy_from, "r") as file:
        content = file.read()

    # opening a file to copy into and saving content from previous file into this file
    # by default all content will be saved in a new file copy_here.txt unless otherwise specified
    with open(file_copy_into, "w") as file:
        file.write(content)
