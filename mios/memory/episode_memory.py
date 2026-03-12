import json
import os

def save_episode(problem, plan, steps, success):
    episode = {
        "problem": problem,
        "plan": plan,
        "steps": steps,
        "success": success
    }

    episodes_file = "episodes.json"

    try:
        if not os.path.exists(episodes_file):
            with open(episodes_file, 'w') as file:
                json.dump([], file, indent=4)

        with open(episodes_file, 'r') as file:
            episodes = json.load(file)

        episodes.append(episode)

        with open(episodes_file, 'w') as file:
            json.dump(episodes, file, indent=4)

    except Exception as e:
        print(f"Error saving episode: {e}")


def load_episodes():
    episodes_file = "episodes.json"

    try:
        if not os.path.exists(episodes_file):
            return []

        with open(episodes_file, 'r') as file:
            episodes = json.load(file)

        return episodes

    except Exception as e:
        print(f"Error loading episodes: {e}")
        return []
