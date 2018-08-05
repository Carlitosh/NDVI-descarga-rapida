
import datetime
from funciones_descarga import download_image_sat
import ee 
import os
import zipfile
import sys
ee.Initialize()
#directorio_descarga = 'fecha/'



satelite = "COPERNICUS/S2"
src = '4326'
folder = "Archivos_descargados/"
path = "Archivos_geojson/"


#==============================================================
DATE1 = datetime.date(2018,1,1)
DATE2 = datetime.date(2018,1,30)
D1 = datetime.date.toordinal(DATE1)
D2 = (datetime.date.toordinal(DATE2))+1
dirs = os.listdir( path )
#===============================================================
# Esto va a imprimir todos los archivos del directorio
for archivo_geojson in dirs:
	for i in range(D1,D2):
		fecha_inicio = '{d.year}-{d.month}-{d.day}'.format(d=datetime.date.fromordinal(i))
		i2 = i+1 
		fecha_fin = '{d.year}-{d.month}-{d.day}'.format(d=datetime.date.fromordinal(i2))
		if not os.path.exists(str(folder+archivo_geojson)):
				os.makedirs(str(folder+archivo_geojson))
		directorio_descarga = str(folder+'/'+archivo_geojson +'/')		
		try:
			if os.path.isfile(str(archivo_geojson+'_'+fecha_inicio)) == False:
				download_image_sat(archivo_geojson,fecha_inicio,fecha_fin,directorio_descarga,src,satelite)
		except:
			pass

print "proceso terminado"
sys.exit(0)

   