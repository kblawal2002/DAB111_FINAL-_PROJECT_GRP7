import pathlib
import sqlite3
import pandas as pd

# use pathlib to get current working directory
path = pathlib.Path.cwd()

def create_db(db_name, filename, table_name):
    file_path = path / filename # create a path to the data file
    
    con =  sqlite3.connect(db_name) # create a connection to the database
    cursor = con.cursor() # create a cursor

    housing = pd.read_csv(file_path)
    
    housing.to_sql(table_name, con, index=False, if_exists='replace')
    
    view_housing = cursor.execute(f"SELECT * FROM {table_name}").fetchall()
    
    print(view_housing)
    
    con.commit()
    con.close()
               
    # read in the data 
    # insert the data into the specified table 

    # execute a select statement as f-string and print results to verify insertion

    # commit the changes to the database
    # close the connection


if __name__=="__main__":
    db_name = "Nig_Housing.db"
    filename = "Nig_Housing_Data.csv"
    table_name = "housing"
    create_db(db_name, filename, table_name)
