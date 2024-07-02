from database.DB_connect import DBConnect
from model.geni import Gene


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getGeniEssenziali():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct GeneID as gene 
        from genes_small.genes g
        where g.Essential = 'Essential' """

        cursor.execute(query, )

        for row in cursor:
            result.append(Gene(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getIterazioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select i.GeneID1 as gene1,i.GeneID2 as gene2,i.Expression_Corr as peso
        from genes_small.interactions i , genes_small.genes g, genes_small.genes g2 
        where i.GeneID1 <> i.GeneID2 and g.GeneID = i.GeneID1 and g.Essential = 'Essential' 
        and g2.GeneID = i.GeneID2 and g2.Essential  = 'Essential'"""

        cursor.execute(query, )

        for row in cursor:
            result.append([row["gene1"],row["gene2"]])

        cursor.close()
        conn.close()
        return result

