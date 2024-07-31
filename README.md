# Weight Gauge Application

This is a PyQt5-based application that displays a weight gauge with a semicircular progress bar. The gauge updates every second with a random weight value, and the application starts in full-screen mode. The background of the application is set to a light cyan color. Pressing any key will exit the application.

## Features

- Semicircular gauge that changes color based on the weight value.
  - Green: weight < 33
  - Yellow: 33 ≤ weight < 66
  - Red: weight ≥ 66
- Full-screen mode on startup.
- Light cyan background color.
- Random weight updates every second.
- Exit the application by pressing any key.

## Requirements

- Python 3.x
- PyQt5

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/karthickrajathedeveloper/weight-gauge-app.git
    ```
2. Navigate to the project directory:
    ```bash
    cd weight-gauge-app
    ```
3. Install the required packages:
    ```bash
    pip install PyQt5
    ```

## Usage

Run the `main.py` file to start the application:
```bash
python main.py
```
The application will start in full-screen mode and display a semicircular gauge. The gauge will update every second with a random weight value. Press any key to exit the application.

## Code Overview
- **main.py**:           Main script that runs the application.
- **SemicircleGauge**: A custom QWidget that draws the semicircular gauge.
- **WeightGauge**:     Main window that contains the gauge and a label showing the weight.

## SemicircleGauge Class
This class is responsible for drawing the semicircular gauge. It overrides the paintEvent method to draw the background semicircle, the progress arc, and the weight text.

## WeightGauge Class
This class creates the main window, which includes the SemicircleGauge and a label. It also sets the application to full-screen mode and handles updating the weight every second. The keyPressEvent method is overridden to exit the application when any key is pressed.

## Author 
[karthickrajathedeveloper](https://github.com/karthickrajathedeveloper)

## License
This project is licensed under the MIT License.



