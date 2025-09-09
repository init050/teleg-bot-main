# Telegram Bot Toolkit

This project is a toolkit of Python functions for interacting with the Telegram API using the `telethon` library. It provides a set of tools for automating various tasks, like sending messages, downloading media, and retrieving chat information.

## Project Overview

The Telegram Bot Toolkit is not a single, cohesive bot, but rather a collection of individual functions that you can use to build your own custom Telegram automation scripts. Each function is designed to perform a specific action and can be run independently.

This project is a great starting point for anyone who wants to learn how to use the `telethon` library to interact with the Telegram API.

## Features

The toolkit includes functions for the following actions:

*   **List dialogs:** Get a list of all your chats (users, groups, and channels).
*   **Send messages:** Send text messages, links, and files to any chat.
*   **Get messages:** Retrieve message history from a chat.
*   **Download media:** Download photos, videos, and other media from a chat.
*   **Download profile photos:** Download the profile photos of users or group members.
*   **Upload files:** Send local files to a chat.

## Technologies Used

*   **Language:** Python
*   **Telegram Library:** [Telethon](https://docs.telethon.dev/en/stable/)

## Installation and Setup

To use this toolkit, you'll need Python and pip installed.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/init050/teleg-bot-main.git
    cd teleg-bot-main
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install telethon
    ```

4.  **Get your API credentials:**
    You'll need to get your own `API_ID` and `API_HASH` from Telegram.
    *   Go to [my.telegram.org](https://my.telegram.org) and log in with your Telegram account.
    *   Click on "API development tools" and fill out the form.
    *   You'll be given your `API_ID` and `API_HASH`.

5.  **Configure the script:**
    Open the `py_test.py` file and replace the placeholder values for `API_ID` and `API_HASH` with your own credentials.

## How to Use

Each function in `py_test.py` is designed to be run individually.

1.  **Choose a function:**
    Decide which action you want to perform (e.g., send a message, download media).

2.  **Configure the function:**
    Fill in the placeholder variables within the function you want to use (e.g., `RECIVER`, `MESSAGE`, `USERNAME`).

3.  **Uncomment the function call:**
    At the end of each function, there is a commented-out line that runs the function (e.g., `#asyncio.run(send())`). Uncomment this line for the function you want to run.

4.  **Run the script:**
    ```bash
    python py_test.py
    ```

When you run the script for the first time, you'll be prompted to log in with your phone number, password, and a code that Telegram sends you. After you log in successfully, a `.session` file will be created, and you won't need to log in again.

## Future Improvements

*   **Create a command-line interface:** Instead of editing the script to run different functions, a command-line interface could be created to allow the user to choose which action to perform.
*   **More organized structure:** The project could be restructured into multiple files for better organization.
*   **More error handling:** Add more robust error handling to gracefully manage potential issues, like invalid usernames or network problems.
*   **Interactive bot:** The functions could be combined to create an interactive bot that responds to user commands.


