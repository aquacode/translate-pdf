# Translate text in PDF file

Python script that uses Google Translate to translate text in a PDF file


# Prerequisites:

**Note:** *Only used/tested with Python3*

Google Cloud SDK
* Follow instructions to download and install here: https://cloud.google.com/sdk/

Google API Client Library for Python
* Follow instructions to install here: https://developers.google.com/api-client-library/python/

pdftotext as a Python module
* Install using PIP: https://pypi.org/project/pdftotext/

# How To Use:

1. Complete the Prerequisites above
2. Acquire/generate Google API credentials and set them 
3. Execute the main.py script according to the following:

	`python3 main.py \<PDF input file\> \<target language\> \<name of output file\>`

## Expected output:

- Console (stdout) will print the translated text for each page
- The named output file will contain all the translated text with a Page number heading correlated to the page found in the PDF file


# Sample:

The `/sample` directory contains a PDF file that can be used for testing
The file has French text of an Edgar Allen Poe poem titled "The Raven"

