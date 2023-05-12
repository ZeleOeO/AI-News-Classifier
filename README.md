# AI-News-Classifier

## Description

This is a web application that uses a machine learning model trained on a dataset of 40,000 news articles to classify news headlines into four categories: Sports, Crime, Science, and Business. The model was trained using the scikit-learn Python library with a naive Bayes classifier. The web app was built using Flask and deployed on Heroku. The frontend design was contributed by @pineapplegoose.

## Usage

To use the application, simply enter a news headline into the text field and click the "Classify" button. The application will then predict which category the headline belongs to and display the result.


## Installation

To run the application locally, you can follow these steps:

1. Clone the repository: `git clone https://github.com/ZeleOeO/AI-News-Classifier.git`
2. Navigate to the project directory: `cd AI-News-Classifier`
3. Install the required Python packages: `pip install -r requirements.txt`
4. Run the app: `python app.py`


## Issues

The application is currently not optimized for phone screens and may not display properly on smaller devices. Additionally, if no text is entered into the text field, the model will predict the empty line as "BUSINESS NEWS".

## Credits

- Frontend design by [@pineapplegoose](https://github.com/pineapplegoose)
- Machine learning model trained using scikit-learn
- Web app built using Flask and deployed on Heroku
