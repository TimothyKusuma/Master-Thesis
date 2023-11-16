import os
import re

def check_yaml_files(directory):
    # List all files in the specified directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Filter for YAML files with the specified naming pattern
    yaml_files = [f for f in files if (f.endswith('.yaml') or f.endswith('.yml')) and f.startswith('diagram')]
    
    # Sort the YAML files by the numeric portion of their names
    yaml_files.sort(key=lambda f: int(re.search(r'\d+', f).group()))
    
    # Check each YAML file to see if it's empty
    empty_files = [f for f in yaml_files if os.path.getsize(os.path.join(directory, f)) == 0]
    non_empty_files = [f for f in yaml_files if os.path.getsize(os.path.join(directory, f)) != 0]
    
    return empty_files, non_empty_files

def main():
    directory = 'chatGPT_short'
    
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return
    
    # Get lists of empty and non-empty YAML files
    empty_files, non_empty_files = check_yaml_files(directory)
    
    if empty_files:
        print("Empty YAML files:")
        for f in empty_files:
            print(f)
    else:
        print("No empty YAML files found.")
    
    if non_empty_files:
        print("\nNon-empty YAML files:")
        for f in non_empty_files:
            print(f)
    else:
        print("No non-empty YAML files found.")

if __name__ == '__main__':
    main()
