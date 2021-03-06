import unittest
import os
from Vier_Gewinnt_KI import KI

class Test_test_KI(unittest.TestCase):
    ###################################################
    #                                                 #
    #  Gewinnen des Gegners soll verhindert werden    #
    #                                                 #
    ###################################################

    # erkennung von Diagonalen, wenn drei Steine gegeben sind
    #==========================================================================================================
    def test_A(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[2][1] = "ge"
        Array[3][2] = "ge"
        Array[4][3] = "ge"
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(4,Output,"Diagonale nach rechts unten funktionier nicht")
        print("Test A Zug: "+ str(Output))

    def test_A_1(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[1][2] = "gr"
        Array[2][3] = "gr"
        Array[3][0] = "gr"
        #Array[3][4] = "gr"
        Array[4][1] = "gr"
        Array[5][2] = "gr"
        #====
        Array[1][0] = "gr"
        Array[2][1] = "ge"
        Array[3][2] = "ge"
        Array[4][3] = "ge"
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(4,Output,"Diagonale nach rechts unten funktionier nicht")
        print("Test A_1 Zug: "+ str(Output))
    #=========================================================================================================================================



    # Erkennung von Waagerechten wenn drei Steine gegeben sind
    #=========================================================================================================================================
    def test_B(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][0] = "ge"
        Array[5][1] = "ge"
        Array[5][2] = "ge"
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(3,Output,"einfache waagerechte funktioniert nicht")
        print("Test B Zug: "+ str(Output))

    def test_C(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][0] = "gr"
        Array[5][1] = "ge"
        Array[5][2] = "ge"
        Array[5][3] = "ge"
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(4,Output,"einfache waagerechte mit einem grünen Stein funktioniert nicht")
        print("Test C Zug: "+ str(Output))

    def test_D(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][0] = "gr"
        Array[5][3] = "ge"
        Array[5][4] = "ge"
        Array[5][5] = "ge"
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(2,Output,"waagerechte funktioniert nicht")
        print("Test D Zug: "+ str(Output))

    def test_E(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][0] = "gr"
        Array[5][1] = "gr"
        Array[5][2] = "gr"
        Array[5][3] = "ge"
        Array[5][4] = "ge"
        Array[5][5] = "ge"
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(6,Output,"waagerechte funktioniert nicht")
        print("Test E Zug: "+ str(Output))
    #==============================================================================================================================

    # Erkennung von senkrechten wenn drei Steine gegeben sind
    #============================================================================================================================
    def test_F(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][0] = "gr"
        Array[5][1] = "gr"
        Array[5][5] = "gr"
        Array[4][3] = "gr"
        Array[3][3] = "gr"
        Array[1][3] = "gr"

        Array[5][2] = "ge"
        Array[5][3] = "ge"
        Array[5][4] = "ge"
        Array[4][1] = "ge"
        Array[4][2] = "ge"
        Array[2][3] = "ge"
        Array[3][2] = "ge"

        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(2,Output,"senkrechte funktioniert nicht")
        print("Test F Zug: "+ str(Output))

    #==============================================================================================================================

    # Überprüfung ob KI spalten auslässt, damit sie nicht verliert
    #============================================================================================================================
    def test_G(self):
        #for i in range(100):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][5] = "gr"
        Array[5][4] = "gr"
        Array[4][5] = "gr"
        Array[4][2] = "gr"
        Array[2][3] = "gr"


        Array[5][2] = "ge"
        Array[5][3] = "ge"
        Array[4][4] = "ge"
        Array[4][3] = "ge"
        Array[3][2] = "gr"
        Array[3][3] = "ge"
        Array[3][4] = "ge"

        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertIsNot(5,Output,"waagerecht und Diagonal")
        print("Test G Zug: "+ str(Output))
            #print("Zug: "+str(Output))
    
    def test_H(self):
        #for i in range(100):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[4][2] = "ge"
        Array[4][3] = "ge"
        Array[4][4] = "ge"
        Array[5][2] = "gr"
        Array[5][3] = "ge"
        Array[5][4] = "gr"

        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertIsNot(1,Output,"waagerechte")
        self.assertIsNot(5,Output,"waagerechte")
        print("Test H Zug: "+ str(Output))
        #print("Zug: "+str(Output))

    ## zwei Stein Erkennung
    def test_I(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][4] = "ge"
        Array[5][3] = "ge"

        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(2,Output,"Test I ist fehlgeschlagen")
        print("Test I Zug: "+ str(Output))

    def test_J(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][3] = "ge"
        Array[4][3] = "gr"

        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(2,Output,"Test J ist fehlgeschlagen")
        print("Test J Zug: "+ str(Output))

    def test_K(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][3] = "ge"
        Array[4][3] = "ge"

        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(3,Output,"Test K ist fehlgeschlagen")
        print("Test K Zug: "+ str(Output))

    def test_L(self):
        Viergewinnt_ki = KI("ge","gr")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][0] = "gr"
        Array[5][1] = "ge"
        Array[5][2] = "ge"
        Array[5][3] = "ge"
        Array[5][4] = "gr"

        Array[4][0] = "gr"
        Array[4][1] = "ge"
        Array[4][2] = "gr"
        Array[4][3] = "gr"
        Array[4][4] = "gr"
        
        Array[3][0] = "ge"
        Array[3][1] = "ge"
        Array[3][2] = "ge"
        Array[3][3] = "gr"

        Array[2][1] = "gr"
        Array[2][2] = "gr"
        Array[2][3] = "ge"
    
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(1,Output,"Test L ist fehlgeschlagen")
        print("Test L Zug: "+ str(Output))

    def test_M(self):

        Viergewinnt_ki = KI("ge","gr")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][0] = "gr"
        Array[5][1] = "ge"
        Array[5][2] = "ge"
        Array[5][3] = "ge"
        Array[5][4] = "gr"

        Array[4][0] = "gr"
        Array[4][1] = "ge"
        Array[4][2] = "gr"
        Array[4][3] = "gr"
        Array[4][4] = "gr"
        
        Array[3][0] = "ge"
        Array[3][1] = "ge"
        Array[3][2] = "ge"
        Array[3][3] = "gr"
        Array[3][4] = "gr"

        Array[2][1] = "gr"
        Array[2][2] = "gr"
        Array[2][3] = "ge"

        Array[1][1] = "ge"
    
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(4,Output,"Test M ist fehlgeschlagen")
        print("Test M Zug: "+ str(Output))

    def test_N(self):
        Viergewinnt_ki = KI("ge","gr")
        Array = [["w" for x in range(7)] for y in range(6)]


        Array[5][2] = "gr"
        Array[5][3] = "ge"
        Array[5][4] = "ge"

        Array[4][3] = "gr"
        Array[4][4] = "gr"

    
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(2,Output,"Test N ist fehlgeschlagen")
        print("Test N Zug: "+ str(Output))

    def test_O(self):
        #for i in range(100):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]

        Array[5][0] = "gr"
        Array[5][1] = "gr"
        Array[5][2] = "gr"
        Array[5][3] = "ge"
        Array[5][4] = "ge"
        Array[5][5] = "ge"
        Array[5][6] = "gr"

        Array[4][0] = "ge"
        Array[4][1] = "ge"
        Array[4][2] = "ge"
        Array[4][3] = "gr"
        Array[4][4] = "gr"

        Array[3][1] = "gr"
        Array[3][2] = "ge"
        Array[3][3] = "ge"
        Array[3][4] = "ge"

        Array[2][2] = "gr"
        Array[2][3] = "ge"

        Array[1][2] = "gr"
        Array[1][3] = "ge"

        Array[0][3] = "gr"

    
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertIsNot(5,Output,"Test O ist fehlgeschlagen")
        print("Test O Zug: "+ str(Output))

    def test_P(self):
        Viergewinnt_ki = KI("ge","gr")
        Array = [["w" for x in range(7)] for y in range(6)]

        Array[5][0] = "gr"
        Array[5][1] = "gr"
        Array[5][2] = "gr"
        Array[5][3] = "ge"
        Array[5][4] = "ge"
        Array[5][5] = "ge"
        Array[5][6] = "gr"

        Array[4][0] = "ge"
        Array[4][1] = "ge"
        Array[4][2] = "ge"
        Array[4][3] = "gr"
        Array[4][4] = "gr"

        Array[3][1] = "gr"
        Array[3][2] = "ge"
        Array[3][3] = "ge"
        Array[3][4] = "ge"

        Array[2][2] = "gr"
        Array[2][3] = "ge"

        Array[1][2] = "gr"
        Array[1][3] = "ge"

        Array[0][3] = "gr"

    
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
  #      print("Test P Zug: "+ str(Output))
        self.assertIsNot(5,Output,"Test P ist fehlgeschlagen")
        print("Test P Zug: "+ str(Output))

    def test_Q(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]


        Array[5][1] = "gr"
        Array[5][2] = "ge"
        Array[5][3] = "ge"
        Array[5][4] = "ge"
        Array[5][5] = "gr"
        Array[5][6] = "gr"

        Array[4][1] = "gr"
        Array[4][2] = "ge"
        Array[4][3] = "ge"
        Array[4][4] = "gr"

        Array[3][1] = "ge"
        Array[3][2] = "w"
        Array[3][3] = "gr"
        Array[3][4] = "ge"
    
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertIsNot(2,Output,"Test Q ist fehlgeschlagen")
        print("Test Q Zug: "+ str(Output))

    def test_R(self):
        #for i in range(100):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]


     
        Array[5][2] = "gr"
        Array[5][3] = "ge"
        Array[5][4] = "gr"
 

        Array[4][2] = "ge"
        Array[4][3] = "ge"
        Array[4][4] = "ge"

        Array[3][2] = "gr"
        Array[3][3] = "gr"
        Array[3][4] = "gr"

        Array[2][2] = "ge"
        Array[2][3] = "gr"
        Array[2][4] = "ge"

        Array[1][2] = "ge"
        Array[1][3] = "w"
        Array[1][4] = "gr"

        Array[0][4] = "ge"
    
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        print("Test R Zug: "+ str(Output))
        self.assertIsNot(5,Output,"Test R ist fehlgeschlagen")

    def test_S(self):
        Viergewinnt_ki = KI("ge","gr")
        Array = [["w" for x in range(7)] for y in range(6)]


     
        Array[5][1] = "ge"
        Array[5][2] = "gr"
        Array[5][3] = "ge"
        Array[5][5] = "ge"
        Array[5][6] = "gr"
 

        Array[4][1] = "gr"
        Array[4][2] = "ge"
        Array[4][3] = "ge"
        Array[4][5] = "ge"
        Array[4][6] = "gr"

        Array[3][2] = "gr"
        Array[3][3] = "gr"
        Array[3][5] = "gr"

        Array[2][2] = "ge"
        Array[2][3] = "gr"
        Array[2][5] = 'ge'

        Array[1][2] = "ge"
        Array[1][5] = "gr"
        Array[1][4] = "w"

        Array[0][2] = "gr"
        Array[0][5] = "ge"
    
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        print("Test S Zug: "+ str(Output))
        self.assertEqual(0,Output,"Test S ist fehlgeschlagen")
  
    def test_T(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]


        Array[0][0] = 'gr'
        Array[1][0] = 'ge'
        Array[2][0] = 'gr'
        Array[3][0] = 'ge'
        Array[4][0] = 'ge'
        Array[5][0] = 'gr'
        Array[0][2] = 'gr'
        Array[1][2] = 'ge'
        Array[2][2] = 'ge'
        Array[3][2] = 'gr'
        Array[4][2] = 'ge'
        Array[5][2] = 'gr'
        Array[0][3] = 'gr'
        Array[1][3] = 'ge'
        Array[2][3] = 'gr'
        Array[3][3] = 'gr'
        Array[4][3] = 'ge'
        Array[5][3] = 'ge'
        Array[5][4] = 'ge'
        Array[0][5] = 'ge'
        Array[1][5] = 'gr'
        Array[2][5] = 'w'
        Array[3][5] = 'gr'
        Array[4][5] = 'ge'
        Array[5][5] = 'gr'
        Array[0][6] = 'gr'
        Array[1][6] = 'ge'
        Array[2][6] = 'gr'
        Array[3][6] = 'ge'
        Array[4][6] = 'ge'
        Array[5][6] = 'gr'

    
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        print("Test T Zug: "+ str(Output))
        self.assertEqual(4,Output,"Test T ist fehlgeschlagen")


    def test_U(self):
      # for i in range(10000):
        Viergewinnt_ki = KI("ge","gr")
        Array = [["w" for x in range(7)] for y in range(6)]

        Array[0][0] = 'ge'
        Array[1][0] = 'gr'
        Array[2][0] = 'ge'
        Array[3][0] = 'gr'
        Array[4][0] = 'ge'
        Array[5][0] = 'gr'
        Array[0][2] = 'gr'
        Array[1][2] = 'ge'
        Array[2][2] = 'ge'
        Array[3][2] = 'gr'
        Array[4][2] = 'ge'
        Array[5][2] = 'gr'
        Array[0][3] = 'gr'
        Array[1][3] = 'ge'
        Array[2][3] = 'gr'
        Array[3][3] = 'gr'
        Array[4][3] = 'ge'
        Array[5][3] = 'ge'
        Array[0][5] = 'ge'
        Array[1][5] = 'gr'
        Array[2][5] = 'ge'
        Array[3][5] = 'gr'
        Array[4][5] = 'ge'
        Array[5][5] = 'gr'
        Array[0][6] = 'gr'
        Array[1][6] = 'ge'
        Array[2][6] = 'gr'
        Array[3][6] = 'ge'
        Array[4][6] = 'ge'
        Array[5][6] = 'gr'

    
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        print("Test U Zug: "+ str(Output))
        self.assertEqual(4,Output,"Test U ist fehlgeschlagen")


    def test_V(self):
        Viergewinnt_ki = KI("ge","gr")
        Array = [["w" for x in range(7)] for y in range(6)]

        Array[4][0] = 'ge'
        Array[5][0] = 'ge'
        Array[0][1] = 'gr'
        Array[1][1] = 'gr'
        Array[2][1] = 'ge'
        Array[3][1] = 'ge'
        Array[4][1] = 'gr'
        Array[5][1] = 'gr'
        Array[0][2] = 'ge'
        Array[1][2] = 'gr'
        Array[2][2] = 'gr'
        Array[3][2] = 'gr'
        Array[4][2] = 'ge'
        Array[5][2] = 'ge'
        Array[0][3] = 'gr'
        Array[1][3] = 'gr'
        Array[2][3] = 'ge'
        Array[3][3] = 'ge'
        Array[4][3] = 'gr'
        Array[5][3] = 'ge'
        Array[0][4] = 'gr'
        Array[1][4] = 'ge'
        Array[2][4] = 'gr'
        Array[3][4] = 'ge'
        Array[4][4] = 'ge'
        Array[5][4] = 'ge'
        Array[2][5] = 'gr'
        Array[3][5] = 'gr'
        Array[4][5] = 'ge'
        Array[5][5] = 'gr'
        Array[0][6] = 'gr'
        Array[1][6] = 'ge'
        Array[2][6] = 'gr'
        Array[3][6] = 'ge'
        Array[4][6] = 'ge'
        Array[5][6] = 'gr'
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        print("Test V Zug: "+ str(Output))
        self.assertEqual(0,Output,"Test V ist fehlgeschlagen")

    
    def test_X(self):  
        Viergewinnt_ki = KI("ge","gr")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[0][0] = 'gr'
        Array[1][0] = 'ge'
        Array[2][0] = 'gr'
        Array[3][0] = 'ge'
        Array[4][0] = 'ge'
        Array[5][0] = 'gr'
        Array[0][2] = 'gr'
        Array[1][2] = 'ge'
        Array[2][2] = 'ge'
        Array[3][2] = 'gr'
        Array[4][2] = 'ge'
        Array[5][2] = 'gr'
        Array[0][3] = 'gr'
        Array[1][3] = 'ge'
        Array[2][3] = 'gr'
        Array[3][3] = 'gr'
        Array[4][3] = 'ge'
        Array[5][3] = 'ge'
        Array[0][5] = 'gr'
        Array[1][5] = 'ge'
        Array[2][5] = 'gr'
        Array[3][5] = 'ge'
        Array[4][5] = 'ge'
        Array[5][5] = 'gr'
        Array[0][6] = 'gr'
        Array[1][6] = 'ge'
        Array[2][6] = 'gr'
        Array[3][6] = 'ge'
        Array[4][6] = 'gr'
        Array[5][6] = 'ge'


        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        print("Test X Zug: "+ str(Output))
        self.assertIsNot(1,Output,"Test X ist fehlgeschlagen")

    def test_Y(self):
        Viergewinnt_ki = KI("ge","gr")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[0][0] = 'gr'
        Array[1][0] = 'ge'
        Array[2][0] = 'gr'
        Array[3][0] = 'ge'
        Array[4][0] = 'ge'
        Array[5][0] = 'gr'
        Array[0][1] = 'gr'
        Array[1][1] = 'ge'
        Array[2][1] = 'gr'
        Array[3][1] = 'ge'
        Array[4][1] = 'ge'
        Array[5][1] = 'gr'
        Array[0][3] = 'gr'
        Array[1][3] = 'ge'
        Array[2][3] = 'ge'
        Array[3][3] = 'gr'
        Array[4][3] = 'ge'
        Array[5][3] = 'ge'
        Array[0][4] = 'gr'
        Array[1][4] = 'ge'
        Array[2][4] = 'gr'
        Array[3][4] = 'gr'
        Array[4][4] = 'ge'
        Array[5][4] = 'gr'
        Array[0][5] = 'gr'
        Array[1][5] = 'ge'
        Array[2][5] = 'gr'
        Array[3][5] = 'ge'
        Array[4][5] = 'gr'
        Array[5][5] = 'ge'
        Array[4][6] = 'ge'
        Array[5][6] = 'gr'
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        print("Test Y Zug: "+ str(Output))
        self.assertEqual(6,Output,"Test Y ist fehlgeschlagen")

    def test_Z(self):
        Viergewinnt_ki = KI("ge","gr")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][3] = 'ge'
        Array[5][4] = 'gr'

        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        print("Test Z Zug: "+ str(Output))
        self.assertEqual(2,Output,"Test Z ist fehlgeschlagen")

    def test_AA(self):
   #     for i in range(100):
        Viergewinnt_ki = KI("ge","gr")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[4][0] = 'ge'
        Array[5][0] = 'gr'
        Array[0][1] = 'ge'
        Array[1][1] = 'gr'
        Array[2][1] = 'ge'
        Array[3][1] = 'ge'
        Array[4][1] = 'gr'
        Array[5][1] = 'ge'
        Array[0][2] = 'ge'
        Array[1][2] = 'ge'
        Array[2][2] = 'gr'
        Array[3][2] = 'ge'
        Array[4][2] = 'ge'
        Array[5][2] = 'gr'
        Array[0][3] = 'gr'
        Array[1][3] = 'gr'
        Array[2][3] = 'ge'
        Array[3][3] = 'gr'
        Array[4][3] = 'gr'
        Array[5][3] = 'ge'
        Array[0][4] = 'gr'
        Array[1][4] = 'gr'
        Array[2][4] = 'ge'
        Array[3][4] = 'gr'
        Array[4][4] = 'ge'
        Array[5][4] = 'ge'
        Array[4][5] = 'gr'
        Array[5][5] = 'gr'


        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        print("Test AA Zug: "+ str(Output))
        self.assertEqual(6,Output,"Test AA ist fehlgeschlagen")

    def test_AB(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]

        Array[0][0] = 'ge'
        Array[1][0] = 'gr'
        Array[2][0] = 'ge'
        Array[3][0] = 'gr'
        Array[4][0] = 'ge'
        Array[5][0] = 'gr'
        Array[3][1] = 'gr'
        Array[4][1] = 'ge'
        Array[5][1] = 'ge'
        Array[0][2] = 'ge'
        Array[1][2] = 'gr'
        Array[2][2] = 'ge'
        Array[3][2] = 'ge'
        Array[4][2] = 'gr'
        Array[5][2] = 'gr'
        Array[0][3] = 'ge'
        Array[1][3] = 'gr'
        Array[2][3] = 'gr'
        Array[3][3] = 'ge'
        Array[4][3] = 'gr'
        Array[5][3] = 'ge'
        Array[0][4] = 'gr'
        Array[1][4] = 'ge'
        Array[2][4] = 'gr'
        Array[3][4] = 'gr'
        Array[4][4] = 'ge'
        Array[5][4] = 'ge'
        Array[4][5] = 'ge'
        Array[5][5] = 'gr'
        Array[2][6] = 'ge'
        Array[3][6] = 'gr'
        Array[4][6] = 'ge'
        Array[5][6] = 'gr'



        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        print("Test AB Zug: "+ str(Output))
        self.assertEqual(5,Output,"Test AB ist fehlgeschlagen")

    def test_AC(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]

        Array[4][1] = 'ge'
        Array[5][1] = 'ge'
        Array[1][2] = 'gr'
        Array[2][2] = 'gr'
        Array[3][2] = 'ge'
        Array[4][2] = 'gr'
        Array[5][2] = 'gr'
        Array[0][3] = 'ge'
        Array[1][3] = 'ge'
        Array[2][3] = 'gr'
        Array[3][3] = 'gr'
        Array[4][3] = 'ge'
        Array[5][3] = 'ge'
        Array[2][5] = 'gr'
        Array[3][5] = 'ge'
        Array[4][5] = 'ge'
        Array[5][5] = 'gr'
        Array[4][6] = 'ge'
        Array[5][6] = 'gr'




        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        print("Test AC Zug: "+ str(Output))
        self.assertIsNot(4,Output,"Test Ac ist fehlgeschlagen")

    def test_AD(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]

        Array[3][0] = 'ge'
        Array[4][0] = 'ge'
        Array[5][0] = 'ge'
        Array[0][1] = 'gr'
        Array[1][1] = 'ge'
        Array[2][1] = 'gr'
        Array[3][1] = 'ge'
        Array[4][1] = 'gr'
        Array[5][1] = 'gr'
        Array[0][2] = 'gr'
        Array[1][2] = 'ge'
        Array[2][2] = 'gr'
        Array[3][2] = 'gr'
        Array[4][2] = 'ge'
        Array[5][2] = 'ge'
        Array[0][3] = 'gr'
        Array[1][3] = 'ge'
        Array[2][3] = 'ge'
        Array[3][3] = 'gr'
        Array[4][3] = 'ge'
        Array[5][3] = 'ge'
        Array[0][5] = 'gr'
        Array[1][5] = 'ge'
        Array[2][5] = 'gr'
        Array[3][5] = 'ge'
        Array[4][5] = 'gr'
        Array[5][5] = 'gr'
        Array[0][6] = 'gr'
        Array[1][6] = 'ge'
        Array[2][6] = 'gr'
        Array[3][6] = 'ge'
        Array[4][6] = 'gr'
        Array[5][6] = 'ge'

        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        print("Test AD Zug: "+ str(Output))
        self.assertEqual(0,Output,"Test AD ist fehlgeschlagen")

        


if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        print("Absturz")

