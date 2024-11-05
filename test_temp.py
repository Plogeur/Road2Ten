import unittest
import dd_class_temp

# Website to generated test : https://felis-silvestris.lescigales.org/
class TestCrosing(unittest.TestCase):

    def setUp(self) :
        self.maxDiff = None # unittest parameter

        #                    id  sex   color  generation   root
        # dd_class_temp.Dragodinde(1, "M", "Rousse", 1, self.genealogie_s1, gestation_time)

        # simple mono
        self.dd_sm1 = dd_class_temp.Dragodinde(100, "M", "Rousse", 1)
        self.dd_sm2 = dd_class_temp.Dragodinde(101, "F", "Amande", 1)

        # simple bi 
        self.dd_sb1 = dd_class_temp.Dragodinde(200, "M", "Indigo et Orchidée", 6)
        self.dd_sb2 = dd_class_temp.Dragodinde(201, "F", "Pourpre et Ivoire", 8)

        # simple bi 2
        self.dd_sb3 = dd_class_temp.Dragodinde(202, "M", "Rousse et Amande", 2)
        self.dd_sb4 = dd_class_temp.Dragodinde(203, "F", "Rousse et Amande", 2)
 
        self.elevage = dd_class_temp.Elevage([self.dd_sm1, self.dd_sm2, self.dd_sb1, self.dd_sb2, self.dd_sb3, self.dd_sb4])

if __name__ == "__main__":
    unittest.main()
