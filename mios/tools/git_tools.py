import subprocess

def git_status():
    """Runs 'git status' and returns stdout."""
    result = subprocess.run(['git', 'status'], capture_output=True, text=True)
    return result.stdout, result.stderr

def git_add_all():
    """Runs 'git add .' and returns stdout and stderr."""
    result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
    return result.stdout, result.stderr

def git_commit(message):
    """Runs 'git commit -m <message>' and returns stdout and stderr."""
    result = subprocess.run(['git', 'commit', '-m', message], capture_output=True, text=True)
    return result.stdout, result.stderr

def git_push():
    """Runs 'git push' and returns stdout and stderr."""
    result = subprocess.run(['git', 'push'], capture_output=True, text=True)
    return result.stdout, result.stderr
