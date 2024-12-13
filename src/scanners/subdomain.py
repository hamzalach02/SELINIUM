import subprocess
import re

def find_subdomains(domain):
    # Run Sublist3r as a subprocess
    command = ["sublist3r", "-d", domain]
    
    try:
        # Capture the output
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            # Filter only subdomain lines (e.g., remove banners, errors, etc.)
            output_lines = result.stdout.splitlines()
            subdomains = [line for line in output_lines if re.match(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", line)]
            
            # Print the cleaned array to see the subdomains
            print(subdomains)
            
            # Save the filtered subdomains to a txt file
            with open("subdomains.txt", "w") as file:
                for subdomain in subdomains:
                    file.write(subdomain + "\n")
                    
            print("Filtered subdomains saved to subdomains.txt.")
        else:
            print("Error:", result.stderr)
    
    except FileNotFoundError:
        print("Sublist3r is not installed or not in PATH.")

# Example usage
find_subdomains("amazon.com")
