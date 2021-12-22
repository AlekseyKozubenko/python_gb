"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата
"""


class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    #  сделал много частных случаев, потом проверил, как принтуются реальные комплексные, исправил частные случаи
    #  но уже не группировал их
    def __str__(self):
        if self.real_part == 0 and self.imaginary_part == 0:
            return f"0i"
        elif self.real_part == 0 and self.imaginary_part == 1:
            return f"1i"
        elif self.real_part == 0 and self.imaginary_part == -1:
            return f"-1i"
        elif self.real_part == 0:
            return f"{self.imaginary_part}i"
        elif self.imaginary_part == -1:
            return f"({self.real_part}-1i)"
        elif self.imaginary_part < 0:
            return f"({self.real_part}-{-self.imaginary_part}i)"
        elif self.imaginary_part == 0:
            return f"({self.real_part}+0i)"
        elif self.imaginary_part == 1:
            return f"({self.real_part}+1i)"
        else:
            return f"({self.real_part}+{self.imaginary_part}i)"

    def __add__(self, other):
        new_real = self.real_part + other.real_part
        new_imaginary = self.imaginary_part + other.imaginary_part
        return ComplexNumber(new_real, new_imaginary)

    """
    http://mathprofi.ru/kompleksnye_chisla_dlya_chainikov.html
    real:      a1 * a2 + (-1) * b1 * b2
    imaginary: a1 * b2 + b1 * a2
    """
    def __mul__(self, other):
        new_real = self.real_part * other.real_part + (-1) * self.imaginary_part * other.imaginary_part
        new_imaginary = self.real_part * other.imaginary_part + self.imaginary_part * other.real_part
        return ComplexNumber(new_real, new_imaginary)


cn1 = ComplexNumber(1, 1)
print(cn1, complex(1, 1))
cn2 = ComplexNumber(0, 0)
print(cn2, complex(0, 0))
cn3 = ComplexNumber(1, 0)
print(cn3, complex(1, 0))
cn4 = ComplexNumber(0, 1)
print(cn4, complex(0, 1))
cn5 = ComplexNumber(-1, -1)
print(cn5, complex(-1, -1))
cn6 = ComplexNumber(-5, 0)
print(cn6, complex(-5, 0))
cn7 = ComplexNumber(0, -1)
print(cn7, complex(0, -1))
cn8 = ComplexNumber(-2, -2)
print(cn8, complex(-2, -2))
cn9 = ComplexNumber(1, -1)
print(cn9, complex(1, -1))
cn10 = ComplexNumber(6, 0.1)
print(cn10, complex(6, 0.1))
print("Operations")
cn_1 = ComplexNumber(1, 3)
print(cn_1)
cn_2 = ComplexNumber(4, -5)
print(cn_2)
cn_3 = cn_1 + cn_2
print(cn_3, complex(1, 3) + complex(4, -5))
cn_4 = cn_1 * cn_2
print(cn_4, complex(1, 3) * complex(4, -5))
