import os

def convert_txt_to_bin():
    working_dir = r"F:\NW_TRNG"
    input_file = os.path.join(working_dir, "range_test_output_1.txt")
    output_file = os.path.join(working_dir, "range_test_output_1.bin")
    
    print("==================================================================")
    print("        TRNG DATA COMPACTOR - TEXT TO RAW BINARY")
    print("==================================================================")
    
    if not os.path.exists(input_file):
        print(f"[-] Error: Could not find '{input_file}'")
        print("Please ensure your range_test_output_1.txt file is in F:\\NW_TRNG")
        return

    print(f"[+] Reading text dataset: {input_file}")
    
    # Read the raw file and strip text artifacts (newlines, carriage returns, spaces)
    with open(input_file, "r") as txt_f:
        raw_text = txt_f.read()
    
    # Isolate only the pure numeric characters
    numeric_string = "".join(ch for ch in raw_text if ch.isdigit())
    
    total_digits = len(numeric_string)
    print(f"[+] Cleaned digits extracted: {total_digits}")
    
    if total_digits == 0:
        print("[-] Error: No numeric data found in the file.")
        return

    print("[+] Compressing digits into raw binary byte chunks...")
    
    # Group the digits into standard 8-bit binary structures (bytes)
    # We take chunks of characters, convert to integer, and map to a 0-255 byte array
    byte_list = []
    
    # Using pairs of digits (00-99) safely maps values under the 255 byte limit
    for i in range(0, total_digits - 1, 2):
        digit_pair = numeric_string[i:i+2]
        byte_value = int(digit_pair)
        byte_list.append(byte_value)
        
    binary_data = bytes(byte_list)
    
    # Write the unformatted raw bytes to the new .bin file
    with open(output_file, "wb") as bin_f:
        bin_f.write(binary_data)
        
    print("==================================================================")
    print(f"[+] Conversion Complete! Raw binary saved to: {output_file}")
    print(f"[+] New File Size: {len(binary_data)} bytes")
    print("==================================================================")

if __name__ == "__main__":
    convert_txt_to_bin()
