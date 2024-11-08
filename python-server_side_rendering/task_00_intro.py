import os
import logging

logging.basicConfig(level=logging.ERROR)


def generate_invitation(template, attendees):
    """verify that template is a string and attendees is a
    list of dictionaries"""

    if not isinstance(template, str):
        logging.error("Invalid input: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(i, dict)
                                                  for i in attendees):
        logging.error(
            "Invalid input: attendees must be a list of dictionaries.")
        return

    if not template:
        logging.error("Template is empty, no output files generated.")
        return
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    for index, attendees in enumerate(attendees, start=1):
        output = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendees.get(key, "N/A")
            output = output.replace(f'{{key}}', str(value))

        output_filename = f'output_{index}.txt'

        if os.path.exists(output_filename):
            logging.error(f"{output_filename} already exists.
                          Skipping file creation.")
            continue

        with open(output_filename, 'w') as f:
            f.write(output)
