import pandas as pd

#Localizaciones
ruta_geo = (
    r"C:\Users\formacio\Documents\PythonPBI\Datasets\GeoLite2-Country-Locations-es.csv"
)
df_locations = pd.read_csv(ruta_geo)

#ApacheBD - trafico
import sqlite3
ruta_trafic = (
    r"C:\Users\formacio\Documents\PythonPBI\Datasets\apache_logs.db"
)
conn = sqlite3.connect(ruta_trafic)
df_trafic = pd.read_sql("""
    select * from ApacheLog
    """,conn)

#Relacion trafico - geolocalizacion
ruta_trafic_geo = (
    r"C:\Users\formacio\Documents\PythonPBI\Datasets\GeoLite2-Country-Blocks-IPv4.csv"
)
columnes = ['geoname_id', 'network']
df_geoip = pd.read_csv(ruta_trafic_geo, usecols=columnes)
df_geoip = df_geoip.dropna()
df_geoip['network']=df_geoip['network'].str.split(".").str[:3].str.join(".")
df_geoip['geoname_id']=df_geoip['geoname_id'].astype(int)
df_geoip = df_geoip.drop_duplicates(subset=['network'])
df_geoip = df_geoip.reset_index(drop=True)