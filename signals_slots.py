class SigSlotObject:
	def __init__(self):
		#********************************************
		#mapF : key = signalName
		#      value = {obj: objReciver  , slot: slotName}
		#
		#*********************************************/
		self.mapF = {}
		
	def signal(self, nameFun):
		self.mapF[nameFun] =  [] 
		className = type(self).__name__
		exec('def {nameFun}(self, val):\n\tfor v in self.mapF[\'{nameFun}\']:\n\t\tf=getattr(v[0],v[1])\n\t\tf(val)'.format(nameFun=nameFun))
		exec('{className}.{nameFun}={nameFun}'.format(className=className,nameFun=nameFun))
		f= getattr(self,nameFun)
		f=getattr(self,'signal')
		
	def connect(self, signalName , objReciver , slotName ):
		self.mapF[signalName].append( ( objReciver  , slotName) )	
	
class Emiter(SigSlotObject):
	def __init__(self):
		SigSlotObject.__init__(self)
		self.signal('ready')
		
	def emitir(self , msg):
		self.ready(msg )

class Receiver:
	def __init__(self , val):
		self.val =val
		
	def doer(self, msg ):
		print('Receiver::doer -> {msg} , and val = {val}'.format(msg=msg, val=self.val));
	

		
def main():		
	e = Emiter()
	r1 = Receiver('soy r1')
	r2 = Receiver('y yo r2')
	e.connect('ready' , r1 , 'doer')
	e.connect('ready' , r2 , 'doer')
	e.emitir('HOla ')
	

if __name__ == '__main__':
    main()