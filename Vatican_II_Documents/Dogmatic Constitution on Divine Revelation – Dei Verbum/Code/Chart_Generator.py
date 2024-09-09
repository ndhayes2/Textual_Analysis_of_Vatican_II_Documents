import re
from functions import *

data = count_references(r'C:\Users\Nikolas.Hayes\Desktop\Textual_Analysis_of_V2\Vatican_II_Documents\Dogmatic Constitution on Divine Revelation – Dei Verbum\Dei_Verbum_fulltext.txt')

chapter_number ='6'

title = '''References to Sacred Scripture\n in Dei Verbum'''
#generate_pie_chart(data, title)
generate_bar_chart(data, title)

data_to_csv(data, 'Dei Verbum')