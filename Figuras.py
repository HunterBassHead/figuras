class Figuras:
	
	def cuadrado(self,lado):
		try:
		
			if lado%1==0:
				return lado * lado
			else :
				return float( lado * lado )

		except Exception, e:
			return 'dato incorrecto'
	def rectangulo(self,base,altura):
		
		try:
			if base%1==0:
				if altura%1==0:
					return base * altura
			else:
				return float(base * altura)
		except Exception, e:
			return 'dato incorrecto'
	def triangulo(self,base,altura):
		
		try:
			if base%1==0:
				if altura%1==0:
					return (base * altura)/2
			else:
				return float(base * altura)/2
		except Exception, e:
			return 'dato incorrecto'
	def circulo(self,radeo):
		
		try:
			if radeo%1==0:
				return 3.1416 * (radeo*radeo)
			else:
				return float( 3.1416 * (radeo*radeo))
		except Exception, e:
			return 'dato incorrecto'