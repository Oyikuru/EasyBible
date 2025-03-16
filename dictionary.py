import csv
import sqlite3

conn = sqlite3.connect('eng_dict.db')
cursor = conn.cursor()

# with open('eng.csv',newline ='') as csvfile:
# 	#mybible = csv.reader(csvfile, delimiter ='.',quotechar='|')
# 	myrows = csv.DictReader(csvfile)
# 	for row in myrows:
# 		r = [row['word'],row["pos"],row["def"]]
# 		# print(r)
# 		cursor.execute('INSERT INTO dictionary (word,pos,def) values (?,?,?)',r)
# conn.commit()
# conn.close()

class dictionary():
	"""docstring for dictionary"""
	def __init__(self):
		super(dictionary, self).__init__()
	
	def meaning(word):
		sql = 'SELECT * from dictionary where word like ?'
		result = cursor.execute(sql, (f'{word.strip(' ,.!?~`"*&()[]{}:;')}%',)).fetchall()
		if result:
			return result
		else:
			return [('Not found!','','')]

# print(dictionary.meaning('peace'))
