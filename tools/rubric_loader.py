# Rubric loader placeholder
import json


def load_rubric():
    with open("rubric.json", "r") as f:
        return json.load(f)