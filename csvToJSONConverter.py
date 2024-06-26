import csv
import json
import os
import random
import string

# Class to convert csv documents into a json document


class convert_csv_to_json:

    # Constructor method that takes the csv file name in the current directory and creates a dictionary
    def __init__(self, file_name):
        self.file_name = file_name
        self.content_dict = {}

    # Convert csv to json, return true on success and false on failure
    def run_conversion(self):
        # Check if a file exists in the directory with the inputted name
        if os.path.exists(self.get_csv_name()):
            with open(self.get_csv_name(), 'r', encoding='utf-8') as csv_file:
                # Read the content of the csv as a dictionary
                csv_content = csv.DictReader(csv_file)
                for content in csv_content:
                    # Insert into the dictionary the object with the uniquely generated key
                    self.get_dict()[self.generate_key()] = content
            with open(self.file_name[0:-4] + '.json', 'w', encoding='utf-8') as json_file:
                # Write each object to the json document
                json_file.write(json.dumps(self.get_dict(), indent=4))
            return True
        return False

    # Return csv name
    def get_csv_name(self):
        return self.file_name

    # Return dictionary
    def get_dict(self):
        return self.content_dict

    # Generate document key
    def generate_key(self):
        return (''.join(random.choices(string.ascii_lowercase, k=15))).upper()
