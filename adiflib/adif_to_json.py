import re
import json
from typing import List, Dict, Optional, Tuple

def parse_adif_field(field: str) -> Optional[Tuple[str, str]]:
    """Parse an ADIF field like <CALL:5>AB1CD into (key, value)."""
    match = re.match(r"<([A-Za-z0-9_]+):(\d+)(:[A-Za-z])?>([^<]*)", field.strip())
    if match:
        key = match.group(1).upper()
        length = int(match.group(2))
        value = match.group(4)[:length].strip()
        if value:
            return key, value
    return None

def adif_to_json(adif_content: str) -> Dict[str, any]:
    """Convert ADIF content to a JSON-compatible dictionary with header and QSOs."""
    qsos: List[Dict[str, str]] = []
    current_qso: Dict[str, str] = {}
    header: str = ""
    header_passed: bool = False
    buffer: str = ""

    for line in adif_content.replace("\r\n", "\n").splitlines():
        line = line.strip()
        if not line:
            continue

        buffer += line
        if not header_passed and buffer.upper().endswith("<EOH>"):
            header = buffer
            header_passed = True
            buffer = ""
            continue

        if header_passed:
            if buffer.upper().endswith("<EOR>"):
                # Process the entire QSO line
                fields = re.split(r"(<[^>]+>[^<]*)", buffer[:-5])  # Remove <EOR>
                fields = [f for f in fields if f and f.startswith("<")]
                for field in fields:
                    parsed = parse_adif_field(field)
                    if parsed:
                        key, value = parsed
                        current_qso[key] = value
                if current_qso:
                    qsos.append(current_qso)
                    current_qso = {}
                buffer = ""

    if not header_passed:
        raise ValueError("ADIF content missing <EOH> marker")

    return {"header": header, "qsos": qsos}

def convert_adif_file(
    input_file: str, output_file: Optional[str] = None
) -> Dict[str, any]:
    """Read an ADIF file and convert it to JSON. Optionally save to a file."""
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            adif_content = f.read()

        result = adif_to_json(adif_content)

        if output_file:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)

        return result

    except FileNotFoundError:
        raise FileNotFoundError(f"ADIF file {input_file} not found.")
    except Exception as e:
        raise Exception(f"Error processing ADIF file: {str(e)}")

if __name__ == "__main__":
    sample_adif = """
ADIF Export
<ADIF_VER:5>2.2.7
<PROGRAMID:7>ADIFTool
<CREATED_TIMESTAMP:15>20250709 210900
<EOH>
<CALL:5>AB1CD<QSO_DATE:8>20230715<TIME_ON:6>143000<BAND:3>20m<MODE:3>SSB<EOR>
<CALL:5>XY2ZW<QSO_DATE:8>20230716<TIME_ON:6>091500<BAND:3>40m<MODE:2>CW<EOR>
"""
    result = adif_to_json(sample_adif)
    print(json.dumps(result, indent=2))