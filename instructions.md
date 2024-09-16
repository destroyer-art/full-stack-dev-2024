# Hardian Health - Full Stack Developer 2024 Task

## Introduction

Welcome to the Full Stack Developer technical task for Hardian Health! This task is designed to simulate real-world challenges you might face in the role here. Your solution will help us evaluate your technical and problem-solving skills, attention to detail, and ability to work with messy data.

## Contents

Within this folder, you will find the following files:

1. **This instructions document** (`instructions.md`).
2. **An SQLite3 database** (`db.sqlite3`).
3. **A `task_description.md` file**.
4. **A `tests.py` file** (a basic testing structure put together to help you get started).

The SQLite3 database contains two small tables: **`fda_data`** and **`eudamed_data`**, each with approximately 40 rows of data. This data has not been cleaned, and there are no foreign keys linking the tables. Some devices may be found in both tables, while others only exist in one. The tables can be matched based on the `device_name` column, but you should be aware that there may be inconsistencies (e.g., case differences, duplicates, or missing data). Please take a moment to familiarise youself with the data. 

## Task

### Objective

Create a Django web application with the following functionality:

1. **Single-page app**: The app should contain one main page only.
2. **Search bar**: Include a search bar in the header where users can search for a device by `device_name`.
3. **Display Results**:
    - When a device is searched, return the respective data from **both** the `fda_data` and `eudamed_data` tables.
    - If the device is found in one table but not the other, return the data from the table where it exists and display a message indicating it was not found in the other table.
    - If the device is not found in either table, return a "not found" message.
4. **Data Cleaning**: Handle any inconsistencies in the `device_name` (e.g., case differences, duplicates) so that devices can be properly matched across both tables.

### Front-End Requirements

- You are free to choose how to style the front end, but it should be functional and user-friendly.
- Feel free to use frameworks like Bootstrap, Tailwind, or custom CSS but include any custom requirements in `requirements.txt`.

### Bonus Task (Optional)

1. **API Endpoint**: Expose an API endpoint that accepts a `GET` request with a `device_name` parameter and returns the search results in JSON format.

## Testing

I have provided a basic `tests.py` file to help you get started. It includes a test structure and some basic test cases. You are expected to:

- Add or extend unit tests for the search functionality and any other key logic as you see fit.
- Use Django's built-in testing framework to run your tests.

### Basic Test Setup

The provided `tests.py` includes:

- A test case for when a device exists in **both** the `fda_data` and `eudamed_data` tables.
- A test case for when a device exists only in **one** of the tables.
- A test case for when a device is **not found** in either table.

## Submission Requirements

1. **Fork this repository** and create a new branch with your name.
2. Implement the task as described above.
3. **Include a `requirements.txt` file**: This should list all necessary dependencies required to run your project.
4. Ensure your code is properly commented and follows best practices.
5. **Include a `task_description.md` file**: In this file, include:
   - A brief overview of your approach.
   - Instructions on how to set up and run the project locally.
   - Any assumptions or decisions you made while implementing the task.
   - Any suggestions or recommendations for how you would expand on this functionality further. 
6. **Ensure your app runs without issues**: I should be able to set up and run the project easily using the provided instructions.
7. Push your solution to your branch and **create a pull request**.
8. Notify us via email when your task is complete.

## Evaluation Criteria

Your submission will be evaluated based on the following criteria:

1. **Functionality**: Does the app meet all the requirements outlined in the task?
2. **Code quality**: Is the code well-structured, readable, and maintainable? Are there any redundant or unnecessary parts of the code?
3. **Testing**: Are there meaningful unit tests in place that cover key functionality? How well is the search functionality tested?
4. **Front-end styling**: Is the UI clean, user-friendly, and functional?
5. **Data Cleaning**: How well did you handle inconsistencies in the `device_name` column across the two tables?
6. **Bonus points**: For API integration (optional).

---

Feel free to contact me if you have any issues.

Good luck!
