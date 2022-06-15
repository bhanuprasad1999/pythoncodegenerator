"""
curtsies
objects are strings formatted with colors and styles displayable in a terminal with ANSI escape sequences. 
"""
import os
# from curtsies.fmtfuncs import red, bold, green, on_blue, yellow , blue, cyan

# Take the repos folder name
repo = 'repos'

for dirpath, dirnames, filenames in os.walk(repo):
    """
    Here, we are cleaning the data consisting of '.js', '.c' and any other extensions other than '.py'...
    """
    for file in filenames:
        full_path = os.path.join(dirpath, file)

        try:
            if full_path.endswith('.py'):
                print(f"keeping {full_path}")
            else:
                print(f"Deleting {full_path}")
                if repo in full_path:
                    os.remove(full_path)
                else:
                    print("something is wrong")
        except:
            os.chmod(full_path, 0o777)
            os.remove(full_path)
            print('Something went wrong')    
