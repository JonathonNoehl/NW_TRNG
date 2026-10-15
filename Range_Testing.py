import subprocess
import os
import sys

def get_next_filename(directory, base_name="range_test_output", extension=".txt"):
    """Scans the folder to find the next sequential file number so data is never wasted."""
    counter = 1
    while True:
        filename = f"{base_name}_{counter}{extension}"
        full_path = os.path.join(directory, filename)
        if not os.path.exists(full_path):
            return full_path
        counter += 1

def run_range_test():
    working_dir = r"F:\NW_TRNG"
    
    print("==================================================================")
    print("   NETWORK WEATHER TRNG - AUTOMATED RANGE TESTING LOOP")
    print("==================================================================")
    print("Methodology:     Strict extraction loop. Fully neutralizes and resets")
    print("                 AI oracle agents via isolated execution environments.")
    print("==================================================================\n")
    
    # Automatically generate the next unique sequential file path
    output_file = get_next_filename(working_dir)
    print(f"[+] Unique Output File Allocated: {output_file}")
    
    try:
        total_strings = int(input("How many 17-digit random strings do you want to harvest? "))
    except ValueError:
        print("[-] Error: Please enter a valid integer.")
        return

    print(f"\n[+] Initializing harvest sequence for {total_strings} strings...")
    
    # Open the newly allocated sequential text file
    with open(output_file, "w") as outfile:
        count = 0
        while count < total_strings:
            try:
                # Isolated subprocess execution ensures total agent reset
                process = subprocess.Popen(
                    ["python", "Main.py"],
                    cwd=working_dir,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                
                stdout, stderr = process.communicate()
                generated_string = stdout.strip()
                
                # Clean validation logic for the 17-digit engine output
                if generated_string.isdigit() and len(generated_string) == 17:
                    outfile.write(generated_string + "\n")
                    count += 1
                    sys.stdout.write(f"\r[+] Strings Collected: {count}/{total_strings} | Extracted: {generated_string}")
                    sys.stdout.flush()
                else:
                    digits = [word for word in generated_string.split() if word.isdigit() and len(word) == 17]
                    if digits:
                        outfile.write(digits[0] + "\n")
                        count += 1
                        sys.stdout.write(f"\r[+] Strings Collected: {count}/{total_strings} | Extracted: {digits[0]}")
                        sys.stdout.flush()
                        
            except Exception as e:
                print(f"\n[-] Execution interruption during agent reset cycle: {e}")
                break

    print(f"\n\n[+] Harvest Complete! Safe data cleanly preserved in: {output_file}")

if __name__ == "__main__":
    run_range_test()
