# JavaScript DOM Manipulation

## Description
This project is a hands-on exploration of JavaScript's DOM manipulation capabilities. It involves learning how to interact with, modify, and enhance web pages dynamically using JavaScript.

## Resources
To complete this project, it's recommended to review the following materials:
- **General JavaScript Concepts**:
  - [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  - [Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
- **Selectors and Styling**:
  - [Document Interface](https://developer.mozilla.org/en-US/docs/Web/API/Document)
  - [Element Class](https://developer.mozilla.org/en-US/docs/Web/API/Element)
  - [Locating DOM elements using selectors](https://developer.mozilla.org/en-US/docs/Web/API/Document_object_model/Locating_DOM_elements_using_selectors)
  - [CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)
  - [CSS Diner](https://flukeout.github.io/)
- **Web APIs**:
  - [Client-side Web APIs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs)
  - [Manipulating documents](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents)
  - [Fetching data from the server](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
  - [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)

---

## Learning Objectives
By the end of this project, you will be able to:
- Select HTML elements using JavaScript.
- Understand the differences between ID, class, and tag name selectors.
- Modify an HTML element’s style and content.
- Make requests using `XMLHttpRequest` and the Fetch API.
- Bind and listen to DOM and user events.

---

## Requirements
### General
- **Editors**: Any editor of your choice.
- **Browser**: Google Chrome (version 57.0 or later).
- Files should adhere to JavaScript best practices, such as:
  - End with a newline.
  - No usage of `var`.
  - DOM manipulations should not reload the HTML page.
- The root folder must contain a `README.md` file with meaningful information.

---

## Tasks
| Task # | Task Name               | Description                                                                                                                                       | File             |
|--------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| 0      | Color Me               | Use `document.querySelector` to change the text color of the header element to red.                                                              | `0-script.js`    |
| 1      | Click and turn red     | Update the header text color to red when the user clicks on the element with `id="red_header"`.                                                   | `1-script.js`    |
| 2      | Add `.red` class       | Add the `red` class to the header when the user clicks on the element with `id="red_header"`.                                                     | `2-script.js`    |
| 3      | Toggle classes         | Toggle between `red` and `green` classes for the header when the user clicks on the element with `id="toggle_header"`.                            | `3-script.js`    |
| 4      | List of elements       | Append an `<li>Item</li>` to a list with `class="my_list"` when the user clicks on the element with `id="add_item"`.                               | `4-script.js`    |
| 5      | Change the text        | Change the header text to `New Header!!!` when the user clicks on the element with `id="update_header"`.                                          | `5-script.js`    |
| 6      | Star Wars character    | Fetch the name of a Star Wars character from a URL and display it in the element with `id="character"`.                                           | `6-script.js`    |
| 7      | Star Wars movies       | Fetch and list all Star Wars movie titles in a `<ul>` with `id="list_movies"`.                                                                   | `7-script.js`    |
| 8      | Say Hello!             | Fetch the translation of "hello" from a URL and display it in the element with `id="hello"`.                                                     | `8-script.js`    |

---

## Repository Structure
```plaintext
holbertonschool-higher_level_programming
└── javascript-dom_manipulation
    ├── 0-script.js
    ├── 1-script.js
    ├── 2-script.js
    ├── 3-script.js
    ├── 4-script.js
    ├── 5-script.js
    ├── 6-script.js
    ├── 7-script.js
    ├── 8-script.js
    └── README.md
```
## Usage

1. Clone the repository:
	https://github.com/Weebaay/holbertonschool-higher_level_programming

2. Navigate to the project directory:
	cd javascript-dom_manipulation

3. Open the corresponding HTML file in your browser to test each script.

## Author
This project was completed as part of the Holberton School curriculum by **Jean-Paul Dijeont**.