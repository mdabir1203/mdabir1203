import feedparser
import re

# RSS feed URL of your Medium blog
rss_url = 'https://medium.com/feed/@md.abir1203'

def fetch_blog_posts():
    posts = feedparser.parse(rss_url).entries
    return posts[:5]  # Fetches the latest 5 posts

def generate_md(posts):
    md_content = ''
    for post in posts:
        title = post.title
        link = post.link
        md_content += f'- [{title}]({link})\n'
    return md_content

def update_readme(content):
    with open('README.md', 'r') as file:
        readme = file.read()

    # Replace content between <!-- BLOG-POST-LIST:START --> and <!-- BLOG-POST-LIST:END -->
    updated_readme = re.sub('<!-- LIST:START --> LIST:END -->',
                            f'<!-- LIST:START -->\n{content}<!-- LIST:END -->', 
                            readme, 
                            flags=re.DOTALL)
    
    with open('README.md', 'w') as file:
        file.write(updated_readme)

if __name__ == "__main__":
    posts = fetch_blog_posts()
    md_content = generate_md(posts)
    update_readme(md_content)
