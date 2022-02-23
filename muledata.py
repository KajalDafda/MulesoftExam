# Import database for sqlite3..
import sqlite3
class connect:
    # Create constructor..
    def __init__(self):
        # Create database name
        self.con = sqlite3.connect("FavMovies.db")
        # Creating tabel movies ..
        self.con.execute('create table if not exists Movies(MoviesName text, ActorName text, ActressName text, Director text,YearOfRelease int)')
    def insert(self,MoviesName,ActorName,ActressName,Director,YearOfRelease):
    #   Insert data in movies table..
        self.con.execute('insert into Movies(MoviesName,ActorName,ActressName,Director,YearOfRelease)values(?,?,?,?,?)',(MoviesName,ActorName,ActressName,Director,YearOfRelease))
        # commit used for save data..
        self.con.commit()
       
    def display(self):
        # select all data for database table..
        data=self.con.execute('select *from Movies')
        rows=data.fetchall()
      
        for row in rows:
            print('MoviesName:',row[0])
            print('ActorName:',row[1])
            print('ActressName:',row[2])
            print('Director:',row[3])
            print('YearOfRelease:',row[4])
            print('record added')  
         
con=connect()
con.insert('Dangerous Khiladi 5','Ram Pothineni ','Tamannaah Bhatia','A. Karunakaran',2012)
con.insert('BusinessMan','Mahesh Babu ','Kajal aggarwal','Puri Jagannadh',2017)
con.display()


    
