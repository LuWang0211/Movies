import csv
from collections import Counter

def analysis(datafile):
	print "ANALYSIS FOR ", datafile

	data = list(csv.DictReader(open(datafile), delimiter='\t'))

	print "     n = ", len(data)

	print "     Q11 answers: "
	ansd = Counter([x["Q11"] for x in data])
	for i in range(0,6):
		print "          ", i, ansd[str(i)]

	print "     Q12 answers: "
	ansd = Counter([x["Q12"] for x in data])
	for i in range(0,6):
		print "          ", i, ansd[str(i)]

	dataf = list()
	for d in data:
		if d["Q2"] == '5':
			dataf.append(d)

	print "     Q1 answers (filtered for Q2=5): "
	ansd = Counter([x["Q1"] for x in dataf])
	for i in range(0,6):
		print "          ", i, ansd[str(i)]


analysis("data_amt.csv")
analysis("data_ospp.csv")
