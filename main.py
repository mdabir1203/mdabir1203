from src.github_api import repo_to_text
from src.vector_db import WeaviateDB
from src.text_to_speech import synthesize_text

def main():
    # Get repository contents
    owner = 'octocat'
    repo = 'Hello-World'
    repo_text = repo_to_text(owner, repo)

    # Store in Weaviate
    weaviate_db = WeaviateDB()
    weaviate_db.store_repo_content(f"{owner}/{repo}", repo_text)

    # Example of searching similar content
    similar_content = weaviate_db.search_similar_content("Hello World")
    print("Similar content:", similar_content)

    # Convert to speech
    audio = synthesize_text(repo_text)
    
    # Save audio file
    with open("output.mp3", "wb") as out:
        out.write(audio)

if __name__ == "__main__":
    main()
