# load tsv data files->spark df
import pyspark as ps

spark = (ps.sql.SparkSession
        .builder
        .master('local[4]')
        .appName('lecture')
        .getOrCreate()
    )

sc = spark.sparkContext

def transform_to_df(path):
    return spark.read.csv(path,
                         header=True,       
                         quote='"',        
                         sep="\t",          
                         inferSchema=True)  