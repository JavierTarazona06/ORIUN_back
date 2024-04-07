import json
import os


class Constants:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    constants_file = os.path.join(base_dir, 'constants.json')
    with open(constants_file, 'r', encoding='UTF-8') as file:
        constants_dict = json.load(file)

    SEX_CHOICES = constants_dict["sex_en"]
    ETHNICITY_CHOICES = constants_dict["ethnicity_en"]
    TYPE_DOC_CHOICES = constants_dict["typ_doc_en"]
    REGION_CHOICES = constants_dict["regions_en"]