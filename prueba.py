import pandas as pd
def calidad( año, nombre):
    datos= pd.read_excel('datos/datosprueba.xlsx')
    datos = datos.dropna()
    index= datos.query('nombre_rio=="{}"'.format(nombre)).index
    calidad=0


    if(index.empty):
        calidad=-1
    else:
        if(año==2009):

            if((datos.PHS09[index].values>6.5).any() ):
                calidad=calidad+7
            if(datos.PHH09[index].values>6.5 ):
                calidad=calidad+7
            if(datos.DBOS09[index].values<3):
                calidad=calidad+7
            if(datos.DBOH09[index].values<3):
                calidad=calidad+7
            if(datos.TURBS09[index].values<50):
                calidad=calidad+7
            if(datos.TURBH09[index].values<50):
                calidad=calidad+7
            if(datos.ODS09[index].values>7):
                calidad=calidad+7
            if(datos.ODH09[index].values>7):
                calidad=calidad+7
            if(datos.COLFS09[index].values<250):
                calidad=calidad+7
            if(datos.COLFH09[index].values<250):
                calidad=calidad+7
            if(datos.NO3S09[index].values<1.5):
                calidad=calidad+7
            if(datos.NO3H09[index].values<1.5):
                calidad=calidad+7
            if(datos.SOLTS09[index].values<50):
                calidad=calidad+7
            if(datos.SOLTH09[index].values<50):
                calidad=calidad+7

        if(año==2010):
            if(datos.PHS10[index].values>6.5 ):
                calidad=calidad+7
            if(datos.PHH10[index].values>6.5):
                calidad=calidad+7
            if(datos.DBOS10[index].values<3):
                calidad=calidad+7
            if(datos.DBOH10[index].values<3):
                calidad=calidad+7
            if(datos.TURBS10[index].values<50):
                calidad=calidad+7
            if(datos.TURBH10[index].values<50):
                calidad=calidad+7
            if(datos.ODS10[index].values>7):
                calidad=calidad+7
            if(datos.ODH10[index].values>7):
                calidad=calidad+7
            if(datos.COLFS10[index].values<250):
                calidad=calidad+7
            if(datos.COLFH10[index].values<250):
                calidad=calidad+7
            if(datos.NO3S10[index].values<1.5):
                calidad=calidad+7
            if(datos.NO3H10[index].values<1.5):
                calidad=calidad+7
            if(datos.SOLTS10[index].values<50):
                calidad=calidad+7
            if(datos.SOLTH10[index].values<50):
                calidad=calidad+7
        if(año==2011):
            if(datos.PHS11[index].values>6.5):
                calidad=calidad+7
            if(datos.PHH11[index].values>6.5):
                calidad=calidad+7
            if(datos.DBOS11[index].values<3):
                calidad=calidad+7
            if(datos.DBOH11[index].values<3):
                calidad=calidad+7
            if(datos.TURBS11[index].values<50):
                calidad=calidad+7
            if(datos.TURBH11[index].values<50):
                calidad=calidad+7
            if(datos.ODS11[index].values>7):
                calidad=calidad+7
            if(datos.ODH11[index].values>7):
                calidad=calidad+7
            if(datos.COLFS11[index].values<250):
                calidad=calidad+7
            if(datos.COLFH11[index].values<250):
                calidad=calidad+7
            if(datos.NO3S11[index].values<1.5):
                calidad=calidad+7
            if(datos.NO3H11[index].values<1.5):
                calidad=calidad+7
            if(datos.SOLTS11[index].values<50):
                calidad=calidad+7
            if(datos.SOLTH11[index].values<50):
                calidad=calidad+7
        if(año==2012):
            if(datos.PHS12[index].values>6.5):
                calidad=calidad+7
            if(datos.PHH12[index].values>6.5 ):
                calidad=calidad+7
            if(datos.DBOS12[index].values<3):
                calidad=calidad+7
            if(datos.DBOH12[index].values<3):
                calidad=calidad+7
            if(datos.TURBS12[index].values<50):
                calidad=calidad+7
            if(datos.TURBH12[index].values<50):
                calidad=calidad+7
            if(datos.ODS12[index].values>7):
                calidad=calidad+7
            if(datos.ODH12[index].values>7):
                calidad=calidad+7
            if(datos.COLFS12[index].values<250):
                calidad=calidad+7
            if(datos.COLFH12[index].values<250):
                calidad=calidad+7
            if(datos.NO3S12[index].values<1.5):
                calidad=calidad+7
            if(datos.NO3H12[index].values<1.5):
                calidad=calidad+7
            if(datos.SOLTS12[index].values<50):
                calidad=calidad+7
            if(datos.SOLTH12[index].values<50):
                calidad=calidad+7
                
    return calidad
