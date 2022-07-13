import geoalchemy2 
from sqlalchemy import create_engine
import geopandas as gpd
import psycopg2
import pandas as pd
import dash
import folium
import plotly.express as px
import json
from folium.plugins import MiniMap
from pandas._libs import index
import branca
#import xgboost as xgb
#import jinja2
from pandas import MultiIndex, Int16Dtype
import queryspaciales as qs
import prueba as pru

def popup_html(nombre, datos, año, tipo_tiempo):
    index= datos.query('nombre_rio=="{}"'.format(nombre)).index
    rio=""
    ph1=""
    ph2=""
    temp1=""
    temp2=""
    dbo1=""
    dbo2=""
    turb1=""
    turb2=""
    od1= ""  
    od2=""                 
    fecales1 = ""
    fecales2=""
    no31=""
    no32=""
    solt1=""
    solt2=""

    if(año==2009):
        if(index.empty):
          rio=nombre
          ph1="Sin info"
          ph2="Sin info"
          temp1="Sin info"
          temp2="Sin info"
          dbo1="Sin info"
          dbo2="Sin info"
          turb1="Sin info"
          turb2="Sin info"
          od1= "Sin info"
          od2="Sin info"          
          fecales1 ="Sin info"
          fecales2="Sin info"
          no31="Sin info"
          no32="Sin info"
          solt1="Sin info"
          solt2="Sin info"

        else:
          rio=((datos.nombre_rio[index]).to_string())

          ph1=(datos.PHS09[index]).to_string()
          ph2=(datos.PHH09[index]).to_string()

          temp1=(datos.TEMS09[index]).to_string()
          temp2=(datos.TEMPH09[index]).to_string()

          dbo1=(datos.DBOS09[index]).to_string()
          dbo2=(datos.DBOH09[index]).to_string()

          turb1=(datos.TURBS09[index]).to_string()
          turb2=(datos.TURBH09[index]).to_string()

          od1= (datos.ODS09[index]).to_string()
          od2=(datos.ODH09[index]).to_string()  

          fecales1 = (datos.COLFS09[index]).to_string()
          fecales2=(datos.COLFH09[index]).to_string()

          no31=(datos.NO3S09[index]).to_string()
          no32=(datos.NO3H09[index]).to_string()

          solt1=(datos.SOLTS09[index]).to_string()
          solt2=(datos.SOLTH09[index]).to_string()

          rio=str(rio)
          rio=rio[5:]
          ph1=str(ph1)
          ph1=ph1[5:]
          ph2=str(ph2)
          ph2=ph2[5:]
          temp1=str(temp1)
          temp1=temp1[5:]
          temp1=temp1+" °C"
          temp2=str(temp2)
          temp2=temp2[5:]
          temp2=temp2+" °C"
          dbo1=str(dbo1)
          dbo1=dbo1[5:]
          dbo1=dbo1+" mg/l"
          dbo2=str(dbo2)
          dbo2=dbo2[5:]
          dbo2=dbo2+" mg/l"
          turb1=str(turb1)
          turb1=turb1[5:]
          turb1=turb1+" NTU"
          turb2=str(turb2)
          turb2=turb2[5:]
          turb2=turb2+" NTU"
          od1= str( od1)
          od1=od1[5:]
          od1=od1+" mg/l"
          od2=str(od2)
          od2=od2[5:]
          od2=od2+" mg/l"
          fecales1 = str(fecales1)
          fecales1=fecales1[5:]
          fecales1=fecales1+" UFC/100 ml"
          fecales2=str(fecales2)
          fecales2=fecales2[5:]
          fecales2=fecales2+" UFC/100 ml"
          no31=str(no31)
          no31=no31[5:]
          no31=no31+" mg/l"
          no32=str(no32)
          no32=no32[5:]
          no32=no32+" mg/l"
          solt1=str(solt1)
          solt1=solt1[5:]
          solt1=solt1+" mg/l"
          solt2=str(solt2)
          solt2=solt2[5:]
          solt2=solt2+" mg/l"
         

    if(año==2010):
        if(index.empty):
          rio=nombre
          ph1="Sin info"
          ph2="Sin info"
          temp1="Sin info"
          temp2="Sin info"
          dbo1="Sin info"
          dbo2="Sin info"
          turb1="Sin info"
          turb2="Sin info"
          od1= "Sin info"
          od2="Sin info"          
          fecales1 ="Sin info"
          fecales2="Sin info"
          no31="Sin info"
          no32="Sin info"
          solt1="Sin info"
          solt2="Sin info"
        else:
          rio=((datos.nombre_rio[index]).to_string())

          ph1=(datos.PHS10[index]).to_string()
          ph2=(datos.PHH10[index]).to_string()

          temp1=(datos.TEMS10[index]).to_string()
          temp2=(datos.TEMPH10[index]).to_string()

          dbo1=(datos.DBOS10[index]).to_string()
          dbo2=(datos.DBOH10[index]).to_string()

          turb1=(datos.TURBS10[index]).to_string()
          turb2=(datos.TURBH10[index]).to_string()

          od1= (datos.ODS10[index]).to_string()
          od2=(datos.ODH10[index]).to_string()  

          fecales1 = (datos.COLFS10[index]).to_string()
          fecales2=(datos.COLFH10[index]).to_string()

          no31=(datos.NO3S10[index]).to_string()
          no32=(datos.NO3H10[index]).to_string()

          solt1=(datos.SOLTS10[index]).to_string()
          solt2=(datos.SOLTH10[index]).to_string()
          rio=str(rio)
          rio=rio[5:]
          ph1=str(ph1)
          ph1=ph1[5:]
          ph2=str(ph2)
          ph2=ph2[5:]
          temp1=str(temp1)
          temp1=temp1[5:]
          temp1=temp1+" °C"
          temp2=str(temp2)
          temp2=temp2[5:]
          temp2=temp2+" °C"
          dbo1=str(dbo1)
          dbo1=dbo1[5:]
          dbo1=dbo1+" mg/l"
          dbo2=str(dbo2)
          dbo2=dbo2[5:]
          dbo2=dbo2+" mg/l"
          turb1=str(turb1)
          turb1=turb1[5:]
          turb1=turb1+" NTU"
          turb2=str(turb2)
          turb2=turb2[5:]
          turb2=turb2+" NTU"
          od1= str( od1)
          od1=od1[5:]
          od1=od1+" mg/l"
          od2=str(od2)
          od2=od2[5:]
          od2=od2+" mg/l"
          fecales1 = str(fecales1)
          fecales1=fecales1[5:]
          fecales1=fecales1+" UFC/100 ml"
          fecales2=str(fecales2)
          fecales2=fecales2[5:]
          fecales2=fecales2+" UFC/100 ml"
          no31=str(no31)
          no31=no31[5:]
          no31=no31+" mg/l"
          no32=str(no32)
          no32=no32[5:]
          no32=no32+" mg/l"
          solt1=str(solt1)
          solt1=solt1[5:]
          solt1=solt1+" mg/l"
          solt2=str(solt2)
          solt2=solt2[5:]
          solt2=solt2+" mg/l"

    if(año==2011):
        if(index.empty):
          rio=nombre
          ph1="Sin info"
          ph2="Sin info"
          temp1="Sin info"
          temp2="Sin info"
          dbo1="Sin info"
          dbo2="Sin info"
          turb1="Sin info"
          turb2="Sin info"
          od1= "Sin info"
          od2="Sin info"          
          fecales1 ="Sin info"
          fecales2="Sin info"
          no31="Sin info"
          no32="Sin info"
          solt1="Sin info"
          solt2="Sin info"
        else:
          rio=((datos.nombre_rio[index]).to_string())

          ph1=(datos.PHS11[index]).to_string()
          ph2=(datos.PHH11[index]).to_string()

          temp1=(datos.TEMS11[index]).to_string()
          temp2=(datos.TEMPH11[index]).to_string()

          dbo1=(datos.DBOS11[index]).to_string()
          dbo2=(datos.DBOH11[index]).to_string()

          turb1=(datos.TURBS11[index]).to_string()
          turb2=(datos.TURBH11[index]).to_string()

          od1= (datos.ODS11[index]).to_string()
          od2=(datos.ODH11[index]).to_string()  

          fecales1 = (datos.COLFS11[index]).to_string()
          fecales2=(datos.COLFH11[index]).to_string()

          no31=(datos.NO3S11[index]).to_string()
          no32=(datos.NO3H11[index]).to_string()

          solt1=(datos.SOLTS11[index]).to_string()
          solt2=(datos.SOLTH11[index]).to_string()
          rio=str(rio)
          rio=rio[5:]
          ph1=str(ph1)
          ph1=ph1[5:]
          ph2=str(ph2)
          ph2=ph2[5:]
          temp1=str(temp1)
          temp1=temp1[5:]
          temp1=temp1+" °C"
          temp2=str(temp2)
          temp2=temp2[5:]
          temp2=temp2+" °C"
          dbo1=str(dbo1)
          dbo1=dbo1[5:]
          dbo1=dbo1+" mg/l"
          dbo2=str(dbo2)
          dbo2=dbo2[5:]
          dbo2=dbo2+" mg/l"
          turb1=str(turb1)
          turb1=turb1[5:]
          turb1=turb1+" NTU"
          turb2=str(turb2)
          turb2=turb2[5:]
          turb2=turb2+" NTU"
          od1= str( od1)
          od1=od1[5:]
          od1=od1+" mg/l"
          od2=str(od2)
          od2=od2[5:]
          od2=od2+" mg/l"
          fecales1 = str(fecales1)
          fecales1=fecales1[5:]
          fecales1=fecales1+" UFC/100 ml"
          fecales2=str(fecales2)
          fecales2=fecales2[5:]
          fecales2=fecales2+" UFC/100 ml"
          no31=str(no31)
          no31=no31[5:]
          no31=no31+" mg/l"
          no32=str(no32)
          no32=no32[5:]
          no32=no32+" mg/l"
          solt1=str(solt1)
          solt1=solt1[5:]
          solt1=solt1+" mg/l"
          solt2=str(solt2)
          solt2=solt2[5:]
          solt2=solt2+" mg/l"

    if(año==2012):
        if(index.empty):
          rio=nombre
          ph1="Sin info"
          ph2="Sin info"
          temp1="Sin info"
          temp2="Sin info"
          dbo1="Sin info"
          dbo2="Sin info"
          turb1="Sin info"
          turb2="Sin info"
          od1= "Sin info"
          od2="Sin info"          
          fecales1 ="Sin info"
          fecales2="Sin info"
          no31="Sin info"
          no32="Sin info"
          solt1="Sin info"
          solt2="Sin info"
        else:
          rio=((datos.nombre_rio[index]).to_string())

          ph1=(datos.PHS10[index]).to_string()
          ph2=(datos.PHH10[index]).to_string()

          temp1=(datos.TEMS12[index]).to_string()
          temp2=(datos.TEMPH12[index]).to_string()

          dbo1=(datos.DBOS12[index]).to_string()
          dbo2=(datos.DBOH12[index]).to_string()

          turb1=(datos.TURBS12[index]).to_string()
          turb2=(datos.TURBH12[index]).to_string()

          od1= (datos.ODS12[index]).to_string()
          od2=(datos.ODH12[index]).to_string()  

          fecales1 = (datos.COLFS12[index]).to_string()
          fecales2=(datos.COLFH12[index]).to_string()

          no31=(datos.NO3S12[index]).to_string()
          no32=(datos.NO3H12[index]).to_string()

          solt1=(datos.SOLTS12[index]).to_string()
          solt2=(datos.SOLTH12[index]).to_string()
          rio=str(rio)
          rio=rio[5:]
          ph1=str(ph1)
          ph1=ph1[5:]
          ph2=str(ph2)
          ph2=ph2[5:]
          temp1=str(temp1)
          temp1=temp1[5:]
          temp1=temp1+" °C"
          temp2=str(temp2)
          temp2=temp2[5:]
          temp2=temp2+" °C"
          dbo1=str(dbo1)
          dbo1=dbo1[5:]
          dbo1=dbo1+" mg/l"
          dbo2=str(dbo2)
          dbo2=dbo2[5:]
          dbo2=dbo2+" mg/l"
          turb1=str(turb1)
          turb1=turb1[5:]
          turb1=turb1+" NTU"
          turb2=str(turb2)
          turb2=turb2[5:]
          turb2=turb2+" NTU"
          od1= str( od1)
          od1=od1[5:]
          od1=od1+" mg/l"
          od2=str(od2)
          od2=od2[5:]
          od2=od2+" mg/l"
          fecales1 = str(fecales1)
          fecales1=fecales1[5:]
          fecales1=fecales1+" UFC/100 ml"
          fecales2=str(fecales2)
          fecales2=fecales2[5:]
          fecales2=fecales2+" UFC/100 ml"
          no31=str(no31)
          no31=no31[5:]
          no31=no31+" mg/l"
          no32=str(no32)
          no32=no32[5:]
          no32=no32+" mg/l"
          solt1=str(solt1)
          solt1=solt1[5:]
          solt1=solt1+" mg/l"
          solt2=str(solt2)
          solt2=solt2[5:]
          solt2=solt2+" mg/l"




       


    left_col_color = "#19a7bd"
    right_col_color = "#f2f0d3"
    cabecera_color="#f5514e"
    
    if(tipo_tiempo=="Ambos"): #tipo tiempo es un control en el dash para indicar si se quiere temporada o  o ambas

        html = """<!DOCTYPE html>
<html>
<head>
<h4 style="margin-bottom:10"; width="200px"; id="titulo_rio">Río {}</h4>""".format(rio) + """
</head>
    <table style="height: 126px; width: 400px;">
<tbody>


<tr>
<td style="background-color: """+ cabecera_color +""";"><span style="color: #ffffff;">Estación Seca</span></td>
<td style="width: 70px;background-color: """+ cabecera_color +""";"></td>""" + """
<td style="background-color: """+ cabecera_color +""";"><span style="color: #ffffff;"> Estación Lluviosa </span></td>
<td style="width: 70px;background-color: """+ cabecera_color +""";"></td>""" + """
</tr>


<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">PH</span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(ph1) + """
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">PH </span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(ph2) + """
</tr>

<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Temp</span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(temp1) + """
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Temp </span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(temp2) + """
</tr>



<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">DBO</span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(dbo1) + """
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">DBO </span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(dbo2) + """
</tr>


<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">TURBIEDAD</span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(turb1) + """
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">TURBIEDAD </span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(turb2) + """
</tr>


<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">OD</span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(od1) + """
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">OD </span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(od2) + """
</tr>



<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">SOL. TOTALES</span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(solt1) + """
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">SOL. TOTALES </span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(solt2) + """
</tr>



<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">COL FECALES</span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(fecales1) + """
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">COL FECALES </span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(fecales2) + """
</tr>


<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">NO3</span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(no31) + """
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">NO3 </span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(no32) + """
</tr>
</tbody>
</table>
</html>
"""
    elif(tipo_tiempo=="Seca"):
        html = """<!DOCTYPE html>
<html>
<head>
<h4 style="margin-bottom:10"; width="200px"; id="titulo_rio">Río {}</h4>""".format(rio) + """
</head>
    <table style="height: 126px; width: 400px;">
<tbody>
<tr>

<tr>
<td style="background-color: """+ cabecera_color +""";"><span style="color: #ffffff;">Estación Seca</span></td>
<td style="width: 70px;background-color: """+ cabecera_color +""";"></td>""" + """
</tr>

<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">PH</span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(ph1) + """

</tr>

<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Temp</span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(temp1) + """

</tr>



<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">DBO</span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(dbo1) + """

</tr>


<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">TURBIEDAD</span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(turb1) + """
</tr>


<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">OD</span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(od1) + """
</tr>



<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">SOL. TOTALES</span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(solt1) + """



<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">COL FECALES</span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(fecales1) + """
</tr>


<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">NO3</span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(no31) + """
</tr>
</tbody>
</table>
</html>
"""
    elif(tipo_tiempo=="Lluviosa"):
        html = """<!DOCTYPE html>
<html>
<head>
<h4 style="margin-bottom:10"; width="200px"; id="titulo_rio">Río {}</h4>""".format(rio) + """

</head>
    <table style="height: 126px; width: 400px;">
<tbody>
<tr>
<tr>

<td style="background-color: """+ cabecera_color +""";"><span style="color: #ffffff;"> Estación Lluviosa </span></td>
<td style="width: 70px;background-color: """+ cabecera_color +""";"></td>""" + """
</tr>


<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">PH </span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(ph2) + """
</tr>

<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Temp </span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(temp2) + """
</tr>



<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">DBO </span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(dbo2) + """
</tr>


<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">TURBIEDAD </span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(turb2) + """
</tr>


<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">OD </span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(od2) + """
</tr>



<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">SOL. TOTALES </span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(solt2) + """
</tr>



<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">COL FECALES </span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(fecales2) + """
</tr>


<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">NO3 </span></td>
<td style="width: 70px;background-color: """+ right_col_color +""";">{}</td>""".format(no32) + """
</tr>
</tbody>
</table>
</html>
"""
    return html
def leerDatos():
    datos= pd.read_excel('datos/datosprueba.xlsx')
    return datos
def conectardatabase():

    con = create_engine("postgresql://mhadowttqmagtm:f4dc05d80d3de908a5be899a7b8573bb70e680f94fb084aa56b480ed989ccf96@ec2-34-198-186-145.compute-1.amazonaws.com:5432/d5fc7aj19ad8q7")
    return con






def mapaFolium(año, temporada):
    con = conectardatabase()
    datos = leerDatos()
    sql = """
    SELECT 
    "OBJECTID",                                                                                                         
    "SHAPE_Leng",                                                                                             
    "SHAPE_Area",                                                                                                                                                                                                                                                                                                          
    "COD_PROV",                                                                                                              
    "NOMBRE",
    ST_AsText(geometry) as geometry
        from provincias;
    """


    sql1 = """
    SELECT 
    "Cod_Cuen_H",
    "Nom_Cuen_H",
    "Nom_Rio_Pr",
    "Peri_km",
    "Area_km2",
    "SHAPE_STAr",
    "SHAPE_STLe",
    ST_AsText(geometry) as geometry
        from cuencas;
    """

    sql2 = """
    SELECT 
    "OBJECTID",
    "DrenajeTip",
    "DrenajeNom",
    "Longitud_k",
    "Label",
    "SHAPE_Leng",
    ST_AsText(geometry) as geometry
        from rios;
    """

    df_provincias=pd.read_sql(sql, con=con)
    df_cuencas=pd.read_sql(sql1, con=con)
    df_rios=pd.read_sql(sql2, con=con)


    df_cuencas['geometry'] = gpd.GeoSeries.from_wkt(df_cuencas['geometry'])
    df_cuencas = gpd.GeoDataFrame(df_cuencas, geometry='geometry')

    df_provincias['geometry'] = gpd.GeoSeries.from_wkt(df_provincias['geometry'])
    df_provincias = gpd.GeoDataFrame(df_provincias, geometry='geometry')

    df_rios['geometry'] = gpd.GeoSeries.from_wkt(df_rios['geometry'])
    df_rios = gpd.GeoDataFrame(df_rios, geometry='geometry')

    df_provincias.to_file('provincias.geojson', driver='GeoJSON')

    with open ("provincias.geojson",'r' ) as infile:
        pacitiesjson = json.load(infile)

    mapa = folium.Map(width=720,height=350, location=[8.537981, -80.782127], zoom_start=6, tiles='CartoDB positron')

    for _, r in df_provincias.iterrows():
        sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j,
                               style_function=lambda x: {'fillColor': 'white', 'color': 'black',})
        geo_j.add_to(mapa)
    for _, r in df_rios.iterrows():
        sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
        control=pru.calidad(año, r['DrenajeNom'])
        if (control>=71):
            geo_j = folium.GeoJson(data=geo_j,style_function=lambda x: {'fillColor': 'white', 'color': 'green'})   
        if (control<71 and control>0):
            geo_j = folium.GeoJson(data=geo_j,style_function=lambda x: {'fillColor': 'white', 'color': 'red'})
        if (control<0):
            geo_j = folium.GeoJson(data=geo_j,style_function=lambda x: {'fillColor': 'white', 'color': 'gray'})
        
        html = popup_html(r['DrenajeNom'], datos, año, "Ambos")
        iframe = branca.element.IFrame(html=html,width=510,height=280)
        popup = folium.Popup(folium.Html(html, script=True), max_width=500).add_to(geo_j)
        geo_j.add_to(mapa)


    miniMapa= MiniMap(tile_layer='Stamen Terrain')

    folium.TileLayer('Stamen Terrain').add_to(mapa)
    folium.TileLayer('Cartodb Positron').add_to(mapa)

    mapa.add_child(miniMapa)
    #mapa.save("assets/html/mapaprincipal.html")
    return mapa


a=mapaFolium(2009, "Ambos")
a.save("assets/html/ambos2009.html")
print("mapa 1 done")
a=mapaFolium(2010, "Ambos")
a.save("assets/html/ambos2010.html")
print("mapa 2 done")
a=mapaFolium(2011, "Ambos")
a.save("assets/html/ambos2011.html")
print("mapa 3 done")
a=mapaFolium(2012, "Ambos")
a.save("assets/html/ambos2012.html")

"""
a=mapaFolium(2009, "Lluviosa")
a.save("assets/html/Lluviosa2009.html")
a=mapaFolium(2010, "Lluviosa")
a.save("assets/html/Lluviosa2010.html")
a=mapaFolium(2011, "Lluviosa")
a.save("assets/html/Lluviosa2011.html")
a=mapaFolium(2012, "Lluviosa")
a.save("assets/html/Lluviosa2012.html")

a=mapaFolium(2009, "Seca")
a.save("assets/html/Seca2009.html")
a=mapaFolium(2010, "Seca")
a.save("assets/html/Seca2010.html")
a=mapaFolium(2011, "Seca")
a.save("assets/html/Seca2011.html")
a=mapaFolium(2012, "Seca")
a.save("assets/html/Seca2012.html")
"""
