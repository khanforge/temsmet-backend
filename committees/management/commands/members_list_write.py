from django.core.management.base import BaseCommand
from django.core.files import File
import json
import os
from committees.models import CommitteeMember
from django.conf import settings

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
            abs_image_path = settings.BASE_DIR / imagePath
            if not os.path.exists(abs_image_path):
                print(name)
                continue
            member, created = CommitteeMember.objects.get_or_create(
                committee_id = com_id,
                name = name,
                affiliation = affiliation,
                profile_link = link
            )
            
            with open(abs_image_path, "rb") as image_file:
                django_file = File(image_file)
                member.image_path.save(os.path.basename(abs_image_path), django_file, save = True)

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        help_string = """
        choose any option:
        1) Speakers
        2) Committee Members
        """
        parser.add_argument("file_type", type=str, help=help_string)      

    def handle(self, *args, **options):
        file_name = options['name']
        if file_name == "speakers":

        process_file()