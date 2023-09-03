# File Integrity Checker 🔒

Ensure the authenticity and integrity of your files by comparing checksums.

## Description

The File Integrity Checker generates and compares checksums for files using a variety of algorithms supported by the `hashlib` library, including MD5, SHA-256, and more. By comparing checksums, users can identify if a file's content has changed, which can be crucial for verifying the integrity of critical files or detecting potentially malicious modifications.

## Features

- **Multiple Algorithms**: Supports a range of hashing algorithms provided by `hashlib`.
- **Quick Comparison**: Easily compare the checksum of a file against a known value.

## Libraries:

This tool uses Python's built-in `hashlib` library, so no additional installations are required.

## Setup

1. Clone the repository or download the File Integrity Checker script.
2. Navigate to the project directory.

## Usage

Run the script:

```
python filechecker.py
```

Follow the on-screen prompts to provide the file path, select the hashing algorithm, and optionally compare against a known checksum.
