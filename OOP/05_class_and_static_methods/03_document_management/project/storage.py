from project import Category
from project import Document
from project import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for category in self.categories:
            if category_id == category.id:
                category.name = new_name
                break

    # def edit_category(self, category_id: int, new_name: str):
    #     category = next((cat for cat in self.categories if cat.id == category_id), None)
    #     if category:
    #         category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = next((topic for topic in self.topics if topic.id == topic_id), None)
        if topic:
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = next((doc for doc in self.documents if doc.id == document_id), None)
        if document:
            document.file_name = new_file_name

    def delete_category(self, category_id: int):
        category = next((cat for cat in self.categories if cat.id == category_id), None)
        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id: int):
        topic = next((topic for topic in self.topics if topic.id == topic_id), None)
        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id: int):
        document = next((doc for doc in self.documents if doc.id == document_id), None)
        if document:
            self.documents.remove(document)

    def get_document(self, document_id: int):
        document = next((doc for doc in self.documents if doc.id == document_id), None)
        if document:
            return document

    def __repr__(self):
        for document in self.documents:
            return str(document)
