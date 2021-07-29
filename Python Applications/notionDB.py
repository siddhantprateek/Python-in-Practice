

from notion_database.database import Database

D = Database(integrations_token=NOTION_KEY)
D.retrieve_database(database_id=database_id)