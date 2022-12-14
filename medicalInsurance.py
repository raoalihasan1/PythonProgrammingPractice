from csvToJSONConverter import convert_csv_to_json
import json


class medical_insurance:

    def __init__(self, file_name):
        self.medical_dict = {}
        self.file_name = file_name

    def convert_csv_to_json(self):
        if (convert_csv_to_json("medicalInsurance.csv").run_conversion()):
            print("----- FILE CONVERTED TO JSON SUCCESSFULLY -----")
        else:
            print("----- FAILED TO CONVERT FILE TO JSON -----")

    def read_file_as_json(self):
        file = open("medicalInsurance.json")
        medical_data = json.load(file)
        for x in medical_data:
            self.medical_dict[x] = medical_data[x]

    def find_average(self, value):
        total = 0
        for x in self.get_dict():
            total += float(self.medical_dict[x][value])
        return total / len(self.medical_dict)

    def find_common_gender(self):
        male = 0
        female = 0
        for x in self.get_dict():
            if (self.get_dict()[x]["Sex"] == "female"):
                female += 1
            else:
                male += 1
        return ("Male" if male > female else ("Female" if female > male else "Same"))

    def find_common_gender(self):
        male = 0
        female = 0
        for x in self.get_dict():
            if (self.get_dict()[x]["Sex"] == "female"):
                female += 1
            else:
                male += 1
        return ("Male" if male > female else ("Female" if female > male else "Same"))

    def get_dict(self):
        return self.medical_dict


medical_insurance_uk = medical_insurance("medicalInsurance.csv")
medical_insurance_uk.convert_csv_to_json()
medical_insurance_uk.read_file_as_json()
print(
    f"Average Charge: £{round(medical_insurance_uk.find_average('Charges'), 2)}")
print(f"Average BMI: {round(medical_insurance_uk.find_average('BMI'), 2)}")
print(f"Average Age: {round(medical_insurance_uk.find_average('Age'), 2)}")
print(
    f"Average No. Of Children: {round(medical_insurance_uk.find_average('Children'), 2)}")
print(f"Common Gender: {medical_insurance_uk.find_common_gender()}")
