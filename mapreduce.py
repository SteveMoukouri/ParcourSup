from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from pyspark.sql.functions import col,struct,when, desc

spark = SparkSession \
    .builder \
    .appName("Read Parcoursup csv files") \
    .getOrCreate()

df = spark.read.format("csv") \
      .option("header", True) \
      .option("delimiter",";") \
      .load("fr-esr-parcoursup.csv")

#Comparaison du nombre de place disponible et de candidature pour les 5 formations les plus demandés
df.select(col("fili").alias("filiere"),col("fil_lib_voe_acc").alias("formation"),col("form_lib_voe_acc").alias("formation_c"),(col("capa_fin").alias("nb_place")).astype(IntegerType()),(col("voe_tot").alias("nb_candidat")).astype(IntegerType()))\
    .groupBy(["filiere", "Formation", "formation_c"])\
    .sum("nb_candidat", "nb_place")\
    .sort(desc("sum(nb_candidat)"))\
    .limit(5).toPandas().to_csv('nb_candidat_max.csv',sep=";")



#1/3 - 5 foramtions par filière de terminal (Général)
df.select(col("fili").alias("filiere"),col("fil_lib_voe_acc").alias("formation"),col("form_lib_voe_acc").alias("formation_c"),(col("Acc_BG").alias("admis_bg")).astype(IntegerType()))\
    .groupBy(["filiere", "Formation", "formation_c"])\
    .sum("admis_bg")\
    .sort(desc("sum(admis_bg)"))\
    .limit(5).toPandas().to_csv('choix_filiere_bg.csv',sep=";")
#2/3 - 5 foramtions par filière de terminal (techo)
df.select(col("fili").alias("filiere"),col("fil_lib_voe_acc").alias("formation"),col("form_lib_voe_acc").alias("formation_c"),(col("Acc_BT").alias("admis_bt")).astype(IntegerType()))\
    .groupBy(["filiere", "Formation", "formation_c"])\
    .sum("admis_bt")\
    .sort(desc("sum(admis_bt)"))\
    .limit(5).toPandas().to_csv('choix_filiere_bt.csv',sep=";")
#3/3 - 5 foramtions par filière de terminal (pro)
df.select(col("fili").alias("filiere"),col("fil_lib_voe_acc").alias("formation"),col("form_lib_voe_acc").alias("formation_c"),(col("Acc_BP").alias("admis_bp")).astype(IntegerType()))\
    .groupBy(["filiere", "Formation", "formation_c"])\
    .sum("admis_bp")\
    .sort(desc("sum(admis_bp)"))\
    .limit(5).toPandas().to_csv('choix_filiere_bp.csv',sep=";")