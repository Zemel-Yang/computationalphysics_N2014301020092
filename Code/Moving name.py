import os
import time
i=os.system('cls')
a0 = "##### ##### #       # ##### #     #    # ######  #     # ######"
a1 = "   #  #     ##     ## #     #      #  #  #    #  # #   # #     "
a2 = "  #   ##### # #   # # ##### #        #   ######  #  #  # #  ###"
a3 = " #    #     #  # #  # #     #        #   #    #  #   # # #    #"
a4 = "##### ##### #   #   # ##### #####    #   #    #  #     # ######"
b = 0
while b < 11:
      print ('   '*b+a0)
      print ('   '*b+a1) 
      print ('   '*b+a2)
      print ('   '*b+a3)
      print ('   '*b+a4)
      time.sleep(1)
      i=os.system('cls')
      b += 1