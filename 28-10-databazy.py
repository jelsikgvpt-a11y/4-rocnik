import random,sqlite3

connection = sqlite3.connect('D:/škola/Richard Zilinec/pokusna.db')
cursor = connection.cursor()
oci =  ['modra','hneda','zelena']

def create_name(dlzka:int)->str:
    temp = ''
    samo = 'aeiouy'
    spolu = 'bcdfghjklmnpqrstvwxz'
    for i in range(dlzka):
        if i % 2 == 0:
            temp += random.choice(spolu)
        else:
            temp += random.choice(samo)
    return temp.capitalize()




for i in range(1000):
    x = "INSERT INTO studenti (meno,priezvisko,vek,noha,oci) VALUES ('"+create_name(8)+"', '"+create_name(10)+"','"+str(random.randrange(18,21))+"','"+str(random.randrange(36,47))+"','"+random.choice(oci)+"');"
    cursor.execute(x)
connection.commit()
connection.close()
