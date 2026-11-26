import unittest
from iberos.route_definitive_g143 import evaluar,geometria,PERIODO
class G143Tests(unittest.TestCase):
 def test_periodo(self): self.assertEqual(PERIODO,(-429,-349))
 def test_distancia(self): self.assertAlmostEqual(geometria()["distancia_recta_referencias_m"],12252.154,3)
 def test_azimut(self): self.assertAlmostEqual(geometria()["azimut_referencias_grados"],290.956,3)
 def test_dos_alternativas(self): self.assertEqual(len(evaluar()["rutas"]),2)
 def test_abstencion(self): self.assertFalse(evaluar()["confirmada"])
 def test_no_descarta(self): self.assertFalse(evaluar()["descartada"])
 def test_ninguna_certificada(self): self.assertTrue(all(not x["certificada"] for x in evaluar()["rutas"].values()))
 def test_sin_falso_camino(self): self.assertTrue(all(x["longitud_camino_m"] is None for x in evaluar()["rutas"].values()))
 def test_foso_es_bloqueo(self): self.assertIn("cruce_foso",evaluar()["rutas"]["litoral"]["faltas"])
 def test_paleoterreno_es_bloqueo(self): self.assertIn("paleoterreno",evaluar()["rutas"]["interior_molar"]["faltas"])
if __name__=="__main__": unittest.main()
