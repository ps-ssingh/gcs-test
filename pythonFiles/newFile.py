import os

def create_or_append_to_file(file_path, content):
    """Create or append to a file."""
    try:
        # Open the file in append mode (if it exists) or create a new one
        with open(file_path, 'a') as file:
            # Write content to the file
            file.write(content + '\n')
        print(f"Content appended to {file_path} successfully.")
    except Exception as e:
        print(f"error: {e}")

def main():
    """Main function."""
    # Use an environment variable for the file path, defaulting to './sample' if not set
    output_dir = os.getenv('CLOUDBEES_OUTPUTS', '.')
    file_path = os.path.join(output_dir, 'sample')
    
    create_or_append_to_file(file_path, 'foobar')

if __name__ == "__main__":
    main()
