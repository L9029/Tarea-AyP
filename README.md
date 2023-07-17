# Tarea-AyP

Realizado por: Angel Oca

## Informe de Resolución del Ejercicio

<p style="text-align: justify">El ejercicio de esta tarea requiere que dado cualquier arreglo de números enteros (pueden ser positivos o negativos) se debe de aplicar las operaciones necesarias para poder insertar en una pila los elementos de forma ordenada.</p>

<p style="text-align: justify">Para la resolución del ejercicio primero se creo la clase “Stack”, esta contiene todos los métodos que caracterizan a la pila con el fin de poder simular su funcionamiento. Toda la clase se guardo en el directorio “modules”, esto con el fin de llamarla como un modulo y que así sea mas fácil de leer el código, luego se creo el archivo “main.py”, el cual contiene la función que se encargara de organizar todos los elementos de un arreglo dado y retornar al final los elementos ordenados en una pila.</p>

<p style="text-align: justify">De “modules” se importo la clase “Stack” en el archivo “main.py” y se creo la función “my_stack_function()”, esta recibe como parámetro un arreglo de números y retorna una pila.</p>

<p style="text-align: justify">En la función principal, primero se crearon dos objetos pila, llamados “p” y “p2”, usando los métodos de la clase “Stack”, se creo un bucle for que recorriera todos los elementos del arreglo dado y los mismos fueran apilados en “p”.</p>

<p style="text-align: justify">Una vez apilado todos los elementos en “p”, se procedió a crear un ciclo while que como condición valide si la pila 1 “p” esta llena, en el caso de que este vaciá no entrara en el ciclo, luego se procede a desapilar el elemento top de la pila 1 “p” con el método “pop” de la clase “Stack”, este elemento es almacenado en la variable “act”, la cual servirá como un auxiliar para el elemento actual que se esta trabajando.</p>

<p style="text-align: justify">A continuación el algoritmo entra en la primera condición, la cual se encarga de verificar si la pila 2 “p2” se encuentra llena, en el caso de que este vaciá, se procede a apilar el elemento almacenado en la variable “act” a la pila 2 “p2”. Luego de que la pila 2 “p2” contenga un elemento procede a continuar de esa primera condición, se crea una variable “c” la cual contiene un valor negativo, el cual es el -1.</p>

<p style="text-align: justify">Luego se crea otro bucle while que tiene como condición que mientras “c” sea diferente del tamaño de “p2” este verificara unas condiciones las cuales son, primero verifica si “p2” esta vació, en el caso de que lo este, se apilara en “p2” el valor almacenado en “act” y se cambiara el valor de “c” para que el mismo sea el tamaño actual de la pila 2 “p2”, esto con el fin de que cuando entre de nuevo en el ciclo este detecte que los valores ya no son diferentes y salga del ciclo, la segunda condición es que valide si el elemento top de la pila 2 “p2” es menor que el elemento en “act” (esto se realizo con el método “top” de la clase “Stack”), entonces se desapila el elemento top en “p2”, se guarda ese proceso en una variable “s” y se apila el elemento en “s” en la pila 1 “p”, en caso de que esas dos condiciones no se ejecuten, se apilara el elemento en “act” en la pila 2 “p2” y se cambiara el valor de “c” para que el mismo igual al tamaño actual de la pila 2 “p2” con la finalidad de romper el ciclo.</p>

<p style="text-align: justify">Por ultimo la función retornara los elementos ordenados de la pila 2 “p2” y se imprimirán por pantalla. La lógica detrás del algoritmo es que este va a ir validando que el elemento top de la pila 2 sea menor que el elemento en la variable “act” y ira realizando el proceso de apilar en caso de que sea falso, en el caso de que sea verdadero, se desapilara el valor top de la pila 2 para sea apilado luego en la pila 1, todo esto con la finalidad de que llegue a un punto de que solo apilara los elementos ordenadamente, llegado a ese punto el primer ciclo while se detendrá, ya que la pila 1 “p” ya se se encuentra totalmente vaciá porque todos los elementos que se encontraban en la misma ya están almacenados ordenadamente en la pila 2 “p2” provocando así un break en el ciclo y la finalización del algoritmo de ordenamiento con el retorno de la pila 2 y sus elementos.</p>