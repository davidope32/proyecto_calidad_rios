import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import Input, Output, dcc, dash_table
from flask import Flask
import pandas as pd
from pandas import MultiIndex, Int16Dtype
#import xgboost as xgb
import plotly.express as px
#import cufflinks as cf
#from IPython.display import display, HTML
#cf.set_config_file(sharing='public', theme='solar', offline=False)
import plotly.graph_objects as go
import geopandas as gpd
import queryspaciales as qs
import prueba as pru

def graficaSearh(busqueda, rango):
    datos= pd.read_excel('datos/datosprueba.xlsx')
    index= datos.query('nombre_rio=="{}"'.format(busqueda)).index
    todo=html.P("")
    if(index.empty):
        html.H1(f"El Río {busqueda} no tiene informacion",className="text-danger" )
    else:
        if(rango[0]==9 and rango[1]==9):
            #if('PH' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["PHS09"], name="PH Seca")
                trace2= go.Bar( x=informacion["PHH09"],name="PH LLuviosa")
                ph= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='PH del Río {}'.format(busqueda))})

            #if('DBO' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["DBOS09"], name="DBO Seca")
                trace2= go.Bar( x=informacion["DBOH09"],name="DBO LLuviosa")
                dbo= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='DBO del Río {}'.format(busqueda))})


            #if('OD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["ODS09"], name="OD Seca")
                trace2= go.Bar( x=informacion["ODH09"],name="OD LLuviosa")
                od= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='OD del Río {}'.format(busqueda))})


            #if('TEMP' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["TEMS09"], name="TEMP Seca")
                trace2= go.Bar( x=informacion["TEMPH09"],name="TEMP LLuviosa")
                temp= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='TEMPERATURA del Río {}'.format(busqueda))})


            #if('TURBIEDAD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["TURBS09"], name="TURB Seca")
                trace2= go.Bar( x=informacion["TURBH09"],name="TURB LLuviosa")
                turb= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='TURBIEDAD del Río {}'.format(busqueda))})
            
            #if('COL_FECALES' in opcionesgraficas ):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["COLFS09"], name="COL FECALES Seca")
                trace2= go.Bar( x=informacion["COLFH09"],name="COL FECALES LLuviosa")
                col= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='COLIFORMES FECALES del Río {}'.format(busqueda))})
           # if('NO3' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["NO3S09"], name="NO3 Seca")
                trace2= go.Bar( x=informacion["NO3H09"],name="NO3 LLuviosa")
                no3= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='NO3 del Río {}'.format(busqueda))})
         

        if(rango[0]==10 and rango[1]==10):
            #if('PH' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["PHS10"], name="PH Seca")
                trace2= go.Bar( x=informacion["PHH10"],name="PH LLuviosa")
                ph= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='PH del Río {}'.format(busqueda))})

            #if('DBO' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["DBOS10"], name="DBO Seca")
                trace2= go.Bar( x=informacion["DBOH10"],name="DBO LLuviosa")
                dbo= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='DBO del Río {}'.format(busqueda))})


            #if('OD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["ODS10"], name="OD Seca")
                trace2= go.Bar( x=informacion["ODH10"],name="OD LLuviosa")
                od= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='OD del Río {}'.format(busqueda))})


            #if('TEMP' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["TEMS10"], name="TEMP Seca")
                trace2= go.Bar( x=informacion["TEMPH10"],name="TEMP LLuviosa")
                temp= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='TEMPERATURA del Río {}'.format(busqueda))})


            #if('TURBIEDAD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["TURBS10"], name="TURB Seca")
                trace2= go.Bar( x=informacion["TURBH10"],name="TURB LLuviosa")
                turb= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='TURBIEDAD del Río {}'.format(busqueda))})
            
            #if('COL_FECALES' in opcionesgraficas ):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["COLFS10"], name="COL FECALES Seca")
                trace2= go.Bar( x=informacion["COLFH10"],name="COL FECALES LLuviosa")
                col= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='COLIFORMES FECALES del Río {}'.format(busqueda))})
            #if('NO3' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["NO3S10"], name="NO3 Seca")
                trace2= go.Bar( x=informacion["NO3H10"],name="NO3 LLuviosa")
                no3= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='NO3 del Río {}'.format(busqueda))})
        if(rango[0]==11 and rango[1]==11):
           # if('PH' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["PHS11"], name="PH Seca")
                trace2= go.Bar( x=informacion["PHH11"],name="PH LLuviosa")
                ph= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='PH del Río {}'.format(busqueda))})

            #if('DBO' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["DBOS11"], name="DBO Seca")
                trace2= go.Bar( x=informacion["DBOH11"],name="DBO LLuviosa")
                dbo= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='DBO del Río {}'.format(busqueda))})


            #if('OD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["ODS11"], name="OD Seca")
                trace2= go.Bar( x=informacion["ODH11"],name="OD LLuviosa")
                od= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='OD del Río {}'.format(busqueda))})


            #if('TEMP' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["TEMS11"], name="TEMP Seca")
                trace2= go.Bar( x=informacion["TEMPH11"],name="TEMP LLuviosa")
                temp= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='TEMPERATURA del Río {}'.format(busqueda))})


            #if('TURBIEDAD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["TURBS11"], name="TURB Seca")
                trace2= go.Bar( x=informacion["TURBH11"],name="TURB LLuviosa")
                turb= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='TURBIEDAD del Río {}'.format(busqueda))})
            
          #  if('COL_FECALES' in opcionesgraficas ):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["COLFS11"], name="COL FECALES Seca")
                trace2= go.Bar( x=informacion["COLFH11"],name="COL FECALES LLuviosa")
                col= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='COLIFORMES FECALES del Río {}'.format(busqueda))})
            #if('NO3' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["NO3S11"], name="NO3 Seca")
                trace2= go.Bar( x=informacion["NO3H11"],name="NO3 LLuviosa")
                no3= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='NO3 del Río {}'.format(busqueda))})

        if(rango[0]==12 and rango[1]==12):
           # if('PH' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["PHS12"], name="PH Seca")
                trace2= go.Bar( x=informacion["PHH12"],name="PH LLuviosa")
                ph= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='PH del Río {}'.format(busqueda))})

            #if('DBO' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["DBOS12"], name="DBO Seca")
                trace2= go.Bar( x=informacion["DBOH12"],name="DBO LLuviosa")
                dbo= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='DBO del Río {}'.format(busqueda))})


            #if('OD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["ODS12"], name="OD Seca")
                trace2= go.Bar( x=informacion["ODH12"],name="OD LLuviosa")
                od= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='OD del Río {}'.format(busqueda))})


            #if('TEMP' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["TEMS12"], name="TEMP Seca")
                trace2= go.Bar( x=informacion["TEMPH12"],name="TEMP LLuviosa")
                temp= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='TEMPERATURA del Río {}'.format(busqueda))})


            #if('TURBIEDAD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["TURBS12"], name="TURB Seca")
                trace2= go.Bar( x=informacion["TURBH12"],name="TURB LLuviosa")
                turb= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='TURBIEDAD del Río {}'.format(busqueda))})
            
          #  if('COL_FECALES' in opcionesgraficas ):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["COLFS12"], name="COL FECALES Seca")
                trace2= go.Bar( x=informacion["COLFH12"],name="COL FECALES LLuviosa")
                col= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='COLIFORMES FECALES del Río {}'.format(busqueda))})
            #if('NO3' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["NO3S12"], name="NO3 Seca")
                trace2= go.Bar( x=informacion["NO3H12"],name="NO3 LLuviosa")
                no3= dcc.Graph(figure={'data': [trace1, trace2],'layout': go.Layout(title='NO3 del Río {}'.format(busqueda))})

        if(rango[0]==9 and rango[1]==10):
           # if('PH' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["PHS09"], name="PH Seca 2009")
                trace2= go.Bar( x=informacion["PHH09"],name="PH LLuviosa 2009")
                trace3= go.Bar(x=informacion["PHS10"], name="PH Seca 2010")
                trace4= go.Bar( x=informacion["PHH11"],name="PH LLuviosa 2010")
                ph= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4],'layout': go.Layout(title='PH del Río {}'.format(busqueda))})

            #if('DBO' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["DBOS09"], name="DBO Seca 2009")
                trace2= go.Bar( x=informacion["DBOH09"],name="DBO LLuviosa 2009")
                trace3= go.Bar(x=informacion["DBOS10"], name="DBO Seca 2010")
                trace4= go.Bar( x=informacion["DBOH10"],name="DBO LLuviosa 2010")
                dbo= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4],'layout': go.Layout(title='DBO del Río {}'.format(busqueda))})


            #if('OD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["ODS09"], name="OD Seca 2009")
                trace2= go.Bar( x=informacion["ODH09"],name="OD LLuviosa 2009")
                trace3= go.Bar(x=informacion["ODS10"], name="OD Seca 2010")
                trace4= go.Bar( x=informacion["ODH10"],name="OD LLuviosa 2010")
                od= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4],'layout': go.Layout(title='OD del Río {}'.format(busqueda))})


            #if('TEMP' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["TEMS09"], name="TEMP Seca 2009")
                trace2= go.Bar( x=informacion["TEMPH09"],name="TEMP LLuviosa 2009")
                trace3= go.Bar(x=informacion["TEMS10"], name="TEMP Seca 2010")
                trace4= go.Bar( x=informacion["TEMPH10"],name="TEMP LLuviosa 2010")
                temp= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4],'layout': go.Layout(title='TEMPERATURA del Río {}'.format(busqueda))})


            #if('TURBIEDAD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["TURBS09"], name="TURB Seca 2009")
                trace2= go.Bar( x=informacion["TURBH09"],name="TURB LLuviosa 2009")
                trace3= go.Bar(x=informacion["TURBS10"], name="TURB Seca 2010")
                trace4= go.Bar( x=informacion["TURBH10"],name="TURB LLuviosa 2010")
                turb= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4],'layout': go.Layout(title='TURBIEDAD del Río {}'.format(busqueda))})
            
          #  if('COL_FECALES' in opcionesgraficas ):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["COLFS09"], name="COL FECALES Seca 2009")
                trace2= go.Bar( x=informacion["COLFH09"],name="COL FECALES LLuviosa 2009")
                trace3= go.Bar(x=informacion["COLFS10"], name="COL FECALES Seca 2010")
                trace4= go.Bar( x=informacion["COLFH10"],name="COL FECALES LLuviosa 2010")
                col= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4],'layout': go.Layout(title='COLIFORMES FECALES del Río {}'.format(busqueda))})
            #if('NO3' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["NO3S09"], name="NO3 Seca 2009")
                trace2= go.Bar( x=informacion["NO3H09"],name="NO3 LLuviosa 2009")
                trace3= go.Bar(x=informacion["NO3S10"], name="NO3 Seca 2010")
                trace4= go.Bar( x=informacion["NO3H10"],name="NO3 LLuviosa 2010")
                no3= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4],'layout': go.Layout(title='NO3 del Río {}'.format(busqueda))})
        if(rango[0]==9 and rango[1]==11):
           # if('PH' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["PHS09"], name="PH Seca 2009")
                trace2= go.Bar( x=informacion["PHH09"],name="PH LLuviosa 2009")
                trace3= go.Bar(x=informacion["PHS10"], name="PH Seca 2010")
                trace4= go.Bar( x=informacion["PHH10"],name="PH LLuviosa 2010")
                trace5= go.Bar(x=informacion["PHS11"], name="PH Seca 2011")
                trace6= go.Bar( x=informacion["PHH11"],name="PH LLuviosa 2011")
                ph= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4,trace5, trace6],'layout': go.Layout(title='PH del Río {}'.format(busqueda))})

            #if('DBO' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["DBOS09"], name="DBO Seca 2009")
                trace2= go.Bar( x=informacion["DBOH09"],name="DBO LLuviosa 2009")
                trace3= go.Bar(x=informacion["DBOS10"], name="DBO Seca 2010")
                trace4= go.Bar( x=informacion["DBOH10"],name="DBO LLuviosa 2010")
                trace5= go.Bar(x=informacion["DBOS11"], name="DBO Seca 2011")
                trace6= go.Bar( x=informacion["DBOH11"],name="DBO LLuviosa 2011")
                dbo= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4,trace5, trace6],'layout': go.Layout(title='DBO del Río {}'.format(busqueda))})


            #if('OD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["ODS09"], name="OD Seca 2009")
                trace2= go.Bar( x=informacion["ODH09"],name="OD LLuviosa 2009")
                trace3= go.Bar(x=informacion["ODS10"], name="OD Seca 2010")
                trace4= go.Bar( x=informacion["ODH10"],name="OD LLuviosa 2010")
                trace5= go.Bar(x=informacion["ODS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["ODH11"],name="OD LLuviosa 2011")
                od= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4,trace5, trace6],'layout': go.Layout(title='OD del Río {}'.format(busqueda))})


            #if('TEMP' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["TEMS09"], name="TEMP Seca 2009")
                trace2= go.Bar( x=informacion["TEMPH09"],name="TEMP LLuviosa 2009")
                trace3= go.Bar(x=informacion["TEMS10"], name="TEMP Seca 2010")
                trace4= go.Bar( x=informacion["TEMPH10"],name="TEMP LLuviosa 2010")
                trace5= go.Bar(x=informacion["TEMS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["TEMPH11"],name="OD LLuviosa 2011")
                temp= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4,trace5, trace6],'layout': go.Layout(title='TEMPERATURA del Río {}'.format(busqueda))})


            #if('TURBIEDAD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["TURBS09"], name="TURB Seca 2009")
                trace2= go.Bar( x=informacion["TURBH09"],name="TURB LLuviosa 2009")
                trace3= go.Bar(x=informacion["TURBS10"], name="TURB Seca 2010")
                trace4= go.Bar( x=informacion["TURBH10"],name="TURB LLuviosa 2010")
                trace5= go.Bar(x=informacion["TURBS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["TURBH11"],name="OD LLuviosa 2011")
                turb= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4,trace5, trace6],'layout': go.Layout(title='TURBIEDAD del Río {}'.format(busqueda))})
            
          #  if('COL_FECALES' in opcionesgraficas ):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["COLFS09"], name="COL FECALES Seca 2009")
                trace2= go.Bar( x=informacion["COLFH09"],name="COL FECALES LLuviosa 2009")
                trace3= go.Bar(x=informacion["COLFS10"], name="COL FECALES Seca 2010")
                trace4= go.Bar( x=informacion["COLFH10"],name="COL FECALES LLuviosa 2010")
                trace5= go.Bar(x=informacion["COLFS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["COLFH11"],name="OD LLuviosa 2011")
                col= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4,trace5, trace6],'layout': go.Layout(title='COLIFORMES FECALES del Río {}'.format(busqueda))})
            #if('NO3' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["NO3S09"], name="NO3 Seca 2009")
                trace2= go.Bar( x=informacion["NO3H09"],name="NO3 LLuviosa 2009")
                trace3= go.Bar(x=informacion["NO3S10"], name="NO3 Seca 2010")
                trace4= go.Bar( x=informacion["NO3H10"],name="NO3 LLuviosa 2010")
                trace5= go.Bar(x=informacion["NO3S11"], name="NO3 Seca 2011")
                trace6= go.Bar( x=informacion["NO3H11"],name="NO3 LLuviosa 2011")
                no3= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4,trace5, trace6],'layout': go.Layout(title='NO3 del Río {}'.format(busqueda))})
        if(rango[0]==9 and rango[1]==12):
           # if('PH' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["PHS09"], name="PH Seca 2009")
                trace2= go.Bar( x=informacion["PHH09"],name="PH LLuviosa 2009")
                trace3= go.Bar(x=informacion["PHS10"], name="PH Seca 2010")
                trace4= go.Bar( x=informacion["PHH10"],name="PH LLuviosa 2010")
                trace5= go.Bar(x=informacion["PHS11"], name="PH Seca 2011")
                trace6= go.Bar( x=informacion["PHH11"],name="PH LLuviosa 2011")
                trace7= go.Bar(x=informacion["PHS12"], name="PH Seca 2012")
                trace8= go.Bar( x=informacion["PHH12"],name="PH LLuviosa 2012")
                ph= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4,trace5, trace6, trace7, trace8],'layout': go.Layout(title='PH del Río {}'.format(busqueda))})

            #if('DBO' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["DBOS09"], name="DBO Seca 2009")
                trace2= go.Bar( x=informacion["DBOH09"],name="DBO LLuviosa 2009")
                trace3= go.Bar(x=informacion["DBOS10"], name="DBO Seca 2010")
                trace4= go.Bar( x=informacion["DBOH10"],name="DBO LLuviosa 2010")
                trace5= go.Bar(x=informacion["DBOS11"], name="DBO Seca 2011")
                trace6= go.Bar( x=informacion["DBOH11"],name="DBO LLuviosa 2011")
                trace7= go.Bar(x=informacion["DBOS12"], name="DBO Seca 2012")
                trace8= go.Bar( x=informacion["DBOH12"],name="DBO LLuviosa 2012")
                dbo= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4,trace5, trace6, trace7, trace8],'layout': go.Layout(title='DBO del Río {}'.format(busqueda))})


            #if('OD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["ODS09"], name="OD Seca 2009")
                trace2= go.Bar( x=informacion["ODH09"],name="OD LLuviosa 2009")
                trace3= go.Bar(x=informacion["ODS10"], name="OD Seca 2010")
                trace4= go.Bar( x=informacion["ODH10"],name="OD LLuviosa 2010")
                trace5= go.Bar(x=informacion["ODS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["ODH11"],name="OD LLuviosa 2011")
                trace7= go.Bar(x=informacion["ODS12"], name="OD Seca 2012")
                trace8= go.Bar( x=informacion["ODH12"],name="OD LLuviosa 2012")
                od= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4,trace5, trace6, trace7, trace8],'layout': go.Layout(title='OD del Río {}'.format(busqueda))})


            #if('TEMP' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["TEMS09"], name="TEMP Seca 2009")
                trace2= go.Bar( x=informacion["TEMPH09"],name="TEMP LLuviosa 2009")
                trace3= go.Bar(x=informacion["TEMS10"], name="TEMP Seca 2010")
                trace4= go.Bar( x=informacion["TEMPH10"],name="TEMP LLuviosa 2010")
                trace5= go.Bar(x=informacion["TEMS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["TEMPH11"],name="OD LLuviosa 2011")
                trace7= go.Bar(x=informacion["TEMS12"], name="OD Seca 2012")
                trace8= go.Bar( x=informacion["TEMPH12"],name="OD LLuviosa 2012")
                temp= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4,trace5, trace6, trace7, trace8],'layout': go.Layout(title='TEMPERATURA del Río {}'.format(busqueda))})


            #if('TURBIEDAD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["TURBS09"], name="TURB Seca 2009")
                trace2= go.Bar( x=informacion["TURBH09"],name="TURB LLuviosa 2009")
                trace3= go.Bar(x=informacion["TURBS10"], name="TURB Seca 2010")
                trace4= go.Bar( x=informacion["TURBH10"],name="TURB LLuviosa 2010")
                trace5= go.Bar(x=informacion["TURBS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["TURBH11"],name="OD LLuviosa 2011")
                trace7= go.Bar(x=informacion["TURBS12"], name="OD Seca 2012")
                trace8= go.Bar( x=informacion["TURBH12"],name="OD LLuviosa 2012")
                turb= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4,trace5, trace6, trace7, trace8],'layout': go.Layout(title='TURBIEDAD del Río {}'.format(busqueda))})
            
          #  if('COL_FECALES' in opcionesgraficas ):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["COLFS09"], name="COL FECALES Seca 2009")
                trace2= go.Bar( x=informacion["COLFH09"],name="COL FECALES LLuviosa 2009")
                trace3= go.Bar(x=informacion["COLFS10"], name="COL FECALES Seca 2010")
                trace4= go.Bar( x=informacion["COLFH10"],name="COL FECALES LLuviosa 2010")
                trace5= go.Bar(x=informacion["COLFS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["COLFH11"],name="OD LLuviosa 2011")
                trace7= go.Bar(x=informacion["COLFS12"], name="OD Seca 2012")
                trace8= go.Bar( x=informacion["COLFH12"],name="OD LLuviosa 2012")
                col= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4,trace5, trace6, trace7, trace8],'layout': go.Layout(title='COLIFORMES FECALES del Río {}'.format(busqueda))})
            #if('NO3' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace1= go.Bar(x=informacion["NO3S09"], name="NO3 Seca 2009")
                trace2= go.Bar( x=informacion["NO3H09"],name="NO3 LLuviosa 2009")
                trace3= go.Bar(x=informacion["NO3S10"], name="NO3 Seca 2010")
                trace4= go.Bar( x=informacion["NO3H10"],name="NO3 LLuviosa 2010")
                trace5= go.Bar(x=informacion["NO3S11"], name="NO3 Seca 2011")
                trace6= go.Bar( x=informacion["NO3H11"],name="NO3 LLuviosa 2011")
                trace7= go.Bar(x=informacion["NO3S12"], name="NO3 Seca 2012")
                trace8= go.Bar( x=informacion["NO3H12"],name="NO3 LLuviosa 2012")
                no3= dcc.Graph(figure={'data': [trace1, trace2, trace3, trace4,trace5, trace6, trace7, trace8],'layout': go.Layout(title='NO3 del Río {}'.format(busqueda))})


        if(rango[0]==10 and rango[1]==11):
           # if('PH' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace3= go.Bar(x=informacion["PHS10"], name="PH Seca 2010")
                trace4= go.Bar( x=informacion["PHH10"],name="PH LLuviosa 2010")
                trace5= go.Bar(x=informacion["PHS11"], name="PH Seca 2011")
                trace6= go.Bar( x=informacion["PHH11"],name="PH LLuviosa 2011")

                ph= dcc.Graph(figure={'data': [trace3, trace4,trace5, trace6],'layout': go.Layout(title='PH del Río {}'.format(busqueda))})

            #if('DBO' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]

                trace3= go.Bar(x=informacion["DBOS10"], name="DBO Seca 2010")
                trace4= go.Bar( x=informacion["DBOH10"],name="DBO LLuviosa 2010")
                trace5= go.Bar(x=informacion["DBOS11"], name="DBO Seca 2011")
                trace6= go.Bar( x=informacion["DBOH11"],name="DBO LLuviosa 2011")

                dbo= dcc.Graph(figure={'data': [trace3, trace4,trace5, trace6],'layout': go.Layout(title='DBO del Río {}'.format(busqueda))})


            #if('OD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]

                trace3= go.Bar(x=informacion["ODS10"], name="OD Seca 2010")
                trace4= go.Bar( x=informacion["ODH10"],name="OD LLuviosa 2010")
                trace5= go.Bar(x=informacion["ODS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["ODH11"],name="OD LLuviosa 2011")

                od= dcc.Graph(figure={'data': [trace3, trace4,trace5, trace6],'layout': go.Layout(title='OD del Río {}'.format(busqueda))})


            #if('TEMP' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]

                trace3= go.Bar(x=informacion["TEMS10"], name="TEMP Seca 2010")
                trace4= go.Bar( x=informacion["TEMPH10"],name="TEMP LLuviosa 2010")
                trace5= go.Bar(x=informacion["TEMS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["TEMPH11"],name="OD LLuviosa 2011")

                temp= dcc.Graph(figure={'data': [trace3, trace4,trace5, trace6],'layout': go.Layout(title='TEMPERATURA del Río {}'.format(busqueda))})


            #if('TURBIEDAD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]

                trace3= go.Bar(x=informacion["TURBS10"], name="TURB Seca 2010")
                trace4= go.Bar( x=informacion["TURBH10"],name="TURB LLuviosa 2010")
                trace5= go.Bar(x=informacion["TURBS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["TURBH11"],name="OD LLuviosa 2011")

                turb= dcc.Graph(figure={'data': [trace3, trace4,trace5, trace6],'layout': go.Layout(title='TURBIEDAD del Río {}'.format(busqueda))})
            
          #  if('COL_FECALES' in opcionesgraficas ):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]

                trace3= go.Bar(x=informacion["COLFS10"], name="COL FECALES Seca 2010")
                trace4= go.Bar( x=informacion["COLFH10"],name="COL FECALES LLuviosa 2010")
                trace5= go.Bar(x=informacion["COLFS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["COLFH11"],name="OD LLuviosa 2011")

                col= dcc.Graph(figure={'data': [trace3, trace4,trace5, trace6],'layout': go.Layout(title='COLIFORMES FECALES del Río {}'.format(busqueda))})
            #if('NO3' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]

                trace3= go.Bar(x=informacion["NO3S10"], name="NO3 Seca 2010")
                trace4= go.Bar( x=informacion["NO3H10"],name="NO3 LLuviosa 2010")
                trace5= go.Bar(x=informacion["NO3S11"], name="NO3 Seca 2011")
                trace6= go.Bar( x=informacion["NO3H11"],name="NO3 LLuviosa 2011")

                no3= dcc.Graph(figure={'data': [trace3, trace4,trace5, trace6],'layout': go.Layout(title='NO3 del Río {}'.format(busqueda))})
        if(rango[0]==10 and rango[1]==12):
           # if('PH' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]
                trace3= go.Bar(x=informacion["PHS10"], name="PH Seca 2010")
                trace4= go.Bar( x=informacion["PHH10"],name="PH LLuviosa 2010")
                trace5= go.Bar(x=informacion["PHS11"], name="PH Seca 2011")
                trace6= go.Bar( x=informacion["PHH11"],name="PH LLuviosa 2011")
                trace7= go.Bar(x=informacion["PHS12"], name="PH Seca 2012")
                trace8= go.Bar( x=informacion["PHH12"],name="PH LLuviosa 2012")
                ph= dcc.Graph(figure={'data': [trace3, trace4,trace5, trace6, trace7, trace8],'layout': go.Layout(title='PH del Río {}'.format(busqueda))})

            #if('DBO' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]

                trace3= go.Bar(x=informacion["DBOS10"], name="DBO Seca 2010")
                trace4= go.Bar( x=informacion["DBOH10"],name="DBO LLuviosa 2010")
                trace5= go.Bar(x=informacion["DBOS11"], name="DBO Seca 2011")
                trace6= go.Bar( x=informacion["DBOH11"],name="DBO LLuviosa 2011")
                trace7= go.Bar(x=informacion["DBOS12"], name="DBO Seca 2012")
                trace8= go.Bar( x=informacion["DBOH12"],name="DBO LLuviosa 2012")
                dbo= dcc.Graph(figure={'data': [trace3, trace4,trace5, trace6, trace7, trace8],'layout': go.Layout(title='DBO del Río {}'.format(busqueda))})


            #if('OD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]

                trace3= go.Bar(x=informacion["ODS10"], name="OD Seca 2010")
                trace4= go.Bar( x=informacion["ODH10"],name="OD LLuviosa 2010")
                trace5= go.Bar(x=informacion["ODS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["ODH11"],name="OD LLuviosa 2011")
                trace7= go.Bar(x=informacion["ODS12"], name="OD Seca 2012")
                trace8= go.Bar( x=informacion["ODH12"],name="OD LLuviosa 2012")
                od= dcc.Graph(figure={'data': [trace3, trace4,trace5, trace6, trace7, trace8],'layout': go.Layout(title='OD del Río {}'.format(busqueda))})


            #if('TEMP' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]

                trace3= go.Bar(x=informacion["TEMS10"], name="TEMP Seca 2010")
                trace4= go.Bar( x=informacion["TEMPH10"],name="TEMP LLuviosa 2010")
                trace5= go.Bar(x=informacion["TEMS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["TEMPH11"],name="OD LLuviosa 2011")
                trace7= go.Bar(x=informacion["TEMS12"], name="OD Seca 2012")
                trace8= go.Bar( x=informacion["TEMPH12"],name="OD LLuviosa 2012")
                temp= dcc.Graph(figure={'data': [trace3, trace4,trace5, trace6, trace7, trace8],'layout': go.Layout(title='TEMPERATURA del Río {}'.format(busqueda))})


            #if('TURBIEDAD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]

                trace3= go.Bar(x=informacion["TURBS10"], name="TURB Seca 2010")
                trace4= go.Bar( x=informacion["TURBH10"],name="TURB LLuviosa 2010")
                trace5= go.Bar(x=informacion["TURBS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["TURBH11"],name="OD LLuviosa 2011")
                trace7= go.Bar(x=informacion["TURBS12"], name="OD Seca 2012")
                trace8= go.Bar( x=informacion["TURBH12"],name="OD LLuviosa 2012")
                turb= dcc.Graph(figure={'data': [trace3, trace4,trace5, trace6, trace7, trace8],'layout': go.Layout(title='TURBIEDAD del Río {}'.format(busqueda))})
            
          #  if('COL_FECALES' in opcionesgraficas ):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]

                trace3= go.Bar(x=informacion["COLFS10"], name="COL FECALES Seca 2010")
                trace4= go.Bar( x=informacion["COLFH10"],name="COL FECALES LLuviosa 2010")
                trace5= go.Bar(x=informacion["COLFS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["COLFH11"],name="OD LLuviosa 2011")
                trace7= go.Bar(x=informacion["COLFS12"], name="OD Seca 2012")
                trace8= go.Bar( x=informacion["COLFH12"],name="OD LLuviosa 2012")
                col= dcc.Graph(figure={'data': [trace3, trace4,trace5, trace6, trace7, trace8],'layout': go.Layout(title='COLIFORMES FECALES del Río {}'.format(busqueda))})
            #if('NO3' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]

                trace3= go.Bar(x=informacion["NO3S10"], name="NO3 Seca 2010")
                trace4= go.Bar( x=informacion["NO3H10"],name="NO3 LLuviosa 2010")
                trace5= go.Bar(x=informacion["NO3S11"], name="NO3 Seca 2011")
                trace6= go.Bar( x=informacion["NO3H11"],name="NO3 LLuviosa 2011")
                trace7= go.Bar(x=informacion["NO3S12"], name="NO3 Seca 2012")
                trace8= go.Bar( x=informacion["NO3H12"],name="NO3 LLuviosa 2012")
                no3= dcc.Graph(figure={'data': [trace3, trace4,trace5, trace6, trace7, trace8],'layout': go.Layout(title='NO3 del Río {}'.format(busqueda))})


        if(rango[0]==11 and rango[1]==12):
           # if('PH' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]

                trace5= go.Bar(x=informacion["PHS11"], name="PH Seca 2011")
                trace6= go.Bar( x=informacion["PHH11"],name="PH LLuviosa 2011")
                trace7= go.Bar(x=informacion["PHS12"], name="PH Seca 2012")
                trace8= go.Bar( x=informacion["PHH12"],name="PH LLuviosa 2012")
                ph= dcc.Graph(figure={'data': [trace5, trace6, trace7, trace8],'layout': go.Layout(title='PH del Río {}'.format(busqueda))})

            #if('DBO' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]


                trace5= go.Bar(x=informacion["DBOS11"], name="DBO Seca 2011")
                trace6= go.Bar( x=informacion["DBOH11"],name="DBO LLuviosa 2011")
                trace7= go.Bar(x=informacion["DBOS12"], name="DBO Seca 2012")
                trace8= go.Bar( x=informacion["DBOH12"],name="DBO LLuviosa 2012")
                dbo= dcc.Graph(figure={'data': [trace5, trace6, trace7, trace8],'layout': go.Layout(title='DBO del Río {}'.format(busqueda))})


            #if('OD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]

                trace5= go.Bar(x=informacion["ODS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["ODH11"],name="OD LLuviosa 2011")
                trace7= go.Bar(x=informacion["ODS12"], name="OD Seca 2012")
                trace8= go.Bar( x=informacion["ODH12"],name="OD LLuviosa 2012")
                od= dcc.Graph(figure={'data': [trace5, trace6, trace7, trace8],'layout': go.Layout(title='OD del Río {}'.format(busqueda))})


            #if('TEMP' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]

                trace5= go.Bar(x=informacion["TEMS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["TEMPH11"],name="OD LLuviosa 2011")
                trace7= go.Bar(x=informacion["TEMS12"], name="OD Seca 2012")
                trace8= go.Bar( x=informacion["TEMPH12"],name="OD LLuviosa 2012")
                temp= dcc.Graph(figure={'data': [trace5, trace6, trace7, trace8],'layout': go.Layout(title='TEMPERATURA del Río {}'.format(busqueda))})


            #if('TURBIEDAD' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]

                trace5= go.Bar(x=informacion["TURBS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["TURBH11"],name="OD LLuviosa 2011")
                trace7= go.Bar(x=informacion["TURBS12"], name="OD Seca 2012")
                trace8= go.Bar( x=informacion["TURBH12"],name="OD LLuviosa 2012")
                turb= dcc.Graph(figure={'data': [trace5, trace6, trace7, trace8],'layout': go.Layout(title='TURBIEDAD del Río {}'.format(busqueda))})
            
          #  if('COL_FECALES' in opcionesgraficas ):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]

                trace5= go.Bar(x=informacion["COLFS11"], name="OD Seca 2011")
                trace6= go.Bar( x=informacion["COLFH11"],name="OD LLuviosa 2011")
                trace7= go.Bar(x=informacion["COLFS12"], name="OD Seca 2012")
                trace8= go.Bar( x=informacion["COLFH12"],name="OD LLuviosa 2012")
                col= dcc.Graph(figure={'data': [trace5, trace6, trace7, trace8],'layout': go.Layout(title='COLIFORMES FECALES del Río {}'.format(busqueda))})
            #if('NO3' in opcionesgraficas):
                informacion= datos[datos.nombre_rio=="{}".format(busqueda)]

                trace5= go.Bar(x=informacion["NO3S11"], name="NO3 Seca 2011")
                trace6= go.Bar( x=informacion["NO3H11"],name="NO3 LLuviosa 2011")
                trace7= go.Bar(x=informacion["NO3S12"], name="NO3 Seca 2012")
                trace8= go.Bar( x=informacion["NO3H12"],name="NO3 LLuviosa 2012")
                no3= dcc.Graph(figure={'data': [trace5, trace6, trace7, trace8],'layout': go.Layout(title='NO3 del Río {}'.format(busqueda))})





        #fig = px.bar(informacion, x='DBOS09')
        tabla=dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
        dcc.Tab(label='PH', value='tab-1', style=tab_style, selected_style=tab_selected_style, children=[ph]),
        dcc.Tab(label='DBO', value='tab-2', style=tab_style, selected_style=tab_selected_style, children=[dbo]),
        dcc.Tab(label='OD', value='tab-3', style=tab_style, selected_style=tab_selected_style, children=[od]),
        dcc.Tab(label='TURB', value='tab-4', style=tab_style, selected_style=tab_selected_style, children=[turb]),
        dcc.Tab(label='NO3', value='tab-5', style=tab_style, selected_style=tab_selected_style, children=[no3]),
        dcc.Tab(label='COL', value='tab-6', style=tab_style, selected_style=tab_selected_style, children=[col]),
        dcc.Tab(label='TEMP', value='tab-7', style=tab_style, selected_style=tab_selected_style, children=[temp]),
    ], style=tabs_styles),
    
    return html.Content(html.Div(tabla))


def hacer_tier_list(año):
    datos= pd.read_excel('datos/datosprueba.xlsx')
    cal=[[],[]]
    for _, r in datos.iterrows():
        cal.append([r["nombre_rio"],pru.calidad(int(año), r["nombre_rio"]) ])
    cal=pd.DataFrame(cal)
    cal=cal.dropna(how='all')
    cal=cal.sort_values(1)
    cal = cal.rename(columns={0:'Río', 1:'Calidad'})
    return dash_table.DataTable(cal.to_dict('records'), [{"name": c, "id": c} for c in cal.columns],

        style_cell_conditional=[
        {
            'if': {'column_id': c},
            'textAlign': 'center'
        } for c in ['Río', 'Calidad']
    ],
    style_data={
        'color': 'black',
        'backgroundColor': 'pink'
    },
    style_table={
    'width': '350px', 
    'height': '265px',
    'overflowY': 'scroll'

    },
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(98, 159, 246)',
        }

    ],
    style_header={
        'backgroundColor': 'rgb(229, 0, 63)',
        'color': 'white',
        'fontWeight': 'bold'
    })




    

BS="assets/css/bootstrap.min"
server=Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[BS], suppress_callback_exceptions=True)


#dbc.themes.DARKLY
# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "14rem",
    "padding": "2rem 1rem",
    "color": "black",
    "background-color": "#91FF9E",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

datos= pd.read_excel('datos/datosprueba.xlsx')
#data = graficaSearh("Teribe")
#cuenca=qs.saberCuenca("Teribe")
#mapa2=qs.crearmapacuenca(cuenca)

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'color': 'black'

}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}


search_bar = dbc.Row(
    [
    
        dbc.Col(dbc.Input(id="busqueda", type="search", placeholder="Teribe", value="Teribe") , style={'width': '700px'}),
        dbc.Col(
            dbc.Button(
                "Search", color="primary", className="ms-2", id="boton_buscar",n_clicks=0
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)
sidebar = html.Div(
    [
        html.Title("calidad del agua"),
        html.Img(src='assets/img/calidad.png', width="200", height="120"), html.Hr(),
        html.P(
            "Calidad de las aguas en Panamá ", className="lead", id="titulo_pagina"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Inicio", href="/", active="exact"),
                dbc.NavLink("Limites Permisibles", href="/limper", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)



content = html.Div(id="page-content", style=CONTENT_STYLE)



app.layout = html.Div([dcc.Location(id="url"), sidebar, content])
server = app.server
app.title='Calidad del agua'

def mapainicial():

    contenido=html.Content([html.Div(
    [
        dbc.Row([
            dbc.Col(
                html.Div([
                html.H2(["Explorador de Panamá"],style={"text-align": "center"} ),
                dcc.Dropdown(['2009', '2010', '2011','2012' ],'2009', id='eleccion_mapa', style={'height': '30px', 'width': '100px', 'color': 'black' }),
                html.Iframe(id="mapapanama", width=650, height=400)]),align="start",
                width={"size":6}, style={"height": "100%"},
                # src="assets/html/ambos2009.html",

                
            ),
            
                dbc.Col(html.Div([
                html.H2("Rios y su calidad "),
                html.P(["La lista esta de Ríos de Menor calidad a los de mayor de calidad, sin embargo", html.B(" La ponderación utiliza"), html.P("no es la ideal")], style={'textAlign': 'justify'}),

                html.Div(id="tier_list")
                ]), width={"size":3, "offset": "2"})

        

        ]),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    html.Div([search_bar,
                        #dcc.Dropdown(['PH', 'DBO', 'OD','TEMP','TURBIEDAD','COL_FECALES','NO3'], 'PH',
                           # style = {"color":"black"}, multi=True, id="rango_opciones"), 
                        html.Div(id='grafica'),
                        #, figure=data
                        html.B("Años 2000 "),
                        html.Div([ dcc.RangeSlider(9, 12, 1, count=1, value=[9, 9],  tooltip={"placement": "bottom", "always_visible": True},  id="rango_años")])

                        ]),
                    width={"size": 6},
                ),

                dbc.Col(
                    html.Div([
                        html.Div(id="num_cuenca",style={'font-weight': 'bold'}),
                        html.Iframe(id="cuenca",width=505, height=260)
                        # srcDoc=mapa2._repr_html_()
                        ],),
                width={"size":2 }, style={"height": "300%"},),
            ],
       ),
    ], 
),

       


    


        ],#del content 
        ),# del content
    
    return contenido



def importanciaLimites():
    contenido=html.Content([
            html.Div([
                    html.H1("Importancia de los limites MAX-MIN Permisibles"),
                    dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
                    dcc.Tab(label='PH', value='tab-1', style=tab_style, selected_style=tab_selected_style, children=[
                        html.H1("El PH",style= {"align":"center"}),
                        html.P(""" El pH del agua indica el nivel de acidez o de alcalinidad. Si bien en este caso hablamos de un líquido en particular como el agua, el pH permite medir la actividad del potencial de iones de hidrógeno (H+).
Las mediciones de pH se ejecutan en una escala de 0 a 14. Las soluciones inferiores a 7 puntos se consideran ácidas, mientras que las que se encuentran entre 7 y 14 son alcalinas. El rango normal en agua superficial es de 6,5 a 8,5.
La escala de pH es logarítmica, por lo que cada cambio de la unidad del pH representa un cambio de diez veces en la acidez. Es decir que un pH de 6 es diez veces más ácido que uno de 7."""),
                        
                        html.Center(html.Img(src='assets/img/ph.jpg', width="400", height="400", style={'text-align': 'center'})),

                        html.Br(),html.Br(),
                        html.B("Cómo afecta el pH al agua potable"),
                        html.P("""Agencias internacionales recomiendan que el agua potable tenga un pH de entre 6.5 a 8.5. El agua dura, o el agua con un pH alto contiene una gran concentración de minerales disueltos. Aunque es sana para el cuerpo,
                         los minerales como el calcio pueden causar problemas con su posicionamiento en superficies de cerámica y por su gusto agrio. Los depósitos minerales en las bañeras y los dispositivos del hogar pueden dejar residuos en escamas. 
                         El agua suave, o con bajo pH, tiende a llevar grandes concentraciones de metales como el manganeso y hierro. Estos metales pueden ser potenciales corrosivos de los caños en las casas antiguas."""),
                        html.Br() ,

                        html.B("Importancia del pH en los arroyos y los lagos"),
                        html.P("""Mantener un pH balanceado en el agua es crítico para la vida acuática sana. Los peces y otros organismos dependen de la alta calidad del agua con la cantidad justa de oxígeno disuelto y sus nutrientes. Un alto o bajo
                         pH puede romper el balance de los químicos del agua y movilizar a los contaminantes, causando condiciones tóxicas. Los organismos acuáticos pueden experimentar problemas haciendo que las poblaciones declinen. Por esa razón, 
                         generalmente los científicos de la calidad del agua, la analizan para determinar la salud de los arroyos, los lagos, los ríos y el agua del suelo. """),
                        html.Br() ,
                        html.B("Factores que hacen variar el pH"),
                        html.P("""La polución es uno de los factores que cambia el pH natural de las aguas. El agua de lluvia con un bajo pH, llamada lluvia ácida, causa problemas ambientales que dañan a los animales, plantas y humanos. 
                            Además de la acidez causada por las precipitaciones, los contaminantes pueden entrar al agua a través de las deposiciones atmosféricas. Ahora hay muchas leyes y regulaciones ambientales que están naciendo para manejar
                             y controlar los efectos dañinos de los contaminantes del agua. """)

                        ]), 
                    dcc.Tab(label='DBO', value='tab-2', style=tab_style, selected_style=tab_selected_style, children=[
                       html.H1("la demanda bioquímica de oxígeno",style= {"align":"center"}),
                       html.P(""" Es la cantidad de oxígeno que los microorganismos, especialmente bacterias (aeróbicas o anaeróbicas), hongos y plancton, consumen durante la degradación de las sustancias orgánicas contenidas en la muestra. Se utiliza para medir el grado de contaminación."""),
                    
                       html.Center(html.Img(src='assets/img/dbo.jpg', width="400", height="400", style={'text-align': 'center'})),

                       html.Br(),html.Br(),
                       html.B("Importancia de la demanda bioquimica de oxigeno"),
                       html.P("""Es un parámetro muy útil para medirse en el agua residual ya nos ayuda a evaluar si el agua residual es una carga para el agua receptora del mismo, tambien la demanda biológica de oxígeno se usa también para conocer el nivel de contaminación del agua,
                        pero en este caso vamos a fijarnos tan sólo en componentes orgánicos. Por eso su valor será menor que el obtenido mediante la demanda química de oxígeno. """),
                       html.Br() ,

                       html.B("Algunos factores internacionales de la demanda bioquimica de oxigeno en el agua"),
                       html.P(""" Los valores de la Demanda Biológica de Oxígeno (DBO) es proporcional al nivel de contaminación que encontramos en el agua de la muestra analizada. Por ello a mayores niveles de DBO estamos ante un agua más contaminada por componentes biodegradables."""),
                       html.Br() ,
                       html.P(""" A nivel orientativo podríamos tener uno niveles como los siguientes: Agua Pura: desde 0 a 20 mg/litro, Agua Levemente Contaminada: desde 20 a 100 mg/litro, Agua Moderadamente Contaminada: desde 100 a 500 mg/litro, Agua Muy Contaminada: desde 500 a 3.000 mg/litro, Agua Extremadamente Contaminada: desde los 3.000 mg/litro"""),
                       html.Br() , 

                       html.B("Limites MAX-MIN de la demanda bioquimica de oxigeno en el decreto"),
                       html.P(""" la demanda biquimica de oxigeno tiene como  bajo riesto que debe ser de menor a 3mg/L y en riego medio debe ser entre 3mg/L y 5mg/L"""),
                        ]

                        ,),
                    dcc.Tab(label='Oxig Disuelto', value='tab-3', style=tab_style, selected_style=tab_selected_style, children=[
                        html.H1("El Oxigeno disuelto",style= {"align":"center"}),
                        html.P(""" El oxigeno disuelto (OD) es la cantidad de oxigeno gaseoso que esta disuelto en el agua. El oxigeno libre es fundamental para la vida de los peces, plantas, algas, y otros organismos; por eso, desde siempre, 
                            se ha considerado como un indicador de la capacidad de un río para mantener la vida acuática."""),

                        html.Center(html.Img(src='assets/img/od.png', width="400", height="400", style={'text-align': 'center'})),
                        
                        html.Br(),html.Br(),
                        html.B("Importancia del oxigeno disuelto en los ecosistemas acuaticos"),
                        html.P(""" El oxigeno disuelto es muy importante para los ecosistemas acuáticos, cuando su concentración es alta, es más probable que el entorno sea sano y estable, ya que permite mantener diversidad de organismos.
                                tambien el oxigeno es responsable de dos fenómenos indispensables, la respiración de los seres vivos, y la descomposición de la materia organiza cuando muere. Esta descomposición se realiza a través del oxigeno en si mismo, gracias a su capacidad oxidante y mediante bacterias y hongos que necesitan oxigeno para consumir y degradar los desechos de los seres vivos."""),
                        html.Br() , 

                        html.B(" Funcion del oxigeno disuelto en los ecosistemas acuaticos"),
                        html.P(""" La función que tiene el oxigeno dentro de los sistemas acuáticos, la respiración (el intercambio de gases que se produce en todos los seres vivos) y la descomposición de desechos (el poder oxidante que tiene el gas para estas reacciones químicas)  """),
                        html.Br() , 

                        html.B("Limites MAX-MIN del oxigeno disuleto en el decreto"),
                        html.P(""" El oxigeno disuelto bajo riesto debe ser de mayor a 7mg/L y en riego medio debe ser entre 6mg/L y 7mg/L"""),
                         
        

                        ],),
                    dcc.Tab(label='Turbiedad', value='tab-4', style=tab_style, selected_style=tab_selected_style, children=[
                        html.H1("La Turbiedad",style= {"align":"center"}),
                        html.P(""" es una medida del grado en el cual el agua pierde su transparencia debido a la presencia de partículas en suspensión. Cuantos más sólidos en suspensión haya en el agua, 
                              más sucia parecerá ésta y más alta será la turbidez. La turbidez es considerada una buena medida de la calidad del agua."""),

                        html.Center(html.Img(src='assets/img/turbiedad.jpg', width="400", height="400", style={'text-align': 'center'})),
                        
                        html.Br(),html.Br(),
                        html.B("Importancia del parametro de la turbiedad en el agua"),
                        html.P("""es uno de los parámetros más importantes en la calidad del agua de consumo humano. Un agua turbia no solamente tiene un impacto estético negativo para el consumidor, la turbidez es también un indicativo de una mayor probabilidad de contaminación microbiológica y por compuestos tóxicos, que se adhieren a la materia dispersa en el agua. Y, consecuentemente, indica también una mayor dificultad para la desinfección efectiva del agua. """),
                        html.Br() , 
                        
                        html.B(" El control de la turbidez en el agua"),
                        html.P(""" El control de la turbidez del agua está estrechamente relacionado con la eficacia de los procesos de desinfección, tanto químicos (cloro u otros biocidas) como físicos (radiaciones UV). A mayor turbiedad, mayor particulado en suspensión en el agua, lo que aumenta la posibilidad de refugio de bacterias, virus y protozoos patógenos en los microhuecos de las partículas en suspensión, y la disminución de la eficacia de los desinfectantes, al no poder contactar físicamente con el organismo diana a eliminar. """),
                        html.Br() ,
                        
                        html.B("Limites MAX-MIN de la turbidez en el decreto"),
                        html.P(""" la turbiedad de bajo riesto debe ser de menor a 50 NTU y en riego medio debe ser entre 50 NTU y 100 NTU"""),
                         

                        ],), 

                    dcc.Tab(label='Temperatura', value='tab-5', style=tab_style, selected_style=tab_selected_style, children=[ 
                        html.H1("La Temperatura",style= {"align":"center"}),
                        html.P(""" La interpretación del valor de la temperatura del agua debe realizarse relacionándola con la temperatura ambiente en el lugar y momento de la medida. Las variaciones de temperatura se deben a muchos factores: hora del día, estación, profundidad del agua y otros factores. Así por ejemplo, muchas industrias usan agua como refrigerante y la descarga descuidada de agua caliente en los ríos puede hacer que la temperatura aumente."""),
                        
                        html.Center(html.Img(src='assets/img/temperatura.png', width="400", height="400", style={'text-align': 'center'})),
                        
                        html.Br(),html.Br(),
                        html.B("Importancia de conocer la temperatura en el agua"),
                        html.P(""" La temperatura del agua está relacionada con la temperatura atmosférica, pero influyen igualmente otros factores tales como la altitud, el espesor y duración de la cubierta nival, el deshielo, etc. Se trata de una variable fundamental en el periodo vegetativo, la concentración de oxígeno disuelto en el agua, la emergencia de fases larvarias acuáticas de insectos, etc. """),
                        html.Br() ,

                        html.B("Forma de medir la temperatura en el agua"),
                        html.P(""" se mide la temperatura superficial del agua a unos 10 cm de profundidad y a la misma hora del día, los cambios de temperatura que se observan son fundamentalmente estacionales. Al analizar la evolución de la temperatura a lo largo del año observamos que los valores de temperatura fluctúan entre un valor mínimo de 3,7 ºC en enero de 2009 y un máximo de 15,3 ºC en mayo de 2008. La temperatura superficial media del agua es de 8,8 ºC. Un valor de temperatura satisfactorio, ya que es inferior a 15 ºC (temperaturas superiores a 15 ºC favorecen el desarrollo de microorganismos e intensifican los olores y sabores) y muy inferior a 25 ºC, que marca el inicio de la contaminación térmica.   """),
                        html.Br() ,

                        html.B("Limites MAX-MIN de la temperatura en el decreto"),
                        html.P(""" la temperatura bajo riesto puede ser 3°C y en riego medio es 3°C"""),
                         


                        ],), 

                    dcc.Tab(label='Solid Totales', value='tab-6', style=tab_style, selected_style=tab_selected_style, children=[ 
                        html.H1("los solidos totales",style= {"align":"center"}),
                        html.P(""" son el residuo que queda después de evaporar una muestra de agua previamente filtrada a través de un elemento de fibra de vidrio con abertura de 1.5 micras. El agua se evapora y el residuo se lleva hasta 180°C. El resultado se reporta en mg/L"""),
                        
                        html.Center(html.Img(src='assets/img/solidos.jpg', width="400", height="400", style={'text-align': 'center'})),
                        
                        html.Br(),html.Br(),
                        html.B("Conocer el parametro de los solidos totales en el agua"),
                        html.P(""" es necesario medir la cantidad del material sólido contenido en una gran cantidad de sustancias líquidas y semilíquidas que van desde agua potables hasta aguas contaminadas, aguas residuales, residuos industriales y lodos producidos en proceso de tratamiento. """),
                        html.Br() ,





                        ],),

                    dcc.Tab(label='COL. Fecales', value='tab-7', style=tab_style, selected_style=tab_selected_style, children=[
                        html.H1("La coliformes fecales",style= {"align":"center"}),
                        html.P(""" es el grupo de organismos coliformes que pueden fermentar la lactosa a 44-45 ºC. Incluyen bacterias del género Escherichia y también especies de Klebsiella, Enterobacter y Citrobacter. Aunque frecuentemente su origen es fecal, organismos que dan positivo en este método de prueba pueden provenir de aguas enriquecidas, efluentes industriales y materia vegetal y suelo en descomposición, por lo que el término coliformes fecales no es siempre acertado (la OMS recomienda el término coliformes termorresistentes)."""),
                        
                        html.Center(html.Img(src='assets/img/fecales.jpg', width="400", height="400", style={'text-align': 'center'})),
                        
                        html.Br(),html.Br(),
                        html.B("Conocer el parametro de la coliformes fecales en el agua"),
                        html.P(""" a mayoría de las bacterias del grupo de los coliformes no causan enfermedades, pero cuanto mayor sea su número, mayor será la probabilidad de que haya bacterias que causan enfermedades. Dado que las bacterias coliformes generalmente persisten en el agua más tiempo que la mayoría de los organismos que causan enfermedades, la ausencia de bacterias coliformes lleva a suponer que el suministro de agua es microbiológicamente seguro para beber. Por lo tanto, el estándar del agua potable requiere que no haya bacterias coliformes presentes en el agua potable. Las bacterias coliformes fecales y E. coli también deben estar totalmente ausentes del agua potable. """),
                        html.Br() ,

                        html.B("uso de la luz ultravioleta para detectar las coliformes fecales"),
                        html.P(""" se ha convertido en una opción popular para el tratamiento de desinfección porque no agrega ningún químico al agua. Sin embargo, las unidades de luz ultravioleta no se recomiendan para suministros de agua donde el total de bacterias coliformes supere las 1,000 colonias por 100 ml o las bacterias coliformes fecales superen las 100 colonias por 100 ml. """),
                        html.Br() ,

                        html.B("Limites MAX-MIN de las coliformes fecales en el decreto"),
                        html.P(""" Las coliformes fecales tiene como bajo riesto puede ser menor de 250 UFC/10ML y es entre el riego medio es 250 UFC/100ML y 450 UFC/100ML """),
                         

                     ] 
                        

                    ,),
                    dcc.Tab(label='NO3', value='tab-8', style=tab_style, selected_style=tab_selected_style,
                        children=[html.H1("El nitrato",style= {"align":"center"}),
                        html.P(""" es un compuesto de nitrógeno que se forma en el agua residual al convertirse el amonio en nitrato a través del nitrito (nitrificación). El nitrato es uno de los principales nutrientes de la naturaleza. El exceso de nitrato en las aguas potencia el crecimiento de las algas."""),
                        
                        html.Center(html.Img(src='assets/img/nitrato.jpg', width="400", height="400", style={'text-align': 'center'})),
                          
                        html.Br(),html.Br(),
                        html.B(" razones por la cual se forma el parametro de nitrato en el agua"),
                        html.P(""" Los nitratos pueden ser producidos tanto por fuentes naturales como antropogénicas, siendo estas últimas las responsables del importante aumento en su concentración observado en los últimos años. Así, los residuos industriales constituyen una fuente importante de nitratos en las aguas, siendo las industrias más contaminantes los mataderos, destilerías, azucareras, industrias de levadura, de almidón, textiles y fertilizantes. """),
                        html.Br() ,

                        html.B("afectaciones del nitrato en el cuerpo humano"),
                        html.P("""  El nitrito se une a las moléculas de oxígeno en los glóbulos rojos, lo que agota el oxígeno y puede asfixiar al bebé. Un síntoma obvio de la intoxicación por nitratos es el color azulado de la piel, especialmente alrededor de los ojos y la boca. Si se detecta en esta etapa temprana, la metahemoglobinemia rara vez es fatal, se diagnostica fácilmente y se revierte rápidamente con tratamiento clínico. """),
                        html.Br() ,]),


                ], style=tabs_styles),
            
            ]),

        ])

    return contenido








@app.callback(Output("page-content", "children"),
                Input("url", "pathname"))
def render_page_content(pathname):
    if pathname == "/":
        return mapainicial()
    elif pathname == "/limper":
        #mapa=cm.mapaFolium(2009, "Ambos")
        return importanciaLimites()

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Tab content 3')
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.H3('Tab content 4')
        ])

@app.callback(
    [Output('grafica',component_property='children'),Output('cuenca','srcDoc'), Output('num_cuenca',component_property='children')],
    [Input('boton_buscar','n_clicks'),
    Input('busqueda','value'),
    Input('rango_años', 'value')

    ])
def update_map(n_clicks, busqueda, rango):



    representacion=qs.crearmapacuenca(qs.saberCuenca(busqueda))
    nu_cuenca=qs.saberCuenca(busqueda)
    codigo=nu_cuenca["Cod_Cuen_H"].to_string(index=False)

    return graficaSearh(busqueda, rango), representacion._repr_html_(), "CUENCA #{}".format(codigo)


@app.callback(
 [Output('mapapanama', 'src'),
 Output('tier_list', component_property='children')],
Input('eleccion_mapa', 'value')
    )
def update_image_src(value):
    if(value=="2009"):
        return "assets/html/ambos2009.html", hacer_tier_list(2009)
    if(value=="2010"):
        return "assets/html/ambos2010.html", hacer_tier_list(2010)
    if(value=="2011"):
        return "assets/html/ambos2011.html", hacer_tier_list(2011)
    if(value=="2012"):
        return "assets/html/ambos2012.html", hacer_tier_list(2012)




if __name__ == "__main__":
    app.run_server(debug=True)



#dev_tools_ui=False,dev_tools_props_check=False
