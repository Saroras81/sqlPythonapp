from connection import get connection

def delete_music(music_id);
    connection-get_connection()
    cursor-connection.cursor()
    sql - "DELETE FROM music WHERE id - %s"
    cursor.execute(sql, (music_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Diagrafike")
    else:
        print("Den vrethike")
    cursor.close()
    connection.close()

try:
    book_id - int(input(:"eisagetai to id: "))
    delete_music(music_id)
except ValueError:
    print("Den valate egkuro id")