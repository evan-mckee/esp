"""
ESP Scrum Manager 1.1
7/12/2021
Evan McKee
"""

import json

class EspApp:
    """
    Evan-Style-Python or ESP:
    Decouple the input variables and data from your code and store them in an external JSON file.
    Read the file into a dict at the beginning; update during runtime, save and load whenever.
    """

    def __init__(self, esp_data, output_file):
        """
        Read the JSON file and initialize runtime variables.

        :param esp_data: Path to JSON file to read (str)
        :param output_file: Path to JSON file to write (str)
        """

        self.d = self.read_esp_data(esp_data)
        self.output_file = output_file

    def run(self):
        """
        Modify the data in self.d.
        """
        # Perform functions on the data
        self.write_esp_data('esp_out.json')

    def read_esp_data(self, data_file):
        """
        Read JSON data into a dict.

        :param data_file: Path to JSON file (str)
        :return: Dict of data (dict)
        """
        with open(data_file, 'r') as f:
            return json.load(f)

    def write_esp_data(self, data_file):
        """
        Output modified dict data into JSON file.

        :param data_file: Target json file (str)
        """
        with open(data_file, 'w') as f:
            json.dump(self.d, f, indent=4, sort_keys=True)


A = EspApp('esp_data.json')
A.run()
