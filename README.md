# signals_slots_py

_Clase base para implementar en python el mecanismo de signals y slots estilo Qt_

## Este repo consta de un solo fichero **signals_slots.py**. 
El código tiene una clase base que resuelve el problema:
```
class SigSlotObject:
  ...
```
El resto del código es un ejemplo de cómo usarla: 
La clase **Emiter** hereda de **SigSlotObject** y es la que emite la señal
```
class Emiter(SigSlotObject):
	def __init__(self):
		SigSlotObject.__init__(self)
		self.signal('ready') #declaración de la señal ´ready´
		
  #emiter 
	def emitir(self , msg):
    #algo de procesamiento antes de emitir la señal
		self.ready(msg ) #emitiendo la señal ´ready´
```

La clase **Receiver es la que recibe la señal:
```
class Receiver:
	def __init__(self , val):
		self.val =val
		
	def doer(self, msg ):
		print('Receiver::doer -> {msg} , and val = {val}'.format(msg=msg, val=self.val));	

```
Luego se crean las instancias de **Emiter** y **Receiver**

```		
def main():		
	e = Emiter()
	r1 = Receiver('soy r1')
	r2 = Receiver('y yo r2')
	e.connect('ready' , r1 , 'doer') #conectando la señal ´ready´ de e con el método ´doer´ de r1
	e.connect('ready' , r2 , 'doer') #conectando la señal ´ready´ de e con el método ´doer´ de r2
	e.emitir('HOla ')
  
  if __name__ == '__main__':
    main()
```	

