import geoalchemy2 
from sqlalchemy import create_engine
import geopandas as gpd
import psycopg2
import pandas as pd
import json
#import branca
#import xgboost as xgb
from pandas import MultiIndex, Int16Dtype
import folium
from folium.plugins import MiniMap




def conectardatabase():

    con = create_engine("postgresql://mhadowttqmagtm:f4dc05d80d3de908a5be899a7b8573bb70e680f94fb084aa56b480ed989ccf96@ec2-34-198-186-145.compute-1.amazonaws.com:5432/d5fc7aj19ad8q7")
    return con


def saberCuenca(nombre):
    sql=""" SELECT "Cod_Cuen_H",
"Nom_Cuen_H",
"Nom_Rio_Pr",
"Peri_km",
"Area_km2",
"SHAPE_STAr",
"SHAPE_STLe",
ST_AsText(geometry) as geometry from cuencas

    where ST_Contains(geometry,(select geometry from rios where  "DrenajeNom"='{}' limit 1))
    """.format(nombre)

    cuenca=pd.read_sql(sql,con=conectardatabase())

    return cuenca



def crearmapacuenca(df_cuencas):
    df_cuencas['geometry'] = gpd.GeoSeries.from_wkt(df_cuencas['geometry'])
    df_cuencas = gpd.GeoDataFrame(df_cuencas, geometry='geometry')

    mapa2= folium.Map(location=[8.537981, -80.782127], zoom_start=7, tiles='Stamen Terrain',width=500, height= 250, control_scale=True)
    for _, r in df_cuencas.iterrows():
        test = folium.Html("""<b style="background-color:blue, color:white">Cuenca del {}</b>""".format(r['Nom_Cuen_H'])+"""<br> <bstyle="background-color:blue, color:white" >Rio Principal: {}</b>""".format(r['Nom_Rio_Pr']), script=True)
        iframe=folium.IFrame(html=test, width=305, height=40)
        sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j,
                               style_function=lambda x: {'fillColor': 'green', 'color': 'black',})
        popup = folium.Popup(iframe).add_to(geo_j)
        geo_j.add_to(mapa2)
    folium.TileLayer('Stamen Terrain').add_to(mapa2)
    folium.TileLayer('Cartodb Positron').add_to(mapa2)

    return mapa2
