# NetFault_LLM

NetFault_LLM analyzes broadband network data to identify potential faults and summarize issues.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Output](#output)
- [Dependencies](#dependencies)
- [License](#license)
- [Contributing](#contributing)

## Overview

This project processes network performance data for customers, analyzing metrics such as latency,
jitter, packet loss, channel quality, and the number of distant devices. It identifies issues based
on specified thresholds, categorizes their severity, and generates a text summary of findings.

## Key Features

- **Data Analysis:** Processes network performance data to identify issues.
- **Fault Detection:** Flags potential network faults based on predefined thresholds.
- **Severity Categorization:** Classifies the severity of issues as Normal, Moderate, or Critical.
- **Response Generation:** Produces a plain‑text summary for detected faults.
- **JSON Output:** Saves the analysis results in a structured JSON file for further use.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- `pip` package manager

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/noorcs39/NetFault_LLM.git
   cd NetFault_LLM
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

Analyze the sample dataset and write results to `responses.json`:

```bash
python main.py --input input.csv --output responses.json
```

## Output

Running the script prints a human‑readable summary and writes a JSON file containing the detailed
results and summary text.

## Dependencies

See [`requirements.txt`](requirements.txt) for the complete list of Python dependencies.

## License

MIT

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
