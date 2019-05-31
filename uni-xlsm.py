import os
import pandas as pd
import xlrd
from pandas import ExcelWriter
from pandas import ExcelFile

try:
	dir = os.fsencode(".\\<your path>");
	df = pd.DataFrame();

	for file in os.listdir(dir):
		fxls = str(os.fsdecode(dir) + '\\' + os.fsdecode(file));
		newname = fxls.replace(".XLS", ".xlsm");
		os.rename(fxls, newname);
		fxls = newname;

		fxls = xlrd.open_workbook(fxls, encoding_override="cp1252")
		sheet = str(ExcelFile(fxls).sheet_names[0]);
		
		os.system('cls');
		print("Working on this file: " + str(newname));
		exc = pd.read_excel(fxls, sheet_name=sheet);
		df = df.append(exc);

	df.to_csv('output.csv', sep=';', index = None, header=True)
	os.system('cls');
	print("output.csv was mounted");
except Exception as e:
	raise e
