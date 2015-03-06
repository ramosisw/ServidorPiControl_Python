import socket
import RPi.GPIO as GPIO
import time

pinLedRojo = 12
pinLedAzul = 10
pinLedVerde = 8

pinPwm = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinLedRojo,GPIO.OUT)
GPIO.setup(pinPwm,GPIO.OUT)

p= GPIO.PWM(pinPwm,100)
p.start(0)

def ledRojo(estado):
	if(estado==1):
		GPIO.output(pinLedRojo,True)
	else:
		GPIO.output(pinLedRojo,False)
def Pwm(estado):
	if(estado>=0 and estado<=100):
		p.ChangeDutyCycle(estado)
		print(estado)
		
ledRojo(0)
Pwm(0)

#funcion para decidir que hacer con los comandos
def prosdata(data):
	try:
		if(data.find('A')==0):
			ledRojo(int(data[1:]))
		if(data.find('P')==0):
			Pwm(int(data[1:]))
		print("Recivido: "+data)
	except ValueError:
		print("Error al procesar el dato: "+data)


#Inicializar el Socket
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#ip de la raspberry a donde escuchara el socket
host='0.0.0.0'
#host='0.0.0.0'
#puerto de escucha
port=8080
#imprimir el puerto y host
print("Escuchando en " + host + ":" + str(port))

#crear socket
serversocket.bind((host,port))
#empezar a escuchar
serversocket.listen(5)
print('server started listening')
try:
	while True:
		#enviar comandos por defecto (opcional)
		print("esperando conexion..")
		#si es aceptada una conexion
		(clientsocket,address)=serversocket.accept()
		#si esta inactivo por 15 seg lo desconectara
		clientsocket.settimeout(15)

		print("connection established from : ",address)
		while True:
			try:
				data = clientsocket.recv(512).decode('utf-8')
				#si son datos vacios terminar conexion
				if(data==''):
					break
			#si se acaba el tiempo de espera
			except socket.timeout:
				print ("connection was closed with ",address)
				clientsocket.close()
				break
			#si es interrumpido por el teclado "Ctrl + C"
			except KeyboardInterrupt:
				clientsocket.close()
				break
			#si ocurre un error
			except IOError:
				clientsocket.close()
				print ("error... reset server")
				break
			#si ocurre otro error
			except Error:
				clientsocket.close()
				print ("error... reset server")
				break

			#processar datos enviados al servidor
			prosdata(data)
		print("desconectado...")
except KeyboardInterrupt:
	GPIO.cleanup()
	print ("Cerrar todo")
