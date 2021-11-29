#ENDPOINTS UTILIZADOS
#https://api.mercadolibre.com/sites/$SITE/search?seller_id=$SELLER_ID"
#https://api.mercadolibre.com/categories/$CATEGORY_ID

#Se importa la liberia request para realizar peticiones HTTPS
import requests 

#Se genera el listado de sellers
sellers=[179571326]

#Se recorre el listado de sellers
for seller in sellers:
	
	#Se abre el archivo a trabajar (si no existe se crea)
	archivo = open('./'+str(seller)+'.txt','w')

	#Se obtienen los items publicados en MLA por el seller
	datos = requests.get("https://api.mercadolibre.com/sites/MLA/search?seller_id="+str(seller)).json()
	items = datos['results']
	 
	print ("items del seller: "+str(seller))
	#Se recorre el listado de items, extrayendo de cada uno el ID, title, ID category, name category
	for item in items:
		id_item = item['id']
		title = item['title']
		category_id = item['category_id']
		
		#Se obtiene la categoria espefica para saber su nombre
		datos_categoria = requests.get("https://api.mercadolibre.com/categories/"+str(item['category_id'])).json()
		name_category = datos_categoria['name']
		
		#Se escriben los datos en el archivo correspondiente
		archivo.write(id_item)
		archivo.write('\n')
		archivo.write(title)
		archivo.write('\n')
		archivo.write(category_id)
		archivo.write('\n')
		archivo.write(name_category)
		archivo.write('\n')
		archivo.write('\n')
		print (id_item) 
		print (title)
		print (category_id)
		print (name_category)
		print('\n')
	archivo.close()
