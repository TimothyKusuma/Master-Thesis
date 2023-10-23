import os

def check_empty_yaml_files(directory):
    # List all files in the specified directory
    files = os.listdir(directory)
    
    # Filter for only .yaml files
    yaml_files = [f for f in files if f.endswith('.yaml')]
    
    # Check each YAML file to see if it's empty
    empty_files = [f for f in yaml_files if os.path.getsize(os.path.join(directory, f)) == 0]
    
    return empty_files

# Specify the directory to check
directory = 'chatGPT_results'

# Get the list of empty YAML files
empty_files = check_empty_yaml_files(directory)

# Print the results
if empty_files:
    print(f"Empty YAML files in the '{directory}' directory:")
    for file in empty_files:
        print(f"- {file}")
else:
    print(f"No empty YAML files found in the '{directory}' directory.")
