import pymysql
import csv


#create a connection object
try:
conn = pymysql.connect('sredatabase-1.cpzhwsaewnow.ap-south-1.rds.amazonaws.com',
        'admin','*******','mysredatabase')
		
		print("connected")
except:
    print ("I am unable to connect to the database")

#use cursor object to execute commands
cur=conn.cursor()

#using the cursor to execute sql commands

create_table="""
CREATE  TABLE IF NOT EXISTS `mysredatabase`.`flightscheduler` (
  `Airline_ID` INT,
  `Name` VARCHAR(150),
  `Alias` VARCHAR(255) ,
  `IATA` VARCHAR(255) ,
  `ICAO` VARCHAR(255) ,
  `Callsign` VARCHAR(255) ,
  `Country` VARCHAR(75) ,
  `Active` VARCHAR(255),
  )

"""
cur.execute(create_table)

print ("Table data created successfully")

with open("airlines.csv", "r") as csv_file:

   csv_data = csv.reader(csvfile, delimiter=',')
            for row in csv_data:
                insert_str = "INSERT INTO flightscheduler (Airline_ID, Name, Alias, IATA, ICAO, Callsign, Country, Active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cur.execute(insert_str, row)
cur.close()
conn.commit()
conn.close()


