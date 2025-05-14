import uuid
from notion_client import Client
from pprint import pprint
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

notion_token = os.environ["NOTION_TOKEN"]
notion_page_id = os.environ["NOTION_PAGE_ID"]
notion_database_id = os.environ["NOTION_DATABASE_ID"]

def write_dict_to_file_as_json(content, file_name):
    content_as_json_str = json.dumps(content)

    with open(file_name, 'w') as f:
        f.write(content_as_json_str)

def read_text(client, page_id):
    response = client.blocks.children.list(block_id=page_id)
    return response['results']

def safe_get(data, dot_chained_keys):
    '''
        {'a': {'b': [{'c': 1}]}}
        safe_get(data, 'a.b.0.c') -> 1
    '''
    keys = dot_chained_keys.split('.')
    for key in keys:
        try:
            if isinstance(data, list):
                data = data[int(key)]
            else:
                data = data[key]
        except (KeyError, TypeError, IndexError):
            return None
    return data

def main():
    client = Client(auth=notion_token)
    
    # Get database info
    database_info = client.databases.retrieve(database_id=notion_database_id)
    print("\nDatabase Info:")
    print(f"Title: {database_info['title'][0]['text']['content']}")
    print(f"Description: {database_info.get('description', 'No description')}")
    print(f"Created Time: {database_info['created_time']}")
    print(f"Last Edited Time: {database_info['last_edited_time']}")
    
    # Get database rows
    database_rows = client.databases.query(database_id=notion_database_id)
    print("\nDatabase Rows:")
    for row in database_rows['results']:
        print("\nRow:")
        print(f"ID: {row['id']}")
        print(f"Created Time: {row['created_time']}")
        print(f"Last Edited Time: {row['last_edited_time']}")
        print("Properties:")
        for prop_name, prop_value in row['properties'].items():
            print(f"  {prop_name}: {prop_value}")

if __name__ == '__main__':
    main()

