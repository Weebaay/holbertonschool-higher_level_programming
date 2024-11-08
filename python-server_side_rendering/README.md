# Python - Server-Side Rendering

## Project Overview

This project focuses on implementing server-side rendering (SSR) using Python and Flask, along with the Jinja templating engine. The goal is to generate web pages on the server and send fully formed HTML to the client, making web applications more efficient, SEO-friendly, and easier to maintain.

## Learning Objectives

- Understand server-side rendering and its advantages over client-side rendering.
- Implement SSR using the Flask framework.
- Utilize Jinja for dynamic HTML generation.
- Read and display data from various sources (JSON, CSV, SQLite).
- Handle dynamic content and user inputs effectively.

## Project Structure

- `task_00_intro.py`: Function for generating personalized invitations.
- `task_01_jinja.py`: Basic Flask application with HTML templates.
- `task_02_logic.py`: Dynamic templates with loops and conditions.
- `task_03_files.py`: Displaying data from JSON and CSV files.
- `task_04_db.py`: Extending functionality to include SQLite database.

## Requirements

- Python 3.x
- Flask
- Jinja2

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python-server_side_rendering.git
   cd python-server_side_rendering
	```

**Install Flask:**
	pip install Flask

**Run the application:**
	python task_01_jinja.py
**Open your browser and navigate to http://127.0.0.1:5000 to see your app in action!**

Sure! Let's break this project down into manageable parts, starting with a comprehensive README file that outlines your project. Then, I'll guide you through each task with clear explanations.
README for Python - Server-Side Rendering Project

markdown

# Python - Server-Side Rendering

## Project Overview

This project focuses on implementing server-side rendering (SSR) using Python and Flask, along with the Jinja templating engine. The goal is to generate web pages on the server and send fully formed HTML to the client, making web applications more efficient, SEO-friendly, and easier to maintain.

## Learning Objectives

- Understand server-side rendering and its advantages over client-side rendering.
- Implement SSR using the Flask framework.
- Utilize Jinja for dynamic HTML generation.
- Read and display data from various sources (JSON, CSV, SQLite).
- Handle dynamic content and user inputs effectively.

## Project Structure

- `task_00_intro.py`: Function for generating personalized invitations.
- `task_01_jinja.py`: Basic Flask application with HTML templates.
- `task_02_logic.py`: Dynamic templates with loops and conditions.
- `task_03_files.py`: Displaying data from JSON and CSV files.
- `task_04_db.py`: Extending functionality to include SQLite database.

## Requirements

- Python 3.x
- Flask
- Jinja2

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python-server_side_rendering.git
   cd python-server_side_rendering

    Install Flask:

    bash

pip install Flask

Run the application:

bash

    python task_01_jinja.py

    Open your browser and navigate to http://127.0.0.1:5000 to see your app in action!

Resources

    Flask Documentation
    Jinja2 Documentation
    Python JSON Documentation
    Python CSV Documentation
    Python SQLite Documentation

## Contributing

Feel free to submit issues or pull requests to improve the project. Contributions are welcome!

## License

This project is licensed under the MIT License.


### Task Breakdown and Explanations

#### Task 0: Creating a Simple Templating Program

**Objective**: Learn how to use string templating in Python and implement error handling.

1. **Create the Template**: Start with a template file named `template.txt`. It includes placeholders for `name`, `event_title`, `event_date`, and `event_location`.

2. **Define the Data**: You will use a list of dictionaries (attendees) as your data source. Each dictionary contains keys that match the placeholders in your template.

3. **Write the Templating Function**:
   - **Function Definition**: Create a function called `generate_invitations(template, attendees)`.
   - **Input Type Checks**: Ensure that `template` is a string and `attendees` is a list of dictionaries. If not, log an error.
   - **Empty Checks**: If either the template or attendees list is empty, log an error and stop further execution.
   - **Iterate Over Attendees**: Replace placeholders with values from each attendee’s dictionary. Use `"N/A"` for any missing data.
   - **Generate Output Files**: Save each processed template as `output_X.txt` where X is the index of the attendee.

**Helpful Hints**:
- Use Python’s string `replace` method for substitution.
- Handle file operations (read/write) carefully.
- Use `try` and `except` for graceful error handling.

---

#### Task 1: Creating a Basic HTML Template in Flask

**Objective**: Set up a Flask application and design HTML templates using Jinja.

1. **Set Up Flask**: Install Flask and create a basic app in `task_01_jinja.py`.

2. **Create Routes**: Define a route that renders an HTML template when accessed.

3. **Design HTML Template**: Create `index.html` with headings, paragraphs, and lists. Use the Jinja templating syntax.

4. **Reusable Components**: Create `header.html` and `footer.html` to be included in your main template to promote reusability.

5. **Multiple Pages**: Create additional pages (`about.html` and `contact.html`) that include the header and footer templates.

**Helpful Hints**:
- Utilize `render_template` for rendering HTML.
- Use `{% include 'header.html' %}` to insert header/footer in your pages.

---

#### Task 2: Creating a Dynamic Template with Loops and Conditions in Flask

**Objective**: Use loops and conditions in Jinja to render dynamic content.

1. **Create a New Template**: Make `items.html` which will display a list of items.

2. **Read JSON Data**: Create `items.json` with a list of items and parse it using Python's `json` module.

3. **Dynamic Rendering**: Use Jinja's `{% for %}` loop to iterate over the items. If no items are found, display a message.

4. **New Route**: Add a route in Flask to render `items.html` with the list of items read from `items.json`.

**Helpful Hints**:
- Check the structure of your JSON file.
- Use `{% if %}` to handle conditions like empty lists.

---

#### Task 3: Displaying Data from JSON or CSV Files in Flask

**Objective**: Read and display product data from JSON and CSV files.

1. **Create Data Files**: Prepare `products.json` and `products.csv` with product data.

2. **Dynamic Template**: Create `product_display.html` for displaying products in a table format.

3. **Handle Query Parameters**: Modify your Flask app to accept a `source` query parameter to decide between JSON and CSV.

4. **Implement Error Handling**: Ensure that if the source is invalid, an appropriate error message is displayed.

**Helpful Hints**:
- Use `csv` module for reading CSV files.
- Use Flask's `request.args` to access query parameters.

---

#### Task 4: Extending Dynamic Data Display to Include SQLite in Flask

**Objective**: Fetch and display data from a SQLite database in your Flask app.

1. **Setup SQLite**: Create a database file named `products.db` and a table for products.

2. **Modify Existing Template**: Reuse `product_display.html` to display data from SQLite.

3. **Implement SQLite Logic**: Extend the Flask route to handle `source=sql` and fetch data from the database.

4. **Error Handling**: Similar to previous tasks, display errors for invalid sources or database issues.

**Helpful Hints**:
- Use the `sqlite3` module to interact with the database.
- Ensure your SQL queries return data in a format suitable for rendering.

---

With this structured approach and detailed breakdown of tasks, you should be able to tackle each part of your project systematically. If you have any specific questions about any of the tasks or need further clarification on any points, feel free to ask!

## Author

This project was created as part of the Holberton School curriculum by **Dijeont Jean-Paul**.