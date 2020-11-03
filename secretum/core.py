#!/usr/bin/env python3.8

from pyperclip import copy, PyperclipException
from hashlib import sha256, pbkdf2_hmac
from binascii import hexlify
from getpass import getpass
from os import path


class Secretum(object):
    def __init__(self, args):

        self.key = self.__get_key(args.key)
        self.length = args.length
        self.login = args.login

        if self.length > 30:
            print("[!] Only passwords with a maximum of 30 characters are supported")
            self.length = 30

    def __get_key(self, key):

        if path.isfile(key):
            return open(key, "r").read()
        else:
            print(f"[!] The string \033[32m'{key}'\033[0m will be used as the keyword")
            return key

    def __get_hash(self, password, key) -> bytes:

        return [
            bytes(sha256(password.encode("utf-8")).hexdigest(), encoding="utf-8"),
            bytes(sha256(key.encode("utf-8")).hexdigest(), encoding="utf-8"),
        ]

    def __generate_password(self):

        master_password = getpass() + self.login
        hash_password, hash_keyfile = self.__get_hash(
            password=master_password, key=self.key
        )

        dk = pbkdf2_hmac("sha256", hash_password, hash_keyfile, 100000)
        password = hexlify(dk)
        password = password.decode(encoding="utf-8")
        return password[: self.length] if self.length else password

    def __copy_to_clipboard(self, password):

        try:
            copy(password)
            print("[+] Password was copied to clipboard.")

        except PyperclipException:
            print("[!] Could not copy password to your clipboard.")
            print(f"Password: {password}")

        except Exception:
            print(f"Password: {password}")

    def main(self):

        password = self.__generate_password()
        self.__copy_to_clipboard(password)
