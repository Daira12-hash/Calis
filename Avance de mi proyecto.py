class Oximetro: 
     def ___init__(self,  marca, sp02, frecuencia_cardiaca, modelo):
            self.marca = marca 
            self.sp02 = sp02
            self.frecuencia_cardiaca = frecuencia_cardiaca
            self.modelo= modelo 
            
     def encender(self):
          print (f"El oximetro {self.marca} esta encendido.") 
   
     def registrar_medicion (self, nueva_sp02, nueva_frecuencia):
           self.sp02 = nueva_sp02 
           self.frecuencia_cardiaca = nueva_frecuencia 
           print (f"Medicion registrada: sp02{self.sp02}% y frecuencia cardiaca {self.frecuencia_cardiaca} lpm.")

     def mostrar_resultados(self):
           print (f"Oximetro: {self.marca}{self.modelo}")
           print (f"Frecuencia cardiaca: {self.frecuencia_cardiaca} lpm")  
    
     def actualizar_sp02 (self, nueva_sp02 ):
           self.nueva_sp02= nueva_sp02 
           print (f"La nueva medicion de Sp02 es de {self.sp02}%.")
        


     oximetro1= Oximetro("Beurer", "P030", 72, 98)
     oximetro2= Oximetro("Omron", "MC-725", 80, 95)
     oximetro3= Oximetro("Rossmax", "SB100", 75, 97)  

oximetro1.encender( )
oximetro1.mostrar_resultados( )

oximetro2.encender( )
oximetro2.registrar_medicion(110, 93)

oximetro3.encender( )
oximetro3.actualizar_sp02(99)

print ("Resultados finales")
oximetro1.mostrar_resultados( )
oximetro2.mostrar_resultados( )
oximetro3.mostrar_resultados ( )