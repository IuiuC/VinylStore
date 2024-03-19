from flask import Flask, render_template, jsonify, request, redirect
import cx_Oracle
from datetime import datetime 
import os
os.environ['PATH'] = r'C:\Users\Iuliana\Downloads\instant\instantclient_21_12' + ';' + os.environ['PATH']

app = Flask(__name__)
with open(app.root_path + '/config.cfg', 'r') as f:
    app.config['ORACLE_URI'] = f.readline()

#
username = ""
password = ""
dsn = ""

# Establish a connection
con = cx_Oracle.connect(user=username, password=password, dsn=dsn)

#vinil_generic begin code
@app.route('/')
@app.route('/vinil_generic')
def emp():
	vinil_generic = []
	
	cur = con.cursor()
	cur.execute('select * from vinil_generic')
	for result in cur:
		vinil_generic1 = {}
		vinil_generic1['id_vinilgeneric'] = result[0]
		vinil_generic1['titlu_album'] = result[1]
		vinil_generic1['artist'] =result[2]
		vinil_generic1['gen_muzical'] = result[3]
		vinil_generic1['an_lansare'] = result[4]
		
		vinil_generic.append(vinil_generic1)
	cur.close()
	print(vinil_generic)
	return render_template('vinil_generic.html', vinil_generic=vinil_generic)


@app.route('/addVinilGeneric', methods=['GET', 'POST'])
def add_vg():
	error = None
	if request.method == 'POST':
		vinil=0
		cur=con.cursor()
		cur.execute('select max(id_vinilgeneric) from vinil_generic')
		for result in cur:
			vinil=result[0]
		cur.close()
		if vinil is None:
  		   vinil=0
		vinil+=1
		cur = con.cursor()
		values = []
		values.append("'" + str(vinil) + "'")

		values.append("'" + request.form['titlu_album'] + "'")
		values.append("'" + request.form['artist'] + "'")
		values.append("'" + request.form['gen_muzical'] + "'")
		values.append("'" + request.form['an_lansare'] + "'")
		
		fields = ['id_vinilgeneric','titlu_album', 'artist', 'gen_muzical', 'an_lansare']
		query = 'INSERT INTO %s (%s) VALUES (%s)' % ('vinil_generic',', '.join(fields),', '.join(values))

		cur.execute(query)
		cur.execute('commit')
		return redirect('/vinil_generic')

@app.route('/delVinilGeneric', methods=['POST'])
def del_vingen():
	vin = request.form['id_vinilgeneric']
	cur = con.cursor()
	cur.execute('delete from vinil_generic where id_vinilgeneric=' + vin)
	cur.execute('commit')
	return redirect('/vinil_generic')
	
@app.route('/editVinilGeneric', methods=['POST'])
def edit_vinilgen():
	emp=0
	cur = con.cursor()
	titlu_album="'"+request.form['titlu_album']+"'"
	
	cur.execute('select id_vinilgeneric from vinil_generic where titlu_album='+titlu_album)	
	for result in cur:
		emp=result[0]
	cur.close()
	artist = "'"+request.form['artist']+"'"
	gen_muzical ="'"+request.form['gen_muzical']+"'"
	an_lansare = request.form['an_lansare']
	query = "UPDATE vinil_generic SET titlu_album=%s, artist=%s, gen_muzical=%s, an_lansare=%s where id_vinilgeneric=%s" % (titlu_album,artist,gen_muzical,an_lansare, emp)	
	cur = con.cursor()
	cur.execute(query)

	return redirect('/vinil_generic')

@app.route('/getVinilGeneric', methods=['POST'])
def get_vinilgen():
	emp = request.form['id_vinilgeneric']
	print(emp)
	cur = con.cursor()
	cur.execute('SELECT * FROM vinil_generic WHERE id_vinilgeneric = :emp', {'emp': emp})
	
	emps = cur.fetchone()
	id_vinilgeneric=emps[0]
	titlu_album=emps[1]
	artist=emps[2]
	gen_muzical= emps[3]
	an_lansare = emps[4]
	cur.close()
	return render_template('HTMLPage1.html',id_vinilgeneric=id_vinilgeneric, 
	titlu_album=titlu_album, artist=artist, gen_muzical=gen_muzical, an_lansare=an_lansare)



#vinil_fizic begin code
@app.route('/vinil_fizic')
def vinfiz():
	counselors = []
	
	cur = con.cursor()
	cur.execute('select * from vinil_fizic')
	for result in cur:
		vinil_fizic1 = {}
		vinil_fizic1['id_vinil'] = result[0]
		vinil_fizic1['stare'] = result[1]
		vinil_fizic1['pret'] =result[2]
		vinil_fizic1['stoc'] = result[3]
		vinil_fizic1['id_furnizor'] = result[4]
		vinil_fizic1['id_promotie'] = result[5]
		vinil_fizic1['id_vinilgeneric'] = result[5]

		counselors.append(vinil_fizic1)
	cur.close()
	
	com1 = []
	cur = con.cursor()
	cur.execute('select id_furnizor from furnizor')
		# import pdb;pdb.set_trace()
	for result in cur:
		com1.append(result[0])
	cur.close()
	
	com2 = []
	cur = con.cursor()
	cur.execute('select id_promotie from promotie')
		# import pdb;pdb.set_trace()
	for result in cur:
		com2.append(result[0])
	cur.close()
	
		
	com= []
	cur = con.cursor()
	cur.execute('select id_vinilgeneric from vinil_generic')
		# import pdb;pdb.set_trace()
	for result in cur:
		com.append(result[0])
	cur.close()

	return render_template('vinil_fizic.html', counselors=counselors, vinil_fizic=com, furnizor=com1, promotie=com2)
	
	
@app.route('/addVinilFizic', methods=['GET', 'POST'])
def add_vf():
	error = None
	if request.method == 'POST':
		vinil=0
		cur=con.cursor()
		cur.execute('select max(id_vinil) from vinil_fizic')
		for result in cur:
			vinil=result[0]
		cur.close()
		if vinil is None:
  		   vinil=0
		vinil+=1
		cur = con.cursor()
		values = []
		values.append("'" + str(vinil) + "'")

		values.append("'" + request.form['stare'] + "'")
		values.append("'" + request.form['pret'] + "'")
		values.append("'" + request.form['stoc'] + "'")
		values.append("'" + request.form['id_furnizor'] + "'")
		values.append("'" + request.form['id_promotie'] + "'")
		values.append("'" + request.form['id_vinilgeneric'] + "'")
		
		fields = ['id_vinil','stare', 'pret', 'stoc', 'id_furnizor', 'id_promotie', 'id_vinilgeneric']
		query = 'INSERT INTO %s (%s) VALUES (%s)' % ('vinil_fizic',', '.join(fields),', '.join(values))

		cur.execute(query)
		cur.execute('commit')
		return redirect('/vinil_fizic')


@app.route('/delVinilFizic', methods=['POST'])
def del_vinfiz():
	vini = request.form['id_vinil']
	cur = con.cursor()
	cur.execute('delete from vinil_fizic where id_vinil=' + vini)
	cur.execute('commit')
	return redirect('/vinil_fizic')
	

#promotie start code
@app.route('/promotie')
def prom():
	promotie = []
	
	cur = con.cursor()
	cur.execute('select * from promotie')
	for result in cur:
		promotie1 = {}
		promotie1['id_promotie'] = result[0]
		promotie1['data_inc'] = datetime.strptime(str(result[1]),'%Y-%m-%d %H:%M:%S').strftime('%d-%b-%y')
		promotie1['data_sf'] = datetime.strptime(str(result[2]),'%Y-%m-%d %H:%M:%S').strftime('%d-%b-%y')
		promotie1['procent'] =result[3]
		
		promotie.append(promotie1)
	cur.close()
	return render_template('promotie.html', promotie=promotie)

@app.route('/addPromotie', methods=['GET','POST'])
def ad_prmo():
	error = None
	if request.method == 'POST':
		promo=0
		cur=con.cursor()
		cur.execute('select max(id_promotie) from promotie')
		for result in cur:
			promo=result[0]
		cur.close()
		if promo is None:
  		   promo=0 
		promo+=1
		cur = con.cursor()
		values = []
		values.append("'" + str(promo)+ "'")
		values.append("'" + datetime.strptime(str(request.form['data_inc']),'%Y-%m-%d').strftime('%d-%b-%y') + "'")
		values.append("'" + datetime.strptime(str(request.form['data_sf']),'%Y-%m-%d').strftime('%d-%b-%y') + "'")
		values.append("'" + request.form['procent'] + "'")
		fields = ['id_promotie', 'data_inc', 'data_sf', 'procent']
		query = 'INSERT INTO %s (%s) VALUES (%s)' % (
			'promotie',
			', '.join(fields),
			', '.join(values)
			)

		cur.execute(query)
		cur.execute('commit')
		return redirect('/promotie')

@app.route('/delPromotie', methods=['POST'])
def del_promo():
	pr = "'"+request.form['id_promotie']+"'"
	cur = con.cursor()
	cur.execute('delete from promotie where id_promotie=' + pr)
	cur.execute('commit')
	return redirect('/promotie')


#pozitionare start code
@app.route('/pozitionare')
def poz():
	counselors = []
	
	cur = con.cursor()
	cur.execute('select * from pozitonare')
	for result in cur:
		pozitonare1 = {}
		pozitonare1['biblioteca'] = result[0]
		pozitonare1['raft'] = result[1]
		pozitonare1['id_vinil'] =result[2]
		
		counselors.append(pozitonare1)
	cur.close()
	com= []
	cur = con.cursor()
	cur.execute('select id_vinil from vinil_fizic')
		# import pdb;pdb.set_trace()
	for result in cur:
		com.append(result[0])
	cur.close()
	#print(com)
	return render_template('pozitionare.html', counselors=counselors, pozitonare=com)
	
@app.route('/addPozitionare', methods=['GET', 'POST'])
def add_poz():
	error = None
	if request.method == 'POST':
		cur = con.cursor()
		values = []
		values.append("'" + request.form['biblioteca'] + "'")
		values.append("'" + request.form['raft'] + "'")
		values.append("'" + request.form['id_vinil'] + "'")
		
		fields = ['biblioteca','raft', 'id_vinil']
		query = 'INSERT INTO %s (%s) VALUES (%s)' % ('pozitonare',', '.join(fields),', '.join(values))

		cur.execute(query)
		cur.execute('commit')
		return redirect('/pozitionare')

@app.route('/delPozitionare', methods=['POST'])
def del_poz():
	vini = request.form['id_vinil']
	cur = con.cursor()
	cur.execute('delete from pozitonare where id_vinil=' + vini)
	cur.execute('commit')
	return redirect('/pozitionare')
	

#incasari start code
@app.route('/incasari')
def incas():
	counselors = []
	
	cur = con.cursor()
	cur.execute('select * from incasari')
	for result in cur:
		incasari1 = {}
		incasari1['id_incasari'] = result[0]
		incasari1['metoda_de_plata'] = result[1]
		incasari1['data_vanzare'] =datetime.strptime(str(result[2]),'%Y-%m-%d %H:%M:%S').strftime('%d.%m.%y')
		incasari1['suma'] =result[3]
		incasari1['id_vinil'] =result[4]
		counselors.append(incasari1)
	cur.close()
	com= []
	cur = con.cursor()
	cur.execute('select id_vinil from vinil_fizic')
		# import pdb;pdb.set_trace()
	for result in cur:
		com.append(result[0])
	cur.close()
	#print(com)
	return render_template('incasari.html', counselors=counselors, incasari=com)
	

@app.route('/addIncasari', methods=['GET', 'POST'])
def add_incas():
	error = None
	if request.method == 'POST':
		promo=0
		cur=con.cursor()
		cur.execute('select max(id_incasari) from incasari')
		for result in cur:
			promo=result[0]
		cur.close()
		if promo is None:
  		   promo=0 
		promo+=1
		cur = con.cursor()
		values = []
		values.append("'" + str(promo)+ "'")
		values.append("'" + request.form['metoda_de_plata'] + "'")
		values.append("'" + datetime.strptime(str(request.form['data_vanzare']),'%Y-%m-%d').strftime('%d-%b-%y') + "'")
		values.append("'" + request.form['suma'] + "'")
		values.append("'" + request.form['id_vinil'] + "'")
		
		fields = ['id_incasari', 'metoda_de_plata', 'data_vanzare', 'suma', 'id_vinil']
		query = 'INSERT INTO %s (%s) VALUES (%s)' % ('incasari',', '.join(fields),', '.join(values))

		cur.execute(query)
		cur.execute('commit')

		cur=con.cursor()
		emp = 0
		cur.execute('select max(id_incasari) from incasari')
		for result in cur:
			emp=result[0]
		cur.close()
		cur=con.cursor()
		emp1 = 0
		select_query="SELECT id_vinil from incasari WHERE id_incasari =:emp"
		cur.execute(select_query, {'emp': emp})
		for result in cur:
			emp1=result[0]
		cur.close()
		cur = con.cursor()
		update_query = "UPDATE vinil_fizic SET stoc = stoc-1 WHERE id_vinil =:emp1"
		cur.execute(update_query, {'emp1': emp1})
		con.commit()
		cur.close()
		return redirect('/incasari')


@app.route('/delIncasari', methods=['POST'])
def del_incas():
	vini=0
	vini = request.form['id_incasari']
	emp1 = 0
	cur=con.cursor()
	select_query="SELECT id_vinil from incasari WHERE id_incasari =:vini"
	cur.execute(select_query, {'vini': vini})
	for result in cur:
		emp1=result[0]
	cur.close()
	cur = con.cursor()
	cur.execute('delete from incasari where id_incasari=' + vini)
	cur.execute('commit')
	cur = con.cursor()
	update_query = "UPDATE vinil_fizic SET stoc = stoc+1 WHERE id_vinil =:emp1"
	cur.execute(update_query, {'emp1': emp1})
	con.commit()
	cur.close()
	return redirect('/incasari')


#furnizor begin code
@app.route('/')
@app.route('/furnizor')
def fur():
	furnizor = []
	
	cur = con.cursor()
	cur.execute('select * from furnizor')
	for result in cur:
		furnizor1 = {}
		furnizor1['id_furnizor'] = result[0]
		furnizor1['denumire'] = result[1]
		furnizor1['adresa'] =result[2]
		
		furnizor.append(furnizor1)
	cur.close()
	#print(vinil_generic)
	return render_template('furnizor.html', furnizor=furnizor)
	
	
@app.route('/addFurnizor', methods=['GET', 'POST'])
def add_fur():
	error = None
	if request.method == 'POST':
		furniz=0
		cur=con.cursor()
		cur.execute('select max(id_furnizor) from furnizor')
		for result in cur:
			furniz=result[0]
		cur.close()
		if furniz is None:
  		   furniz=0
		furniz+=1
		cur = con.cursor()
		values = []
		values.append("'" + str(furniz) + "'")

		values.append("'" + request.form['denumire'] + "'")
		values.append("'" + request.form['adresa'] + "'")
		
		
		fields = ['id_furnizor','denumire', 'adresa']
		query = 'INSERT INTO %s (%s) VALUES (%s)' % ('furnizor',', '.join(fields),', '.join(values))

		cur.execute(query)
		cur.execute('commit')
		return redirect('/furnizor')

@app.route('/delFurnizor', methods=['POST'])
def del_fur():
	vin = request.form['id_furnizor']
	cur = con.cursor()
	cur.execute('delete from furnizor where id_furnizor=' + vin)
	cur.execute('commit')
	return redirect('/furnizor')


#main	
if __name__ == '__main__':
	app.run(debug=True)
	con.close()

