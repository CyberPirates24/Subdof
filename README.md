# subdof

`subdof` is a Python-based tool designed to enumerate subdomains for a given domain. It utilizes multiple sources including VirusTotal, crt.sh, and HackerTarget to find and list subdomains. The results can be saved to a user-specified file.

## Features

- **VirusTotal Integration**: Retrieves subdomains from VirusTotal.
- **crt.sh Integration**: Retrieves subdomains from crt.sh.
- **HackerTarget Integration**: Retrieves subdomains from HackerTarget.
- **Interactive Interface**: User-friendly command-line interface with colorful output.
- **Save As Functionality**: Allows users to specify a filename for saving the results.

## Installation

### Prerequisites

Make sure you have Python 3 installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Required Packages

You need to install the `requests` package to run this tool. You can install it using pip:

```bash
pip install requests
```

## Usage
```sh 
python subdof.py 
```
