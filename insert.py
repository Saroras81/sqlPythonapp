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

insert_music("End of the line","metal",2007,"Metallica",3)
insert_music("Come and get it","rock",1998,"Year of the ship",7                                                                         )
