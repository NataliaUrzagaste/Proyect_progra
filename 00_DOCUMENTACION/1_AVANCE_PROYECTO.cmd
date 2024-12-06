Dispensador De Agua  
Natalia Belén Urzagaste Gonzales 
Luis Rodrigo Condori Susaño 
Antonio Vargas Arizaga 
Cristian Alejandro Ferreira Gareca 
Andrés Gallardo Garcia  
Docente: Ing. Kaleb Irahola Azad 
Universidad Católica Boliviana San Pablo 
Departamento de Ciencias de la Tecnología e Innovación 
Carrera de Ingeniería Mecatrónica 
Tarija 
Circuitos Electrónicos I 
29 de noviembre de 2024 

<<Dispensador de agua automático>>  
1 
Resumen ejecutivo 
El presente informe contiene la documentación del proyecto académico para la materia de Circuitos 
Electrónicos I. Este proyecto está diseñado para ofrecer una alternativa automatizada, eficiente, 
económica y rápida al proceso de llenado liquidos, con la capacidad de identificar distintos tipos 
de monedas y medir niveles de líquido mediante sensores inductivos. 
En cuanto al apartado técnico, el proyecto se basa en la implementación de un puente Wheatstone 
para medir variaciones físicas (resistencia, capacitancia o inductancia). El proyecto incluye 
diagramas y simulaciones realizadas en software especializado y la construcción de un prototipo 
funcional. 
El proyecto incluye un seguimiento mediante interfaz sobre el funcionamiento y datos recolectados 
a lo largo del tiempo por los sensores. 
Los resultados obtenidos, logran validar el funcionamiento del proyecto, estos fueron obtenidos en 
base a las simulaciones en el software y las distintas pruebas físicas, logrando así, demostrar la 
viabilidad de la solución con respecto al problema planteado. 
Palabras clave — 5 palabras o frases cortas que representen significativamente el 
trabajo separadas por comas. 
<<Dispensador de agua automático>>  
2 
I. Introducción 
En el presente informe de laboratorio se presenta la documentación del avance de proyecto de un 
dispensador automático de agua que se desarrolla para la materia de Circuitos Electrónicos I. El 
informe describe todas las etapas de la realización de este proyecto, desde la indagación teórica y 
el diseño conceptual hasta su implementación, con el objetivo de aplicar los conocimientos teóricos 
y prácticos adquiridos durante el transcurso de la materia. En el informe se destaca la importancia 
del puente de Wheatstone para medir las variaciones físicas como la resistencia o inductancia, 
haciendo uso de este como un sensor. 
A. Planteamiento del problema 
El dispensador de agua automático está diseñado para solucionar la problemática del llenado de 
botellas o vasos con diferentes tipos de líquidos o bebidas, ofreciendo una alternativa más 
económica, eficiente y rápida. Proporcionando una amplia variedad de bebidas posibles. 
B. Objetivos 
1) Objetivo General: 
Diseñar, simular e implementar un sensor analógico empleando un puente Wheatstone para medir 
variaciones físicas (resistencia, capacitancia o inductancia), con el objetivo de crear una máquina 
expendedora de bebidas con un sistema de tragamonedas con un sensor inductivo que detecte el 
tipo de moneda, además de otro sensor inductivo que mida el nivel de agua del envase. 
2) Objetivos Específicos del Proyecto: 
• Realizar los cálculos correctamente de los componentes resistivos para la 
realización del puente de Wheatstone. 
• Diseñar e implementar el dispositivo dispensador de bebidas con el puente de 
Wheatstone. 
• Crear la simulación del circuito en un software para validar el correcto 
funcionamiento del circuito. 
• El diseño e implementación de sensores para controlar el funcionamiento el 
correcto funcionamiento del dispositivo y recibir datos. 
• Realizar la conexión entre el dispositivo dispensador de bebidas con una interfaz 
para que se observen los datos que midan los sensores. 
<<Dispensador de agua automático>>  
3 
II. Marco teórico o investigativo 
A. Puente Wheatstone. 
1) Definición. 
La red de puentes más común y simple para encontrar la resistencia es el puente de 
Wheatstone. Este puente se utiliza donde se miden pequeños cambios en la resistencia, como en 
las aplicaciones de sensores. Esto se utiliza para convertir un cambio de resistencia en un cambio 
de voltaje de un transductor. 
La combinación de este puente con el amplificador operacional se usa ampliamente en 
industrias para varios transductores y sensores. Un puente de Wheatstone consta de cuatro 
resistencias que están conectadas en forma de diamante con la fuente de suministro y los 
instrumentos indicadores como se muestra en la figura. 
En el mundo real, nos encontramos con varias señales, algunas de ellas medidas por 
cambios en la resistencia y otras con inductancia y capacitancia. 
Si consideramos la resistencia, la mayoría de los sensores industriales como temperatura, 
tensión, humedad, desplazamiento, nivel de líquido, etc. produce el cambio en el valor de la 
resistencia para un cambio variable. Por lo tanto, existe la necesidad de un acondicionamiento de 
señal para cada sensor de resistencia. 
2) Ecuaciones. 
3) Perturbaciones 
Las perturbaciones en el puente Wheatstone o en general en los circuitos electrónicos son cualquier 
factor externo o interno no deseado que interfiere en el funcionamiento del circuito y que afecta su 
equilibrio o la precisión de sus mediciones. Estas perturbaciones pueden venir del entorno o del 
mismo circuito, y pueden o no estar relacionadas con la variable que se desea medir. Un ejemplo 
de perturbación en el puente puede ser una variación en el voltaje de entrada de la fuente de 
alimentación, ya que esto generaría errores en la medición.
4) Variaciones. 
Las variaciones en el puente Wheatstone son los cambios intencionales o esperados en las 
resistencias del puente, provocados por la variable que el sistema está diseñado para medir, estas 
variaciones son las que se capturan y se convierten en señales eléctricas dando al puente una 
funcionalidad de sensor. 
B. Sensor de nivel de líquido capacitivo. 
5) Definición. 
Un sensor capacitivo mide líquidos y solidos más granulados, este sensor detecta los 
cambios de la capacitancia, la capacitancia es la encargada de almacenar la carga eléctrica entre 
dos superficies, este sensor generará un campo eléctrico que va a variar dependiendo del tipo de 
material y que tan cercano esta ese material, a medida que la proximidad del material o liquido 
varia también va variando, el sensor traduce la variacion de carga en una señal que nos da el nivel 
con precisión.  
6) Señal. 
Un sensor capacitivo da una señal que depende del cambio de la capacitancia, el cambio de 
capacitancia de convierta en electricidad, que se procesa para que se pueda monitorear o controlar 
algún proceso, de acuerdo con el diseño del sensor este pueda dar una señal continua osea analógica 
como también puede dar una señal digital 
7) Aplicaciones del sensor de nivel de líquido capacitivo.    
Los sensores capacitivos se usan para medir niveles de líquidos y sólidos. Algunas de sus 
aplicaciones más comunes son: 
• Medición de niveles de agua: Ayudan a monitorear cuánto líquido hay en un 
tanque, evitando que se derrames o fugas. 
• Control de procesos industriales: Se usan en sistemas automáticos para 
controlar el llenado o vaciado de recipientes. 
• Detección de interfase de distintos líquidos y materiales: debido a sus 
propiedades eléctricas es capaz de decir dónde se encuentran dos líquidos 
diferentes, como agua y aceite.
D. Identificación de Requerimientos. 
Para el dispensador de agua, los requerimientos mínimos se definen de la siguiente manera: 
Variables físicas por medir: 
Nivel del agua en el depósito (medido con un sensor capacitivo). 
Detección de la inserción de una moneda (mediante un sensor inductivo). 
Rango de valores a detectar: 
Sensor capacitivo: Debe detectar niveles de agua en un rango de 0% cuando el tanque este 
vacío a 100% que es cuando el tanque está lleno,  
<<Dispensador de agua automático>>  
6 
Sensor inductivo: Debe ser capaz de detectar monedas metálicas utilizadas para que se 
active el sistema, ignorando otros objetos. 
Limitaciones del diseño: 
Sensor capacitivo: El diseño debe ser resistente a la corrosión y a las condiciones de 
humedad dentro del tanque.  
Sensor inductivo: El sensor debe estar calibrado para identificar monedas específicas, 
procurando que otros metales que estén cerca den falsos positivos. 
Otros requerimientos: 
Los sensores deben ser ensamblados manualmente, utilizando componentes accesibles y 
económicos. 
El diseño debe ser seguro y evitar riesgos eléctricos tanto para el usuario como para el 
sistema. 
La interfaz gráfica debe mostrar de forma clara el nivel de agua y registrar cada activación 
de las bombas al detectar una moneda para asegurar el recto mantenimiento del dispensador. 
A. Definición de funcionalidades. 
El diseño del dispensador de agua tendra las siguientes funcionalidades y caracteristicas: 
Obtención de mediciones: 
Sensor 
capacitivo: 
El sensor capacitivo mide el nivel de agua mediante el cambio de la capacitancia entre dos 
superficies. Esta variación se convierte en una señal para determinar el nivel de agua en el tanque. 
La señal será proporcional al nivel de agua y se leerá con un arduino para convertirla en un valor 
analógico y visualizable en la interfaz gráfica. 
Sensor 
inductivo: 
El sensor inductivo da una señal cuando detecta la presencia de una moneda metálica. Esta señal 
es de tipo digital, aunque puede ser analógica porque según la moneda devolverá un voltaje y así 
se reconoce que moneda está entrando, y se utiliza para activar o desactivar el sistema de 
dispensado de agua al ingresar una moneda. 
Puntos de calibración: 
Sensor 
capacitivo: 
El sensor capacitivo debe calibrarse para garantizar que los valores de capacitancia correspondan 
con los niveles de agua específicos. Los puntos de calibración serán: 
<<Dispensador de agua automático>>  
7 
Nivel mínimo (0%): Cuando el depósito está vacío. 
Nivel máximo (100%): Cuando el depósito está completamente lleno. 
Estos puntos serán ajustados manualmente utilizando un código del Arduino. 
Sensor 
inductivo: 
El sensor inductivo debe calibrarse para reconocer únicamente un unico tipo de moneda utilizadas 
en el sistema. El punto de calibración será la distancia a la que el sensor detecta la moneda, y el 
cómo se basa para distinguirla de otros objetos metálicos. 
Otros datos relevantes a la funcionalidad: 
Interfaz gráfica: La interfaz gráfica mostrará en tiempo real el nivel de agua y las 
activaciones de las bombas al detectar monedas. La visualización del nivel de agua será una 
representación proporcional del voltaje que dé el sensor capacitivo. 
Control de bombas: El sistema activará las bombas automáticamente cuando se detecte una 
moneda, y se apagará cuando se complete el dispensado.