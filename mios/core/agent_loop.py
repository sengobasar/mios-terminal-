import json
from typing import Dict, Any
from rich import print

from mios.core.agent_planner import generate_plan
from mios.core.executor import run_action
from mios.core.observer import observe
from mios.tools.project_state import build_world_state
from mios.core.tool_registry import get_tools # Keeping existing import, though not directly used in this loop example yet.


def run_agent(problem: str, max_iterations: int = 5) -> Dict[str, Any]:
    """
    Executes a closed-loop reasoning agent to solve a problem.

    The agent operates in a loop:
    1. Builds the current world state.
    2. Generates a plan based on the problem and current state.
    3. Executes actions defined in the plan.
    4. Observes the results of the executed actions.
    5. Updates its internal state (implicitly by re-building world state in next iteration).
    6. Stops when the goal is satisfied or max iterations are reached.

    Args:
        problem: The problem statement for the agent to solve.
        max_iterations: Maximum number of planning and execution cycles.

    Returns:
        A dictionary representing the final system and project state, or the state
        at the point of stopping.
    """
    current_state = {} # Initialize an empty state, will be updated by build_world_state
    goal_satisfied = False
    iteration = 0

    print(f"[bold blue]Starting agent for problem:[/bold blue] {problem}")

    while not goal_satisfied and iteration < max_iterations:
        print(f"\n[bold magenta]--- Iteration {iteration + 1}/{max_iterations} ---[/bold magenta]")

        # 1. Build World State
        print("[blue]Building world state...[/blue]")
        current_state = build_world_state()
        print("[blue]Current World State:[/blue]")
        print(json.dumps(current_state, indent=4))

        # 2. Generate Plan
        # The generate_plan function is currently simple, in a real agent, it would
        # deeply consider the 'current_state' and 'problem' to create a dynamic plan.
        plan = generate_plan(problem)
        
        if not plan:
            print("[yellow]No further plan generated. Assuming goal satisfied or stuck.[/yellow]")
            goal_satisfied = True # No plan means nothing to do, assume problem solved or unresolvable
            break

        print("[green]Generated Plan:[/green]")
        print(json.dumps(plan, indent=4))

        # 3. Execute Actions & 4. Observe Results
        # Iterate over the plan steps. If an error occurs, the plan is considered
        # failed for this iteration, and a new planning cycle begins.
        current_plan_executed_successfully = True
        for step_num, step in enumerate(plan):
            print(f"\n[bold cyan]Executing Step {step_num + 1}:[/bold cyan] {step.get('action', 'Unknown Action')}")
            
            execution_result = run_action(step)
            observation = observe(execution_result)
            
            print("[cyan]Observation:[/cyan]")
            # Print stdout and stderr from observation
            if observation.get("stdout"):
                print(f"[green]Stdout:[/green]\n{observation['stdout']}")
            if observation.get("stderr"):
                print(f"[red]Stderr:[/red]\n{observation['stderr']}")
            print(f"[cyan]Error Detected:[/cyan] {observation['error_detected']}")
            
            # 5. Update State (Conceptual: In a more advanced agent, this observation
            # would be explicitly processed and integrated into `current_state` for the next planning phase.)
            # For this loop, the `build_world_state()` call at the start of the next iteration
            # acts as the state update mechanism.

            # Simple re-planning trigger: if an error occurred during execution of a step,
            # we consider the current plan invalid and need a new planning cycle.
            if observation.get("error_detected"):
                print("[red]Error detected during step execution. Re-planning for next iteration.[/red]")
                current_plan_executed_successfully = False
                break # Break from current plan execution to allow a new planning cycle
        
        # 6. Stop when goal satisfied (Basic check)
        # If the entire generated plan executed without errors, we assume the problem
        # might be resolved for this basic agent. A more complex agent would have
        # a dedicated goal satisfaction check.
        if current_plan_executed_successfully:
            goal_satisfied = True # Assume goal is satisfied if the plan completed successfully.
            
        iteration += 1

    if goal_satisfied:
        print("\n[bold green]Agent completed: Goal appears to be satisfied![/bold green]")
    else:
        print(f"\n[bold yellow]Agent finished without satisfying goal after {iteration} iterations.[/bold yellow]")

    # Return the final `current_state` which represents the observed world state at the end.
    return current_state
