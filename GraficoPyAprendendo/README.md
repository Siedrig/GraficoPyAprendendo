# GraficoPyAprendendo

## Project Overview
GraficoPyAprendendo is a Python project designed to analyze survey data related to educational inequality. The project reads data from an Excel file, performs keyword analysis, and conducts sentiment analysis using various libraries. The results are visualized using interactive dashboards.

## Project Structure
```
GraficoPyAprendendo
├── src
│   └── main.py          # Main logic for data analysis and visualization
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```

## Installation

To set up the project environment, follow these steps:

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd GraficoPyAprendendo
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare your data**: Ensure that the Excel file `RespostasFormularioDesigualdade.xlsx` is in the correct format and located in the same directory as `main.py`.

2. **Run the application**:
   ```
   python src/main.py
   ```

3. **View the dashboard**: After running the application, an interactive dashboard will be generated using Plotly. Follow the instructions in the console to view the dashboard in your web browser.

## Dependencies
The project requires the following Python packages:
- pandas
- matplotlib
- plotly
- textblob
- vaderSentiment

You can find the complete list of dependencies in the `requirements.txt` file.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.