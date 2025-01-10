import os
import glob

# Define the directory containing the HTML files
directory = "C:/Users/DevOps/Downloads/a/"
html_files = glob.glob(os.path.join(directory, "*.html"))

# Initialize a counter
count = 1  

# Rename each HTML file found
for original_filename in html_files:
    # Get the base name of the file (without path)
    basename = os.path.basename(original_filename)
    new_basename = basename.split('-')[1].split('_')[0] + os.path.splitext(basename)[1]
    
    # Create a new filename. Here, we're appending "_new" before the file extension.
    formatted_count = f"{count:02}"  # Format to two digits
    new_filename = f"{formatted_count} {os.path.splitext(new_basename)[0]}"  # Change this line for different renaming logic
    
    # Increment the counter for the next filename
    count += 1

    # Define the new file path
    new_file_path = os.path.join(directory, new_filename)
    
    # Rename the file (this also ensures we do not overwrite existing files)
    if not os.path.exists(new_file_path):  # to avoid overwriting
        os.rename(original_filename, new_file_path)
        print(f'Renamed file: {original_filename} to: {new_file_path}')
    else:
        print(f'File {new_file_path} already exists. Skipping rename for: {original_filename}')