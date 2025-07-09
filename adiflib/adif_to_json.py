import re
import json
from typing import List, Dict, Optional


def parse_adif_field(field: str) -> Optional[tuple[str, str]]:
    """Parse an ADIF field like <CALL:5>AB1CD into (key, value)."""
    match = re.match(r"<([A-Za-z0-9_]+):(\d+)(:[A-Za-z])?>([^<]+)", field.strip())
    if match:
        key = match.group(1).upper()
        value = match.group(4)[: int(match.group(2))].strip()
        return key, value
    return None


def adif_to_json(adif_content: str) -> List[Dict[str, str]]:
    """Convert ADIF content to a list of JSON-compatible dictionaries."""
    qsos = []
    current_qso = {}
    header_passed = False
    buffer = ""

    # Split content into lines and process
    lines = adif_content.replace("\r\n", "\n").split("\n")
    for line in lines:
        line = line.strip()
        if not line:
            continue

        buffer += line
        # Handle multi-line fields
        if not buffer.endswith(">"):
            continue

        # Check for end of header
        if buffer.upper().endswith("<EOH>"):
            header_passed = True
            buffer = ""
            continue

        # Process QSO records after header
        if header_passed:
            if buffer.upper().endswith("<EOR>"):
                if current_qso:
                    qsos.append(current_qso)
                    current_qso = {}
                buffer = buffer[:-5]  # Remove <EOR>

            # Parse fields in the buffer
            fields = re.findall(r"<[^>]+>[^<]*", buffer)
            for field in fields:
                parsed = parse_adif_field(field)
                if parsed:
                    key, value = parsed
                    current_qso[key] = value
            buffer = ""

    # Handle last QSO if no trailing <EOR>
    if current_qso:
        qsos.append(current_qso)

    return qsos


def convert_adif_file(
    input_file: str, output_file: Optional[str] = None
) -> List[Dict[str, str]]:
    """Read an ADIF file and convert it to JSON. Optionally save to a file."""
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            adif_content = f.read()

        qsos = adif_to_json(adif_content)

        if output_file:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(qsos, f, indent=2)

        return qsos

    except FileNotFoundError:
        raise FileNotFoundError(f"ADIF file {input_file} not found.")
    except Exception as e:
        raise Exception(f"Error processing ADIF file: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Sample ADIF content for testing
    sample_adif = """
ADIF Export
<EOH>
<CALL:5>AB1CD<QSO_DATE:8>20230715<TIME_ON:6>143000<BAND:3>20m<MODE:3>SSB<EOR>
<CALL:5>XY2ZW<QSO_DATE:8>20230716<TIME_ON:6>091500<BAND:3>40m<MODE:2>CW<EOR>
"""
    qsos = adif_to_json(sample_adif)
    print(json.dumps(qsos, indent=2))
