import unittest

def perimeter(a, b, c):
    ''' функция perimeter принимает 3 вещественных аргумента: a, b, c,
        где a, b, c - длины сторон треугольника,
        а возвращает периметр этого треугольника, то есть сумму сторон
    '''
    return a + b + c

def area(a, h):
    ''' функция area принимает 2 вещественных аргумента: a, h,
        где a - длина стороны треугольника,
        а h - длина высоты, проведённой к этой стороне,
        а возвращает площадь этого треугольника, то есть произведение a на h
    '''
    return a * h * 0.5

class TriangleTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
   def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 50)

   def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

   def test_perimeter_mul(self):
       res = perimeter(10, 10, 10)
       self.assertEqual(res, 30)