import sys
import json
from adif_to_json import convert_adif_file


def main():
    if len(sys.argv) != 2:
        print("Usage: python adif_cli.py <input_adif_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    try:
        qsos = convert_adif_file(input_file)
        print(json.dumps(qsos, indent=2))
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing ADIF file: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
