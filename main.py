# standard libraries
import argparse
import time

# installed libraries
from google.cloud import translate
import pdftotext

argparser = argparse.ArgumentParser()
argparser.add_argument("fileinput", help="Enter the PDF file name containing the text to translate")
argparser.add_argument("target", help="Enter the target language to which the text should be translated")
argparser.add_argument("fileoutput", help="Enter the file name for the translated results")

def getListOfTextFromPdf(fileinput):
	print("getListOfTextFromPdf for file: {}".format(fileinput))
	with open(fileinput, "rb") as f:
		pagesAsListOfText = pdftotext.PDF(f)
	return pagesAsListOfText

def translateEachTextToTarget(pagesOfText, target, outputfile):
	
	print("translateEachTextToTarget language: {}".format(target))
	start = time.time()
	index = 1
	total = 0
	result_file = open(outputfile, "w")
	translator = translate.Client()
	for text in pagesOfText:
		print("Page {}".format(index))
		chars = len(text)
		total += chars
		print("Number of characters of current page: {}".format(chars))
		print("Total chars so far (before reaching 100,000): {}".format(total))
		if total >= 100000:
			end = time.time()
			elapsed = end - start
			diff = 100 - elapsed
			print("Reached 100,000 in {} seconds!".format(elapsed))
			if diff > 0:
				print("Waiting {} seconds to continue".format(diff))
				time.sleep(diff)
				start = time.time()
				total = 0
		raw_dict = translator.translate(text, target_language=target, format_="text")
		print(u"{}".format(raw_dict['translatedText']))
		print("\n\n")

		result_file.write("Page {}".format(index))
		result_file.write("\n---------\n")
		result_file.write(u"{}".format(raw_dict['translatedText']))
		result_file.write("\n\n")	

		index += 1

	result_file.close()

if __name__ == "__main__":
	args = argparser.parse_args()
	pagesOfText = getListOfTextFromPdf(args.fileinput)
	translateEachTextToTarget(pagesOfText, args.target, args.fileoutput)

