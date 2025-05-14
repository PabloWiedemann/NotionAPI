# Notion API Integration

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

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 