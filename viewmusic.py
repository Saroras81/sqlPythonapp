from connection import get_connection

def view_music():
    connection =  get_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM music"
    cursor.execute(sql)
    musics = cursor.fetchall()

    if music:
        print("Lista Mousikhs")
        for music in musics:
            print(f"Id: {music[0]},tittle:{music[1]},genre:{music[2]},year{music[3]},artist_name{music[4]},number_of_albums{music[5]}")
    else:
        print("Den uparxei mousiki")
    cursor.close()
    connection.close()

view_music()        