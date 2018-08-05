
import datetime
import urllib
import geojson
import ee 
import os 
ee.Initialize()


#archivo_geojson = str("lote6.geojson")
#fecha_inicio = '2018-1-1'
#fecha_fin = '2018-1-30'
#directorio_descarga = str('fecha/')
#satelite = str("COPERNICUS/S2")
#src = '4326'

def download_image_sat(archivo_geojson,fecha_inicio,fecha_fin,directorio_descarga,src,satelite):
	geodata = ee.ImageCollection(satelite)
	geodata = geodata.filterDate(fecha_inicio, fecha_fin)
	with open(archivo_geojson) as f:
	    gj = geojson.load(f)
	features = gj['features'][0]
	roi = ee.Geometry.Polygon(features.geometry.coordinates)
	geodata = geodata.filterBounds(roi)
	geodata = ee.Image(geodata.first()).clip(roi)
	geodata = geodata.normalizedDifference(['B8', 'B4'])
	#geodata = geodata.expression('(b("B8")-b("B4"))/(b("B8")+b("B4"))')
	name = str(archivo_geojson.replace('.geojson','')+'_'+fecha_inicio)
	path = geodata.getDownloadUrl({
	    'name': name,
	    'scale': 10,
	    'crs': 'EPSG:32720'
	    })
	#return path
	
	if not os.path.exists(directorio_descarga):
		os.makedirs(directorio_descarga)
	sentencia = str(path)
	urllib.urlretrieve(sentencia, str(directorio_descarga+str(archivo_geojson.replace('.geojson','')+'_'+fecha_inicio+'.zip')))
	urllib.urlcleanup()
	#print "Proceso terminado"
	

#download_image_sat(archivo_geojson,fecha_inicio,fecha_fin,directorio_descarga,src,satelite)

def opcion_satelite(opcion_sat):
	if opcion_sat == "Sentinel-2":
		satelite = "COPERNICUS/S2"
	elif opcion_sat == "Landsat-8":
		satelite = 'LANDSAT/LC08/C01/T1_TOA'	
	else:
		pass
	return satelite

def SRC(opcion_src):
	if opcion_src == "WGS 84 - 4326":
		src = '4326'
	elif opcion_src == "WGS 84 - UTM 20S":
		src = '32720'
	else:
		pass
	return src	

#print SRC("WGS 84 - UTM 20S")	
