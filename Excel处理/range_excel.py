#coding=utf-8
import xlrd
import xlwt as ExcelWrite  
import xlwt 
import sys

temp_data_B = "";
temp_datas = [];
temp_data = [];
fileName = "";


def main():
	data = xlrd.open_workbook(fileName);
	tables = data.sheets();
	target_table = data.sheets()[0];
	nrows = target_table.nrows # 获取表的行数
	first_line = 1
	isHighlight = True;

	for i in range(first_line,nrows): # 循环逐行打印
		#print (target_table.row_values(i)) # 取前十三列

		data = target_table.row_values(i);

		if i == first_line:
			data.append(isHighlight);
			temp_datas.append(data);
			temp_data_B = data[1];

		elif i>first_line:	

			if data[1] != temp_data_B:
				isHighlight = not isHighlight;
				temp_data_B = data[1];

				#排序
				temp_datas.sort(key=lambda x:x[5])
				print (temp_datas)
				for j in temp_datas:
					temp_data.append(j);

				del temp_datas[:];
				data.append(isHighlight);
				temp_datas.append(data)

				print("---------------")

			else:
				data.append(isHighlight);
				temp_datas.append(data)


	writeXLS ("king排序_"+fileName);

def XLSStyle(isyellow):
	pattern = xlwt.Pattern() # Create the Pattern
	pattern.pattern = xlwt.Pattern.SOLID_PATTERN # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
	# May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
	if isyellow:
		pattern.pattern_fore_colour = 41;
	else:
		pattern.pattern_fore_colour = 1;
	style = xlwt.XFStyle() # Create the Pattern
	style.pattern = pattern # Add Pattern to Style
	return style


def writeXLS(file_name):  

    xls = ExcelWrite.Workbook(style_compression=2)  
    sheet = xls.add_sheet("Sheet1")  
 
    for i in range(0, len(temp_data)): 
        for j in range(0,len(temp_data[i])):
      	    sheet.write(i, j, temp_data[i][j],XLSStyle(temp_data[i][-1]))

       
    xls.save(file_name)  


if __name__ == '__main__':
	argv = sys.argv;
	if len(argv)>1:
		fileName = argv[-1];
		main();
	else:
		print("请输入文件名带后缀");


		
