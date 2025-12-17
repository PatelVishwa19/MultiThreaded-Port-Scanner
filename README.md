# Multi-Threaded Port Scanner with Banner Grabbing

This project is a Python-based network reconnaissance tool developed for educational and defensive security analysis.

## Features
- Multi-threaded TCP port scanning
- Manual service mapping for non-standard ports
- OS-based service detection fallback
- Safe banner grabbing for open ports
- Ethical usage warning
- Scan result export to file

## How It Works
1. Scans TCP ports using socket programming
2. Confirms open ports before interaction
3. Identifies services using:
   - Manual service mapping
   - OS-level service database
4. Performs banner grabbing using safe protocol-aware requests
5. Saves results to a text report

## Usage
python defence_port_scanner.py
