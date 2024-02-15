import random

class Therapist:
    def __init__(self):
        self.responses = {
            'feelings': ['Tell me more about your feelings.', 'How do you feel about that?'],
            'goodbye': ['Goodbye! Take care.', 'If you need anything else, feel free to reach out.']
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        return "I'm here to help. Could you please elaborate?"

# Example usage
therapist = Therapist()

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Therapist: Goodbye! Take care.")
        break
    response = therapist.get_response(user_input)
    print("Therapist:", response)
    
import sqlite3
from abc import ABC, abstractmethod
from PyPDF2 import PdfReader

class MentalDisorderDatabase(ABC):
    @abstractmethod
    def get_disorder_info(self, disorder_name):
        pass

class LocalDatabase(MentalDisorderDatabase):
    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS disorders (
                name TEXT PRIMARY KEY,
                description TEXT
            )
        ''')
        self.connection.commit()

    def populate_database(self, pdf_path):
        pdf_reader = PdfReader(pdf_path)
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            text = page.extract_text()
          
            disorder_names = ['Disorder1', 'Disorder2'] 
            for disorder_name in disorder_names:
                self.cursor.execute('''
                    INSERT OR IGNORE INTO disorders (name, description)
                    VALUES (?, ?)
                ''', (disorder_name, text))
        self.connection.commit()

    def get_disorder_info(self, disorder_name):
        self.cursor.execute('SELECT description FROM disorders WHERE name = ?', (disorder_name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return f"Information about {disorder_name} not found."

database_path = 'mental_disorders.db'
pdf_path = 'path_to_downloaded_PDF.pdf'
local_db = LocalDatabase(database_path)
local_db.create_table()
local_db.populate_database(pdf_path)

class Therapist:
    def __init__(self, database):
        self.database = database

    def get_disorder_info(self, disorder_name):
        return self.database.get_disorder_info(disorder_name)


therapist = Therapist(local_db)

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Therapist: Goodbye! Take care.")
        break
    elif 'disorder' in user_input.lower():
        disorder_name = input("You: Which disorder are you interested in? ")
        response = therapist.get_disorder_info(disorder_name)
    else:
        response = "I'm here to help. Could you please elaborate?"
    
    print("Therapist:", response)
    
import sqlite3
from abc import ABC, abstractmethod
from PyPDF2 import PdfReader

class DatabaseHandler(ABC):
    @abstractmethod
    def get_link(self):
        pass

class LocalDatabase(DatabaseHandler):
    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS link (
                id INTEGER PRIMARY KEY,
                url TEXT
            )
        ''')
        self.connection.commit()

    def insert_link(self, url):
        self.cursor.execute('INSERT INTO link (url) VALUES (?)', (url,))
        self.connection.commit()

    def get_link(self):
        self.cursor.execute('SELECT url FROM link ORDER BY id DESC LIMIT 1')
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return "Link not found in the database."

class Therapist:
    def __init__(self, database_handler):
        self.database_handler = database_handler

    def get_link(self):
        return self.database_handler.get_link()

database_path = 'chatbot_database.db'
local_db = LocalDatabase(database_path)
local_db.create_tables()


link_to_store = 'https://repository.poltekkes-kaltim.ac.id/657/1/Diagnostic%20and%20statistical%20manual%20of%20mental%20disorders%20_%20DSM-5%20(%20PDFDrive.com%20).pdf'
local_db.insert_link(link_to_store)

therapist = Therapist(local_db)

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Therapist: Goodbye! Take care.")
        break
    elif 'link' in user_input.lower():
        response = therapist.get_link()
    else:
        response = "I'm here to help. Could you please elaborate?"
    
    print("Therapist:", response)
