import json, os, requests
from translate.storage import po,tmx
from dotenv import load_dotenv
load_dotenv()
BOOKS_PATH = 'templates/books.json'
LOCALE_DIR = "locale"
LANGUAGES = ['en'] # Ability to add more languages
PRODUCTION_PO = 'translations'
SOURCE_LANG = 'ar'

students_sheety_url = os.getenv('students_sheety_url')
tenses_rule_sheety_url = os.getenv('tenses_rule_sheety_url')

class Automation:
    def __init__(self) -> None:
        self.new_content_books = {
                "mandatory": {},
                'elective': {},
                "tenses_rule": {},
                "suggested_books": [],
                "suggested_summaries": {},
                "codes":{}}
        with open (BOOKS_PATH, 'r', encoding="UTF-8") as file:
            self.current_content_books = json.load(file)
        self.new_content_books = self.current_content_books
        
    def get_tenses_rule(self):
        response  = requests.get(tenses_rule_sheety_url) # type: ignore
        table = response.json()["table"]
        for row in table:
            code = row["اسم المادة"].split("(")[0]
            link = row['حمل الملف']
            author = row["المشاركون في العمل"]
            if code not in self.current_content_books["tenses_rule"]:
                self.current_content_books["tenses_rule"][code] = []
                book = {
                    "name": '',
                    "image": '',
                    "author":author,
                    "link":link,
                }
                self.current_content_books["tenses_rule"].append(book)
              
                
        self.new_content_books = self.current_content_books
        self.build()
    def get_students_suggstions(self):
        response  = requests.get(students_sheety_url) # type: ignore
        table = response.json()["table"]
        for row in table:
            course = row["اسم المادة"]
            code = row["اسم المادة"].split("(")[0]
            link = row['حمل الملف']
            author = row["المشاركون في العمل"]
            type = row["نوع المرفق"]
            if type == 'كتاب':
                book = {
                    "course": course,
                    "author":author,
                    "link":link,
                }
                self.current_content_books["suggested_books"].append(book)
            else:
                summary = {
                    "author":author,
                    "file":link,
                }
                self.current_content_books["suggested_summaries"][code].append(summary)
        self.new_content_books = self.current_content_books
        self.build()

 
    def create_codes(self):
        for code in self.get_codes():
            self.current_content_books["suggested_summaries"][code] = []
        self.new_content_books = self.current_content_books
        self.build()

  

    def create_tmx_from_po(self):
        """Convert PO to TMX for translation memory"""
        for lang in LANGUAGES:
            tmx_lang_dir = os.path.join('tmx', lang)
            os.makedirs(tmx_lang_dir, exist_ok=True)
            po_lang_dir= os.path.join(PRODUCTION_PO, lang, "LC_MESSAGES")
            if not os.path.exists(po_lang_dir):
                print("Directory does not exist!")
                continue
            for file in os.listdir(po_lang_dir):
                if file.endswith('.po'):
                    print("in")
                    po_path = os.path.join(po_lang_dir, file)
                    tmx_output_path = os.path.join(tmx_lang_dir,  file.replace('.po', ".tmx"))
                    
                    try:
                        po_store = po.pofile.parsefile(po_path)
                        tmx_store = tmx.tmxfile()
                        
                        for unit in po_store.units:
                            if unit.source and unit.target:
                                tmx_store.addtranslation(unit.source, "ar", unit.target, lang)
                                
                        tmx_store.savefile(tmx_output_path)
                        print(f"Successfully created: {tmx_output_path}")
                    except Exception as e:
                        print(f'Error processing {po_path}: {e}')
    
    def get_codes(self):
        return self.current_content_books["codes"]
    
    def build(self):
        with open(BOOKS_PATH, 'w', encoding="UTF-8") as file:
            json.dump(self.new_content_books, file,indent=4,ensure_ascii=False)




