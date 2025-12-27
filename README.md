# Body Fat Calculator

This is an interactive Python Web App that calculates Body Fat %, Fat Mass (KG), and Lean Mass (KG) from user inputs such as gender, age, height, weight, and body measurements. I've created three different implementations of the same core logic in this repository.

Check out the complete articles:
1. Body Fat Calculator Version 1: [Command-Line and Interactive Notebook](https://ai.plainenglish.io/body-fat-calculator-command-line-and-interactive-notebook-aa619e3d0f42)
2. Body Fat Calculator Version 2: [Pandas and Streamlit](https://nsdsda.medium.com/body-fat-calculator-pandas-and-streamlit-a9f91391cc53)

In the first Version, I have used two methods: Command-Line and Interactive Notebook. Second version is the web app. I used the same logic to all, just the approaches are different.

## 1. **Command-Line Version (`Mass Calculator.py`)**

   * Pure Python using the built-in `math` module.
   * Takes input from the user and prints the results in a clean text format.
   * Get the Code: [Mass_Calculator.py](https://github.com/nibeditans/Body-Fat-Calculator/blob/main/Mass_Calculator.py)

## 2. **Interactive Notebook (`Mass Calculator.ipynb`)**

   * Built with **Jupyter Notebook**, and used `math`, `ipywidgets`, and `IPython.display`.
   * Provides sliders, color styling, and real-time updates for a more engaging experience.
   * Get the Code: [Mass Calculator.ipynb](https://github.com/nibeditans/Body-Fat-Calculator/blob/main/Mass%20Calculator.ipynb)

<img width="1749" height="725" alt="image" src="https://github.com/user-attachments/assets/ba99b6c2-133d-4233-92c3-6496d70d7835" />

This is just a screenshot, it's static. But you can simply download the notebook, or clone it and reuse it. Modify the program, add new features, or just play with it.😂 If you only wanna know your Body Fat Percentage, you can know that even from the `Mass Calculator.py` version. But if you wanna enhance it further and utilize your programming skills, just go ahead!😁

## 3. 🌐 **Streamlit Web App (`BFC_App.py`) — NEW**

- A clean, modern web-based version built using Streamlit.
- You don't have to install anything to use this Web App.
- You can try it directly in your browser here 👉 **[Live App](https://nibeditans-body-fat-calculator.hf.space)**

## Features

* Our Program basically calculates:
  * **Body Fat Percentage (%)**
  * **Fat Mass (kg)**
  * **Lean Mass (kg)**
* Uses the **US Navy Body Fat Formula** (gender-specific).
* Supports **Male and Female** inputs
  * Hip measurement required for Females.
* Interactive Jupyter version with sliders & live output.
  * You can also change the numbers using the sliders or simply type the number in the box, in real-time. 

## Features of the Web App:

* Calculates **Body Fat %**, **Fat Mass (kg)**, and **Lean Mass (kg)**
* Neat UI with sections and reference tables
* Works on desktop & mobile
* Super fast and interactive — powered by Streamlit


## 📂 Repository Structure

```
Body-Fat-Calculator/
│
├─ `Mass Calculator.py`      # Command-line version
├─ `Mass Calculator.ipynb`   # Jupyter Notebook interactive version
├─ `BFC_APP.py`              # Streamlit version
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


### 3️. Streamlit Web App

```bash
pip install -r requirements.txt
streamlit run BFC_App.py
```
Or simply use the **[Live App](https://nibeditans-body-fat-calculator.hf.space)**

## 🛠️ Requirements

* **Python 3.8+**
* `ipywidgets` (for the notebook)
* `IPython.display` (for interactive UI)
* `streamlit` (for the web app)
* `pandas`, `math` (built-in / standard libs)

Install notebook dependencies:

```bash
pip install -r requirements.txt
```

**(Create this file if you’d like: `ipywidgets` is the only extra package.)**


## Formula Used

I've implemented the **U.S. Navy Body Fat Formula** in this Program, which calculates both for Men and Women. You can view the formula in the code, or simply search on internet. Or, you can simply read the complete article I have written on this Program: [Body Fat Calculator: Command-Line and Interactive Notebook](https://ai.plainenglish.io/body-fat-calculator-command-line-and-interactive-notebook-aa619e3d0f42).😛 I have explained the formula step-by-step in this article.

From this:

* **Fat Mass (kg)** = (Body Fat % ÷ 100) × Weight
* **Lean Mass (kg)** = Weight – Fat Mass


## Future Enhancements

A lot of Features can be added in both the programs to enhance the UI and interactivilty. Like, 
* Adding BMI comparison and health range indicators.
* Option to export results as a PDF/CSV report.
* Visualizing body fat trends over time
* Enhancing or adding advanced features to the app using **Flask**.

If you're also lazy, leave it as is!😂


## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
