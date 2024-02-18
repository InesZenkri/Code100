import json

with open('puzzle.json') as f:
    puzzle_data = json.load(f)

def get_linked_list_values(linked_list, top):
    values = []
    current_id = top
    while current_id is not None:
        current_node = next(node for node in linked_list if node["id"] == current_id)
        values.append(current_node["value"])
        current_id = current_node["next"]

    return values

solution = get_linked_list_values(puzzle_data["linkedList"], puzzle_data["top"])
print(solution) 
