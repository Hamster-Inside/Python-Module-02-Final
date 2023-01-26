""" File manager """
import typing


class FilesManager:
    """ Class for operating on files """
    def __init__(self, directory="Secrets/"):
        self.dir = directory
        self.passwords_file_name = "passwords.txt"
        self.safe_passwords_file_name = "safe_passwords.txt"
        self.unsafe_passwords_file_name = "unsafe_passwords.txt"
        self._create_safe_and_unsafe_files()
        self.passwords_list = []

    def _create_safe_and_unsafe_files(self) -> None:
        """ Creates files if they do not exist"""
        with open(
                self.dir + self.passwords_file_name,
                mode='a+', encoding="UTF-8") as input_file, open(
                self.dir + self.safe_passwords_file_name,
                mode='w', encoding="UTF-8"), open(
                self.dir + self.unsafe_passwords_file_name,
                mode='w', encoding="UTF-8"):
            input_file.seek(0)
            if input_file.readline() == "":
                input_file.write("TestPassword#000")

    def get_list_of_passwords(self) -> typing.List:
        """ Returns list of passwords from txt file """
        if len(self.passwords_list) == 0:
            with open(self.dir + self.passwords_file_name,
                      mode='r', encoding="UTF-8") as input_file:
                for line in input_file.readlines():
                    self.passwords_list.append(line.strip('\n'))
        return self.passwords_list

    def add_to_safe_passwords_file(self, text):
        """ adds password to safe passwords file it is a safe password """
        with open(self.dir + self.safe_passwords_file_name,
                  mode='a', encoding='UTF-8') as input_file:
            input_file.write(text + '\n')

    def add_to_unsafe_passwords_file(self, text):
        """ adds password to unsafe passwords file it is a unsafe password """
        with open(self.dir + self.unsafe_passwords_file_name,
                  mode='a', encoding='UTF-8') as input_file:
            input_file.write(text + '\n')
