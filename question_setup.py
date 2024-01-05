import os
import leetscrape as leetcode
import re

current_dir = os.getcwd()

categories = {"Dynamic Programming": "dp", "Backtracking": "backtracking"}


stub = "word-search"

question = leetcode.GetQuestion(titleSlug=stub).scrape()

topics_set = set(question.topics)
common_topics = topics_set.intersection(categories.keys())

if not common_topics:
    print(
        f"Category not found please create one in the following {str(categories.keys())}"
    )
    exit()

parent_file = os.path.join(
    current_dir,
    categories[common_topics.pop()].lower(),  
    question.difficulty.lower(),
    f"{str(question.QID)}_" + question.title.replace(" ", "_"),
)


os.makedirs(parent_file, exist_ok=True)

# with open(os.path.join(parent_file, "solution.py"), "w") as f:
#     f.write("")

# print(f"Created {parent_file} folder with solution.py file")

# leetcode.GenerateCodeStub(titleSlug=stub).generate(directory=parent_file)

print(question.Code)