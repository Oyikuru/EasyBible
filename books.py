#import csv
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
# from PIL import Image, ImageTk
from tkinter import filedialog
import re
import os
from pathlib import Path
import shutil
import appdirs

def db_path(db):

	try:
		# Get the AppData directory path
		appdata_path = Path(os.getenv('APPDATA'))

		# Create a directory for your application
		app_dir = appdata_path / 'EasyBible'
		app_dir.mkdir(parents=True, exist_ok=True)

		try:
			shutil.copy2(db, app_dir)
			file_path = app_dir / db
		except Exception as e:
			return app_dir / db
		return app_dir/db
	except Exception as e:
		app_dir = appdirs.user_data_dir('EasyBible', 'HCC')
		path = Path(app_dir)
		shutil.copy2(db, path)
		file_path = path / db
		return file_path
		#showerror('', 'Could not get the bible data.')

def get_bible(version,ref):
	conn = sqlite3.connect(db_path(f'{version}.db'))
	cursor = conn.cursor()

	myverse = cursor.execute("SELECT* FROM "+ version +" where REF like  ? ",[ref])
	genesis = myverse.fetchall()
	conn.commit()
	for v in genesis:
		#print(v[0],v[1],v[2])
		verse_text ='['+v[1]+'] '+ v[2]
		clean = re.sub(r'<.*?>','',verse_text)
		return clean
	conn.close()


def get_bible_paraphrase(version,ref):
	conn = sqlite3.connect(db_path(f'{version}.db'))
	cursor = conn.cursor()

	myverse = cursor.execute("SELECT* FROM "+ version +" where VERSES like  ? ",[ref])
	genesis = myverse.fetchall()
	conn.commit()
	for v in genesis:
		#print(v[1],v[2])
		#verse_ref = v[1]
		verse_text ='['+v[1]+'] '+ v[2]
		clean = re.sub(r'<.*?>','',verse_text)
		yield clean
		#yield verse_ref
		

		
	conn.close()

def get_bible_ch(version,ref):
	conn = sqlite3.connect(db_path(f'{version}.db'))
	cursor = conn.cursor()

	myverse = cursor.execute("SELECT* FROM "+ version +" where REF like  ? ",[ref])
	genesis = myverse.fetchall()
	conn.commit()
	for v in genesis:
		#print(v[0],v[1],v[2])
		verse_text ='['+v[1]+'] '+ v[2]
		clean = re.sub(r'<.*?>','',verse_text)
		yield clean
	conn.close()

def get_psalms():
	conn = sqlite3.connect(db_path('kjv.db'))
	cursor = conn.cursor()

	myverse = cursor.execute("SELECT* FROM kjv where REF like ? order by RANDOM() limit 1", ('%psalm%',))
	genesis = myverse.fetchall()
	conn.commit()
	for v in genesis:
		#print(v[0],v[1],v[2])
		verse_text ='['+v[1]+'] '+ v[2]
		clean = re.sub(r'<.*?>','',verse_text)
		return clean
	conn.close()


def get_rand_verse():
	conn = sqlite3.connect(db_path('kjv.db'))
	cursor = conn.cursor()

	myverse = cursor.execute("SELECT* FROM kjv where REF like ? order by RANDOM() limit 1", ('%%',))
	genesis = myverse.fetchall()
	conn.commit()
	for v in genesis:
		#print(v[0],v[1],v[2])
		verse_text ='['+v[1]+'] '+ v[2]
		clean = re.sub(r'<.*?>','',verse_text)
		return clean
	conn.close()


#par = get_bible_paraphase('kjv','%i am the way%')
#for i in par:
	#print(i)


	


