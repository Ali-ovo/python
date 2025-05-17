class AC(object):
    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_l_wind(self):
        pass
      
    @classmethod
    def make_noise(cls):
        print(f"{cls} make_noise")
        
    @staticmethod
    def make_noise_static():
        print("AC make_noise_static")


class XiaoMi_AC(AC):
    def cool_wind(self):
        print("XiaoMi_AC cool_wind")

    def hot_wind(self):
        print("XiaoMi_AC hot_wind")

    def swing_l_wind(self):
        print("XiaoMi_AC swing_l_wind")

class GREE_AC(AC):
    def cool_wind(self):
        print("GREE_AC cool_wind")

    def hot_wind(self):
        print("GREE_AC hot_wind")

    def swing_l_wind(self):
        print("GREE_AC swing_l_wind")
        
def maketestAC(myac: AC):
    myac.cool_wind()
    myac.hot_wind()
    myac.swing_l_wind()
    
xiaomi_ac = XiaoMi_AC()
GREE_ac = GREE_AC()

maketestAC(xiaomi_ac)
maketestAC(GREE_ac)

xiaomi_ac.make_noise()
GREE_ac.make_noise()

AC.make_noise_static()
AC.make_noise()