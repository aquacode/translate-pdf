# Translate text in PDF file

Python script that uses Google Translate to translate text in a PDF file


# Prerequisties:

Google Cloud SDK
* Follow instructions to download and install here: https://cloud.google.com/sdk/

Google API Client Library for Python
* Follow instructions to install here: https://developers.google.com/api-client-library/python/

pdftotext as a Python module
* Install using PIP: https://pypi.org/project/pdftotext/

Python standard libraries: 
* argparse
* time

# How To Use:

1. Complete the Prerequisites above
2. Acquire/generate Google API credentials and set them 
4. Execute the main.py script according to the following:

	python3 main.py \<PDF input file\> \<target language\> \<name of output file\>

# Sample:

A PDF file of French text of the Edgar Allen Poe poem "The Raven" is available in the /sample directory

