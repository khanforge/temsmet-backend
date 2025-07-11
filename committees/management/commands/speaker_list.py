from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings
from committees.models import Speaker
import json
import os
from pathlib import Path


def get_data(speaker):
    return (
        speaker.get("name", "").strip(),
        speaker.get("affiliation", "").strip(),
        speaker.get("imagePath", "").strip(),
        speaker.get("link", "").strip()
    )


def process_data(data):
    for speaker in data.get("speakers", []):
        print(f"Processing: {speaker.get('name')}")

        name, affiliation, image_path, link = get_data(speaker)

        # Convert relative image path to absolute
        cleaned_path = image_path.lstrip("./")
        abs_image_path = Path(settings.BASE_DIR) / "committees" / cleaned_path

        if not abs_image_path.exists():
            print(f"❌ File not found: {abs_image_path}")
            continue

        # Get or create the speaker
        speaker_obj, created = Speaker.objects.get_or_create(
            name=name,
            affiliation=affiliation,
            link=link
        )

        # Attach image if not already set
        if not speaker_obj.image_path:
            with open(abs_image_path, "rb") as f:
                django_file = File(f)
                speaker_obj.image_path.save(abs_image_path.name, django_file, save=True)
                print(f"✅ Image attached: {abs_image_path.name}")
        else:
            print(f"ℹ️ Image already exists for: {name}")


class Command(BaseCommand):
    help = "Import speaker data from JSON"

    def handle(self, *args, **options):
        file_path = Path(settings.BASE_DIR) / "committees" / "speakers.json"
        if not file_path.exists():
            self.stderr.write(f"❌ JSON file not found at {file_path}")
            return

        with open(file_path, "r") as file:
            try:
                data = json.load(file)
                process_data(data)
                self.stdout.write(self.style.SUCCESS("✅ Speakers imported successfully"))
            except json.JSONDecodeError as e:
                self.stderr.write(f"❌ JSON decode error: {e}")
