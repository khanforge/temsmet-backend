from django.core.files import File
import json
import os
from committees.models import CommitteeMember

def read_json_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def get_data(members_list):
    com_id = members_list[0].get("committee_id")
    com_members = members_list[1:]
    return com_id, com_members

def process_file():
    file_path = "committees/data_committees.json"
    data = read_json_file(file_path)
    for committee_name, members_list in data["org_committes"].items():
        com_id, com_members = get_data(members_list)
        for member in com_members:
            name, affiliation, imagePath, link = member.get("name"), member.get("affiliation"), member.get("imagePath"), member.get("link")
            imagePath = imagePath.replace("./", "")
            print(imagePath)
            # member_id = CommitteeMember.objects.create(
            #     committee_id = com_id,
            #     name = name,
            #     affiliation = affiliation,
            #     image_path = ,
            #     profile_link = link
            # )


if __name__ == "__main__":
    process_file()