# ADIF Toolkit

A Python library and web-based viewer for processing and displaying Amateur Data Interchange Format (ADIF) files, designed for ham radio QSO (contact) data management.

## Overview
ADIF Toolkit provides tools to parse ADIF files into JSON and visualize QSO data in a web-based grid. The project includes:
- A Python library (`adiflib`) for converting ADIF files to JSON, preserving the header.
- A command-line interface (`scripts/adif_cli.py`) for easy conversion.
- A web-based GUI (`gui/static/qso_grid.html`) to display QSOs in a table with autosized columns and customizable column order.

## Features
- Parse ADIF files into structured JSON, including the header and QSOs (fields like `CALL`, `QSO_DATE`, `BAND`, etc.).
- Command-line tool to convert ADIF to JSON, with interactive prompts or file arguments.
- Web-based viewer with:
  - Autosized columns based on content width.
  - Horizontal and vertical scrolling for large datasets.
  - Preferred column order (e.g., `CALL`, `QSO_DATE`, `TIME_ON`, `BAND`, `MODE` first).
  - Displays ADIF header.
- MIT License for open-source collaboration.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/adif-toolkit.git
   cd adif-toolkit
   ```
2. Install the library (editable mode):
   ```bash
   pip install -e .
   ```

## Usage
### Convert ADIF to JSON
Use the CLI script to process an ADIF file and save to a JSON file:
```bash
python scripts/adif_cli.py adiflib/tests/sample.adi output.json
```
Or run interactively:
```bash
python scripts/adif_cli.py
```
Follow prompts to enter input and output file paths.

The script outputs QSOs to the terminal and saves the full JSON (including header) to the file.

### View QSOs in Browser
1. Generate a JSON file using the CLI (e.g., `output.json`).
2. Start a local server:
   ```bash
   python -m http.server 8000
   ```
3. Open `http://localhost:8000/gui/static/qso_grid.html` in a browser and upload the JSON file to view QSOs and the header.

### Example ADIF File
See `adiflib/tests/sample.adi` for a sample:
```
ADIF Export
<ADIF_VER:5>2.2.7
<PROGRAMID:7>ADIFTool
<CREATED_TIMESTAMP:15>20250709 210900
<EOH>
<CALL:5>AB1CD<QSO_DATE:8>20230715<TIME_ON:6>143000<BAND:3>20m<MODE:3>SSB<EOR>
<CALL:5>XY2ZW<QSO_DATE:8>20230716<TIME_ON:6>091500<BAND:3>40m<MODE:2>CW<EOR>
```

### Example Python Usage
```python
from adiflib import convert_adif_file
result = convert_adif_file("adiflib/tests/sample.adi")
print(result)
```

## Project Structure
- `adiflib/`: Python library for ADIF parsing (`adif_to_json.py`).
- `gui/`: Web-based GUI (`qso_grid.html`).
- `scripts/`: CLI tools (`adif_cli.py`).
- `adiflib/tests/`: Sample ADIF files and future unit tests.
- `docs/`: Additional documentation (e.g., `usage.md`).

## Contributing
Contributions are welcome! Please open issues or pull requests on GitHub. See `docs/usage.md` for future guidelines.

## License
MIT License (see `LICENSE` file).

## Future Plans
- Add editing and saving capabilities to the web GUI.
- Integrate a backend (e.g., Flask) for direct ADIF file uploads.
- Support additional output formats (e.g., YAML).
- Add unit tests for the library.
- Implement JSON-to-ADIF conversion.