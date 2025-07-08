# ADIF Toolkit

A Python library and web-based viewer for processing and displaying Amateur Data Interchange Format (ADIF) files, designed for ham radio QSO (contact) data management.

## Overview
ADIF Toolkit provides tools to parse ADIF files into JSON and visualize QSO data in a web-based grid. The project includes:
- A Python library (`adiflib`) for converting ADIF files to JSON.
- A command-line interface (`scripts/adif_cli.py`) for easy conversion.
- A web-based GUI (`gui/static/qso_grid.html`) to display QSOs in a table with autosized columns and customizable column order.

## Features
- Parse ADIF files into structured JSON, handling standard fields like `CALL`, `QSO_DATE`, `BAND`, etc.
- Command-line tool to convert ADIF to JSON and output to terminal or file.
- Web-based viewer with:
  - Autosized columns based on content width.
  - Horizontal and vertical scrolling for large datasets.
  - Preferred column order (e.g., `CALL`, `QSO_DATE`, `TIME_ON`, `BAND`, `MODE` first).
- MIT License for open-source collaboration.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/baumertjohn/adif-toolkit.git
   cd adif-toolkit
   ```
2. Install the library (editable mode):
   ```bash
   pip install -e .
   ```

## Usage
### Convert ADIF to JSON
Use the CLI script to process an ADIF file and output JSON:
```bash
python scripts/adif_cli.py tests/sample.adi > output.json
```

### View QSOs in Browser
1. Generate a JSON file using the CLI (e.g., `output.json`).
2. Open `gui/static/qso_grid.html` in a web browser (e.g., via `python -m http.server 8000`).
3. Upload the JSON file to view QSOs in a table.

### Example ADIF File
See `tests/sample.adi` for a sample:
```
ADIF Export
<EOH>
<CALL:5>AB1CD<QSO_DATE:8>20230715<TIME_ON:6>143000<BAND:3>20m<MODE:3>SSB<EOR>
<CALL:5>XY2ZW<QSO_DATE:8>20230716<TIME_ON:6>091500<BAND:3>40m<MODE:2>CW<EOR>
```

## Project Structure
- `adiflib/`: Python library for ADIF parsing (`adif_to_json.py`).
- `gui/`: Web-based GUI (`qso_grid.html`).
- `scripts/`: CLI tools (`adif_cli.py`).
- `tests/`: Sample ADIF files and future unit tests.
- `docs/`: Documentation, including this README and usage details.

## Contributing
Contributions are welcome! Please open issues or pull requests on GitHub. See `docs/development.md` for guidelines (coming soon).

## License
MIT License (see `LICENSE` file).

## Future Plans
- Add editing and saving capabilities to the web GUI.
- Integrate a backend (e.g., Flask) for direct ADIF file uploads.
- Support additional output formats (e.g., YAML).
- Add unit tests for the library.