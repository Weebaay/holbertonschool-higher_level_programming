import os


def generate_invitations(template, attendees):
    """Verify that template is a string and attendees is a list of dictionaries."""

    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A") if attendee.get("event_date") is not None else "N/A",
            event_location=attendee.get("event_location", "N/A")
        )

        output_file = f"output_{index}.txt"

        if os.path.exists(output_file):
            print(f"Error: {output_file} already exists. Skipping file creation.")
            continue

        with open(output_file, 'w') as file:
            file.write(output)
        print(f"Generated {output_file}")


with open('template.txt', 'r') as file:
    template_content = file.read()

attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Appel de la fonction pour générer les invitations
generate_invitations(template_content, attendees)
