import sqlite3

class LoadPipeline:

    def __init__(self):
        self.con = sqlite3.connect('CMC-coins-simple.db')
        self.cur = self.con.cursor()
        self.create_table
    
    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS coins(
        name TEXT PRIMARY KEY,
        symbols TEXT,
        platform TEXT,
        token_address TEXT
        );""")
        self.con.commit()

    def insert(self, item_1, item_2, item_3, item_4):
        i = 0

        while i < 100:  #CHANGED i's GOAL TO 100 FOR TESTING.
            params = (item_1[i], item_2[i], item_3[i], item_4[i])
            self.cur.execute("INSERT OR IGNORE INTO coins VALUES (?,?,?,?)", params)
            self.con.commit()
            # print("ITEM " + str(i) + " INSERTED") //PRINT IS USED TO CHECK IF THE LOOP IS WORKING AND SEE WHEN IS ABOUT TO END
            i += 1
            
    #TO CHECK IF THE PROCESS WAS DONE INSIDE DOCKER, IT PRINTS THE TABLE AT THE END        
    def get_table(self):
        self.cur.execute("SELECT * FROM coins")    
        print(self.cur.fetchall())    

