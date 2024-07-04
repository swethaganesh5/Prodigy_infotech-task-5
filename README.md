# Prodigy_infotech-task-5
# Packet Sniffer Tool

This is a simple packet sniffer tool developed using Python and Scapy. The tool captures and analyzes network packets, displaying relevant information such as source and destination IP addresses, protocols, and payload data.

## Features

- Captures network packets in real-time
- Displays source and destination IP addresses
- Identifies protocols used (e.g., TCP, UDP)
- Shows packet payload data in hexadecimal format
- Filters packets based on specific criteria (e.g., HTTP packets)

## Requirements

- Python 3.6 or higher
- Scapy library
- Npcap (for Windows users)

## Installation

### Python and Scapy

1. **Install Python:**
   - Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Scapy:**
   - Open Command Prompt or Terminal and run:
     ```bash
     pip install scapy
     ```

### Npcap (for Windows users)

1. **Download and Install Npcap:**
   - Download the latest version of Npcap from [npcap.org](https://npcap.org/).
   - Run the installer and follow the instructions to complete the installation.

## Usage

1. **Run the Packet Sniffer Script:**
   - Open Command Prompt (Windows) or Terminal (macOS/Linux).
   - Navigate to the directory where `packet_sniffer.py` is located:
     ```bash
     cd path/to/your/script
     ```
   - Run the script with administrative privileges:
     ```bash
     sudo python packet_sniffer.py  # for macOS/Linux
     python packet_sniffer.py       # for Windows (run as administrator)
     ```

2. **Output:**
   - The script will start capturing and displaying network packets, including source and destination IP addresses, protocols, and payload data.

### Example Output
Source IP: 192.168.116.108
Destination IP: 172.64.155.141
Protocol: 6
Payload: b'\x17\x03\x03\x00?z@\x18\xb1j\xf0\xe5\xfb9\xad\xf6nL\x9c\x98\xf66\xc5\xeaF\xdc\xf2\x01 :,\xf9\x8e\x1cR\x14\x1a\x97l\xdf\x08L\xf70\xa7\xd5\x11\x89\xdd$\x1b\x00\xfd!/\x9f\xec\xb7\x16\xc9\n\xd5c(\x1373p'

## Ethical Use and Educational Purposes

- Ensure you have permission to capture network traffic on any network you analyze.
- Use this tool responsibly and for educational purposes to understand network protocols, improve network security, and learn about data transmission.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests for any improvements or new features.

## Contact

For any questions or issues, please open an issue in this repository or contact the project maintainer.


