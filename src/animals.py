import urllib
import os
from PIL import Image
import pandas as pd


class Animal:
    def __init__(self, name, icon_link, tutorial_links, description=None) -> None:
        self.name = name
        self.icon_link = icon_link
        self.tutorial_links = tutorial_links
        self.description = description
        self.save_path = os.path.join("assets", self.name + ".png")
        if not os.path.exists(self.save_path):
            self.icon = self._get_icon()

    def __str__(self) -> str:
        return f"Hello, i am {self.name}. Here is something about me: {self.description}"

    def _get_icon(self):
        urllib.request.urlretrieve(self.icon_link, self.save_path)
        icon = Image.open(self.save_path).resize((30, 30))

        return icon

    def flip_icon(self):
        return self.icon.transpose(Image.FLIP_LEFT_RIGHT)


class Zoo:
    def __init__(self, csv_path) -> None:
        self.csv_path = csv_path
        self.animals = self._create_zoo()

    def _create_zoo(self):
        df = pd.read_csv(self.csv_path)
        return [
            Animal(df["name"][i], df["icon_link"][i], df["tutorial_links"][i], df["description"][i]) for i in range(len(df))
        ]

    def __str__(self) -> str:
        return " ".join(animal.name for animal in self.animals)
