from connection import get_connection

def insert_music(title,genre,year,artist_name,number_of_albums):
    connection =  get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO music(title,genre,year,artist_name,number_of_albums) VALUES (%s,%s,%s,%s,%s)"
    values = (title,genre,year,artist_name,number_of_albums)
    cursor.execute(sql,values)
    connection.commit()
    print("H mousiki prostithike")
    cursor.close()
    connection.close()

title = input("Eisagete titlo: ")
genre = input("Eisagete eidos: ")
year = int(input ("Eisagete xronia: "))
artist_name = input("Eisagete onoma kallitexnh: ")
number_of_albums =int (input("Eisagete arithmo album: "))

insert_music(title,genre,year,artist_name,number_of_albums)
