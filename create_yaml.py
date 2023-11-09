import os

# Ensure the directory exists
os.makedirs('chatGPT_shrot', exist_ok=True)

# Loop to create 100 YAML files
for i in range(1, 101):
    filename = f'chatGPT_short/diagram{i}.yaml'
    
    # Check if file already exists
    if os.path.exists(filename):
        print(f"File {filename} already exists, skipping.")
        continue  # Skip to the next iteration
    
    with open(filename, 'w') as file:
        pass  # No content is written, resulting in an empty file

    print(f"Created {filename}")

print("Process completed.")
