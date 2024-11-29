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