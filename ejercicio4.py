print("\tBienvenido\n")

sueldo = float(input("Cantidad de sueldo es: "))


def calcular():


     afp_ars = 0.0591
     res = (sueldo  *  afp_ars)
     print(" De sueldo se le descontara "+ str(res)+ " para su AFP Y ARS ") 
     base_res = sueldo - res 
     sueldo_isr = (base_res * 12)


     if sueldo_isr <= 416220.00:
         print(" Eta exento de impuesto ")
        
     elif sueldo_isr >= 416220.01  and  sueldo_isr <= 624239.00 :
         res1= sueldo_isr - (416220.01)
         res2=  res1 * 0.15
         isr = res2 / 12
         print(" usted pagara " + str(isr)+ " de ISR ")

     elif sueldo_isr >= 624239.01 and sueldo_isr <= 867123.00:
         res1= sueldo_isr - 624239.01
         res2=  res1 * 0.20
         isr = res2 / 12
         print(" usted pagara " + str(isr)+ " de ISR ")

     elif sueldo_isr  >= 867123.01:
         res1= sueldo_isr - 867123.01
         res2=  res1 * 0.25
         isr = res2 / 12
         print(" usted pagara " + str(isr)+ " de ISR ")        

calcular()





