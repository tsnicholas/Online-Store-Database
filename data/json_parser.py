"""Deals with parsing a json file for it's data."""
import json

class JsonParser:
    """Parses a json file."""
    @staticmethod
    def get_file_data(file_path):
        """Retreives the data from a json file from the inputted path."""
        file_data = ""
        with open(file_path, encoding = "utf8") as file:
            file_data = json.load(file)
        return file_data
    