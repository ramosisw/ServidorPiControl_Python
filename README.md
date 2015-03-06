# ServidorPiControl_Python
<h2>PiControl [Servidor]</h2>

<p>Componentes:</p>
<ul>
<li>Raspberry Pi</li>
<li>4 Leds (blanco, rolo, azul, verde)</li>
<li>4 resistencias 1k</li>
<li>Protroboard</li>
<li>Cables</li>
</ul>
<h3>Cargar Servidor</h3>
<p>Como primer paso es necesario cargar el servidor a la raspberry, ya sea pasando el archivo por FTP o Copiando las lineas de codigo</p>

<h3>Configuracion:</h3>
<ul>
  <li>La raspberry debe de estar conectada a la red local de tu Router y debes de saber la direccion IP de la misma (<i>Puedes utilizar una ramienta como <a href="http://www.advanced-ip-scanner.com/es/" target="new">Advanced IP Scanner</a> para saber la ip</i>)</li>
  <li>Realizar la sigueinte conexion de la raspberry pi
    <img src="https://github.com/ramosisw/ServidorPiControl_Python/blob/master/fritzing/serverPiControl_bb.png"/>
    <br/>
    <p>Los pines 8,10,12, son para los leds Rojo, Azul, Verde. el pin 22 es para el led Blanco, este se controlara la Intencidad por medio de PWM</p>
    <small>Cada led tiene su resistencia de 1k. Verificar que el diagrama de conexion este bien echo.</small>
  </li>
  <li>Una vez cargado el servidor y echo el diagrama de conexion, ejecutar el codigo 
    <br/> 
    <br/>
    <i>$ sudo python server.py</i>
    <br/>
    <br/>
    y si todo salio procedemos con la conexion de la App <a href="https://play.google.com/store/apps/details?id=mx.itson.picontrol" target="new">PiControl</a> se encuentra disponible en PlayStore
  </li>
</ul>
