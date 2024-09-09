import re
import matplotlib.pyplot as plt
import seaborn
import pandas as pd

def count_references(document_path):
    with open(document_path, 'r') as file:
        document_text = file.read()
    
    keywords = [
    'Gen', 'Exod', 'Lev', 'Num', 'Deut', 'Josh', 'Judg', 'Ruth',
    '1 Sam', '2 Sam', '1 Kgs', '2 Kgs', '1 Chr', '2 Chr', 'Ezra', 'Neh',
    'Tob', 'Jdt', 'Esth', '1 Macc', '2 Macc', 'Job', 'Ps', 'Prov', 'Eccl',
    'Song', 'Wis', 'Sir', 'Isa', 'Jer', 'Lam', 'Bar', 'Ezek', 'Dan', 'Hos',
    'Joel', 'Amos', 'Obad', 'Jonah', 'Mic', 'Nah', 'Hab', 'Zeph', 'Hag',
    'Zech', 'Mal', 'Matt', 'Mark', 'Luke', 'John', 'Acts', 'Rom', '1 Cor',
    '2 Cor', 'Gal', 'Eph', 'Phil', 'Col', '1 Thess', '2 Thess', '1 Tim',
    '2 Tim', 'Titus', 'Phlm', 'Heb', 'Jas', '1 Peter', '2 Peter', '1 John',
    '2 John', '3 John', 'Jude', 'Rev'
]
    
    keyword_count = {}
    for keyword in keywords:
        # Create a pattern for each individual keyword
        pattern = r'\b' + re.escape(keyword) + r'\b'
        keyword_count[keyword] = len(re.findall(pattern, document_text))

    return keyword_count



def generate_pie_chart(data_dictionary, title):
    data = []
    keys = []
    total_citations = 0
# Iterate over both the key and value of keyword_count
    for key, value in data_dictionary.items():
        total_citations += value
        if value > 0:
            data.append(value)
            keys.append(key + ' ' + '(' + str(value) + ')')  # Add the key to the list if the value is above 0
    
    #Formatting for pie chart
    palette_color = seaborn.color_palette('dark')
    plt.pie(data, labels=keys, color=palette_color, autopct='%.0f%%', labeldistance=1.1)
    plt.title(title, pad=25, fontsize = 15, fontstyle = 'oblique')
    plt.tight_layout()
    plt.show()





def data_to_csv(data_dictionary, filename):
    df = pd.DataFrame(data=data_dictionary, index=[0])
    df.insert(0, "Document Title", filename)

    df.to_csv(filename + '.csv')




def generate_bar_chart(data_dictionary, title):
        data = []
        keys = []
        total_citations = 0
# Iterate over both the key and value of keyword_count
        for key, value in data_dictionary.items():
            total_citations += value
            if value > 0:
                data.append(value)
                keys.append(key)
        
        #Formatting for pie chart
        plt.figure(figsize=(12, 6))
        palette_color = seaborn.color_palette('dark')
        plt.bar(keys, data, color='cornflowerblue', width=0.8)
        plt.title(title)
        plt.xlabel('Book Cited (abbreviated)')
        plt.ylabel('No. of Times Cited')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()