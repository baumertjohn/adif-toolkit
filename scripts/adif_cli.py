import sys
import json
import os
from adiflib import convert_adif_file

def main():
    # Check command-line arguments
    if len(sys.argv) == 1:
        # No arguments: prompt interactively
        print("ADIF to JSON Converter")
        print("---------------------")
        input_file = input("Enter input ADIF file path (e.g., adiflib/tests/sample.adi): ").strip()
        output_file = input("Enter output JSON file path (e.g., output.json): ").strip()
    elif len(sys.argv) == 3:
        # Two arguments: input and output files
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        print("Usage: python adif_cli.py [<input_adif_file> <output_json_file>]")
        print("  - If no arguments are provided, you will be prompted for file paths.")
        sys.exit(1)

    # Validate input file
    if not os.path.isfile(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)

    # Validate output file (ensure directory exists)
    output_dir = os.path.dirname(output_file) or '.'
    if not os.path.isdir(output_dir):
        print(f"Error: Output directory '{output_dir}' does not exist.")
        sys.exit(1)

    try:
        # Convert ADIF to JSON
        qsos = convert_adif_file(input_file)
        if not qsos:
            print("Warning: No QSO records found in the input file.")
        
        # Write to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(qsos, f, indent=2)
        print(f"Successfully converted '{input_file}' to '{output_file}'")
        
        # Print JSON to terminal for feedback
        print("\nOutput JSON:")
        print(json.dumps(qsos, indent=2))
    except Exception as e:
        print(f"Error processing ADIF file: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()