import unittest
import timeit

# Some unit tests for correctness of formulas from each section

# The syllabic verse algorithm for Turkish language,
# used in both the example unit tests and the runtime
# performance test below.
def syllabic_verse_algorithm(str1):
    ch = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü', 'A', 'E', 'I', 'İ', 'O', 'Ö', 'U', 'Ü']
    hs1 = len(str1) - str1.replace(ch[0], "").__len__()
    hs2 = len(str1) - str1.replace(ch[1], "").__len__()
    hs3 = len(str1) - str1.replace(ch[2], "").__len__()
    hs4 = len(str1) - str1.replace(ch[3], "").__len__()
    hs5 = len(str1) - str1.replace(ch[4], "").__len__()
    hs6 = len(str1) - str1.replace(ch[5], "").__len__()
    hs7 = len(str1) - str1.replace(ch[6], "").__len__()
    hs8 = len(str1) - str1.replace(ch[7], "").__len__()
    hs9 = len(str1) - str1.replace(ch[8], "").__len__()
    hs10 = len(str1) - str1.replace(ch[9], "").__len__()
    hs11 = len(str1) - str1.replace(ch[10], "").__len__()
    hs12 = len(str1) - str1.replace(ch[11], "").__len__()
    hs13 = len(str1) - str1.replace(ch[12], "").__len__()
    hs14 = len(str1) - str1.replace(ch[13], "").__len__()
    hs15 = len(str1) - str1.replace(ch[14], "").__len__()
    hs16 = len(str1) - str1.replace(ch[15], "").__len__()
    result = hs1 + hs2 + hs3 + hs4 + hs5 + hs6 + hs7 + hs8 + hs9 + hs10 + hs11 + hs12 + hs13 + hs14 + hs15 + hs16
    return result


class TestSum(unittest.TestCase):

    # Implementation taken from the function at line 159 on CalculatorApp.py
    def test_molcalculation(self):
        # Calculating how many moles of sodium chloride are present in a
        # sample that has a mass of 1.17g
        # The result should be 0.02
        # input1 = mass
        # input2 = molar mass
        input1 = float(1.17)
        input2 = float(58.5)
        molcalculation_formula = input1 / input2
        self.assertEqual(molcalculation_formula, 0.02, "Should be 0.02")

    # Implementation taken from the function at line 462 on CalculatorApp.py
    def test_work(self):
        # Calculating the amount of work done in Joule with 30N applied
        # force and 40m of displacement
        # The result should be 1200
        # input1 = applied force
        # input2 = displacement
        input1 = int(30)
        input2 = int(40)
        work_formula = input1 * input2
        self.assertEqual(work_formula, 1200, "Should be 1200")

    # Implementation taken from the function at line 999 on CalculatorApp.py
    def test_cubevolume(self):
        # Calculating the volume of a cube with 6 cm edge length
        # input1 = edge length
        # The result should be 216.0
        input1 = float(6)
        cubevolume_formula = input1*input1*input1
        self.assertEqual(cubevolume_formula, 216.0, "Should be 216.0")

    # Implementation taken from the function at line 2184 on CalculatorApp.py
    def test_syllabicverse(self):
        # Calculating the number of syllabic verses in the word "Merhaba" from Turkish
        # str1 = The word "Merhaba"
        # The result should be 3
        syllabicverse_formula = syllabic_verse_algorithm("Merhaba")
        self.assertEqual(syllabicverse_formula, 3, "Should be 3")

    # Runtime performance test on the syllabic verse calculator for Turkish
    # I have selected this one specifically because I came up with the
    # algorithm myself and based on running this algorithm multiple times
    # I have concluded that the average runtime is around ~2.3 seconds
    def test_performance(self):
        test_code = syllabic_verse_algorithm("Merhaba benim adım Efe")
        total_time = timeit.timeit('syllabic_verse_algorithm("Merhaba")', globals=globals())
        self.assertEqual(total_time < 5.0, True)




















