import weaviate
from sentence_transformers import SentenceTransformer
from config import WEAVIATE_URL

class WeaviateDB:
    def __init__(self):
        self.client = weaviate.Client(WEAVIATE_URL)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def create_schema(self):
        class_obj = {
            "class": "GitHubRepo",
            "vectorizer": "text2vec-transformers",
            "moduleConfig": {
                "text2vec-transformers": {
                    "model": "sentence-transformers/all-MiniLM-L6-v2",
                    "poolingStrategy": "mean"
                }
            },
            "properties": [
                {
                    "name": "content",
                    "dataType": ["text"],
                },
                {
                    "name": "repo",
                    "dataType": ["string"],
                }
            ]
        }
        self.client.schema.create_class(class_obj)

    def store_repo_content(self, repo_name, content):
        # Check if the schema exists, if not create it
        try:
            self.client.schema.get("GitHubRepo")
        except weaviate.exceptions.UnexpectedStatusCodeException:
            self.create_schema()

        # Create the data object
        data_object = {
            "content": content,
            "repo": repo_name
        }

        # Add the data object to Weaviate
        self.client.data_object.create(
            data_object=data_object,
            class_name="GitHubRepo"
        )

    def search_similar_content(self, query, limit=1):
        vector = self.model.encode(query)
        result = (
            self.client.query
            .get("GitHubRepo", ["content", "repo"])
            .with_near_vector({"vector": vector})
            .with_limit(limit)
            .do()
        )
        return result['data']['Get']['GitHubRepo']
