from github import Github
import os

ACCESS_TOKEN = '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'

g = Github(ACCESS_TOKEN)
print(g.get_user())


# Query search for the github...
query = "language:python created:2022-04-01..2022-04-02"

# the result will return 1000 results for a search query
result = g.search_repositories(query)
print(result.totalCount)


# print(dir(result))
for repo in result:
    # print(f"{repo.git_url}") # print repo url
    # print(f"{repo.clone_url}") 
    # print(f"{repo.tags_url}")
    # print(repo.owner.login)

# clone the each individual repo from github to the repos folder owner_name/repo_name
    os.system(f"git clone {repo.clone_url} repos/{repo.owner.login}/{repo.name}")
    break
