import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

#FILE 1
df1 = pd.read_excel('C:\Users\DELL\Downloads\TESTE_UNIFICAR\ARQR_1.xlsm');
xl1 = ExcelFile('C:\Users\DELL\Downloads\TESTE_UNIFICAR\ARQR_1.xlsm');
xl1.sheet_names
sht1 = str(xl1.sheet_names[0]);
df1 = pd.read_excel('C:\Users\DELL\Downloads\TESTE_UNIFICAR\ARQR_1.xlsm', sheet_name=sht1, index_col=0);
print("Column headings:");
print(df1.columns);

#FILE 2
df2 = pd.read_excel('C:\Users\DELL\Downloads\TESTE_UNIFICAR\ARQR_2.xlsm');
xl2 = ExcelFile('C:\Users\DELL\Downloads\TESTE_UNIFICAR\ARQR_2.xlsm');
xl2.sheet_names
sht2 = str(xl2.sheet_names[0]);
df2 = pd.read_excel('C:\Users\DELL\Downloads\TESTE_UNIFICAR\ARQR_1.xlsm', sheet_name=sht2, index_col=0, columns=list(''));
print("Column headings:");
print(df2.columns);

print df1.columns == df2.columns;
sheet = sht1 if sht1 == sht2 else '';

#NEW FILE
output = df1.copy();
output = output.append(df2);
with pd.ExcelWriter('C:\Users\DELL\Downloads\TESTE_UNIFICAR\output.xlsm') as writer:
 output.to_excel(writer, sheet_name=sheet)

output = pd.read_excel('C:\Users\DELL\Downloads\TESTE_UNIFICAR\output.xlsm', sheet_namename=sheet, index_col=0);
print("Column headings:");
print(output.columns);