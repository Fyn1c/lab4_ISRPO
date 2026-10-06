import unittest

def area(a, b):
    ''' функция area принимает 2 вещественных аргумента: a, b,
        где a, b - длины сторон прямоугольника,
        а возвращает площадь этого прямоугольника, то есть произведение a на b
    '''
    return a*b

def perimeter(a, b):
    ''' функция perimeter принимает 2 вещественных аргумента: a, b,
        где a, b - длины сторон прямоугольника,
        а возвращает периметр этого прямоугольника, то есть сумму сторон, умноженную на 2
    '''
    return 2*(a+b)


class RectangleTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
   def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

   def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

   def test_perimeter_mul(self):
       res = perimeter(10, 10)
       self.assertEqual(res, 40)