#!/usr/bin/env python3

class Dog:
    def __init__(self,name,breed = "Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} ({self.breed}) says woof!"
    