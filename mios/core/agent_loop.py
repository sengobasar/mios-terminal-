import json
from mios.core.agent_planner import generate_plan
from mios.core.tool_registry import get_tools

def run_agent(problem):
    plan = generate_plan(problem)
    print("Generated Plan:")
    print(json.dumps(plan, indent=4))

    for step in plan:
        print(f"Executing step: {step}")

    return plan
