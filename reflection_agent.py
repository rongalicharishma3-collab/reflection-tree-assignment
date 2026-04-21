import json

# Load the reflection tree
with open("reflection_tree.json", "r") as file:
    tree = json.load(file)

nodes = tree["nodes"]
current_node = tree["start"]

answers = {}

print("\nWelcome to the Reflection Tree\n")

while True:
    node = nodes[current_node]
    node_type = node["type"]

    if node_type == "question":
        print("\n" + node["text"])

        options = list(node["options"].keys())

        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        choice = int(input("Select option: ")) - 1
        selected_option = options[choice]

        answers[current_node] = selected_option
        current_node = node["options"][selected_option]

    elif node_type in ["decision", "reflection", "bridge"]:
        print("\n" + node["text"])
        current_node = node["next"]

    elif node_type == "summary":
        print("\nSummary:")
        print(node["text"])
        print("\nYour answers:")
        for q, a in answers.items():
            print(f"{q} -> {a}")
        break
