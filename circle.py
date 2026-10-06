import math
import unittest

def area(r):
    ''' функция area принимает 1 вещественный аргумент: r
        где r - радиус окружности
        а возвращает площадь этого круга, то есть произведение pi*r^2
    '''
    return math.pi * r * r


def perimeter(r):
    ''' функция perimeter принимает 1 вещественный аргумент: r
        где r - радиус окружности
        а возвращает периметр этого круга, то есть произведение 2*pi*r
    '''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)
       
   def test_square_mul(self):
       res = area(10)
       self.assertEqual(res, 314.1592653589793)

   def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

   def test_perimeter_mul(self):
       res = perimeter(10)
       self.assertEqual(res, 62.83185307179586)