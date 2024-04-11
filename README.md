# DzongkhaNextWord
This is my final year project where we have tried to implement Dzongkha next word prediction using Django as the web based framework

# Dzongkha NextWord

This project is designed to provide next-word predictions for Dzongkha language input.

## Installation

Follow the steps below to set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- Pip (Python package installer)
- Git
- [TensorFlow](https://www.tensorflow.org/install)
- [Tailwind CSS](https://tailwindcss.com/docs/installation)
- [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Daisy UI](https://daisyui.com/getting-started/installation)

### Clone the Repository

```bash
git clone https://github.com/Yoezer2020/DzongkhaNextWord.git
cd DzongkhaNextWord

Create and Activate Virtual Environment (Optional but Recommended)

python -m venv env
source env/bin/activate      # On Windows, use `env\Scripts\activate`

## Install Dependencies

pip install -r requirements.txt

Install Frontend Dependencies

# Install Tailwind CSS and dependencies
npm install tailwindcss postcss autoprefixer

# Build CSS
npx tailwindcss-cli@2.2.19 build -o core/static/styles.css


Run the Application

python manage.py runserver
The application will be accessible at http://127.0.0.1:8000/ in your web browser.

Usage
Open your web browser and go to http://127.0.0.1:8000/.
Enter text in the input area to get next-word predictions.

Additional Notes
Make sure to update the model and tokenizer paths in views.py with the correct paths on your machine.
Issues and Contributions
If you encounter any issues or would like to contribute, feel free to open an issue or create a pull request.

Happy coding!
