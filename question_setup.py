import os
import leetscrape as leetcode

current_dir = os.getcwd()

categories = {"Dynamic Programming": "dp", "Backtracking": "backtracking"}


stub = "combination-sum-ii"

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
leetcode.GenerateCodeStub(titleSlug=stub).generate(directory=parent_file)
