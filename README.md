# Body Fat Calculator

This is an interactive Python Program that calculates Body Fat %, Fat Mass, and Lean Mass (in kg) from user inputs such as gender, age, height, weight, and body measurements.

I've created two implementations of the same core logic, to this repository.

1. **Command-Line Version (`Mass Calculator.py`)**

   * Pure Python using the built-in `math` module.
   * Takes input from the user and prints the results in a clean text format.

2. **Interactive Notebook (`Mass Calculator.ipynb`)**

   * Built with **Jupyter Notebook**, and used `math`, `ipywidgets`, and `IPython.display`.
   * Provides sliders, color styling, and real-time updates for a more engaging experience.


## Features

* Our Program basicallyt calculates:
  * **Body Fat Percentage (%)**
  * **Fat Mass (kg)**
  * **Lean Mass (kg)**
* Uses the **US Navy Body Fat Formula** (gender-specific).
* Supports **Male and Female** inputs
  * Hip measurement required for Females.
* Interactive Jupyter version with sliders & live output.
  * You can also change the numbers using the sliders or simply type the number in the box, in real-time. 


## 📂 Repository Structure

```
Body-Fat-Calculator/
│
├─ `Mass Calculator.py`      # Command-line version
├─ `Mass Calculator.ipynb`   # Jupyter Notebook interactive version
└─ README.md                 # Project documentation
```


## Quick Start

### 1️. Command-Line Script

```bash
# Clone the repository
git clone https://github.com/nibeditans/Body-Fat-Calculator.git
cd Body-Fat-Calculator

# Run the program
python "Mass Calculator.py"
```

You’ll be prompted to enter:

* Gender
* Age
* Height (cm)
* Weight (kg)
* Neck, Waist, and (if Female) Hip circumference (inch)

Results will display Body Fat %, Fat Mass (kg), and Lean Mass (kg).


### 2️. Jupyter Notebook

```bash
# Install dependencies
pip install ipywidgets
jupyter notebook
```

Open `Mass Calculator.ipynb`, run the cells, and move the sliders to see results update instantly. 


## 🛠️ Requirements

* **Python 3.8+**
* `ipywidgets` (for the notebook)
* `IPython.display` (for interactive UI)

Install notebook dependencies:

```bash
pip install -r requirements.txt
```

**(Create this file if you’d like: `ipywidgets` is the only extra package.)**


## Formula Used

I've implemented the **U.S. Navy Body Fat Formula** in this Program, which calculates both for Men and Women. You can view the formula in the code, or simply search on internet.😛

From this:

* **Fat Mass (kg)** = (Body Fat % ÷ 100) × Weight
* **Lean Mass (kg)** = Weight – Fat Mass


## Future Enhancements

A lot of Features can be added in both the programs to enhance the UI and interactivilty. You can, 
* Add BMI comparison and health range indicators.
* Option to export results as a PDF/CSV report.
* Build a simple web app using **Streamlit** or **Flask**.

If you're also lazy, leave it as is!😂


## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
