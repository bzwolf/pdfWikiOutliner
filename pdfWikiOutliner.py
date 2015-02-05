#!/usr/bin/python

import csv
import sys
import getopt
import subprocess

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'test.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			documentTitle = arg
		
	
	#inputfile+=".csv"
	outputfile=inputfile.rstrip('.csv')+'.txt'
	
	
	f = open(inputfile)
	csv_f = csv.reader(f)
	fo = open(outputfile, "w")
	lineLevel=''
	lineHeader=''
	fo.write('xxxx\n')
	fo.write("'''" + documentTitle +"'''\n")
	
	#parse csv
	for row in csv_f:
	# wanted to have markup to automatically name page but it broke pymediawiki, 
	# passing page title in -o args for now
	#
	#	if row[2]=="#C0C0C0":
	#		fo.write("'''{0}'''".format(' '.join(row[3].split())))
	#		fo.write("\n")
	#		continue
		if "Underline" in row[0]: #underline, doesn't matter what color it is. could add subheaders tho
			lineLevel='=='
			lineHeader='=='	
		elif row[2]=="#FFFF00":
			lineLevel='==='
			lineHeader='==='
		elif row[2]=="#CCFFFF":
			lineLevel='*'
			lineHeader=''
		elif row[2]=='#CCFFCC':
			lineLevel='**'
			lineHeader=''
		elif row[2]=="#FF6600":
			lineLevel='***'
			lineHeader=''
		elif row[2]=="##FFEBD7":
			lineLevel='****'
			lineHeader=''
		lineContent= ' '.join(row[3].split())
		if "Checked" in row[4]: #annotation property in bluebeam - uses Wiki bold italic format
			lineContent = "'''''{0}'''''".format(lineContent) 
		fo.write(lineLevel + ' ' + lineContent + ' ' + lineHeader + '' + '\n')
	fo.write('yyyy')
	fo.close()
	#upload to wiki
	print outputfile
	outputfile = '"{0}"'.format(outputfile)
	runCmd="pwb.py pagefromfile -notitle -file:" + outputfile + " -start:xxxx -end:yyyy" 
	print runCmd
	subprocess.call(runCmd, shell=True)
	
if __name__ == "__main__":
   main(sys.argv[1:])
   



	
