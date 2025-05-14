# Python Notion API

This project provides a set of Python scripts to interact with the Notion API, allowing you to read from and write to Notion databases and pages.

## Features

- Read database information and rows
- Write new rows to a database
- Read page content
- Environment variable based configuration

## Prerequisites

- Python 3.6 or higher
- Notion API token
- Notion page ID
- Notion database ID

## How to Obtain Notion API Token, Page ID, and Database ID

1. **Get your Notion API Token:**
   - Go to [Notion Integrations](https://www.notion.so/profile/integrations).
   - Create a new integration and copy the generated token.

2. **Share your Notion page with the integration:**
   - Open the Notion page where your database is located.
   - Click the three-dot menu (top right corner), scroll down to "Connections," and enable the integration you just created.

3. **Find your Notion Page ID:**
   - In the same three-dot menu, select "Copy link" to get the page URL.
   - The Page ID is the long string of letters and numbers in the URL. e.g.:
      - url: https://www.notion.so/username/database_name-1f37fa11c9ca80fc9e46fb8dda381111?pvs=4
      - Database id: 1f37fa11c9ca80fc9e46fb8dda381111

4. **Find your Database ID:**
   - On the database block, click the six-dot menu and select "Copy link" to get the database URL.
   - The Database ID is the long string of letters and numbers in the URL (similar to the Page ID).

> Both IDs are typically 32 characters long and may be separated by dashes in the URL.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/NotionAPI.git
cd NotionAPI
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
   - Create a `.env` file in the project root
   - Add the following variables:
   ```
   NOTION_TOKEN=your_token_here
   NOTION_PAGE_ID=your_page_id_here
   NOTION_DATABASE_ID=your_database_id_here
   ```

## Usage

### Reading Database Information
```bash
python notion_db_read.py
```

### Writing to Database
```bash
python notion_db_write.py
```

## Project Structure

- `notion_db_read.py`: Script to read database information and rows
- `notion_db_write.py`: Script to write new rows to the database
- `requirements.txt`: Python package dependencies
- `.env`: Environment variables (not tracked in git)
- `.gitignore`: Git ignore rules

## Security Notes

- Never commit your `.env` file to version control
- Keep your Notion API token secure
- The `.gitignore` file is configured to ignore sensitive files

## License

This project is licensed under the MIT License - see the LICENSE file for details. 