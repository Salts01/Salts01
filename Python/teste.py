import math 
#squares = []
#for value in range(1,11): 
 #   square = value**2
  #  squares.append(square)
#print(squares)
#zed=[]
#	zeds=input('nome ')
#	zed.append(zeds)
#print(zed)	
#ount=[1,4,55,2,342,56]
#print(sum(count))
#cont=count[:]
#cont.insert(1,13)
#print(cont)
#print(count)
#ca="casa"
#print(ca.upper())
#kled=input("inclua a serie ")
#series=['brk','tw']
#for serie in series:
#	if kled in series:
		#resp=1
#	else:
#		resp=0
#if resp==1:
#	print("boa serie")
#else:
#   print("nao foi encontrada")
#users={'cada':str(5),'die':str(6)}
 #for nomes,value in users.items():
	#print(nomes+value)
#cors={'ada':3, 'fek':12}
#ale=[users,cors]
#print(ale)   
#print(users['cada'])
#cors['ada']=1
#print(cors['ada'])
#del cors['fek']
#print(cors)
#cors['ada']= input("digite: ")
#print(cors['ada'])
#print(math.sqrt(4))

#while
#siclo=[]
#while ount:
#	sers=ount.pop()
#	siclo.append(sers)
#for name in siclo:
#	print(name)



#resp={}
#atc=True
#while atc:
#	name=input("digite seu nome: ")
#	respes=input("oq vc faz hj: ")
#	resp[name]=respes
#	perg=input("gostaria de repitir: ")
#	if perg=='nao':
#		break
#print(resp)
#letd=['cnh','cpj','softmarks','cpj']
#while 'cpj' in letd:
#	letd.remove('cpj')
#print(letd)



#função
#def Favb(book):
#	nome=input('escreva o nome do seu livro favorito: ')
#	tipo=input('qual é o genero dele: ')
#	book[nome]=tipo
#	return book

#livro={}
#livro=Favb(livro)
#print(livro)

#def contc(irreg,acet):
#	 while irreg:
#		 rest=irreg.pop()
#		 acet.append(rest)
#	 for acets in acet:
#		 print(acets)	 
		

#falf=['robert','carlos','indus']
#showlance=[]
#contc(falf[:],showlance)
#print(showlance)
#print(falf)

#pizza=('doasi','screans','esgot')
#inutili=13
	
#def refunct(tamanho,*ingredientes):

#	print(str(tamanho))
#	for ing in ingredientes:
#		print(ing)

#refunct(inutili,pizza)



#def info(**inf):
 #    for a in inf:
  #      print(a, inf[a])  


	

#nome=input('primeiro nome: ')
#segundo=input("segundo nome: ")
#info(informa={'loc':'albert','indus':'rose'})

#import
#from Syf import junt as nf
#nf(nome,segundo)


#classe
class carro():
	def __init__(self,tipo,marca,numportas):
		self.tipo=tipo
		self.marca=marca
		self.numportas=numportas
		pass
	

	def ignição(self):
		print('Ligando carro')
	
	
	def acelerando(self):
		print('acelerando carro')
	
    
	def freando(self):
		print('freando carro')
	

	def infocarro(self):
	    print(self.tipo)
	    print(self.marca)
	    print(self.numportas)
class CarroGasosa(carro):
	def __init__(self,tipo,marca,numportas):
		super().__init__(tipo,marca,numportas)
	
	def fumaça(self):
	    print('soltar fumaça')	


class Careletric(carro):
	def __init__(self, tipo, marca, numportas) :
		super().__init__(tipo, marca, numportas)
		self.bateria=bateria()
		self.IA=IA()

	def carregando(self):
	    print('carregando')   
    
	def chamar(self):
		print('chamando')

	def freando(self):
		print('esse carro freia automatico')


class bateria():
	def __init__(self,tam_bateria=80):
		self.tam_bateria=tam_bateria
	def infobateria(self):
		print('capacidade da bateria ',self.tam_bateria)


class IA():		
    def falar(self):
    	print("ola motorista")
    def gps(self):
        print('mostrando rota')
    def atender(self):
        print('atendendo ligaçao')    	

car1=Careletric('suv','tesla','2')
car1.carregando()
car1.freando()
car1.chamar()
car1.acelerando()
car1.bateria.infobateria()
car1.IA.falar()
car1.IA.gps()
car2=CarroGasosa('sedan','ford','4')
car2.freando()
tesl=Careletric('sedan','tesla','2')
tesl.chamar()
tesl.IA.falar()
    

		






	


	

		