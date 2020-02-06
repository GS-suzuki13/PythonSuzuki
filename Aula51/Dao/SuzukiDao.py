import MySQLdb

from PythonSuzuki.Aula51.Model.SuzukiModel import SmartphoneModel


class SmartphoneDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host='mysql.padawans.dev', database='padawans12', user='padawans12', passwd='mg2019')
        self.cursor = self.connection.cursor()

    def list_all(self):
        self.cursor.execute(f"SELECT * FROM padawans12.Suzuki")
        smartphone = self.cursor.fetchall()
        list_smartphone = []
        for phone in smartphone:
            smartphone = SmartphoneModel(phone[1],phone[2],phone[3],phone[0])
            list_smartphone.append(smartphone.__dict__)
        return list_smartphone

    def search_for_id(self, id):
        self.cursor.execute(f"SELECT * FROM padawans12.Suzuki")
        smartphone = self.cursor.fetchone()
        s = SmartphoneModel(smartphone[1],smartphone[2],smartphone[3],smartphone[0])
        return s.__dict__

    def insert(self, smartphone: SmartphoneModel):
        self.cursor.execute(f""" INSERT INTO padawans12.Suzuki
                                (
                                    Name,
                                    Model,
                                    Date
                                )
                                VALUES
                                (
                                    '{smartphone.name}',
                                    '{smartphone.model}',
                                    '{smartphone.date}'
                                )""")
        self.connection.commit()
        id = self.cursor.lastrowid
        smartphone.id = id
        return smartphone.__dict__

    def change(self, smartphone: SmartphoneModel):
        self.cursor.execute(f""" UPDATE padawans12.Suzuki
                                SET
                                    Name = '{smartphone.name}',
                                    Model ='{smartphone.model}',
                                    Date = '{smartphone.date}'
                                WHERE ID = {smartphone.id}
                                """)
        self.connection.commit()
        return smartphone.__dict__

    def delete(self, id):
        self.cursor.execute(f"DELETE FROM padawans12.Suzuki WHERE ID = {id}")
        self.connection.commit()
        return f"Smartphone With ID {id} Has Been Removed"