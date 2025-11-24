import requests
import re
import os

USERNAME = "r3mcos3"
README_PATH = "README.md"
MARKER_START = "<!-- TOP_REPOS_START -->"
MARKER_END = "<!-- TOP_REPOS_END -->"

def get_top_repos():
    url = f"https://api.github.com/users/{USERNAME}/events"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching events: {response.status_code}")
        return []

    events = response.json()
    repo_counts = {}
    
    for event in events:
        if event["type"] == "PushEvent":
            repo_name = event["repo"]["name"]
            # Skip the profile repo itself if desired, or keep it. 
            # Let's keep it for now as it shows activity.
            repo_counts[repo_name] = repo_counts.get(repo_name, 0) + 1

    # Sort by count (descending)
    sorted_repos = sorted(repo_counts.items(), key=lambda item: item[1], reverse=True)
    
    # Get top 2 unique repos
    top_repos = [repo[0] for repo in sorted_repos[:2]]
    
    # If less than 2, fill with defaults (optional, but good for stability)
    defaults = ["r3mcos3/dotfiles", "r3mcos3/n8n_workflows"]
    for default in defaults:
        if len(top_repos) < 2 and default not in top_repos:
            top_repos.append(default)
            
    return top_repos[:2]

def generate_markdown(repos):
    markdown = '<div align="center">\n\n'
    for repo_full_name in repos:
        # repo_full_name is like "user/repo"
        repo_name = repo_full_name.split("/")[-1]
        markdown += f'<a href="https://github.com/{repo_full_name}">\n'
        markdown += f'  <img src="https://github-readme-stats-ten-kohl.vercel.app/api/pin/?username={USERNAME}&repo={repo_name}&title_color=0891b2&text_color=ffffff&icon_color=0891b2&bg_color=1c1917&hide_border=true" />\n'
        markdown += '</a>\n'
    markdown += '\n</div>'
    return markdown

def update_readme(new_content):
    with open(README_PATH, "r") as f:
        content = f.read()

    # Regex to replace content between markers
    pattern = re.compile(f"{re.escape(MARKER_START)}.*?{re.escape(MARKER_END)}", re.DOTALL)
    
    if not pattern.search(content):
        print("Markers not found in README.md")
        return

    new_block = f"{MARKER_START}\n{new_content}\n{MARKER_END}"
    updated_content = pattern.sub(new_block, content)

    if updated_content != content:
        with open(README_PATH, "w") as f:
            f.write(updated_content)
        print("README.md updated successfully.")
    else:
        print("No changes needed.")

if __name__ == "__main__":
    top_repos = get_top_repos()
    if top_repos:
        print(f"Top repos found: {top_repos}")
        markdown = generate_markdown(top_repos)
        update_readme(markdown)
    else:
        print("No repos found.")
