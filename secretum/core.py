#!/usr/bin/env python3

from getpass import getpass
from hashlib import sha256, pbkdf2_hmac
from binascii import hexlify
from pyperclip import copy, PyperclipException
from os import path


class secretum:
    def __init__(self, args):

        self.key = self.get_key(args.key)
        self.login = args.login
        self.length = args.length

        if self.length > 30:
            print("[!] Only passwords with a maximum of 30 characters are supported")

    def get_key(self, key):
        if path.isfile(key):
            return open(key, "r").read()
        else:
            print(f"[x] File not found: {key}")
            print(f"[!] The string '{key}' will be used as the keyword")
            return key

    def get_master_password(self):
        return getpass() + self.login

    def get_hash(self, value):
        return sha256(value.encode("utf-8")).hexdigest()

    def generate_password(self, hash_password, hash_keyfile):
        hash_password = hash_password.encode("utf-8")
        hash_keyfile = hash_keyfile.encode("utf-8")
        dk = pbkdf2_hmac("sha256", hash_password, hash_keyfile, 1000000)
        password = hexlify(dk)
        password = password.decode(encoding="utf-8")
        return password[: self.length] if self.length else password

    def copy_to_clipboard(self, password):
        try:
            copy(password)
            print("[~] Password was copied to clipboard.")
        except PyperclipException:
            print("[!] Could not copy password to your clipboard.")
            print(f"Password: {password}")

    def main(self):
        master_password = self.get_master_password()
        hash_password = self.get_hash(master_password)
        hash_keyfile = self.get_hash(self.key)
        password = self.generate_password(hash_password, hash_keyfile)
        self.copy_to_clipboard(password)
