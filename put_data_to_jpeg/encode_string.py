from cryptography.fernet import Fernet
from typing import Union
import base64
import json


class Encoder:

    def __init__(self, password: str, data: Union[str, bytes]=None,):
        self.data = None
        if data is not None and isinstance(data, str):
            self.data = data.encode()
        elif data is not None and isinstance(data, bytes):
            self.data = data

        self.password = self.password_to_len_32(password)
        self.fernet = Fernet(self.password)
        self.encode_data = None
        self.decode_data = None
        self.cp1251_dict = self.cp1251_dict()

    def encode(self):
        if self.data is not None:
            self.encode_data = self.fernet.encrypt(self.data)

    def decode(self):
        if self.data is not None:
            self.decode_data = self.fernet.decrypt(self.data).decode()

    def prepare_to_file(self):
        max_bits = 8
        if self.encode_data is None:
            return
        file_string = ''
        for elem in self.encode_data.decode():
            double = bin(self.ord_cp1251(elem))[2:]
            file_string += '0'*(max_bits-len(double)) + double
        file_string += '0' * 2 * max_bits
        return file_string

    def prepare_to_decode(self, file_string):
        max_bits = 8
        if not file_string.endswith('0' * 2 * max_bits):
            raise RuntimeError('Wrong data: Not found 16 x 0 in the end of preparing string.')
        file_string = file_string[:-16]
        elems = [file_string[x: x+max_bits] for x in range(0, len(file_string), max_bits)]
        data = ''
        for elem in elems:
            data += str(self.chr_cp1251(int(elem, 2)))
        self.data = data.encode()

    def ord_cp1251(self, element):
        if element not in self.cp1251_dict.keys():
            raise RuntimeError(f'ord_cp1251: Unknown character: {element} for cp1251')
        return self.cp1251_dict[element]

    def chr_cp1251(self, element):
        if element not in self.cp1251_dict.values():
            raise RuntimeError(f'chr_cp1251: Unknown character: {element} for cp1251')
        reverse_cp1251_dict = {value: key for key, value in self.cp1251_dict.items()}
        return reverse_cp1251_dict[element]

    @staticmethod
    def password_to_len_32(password):
        new_password = password
        if len(password) > 32:
            new_password = password[:32]
        elif len(password) < 32:
            new_password = password + 'a' * (32 - len(password))
        b64_password = base64.urlsafe_b64encode(new_password.encode())
        return b64_password

    @staticmethod
    def cp1251_dict():
        with open('cp1251.json') as file:
            data = json.load(file)
        return data


data = Encoder(password='lolkek', data='Дима лох')
data.encode()

a = data.prepare_to_file()
print(a)
data.prepare_to_decode(a)
data.decode()
print(data.decode_data)
