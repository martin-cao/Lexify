# Lexify - An Open-Source Vocabulary Learning Platform

Lexify is a desktop application designed to help users learn and manage vocabulary effectively. It combines the simplicity of a local desktop application with the functionality of cloud-based user synchronization.

> [!NOTE]
>
> This is an course-design project for **2024 Fall** _Python Programming_ by student ID: `547a1ec97aff5d1cc4d5c510fcd126a8`, `344790860170dfd0e32af844eff9dac1`, `7f7948923fe752064204c07ee5e6524e`, `c7ca6a04c927df019ffb5e48374635f7` (MD5 Hash).

## Features

- **Vocabulary Learning**: Memorize and review words.

- **User Accounts**: Register, log in, and synchronize learning progress.

- **Predefined Libraries**: Includes common word libraries such as TOEFL, GRE, and more. (Future support for Japanese word libraries, such as JLPT N1 - N5 is planned.)

## Technology Stack
- **Frontend**: PySide6 for the desktop application.
- **Backend**: Flask for user authentication and data synchronization.
- **Database**: SQLite for local and server-side data storage, with SQLAlchemy ORM for managing data models and queries.

## Project Structure
- `frontend/`: Desktop application source code.
- `backend/`: API and server-side logic.
- `dict/`: Code used for importing the dataset of words. More below.

## Getting Started
Follow these steps to set up.
### 1. Clone the repository
```shell
git clone https://github.com/your_username/lexify.git
cd lexify
```

### 2. Set up the Virtual Environment and Install Dependencies
This project requires Python 3.12 or higher. It's recommended to use a virtual environment to manage dependencies.

#### On Linux/macOS
```shell
python3 -m venv venv
source venv/bin/activate
```

#### Or Windows
```shell
python -m venv venv
venv\Scripts\activate
```

then,
```shell
pip install -r requirements.txt
```

### 3. Run the Code
#### For frontend
```shell
cd frontend
python3 Lexify.py
```

#### For backend
```shell
cd backend
python3 app.py
```

Or you can use Docker Compose
```shell
docker-compose up --build -d
```

### 4. Import Dictionary Data _(Optional)_
If you want to import the dictionary data by your self, follow the instructions below.

You should remove the word, library and library_word data in the databases by yourself. Remove all elements in the `words`, `libraries` and `library_words` tables in `frontend/database/database_fe.db` and `backend/app/database/database_be.db`. These are two SQLite databases. You could use Navicat or other tools to remove the data.

Then, clone the [DictionaryData](https://github.com/LinXueyuanStdio/DictionaryData) repository at Lexify/dict, and run `load_data.py`.
```shell
cd dict
python3 load_data.py
```

At last, you need to run this SQL query in order to remove all words with no definitions.
```sql
DELETE FROM words WHERE definition = ''
```

---

## Open Source Attribution
The dictionary data user in this project comes from [DictionaryData](https://github.com/LinXueyuanStdio/DictionaryData), which is licensed under the Apache-2.0 Licence. Special thanks to the authors for making this data publicly available.

> [!WARNING]
> As this is a course design project, please DO NOT make any pull request. If you have any suggestion with this project, please create an issue.

For more information, please contact <a href="mailto:martincao119@icloud.com">martincao119@icloud.com</a>.

Stay tuned for updates!