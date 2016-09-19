import unittest
from figuras import Figuras

class TestFiguras(unittest.TestCase):

	def setUp(self):
		self.figuras=Figuras()

	def test_area_cuadrado_lado_5(self):
		
		resultado=self.figuras.cuadrado(5)
		self.assertEquals(25,resultado)
	
	def test_area_cuadrado_lado_6(self):
		
		resultado=self.figuras.cuadrado(6)
		self.assertEquals(36,resultado)

	def test_area_cuadrado_lado_g(self):
		
		resultado=self.figuras.cuadrado('g')
		self.assertEquals('dato incorrecto',resultado)

	def test_area_cuadrado_lado_4_punto_5(self):
		
		resultado=self.figuras.cuadrado(4.5)
		self.assertEquals(20.25,resultado)

	def test_area_rectangulo_base_por_altura_6_por_5(self):
		
		resultado=self.figuras.rectangulo(6,5)
		self.assertEquals(30,resultado)

	def test_area_rectangulo__base_por_altura_g_por_g(self):
		
		resultado=self.figuras.rectangulo('g','g')
		self.assertEquals('dato incorrecto',resultado)

	def test_area_rectangulo__base_por_altura_5_punto_5_por_6_punto_6(self):
		
		resultado=self.figuras.rectangulo(5.5,6.6)
		self.assertEquals(36.3,resultado)

	def test_area_triangulo_base_por_altura_entre2_6_por_5_entre2(self):
		
		resultado=self.figuras.triangulo(6,5)
		self.assertEquals(15,resultado)
	def test_area_triangulo_base_por_altura_entre2_6_punto_5_por_5_punto_5_entre2(self):
		
		resultado=self.figuras.triangulo(6.5,5.5)
		self.assertEquals(17.875,resultado)
	def test_area_triangulo_base_por_altura_entre2_g_por_g_entre2(self):
		
		resultado=self.figuras.triangulo('g','g')
		self.assertEquals('dato incorrecto',resultado)
	def test_area_circulo_pi_por_radio_al_cuadrado_35(self):
		
		resultado=self.figuras.circulo(35)
		self.assertEquals(3848.46,resultado)
	def test_area_circulo_pi_por_radio_al_cuadrado_35_punto_5(self):
		
		resultado=self.figuras.circulo(35.5)
		self.assertEquals(3959.2014,resultado)
	def test_area_circulo_pi_por_radio_al_cuadrado_g(self):
		
		resultado=self.figuras.circulo('g')
		self.assertEquals('dato incorrecto',resultado)
		
if __name__ == '__main__':
	unittest.main()