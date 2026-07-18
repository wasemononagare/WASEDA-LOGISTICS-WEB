import subprocess
import sys

def run_command(cmd):
    print(f"Executing: {cmd}")
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result.returncode

def main():
    # 1. Create and switch to new branch
    run_command("git checkout -b feature/reorganize-files")
    
    # 2. Stage changes
    run_command("git add .")
    
    # 3. Commit changes
    run_command('git commit -m "chore: reorganize directory structure and update asset paths"')
    
    # 4. Push to remote
    run_command("git push -u origin feature/reorganize-files")
    
    # 5. Create PR (if gh CLI is installed)
    pr_cmd = 'gh pr create --title "chore: reorganize directory structure and update asset paths" --body "Reorganized repository into images/, videos/, and pages/ directories, updated all asset paths, fixed missing profile, and added root redirect."'
    run_command(pr_cmd)

if __name__ == "__main__":
    main()
