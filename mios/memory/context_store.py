import json
import os

def save_context(key, value):
    context_file = "context.json"
    try:
        if not os.path.exists(context_file):
            with open(context_file, 'w') as file:
                json.dump({}, file, indent=4)

        with open(context_file, 'r') as file:
            context = json.load(file)

        context[key] = value

        with open(context_file, 'w') as file:
            json.dump(context, file, indent=4)

    except Exception as e:
        print(f"Error saving context: {e}")


def load_context(key):
    context_file = "context.json"
    try:
        if not os.path.exists(context_file):
            return None

        with open(context_file, 'r') as file:
            context = json.load(file)

        return context.get(key, None)

    except Exception as e:
        print(f"Error loading context: {e}")
        return None
