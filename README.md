# NetFault_LLM

NetFault_LLM is a tool designed to analyze broadband network data to identify potential faults for customers based on predefined fault conditions. The analysis evaluates various network performance metrics and categorizes the severity of any issues found, providing a fault summary and resolution steps using the LLaMA model.

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

This project processes network performance data for customers, analyzing metrics such as latency, jitter, packet loss, channel quality, and the number of distant devices. It identifies issues based on specified thresholds, categorizes the severity of these issues, and generates a response with fault summaries and resolution steps.

## Key Features

- **Data Analysis:** Processes network performance data to identify issues.
- **Fault Detection:** Flags potential network faults based on predefined thresholds.
- **Severity Categorization:** Classifies the severity of issues as Normal, Moderate, or Critical.
- **Response Generation:** Uses the LLaMA model to provide a summary and resolution steps for detected faults.
- **JSON Output:** Saves the analysis results in a structured JSON file for further use.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- `ollama` tool for running the LLaMA model
- Necessary Python packages: `subprocess`, `json`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/NetFault_LLM.git
