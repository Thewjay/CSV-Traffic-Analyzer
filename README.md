# TrafficAnalyzer

TrafficAnalyzer is a Python-based program designed to analyze traffic data from CSV files and provide valuable insights to assist in traffic management. 

## Features
- Input validation for accurate date selection.
- Analyze traffic data to calculate:
  - Total vehicle counts.
  - Speed violations.
  - Peak traffic hours.
  - Percentage of vehicle types (e.g., trucks, scooters).
- Generate histograms to visualize hourly traffic volumes using `tkinter`.
- Save analysis results to a text file for future reference.
- Supports processing multiple datasets in a single session.

## Usage
1. Select a CSV file by providing the date in DD MM YYYY format.
2. View results directly in the console or as a histogram.
3. Save results to a text file for future use.
4. Optionally, analyze additional datasets in a single run.

## Requirements
- Python 3.12
- `tkinter` module
- CSV files containing traffic data

## How to Run
1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/TrafficAnalyzer.git
2. Open the python file using IDLE python (Or download at https://www.python.org/downloads/)
3. Locate `with open` syntax and change the file path to the location of the clone folder. (replace `\` with `\\` in the path)
4. Double click the `TrafficAnalyzer.py` file to open with cmd or open IDLE and locate the file to run 
