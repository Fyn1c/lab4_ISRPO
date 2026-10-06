import unittest


def area(a):
    ''' функция area принимает 1 вещественный аргумент: a
        где a - длина стороны квадрата,
        а возвращает площадь этого квадрата, то есть произведение a на a
    '''
    return a * a


def perimeter(a):
    ''' функция perimeter принимает 1 вещественный аргумент: a
        где a - длина стороны квадрата,
        а возвращает периметр этого квадрата, то есть a, умноженное на 4
    '''
    return 4 * a


class SquareTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)
       
   def test_square_mul(self):
       res = area(10)
       self.assertEqual(res, 100)

   def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

   def test_perimeter_mul(self):
       res = perimeter(10)
       self.assertEqual(res, 40)