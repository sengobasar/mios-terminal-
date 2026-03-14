import json
from typing import Dict, Any
from rich import print

from mios.core.agent_planner import generate_plan
from mios.core.executor import run_action
from mios.core.observer import observe
from mios.tools.project_state import build_world_state
from mios.core.tool_registry import get_tools # Keeping existing import, though not directly used in this loop example yet.
from mios.tools.run_program import run_python_file # Import the new function
from mios.tools.project_analyzer import analyze_project


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
        problem: The initial problem statement for the agent to solve.
                 If it's a file path ending with ".py", the agent will first
                 attempt to run the script.
        max_iterations: Maximum number of planning and execution cycles.

    Returns:
        A dictionary representing the final system and project state, or the state
        at the point of stopping.
    """
    current_state = {} # Initialize an empty state, will be updated at each iteration
    goal_satisfied = False
    iteration = 0
    original_user_input = problem # Keep track of the original input

    print(f"[bold blue]Starting agent for problem:[/bold blue] {original_user_input}")

    # Step 0: Initial run if the problem is a Python file
    if original_user_input.endswith(".py"):
        file_to_run = original_user_input
        print(f"[bold cyan]Attempting initial run of Python file:[/bold cyan] {file_to_run}")
        
        initial_run_result = run_python_file(file_to_run)
        initial_observation = observe(initial_run_result)
        
        print("[cyan]Initial Script Run Observation:[/cyan]")
        if initial_observation.get("stdout"):
            print(f"[green]Stdout:[/green]\n{initial_observation['stdout']}")
        if initial_observation.get("stderr"):
            print(f"[red]Stderr:[/red]\n{initial_observation['stderr']}")
        print(f"[cyan]Error Detected:[/cyan] {initial_observation['error_detected']}")

        if not initial_observation["error_detected"]:
            print(f"\n[bold green]Script '{file_to_run}' ran successfully on first attempt! Goal satisfied.[/bold green]")
            goal_satisfied = True
            current_state = build_world_state() # Build final state after success
            return current_state
        else:
            print(f"[red]Script '{file_to_run}' failed. Agent will attempt to fix based on stderr.[/red]")
            # The problem for the planner in the first iteration becomes the error message
            problem = initial_observation["stderr"]
    
    # Main agent loop
    while not goal_satisfied and iteration < max_iterations:
        print(f"\n[bold magenta]--- Iteration {iteration + 1}/{max_iterations} ---[/bold magenta]")

        # 1. Build World State at the start of each iteration
        print("[blue]Building world state...[/blue]")
        current_state = build_world_state()
        print("[blue]Current World State:[/blue]")
        print(json.dumps(current_state, indent=4))

        # 2. Generate Plan
        # The `problem` variable here is either the original string (if not a .py file),
        # or the error message from a failed script execution or failed action.
        print("[blue]Analyzing project context...[/blue]")
        project_context = analyze_project()
        
        plan = generate_plan(problem, project_context)
        
        if not plan:
            print("[yellow]No further plan generated. Assuming goal satisfied or stuck.[/yellow]")
            goal_satisfied = True
            break

        print("[green]Generated Plan:[/green]")
        print(json.dumps(plan, indent=4))

        # 3. Execute Actions & 4. Observe Results
        current_plan_executed_successfully = True
        for step_num, step in enumerate(plan):
            print(f"\n[bold cyan]Executing Step {step_num + 1}:[/bold cyan] {step.get('action', 'Unknown Action')}")
            
            execution_result = run_action(step)
            observation = observe(execution_result)
            
            print("[cyan]Observation:[/cyan]")
            if observation.get("stdout"):
                print(f"[green]Stdout:[/green]\n{observation['stdout']}")
            if observation.get("stderr"):
                print(f"[red]Stderr:[/red]\n{observation['stderr']}")
            print(f"[cyan]Error Detected:[/cyan] {observation['error_detected']}")
            
            # 5. Update State (build_world_state at start of next iteration covers this)

            # Re-planning trigger: if an error occurred during execution of a step
            if observation.get("error_detected"):
                print("[red]Error detected during plan step execution. Re-planning for next iteration.[/red]")
                current_plan_executed_successfully = False
                # The problem for the next planning cycle becomes the new error message
                problem = observation["stderr"] if observation["stderr"] else f"Error during action: {step.get('action')}"
                break # Break from current plan execution to allow a new planning cycle
        
        # 6. Check for goal satisfaction after plan execution
        if current_plan_executed_successfully:
            # If the original problem was a Python script, re-run it to verify the fix
            if original_user_input.endswith(".py"):
                print(f"\n[bold green]Plan steps completed. Re-running original script to verify fix: '{original_user_input}'[/bold green]")
                re_run_result = run_python_file(original_user_input)
                re_run_observation = observe(re_run_result)

                print("[cyan]Re-run Script Observation:[/cyan]")
                if re_run_observation.get("stdout"):
                    print(f"[green]Stdout:[/green]\n{re_run_observation['stdout']}")
                if re_run_observation.get("stderr"):
                    print(f"[red]Stderr:[/red]\n{re_run_observation['stderr']}")
                print(f"[cyan]Error Detected:[/cyan] {re_run_observation['error_detected']}")

                if not re_run_observation["error_detected"]:
                    print(f"\n[bold green]Script '{original_user_input}' now runs successfully after plan execution! Goal satisfied.[/bold green]")
                    goal_satisfied = True
                else:
                    print(f"[red]Script '{original_user_input}' still failed after plan execution. Agent will continue trying to fix.[/red]")
                    # The problem for the next planning cycle becomes the new error message
                    problem = re_run_observation["stderr"] if re_run_observation["stderr"] else f"Script '{original_user_input}' failed again."
            else:
                # If the original problem was not a .py file, assume goal is satisfied if the plan completed successfully
                goal_satisfied = True
            
        iteration += 1

    if goal_satisfied:
        print("\n[bold green]Agent completed: Goal appears to be satisfied![/bold green]")
    else:
        print(f"\n[bold yellow]Agent finished without satisfying goal after {iteration} iterations.[/bold yellow]")
        
    # Ensure current_state is returned, even if loop didn't complete (e.g., max_iterations reached)
    return current_state
