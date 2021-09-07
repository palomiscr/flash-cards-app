# flash-cards-app

## Descripción
Esta aplicación de tarjetas o flash cards permite aprender palabras en francés.
Al iniciar el juego la app enseña automáticamente una palabra en francés, y después de 3 segundos "dará la vuelta" a la carta
para mostrar la solución en inglés. En ese momento el usuario podrá pulsar el botón de check verde para indicar que ha aprendido
la palabra, en cuyo caso no volverá a aparecer más. Si por el contrario pulsa el botón rojo con la cruz, significa que no la ha aprendido, 
por lo que podrá aparecer más tarde.

En ambos casos al pulsar el botón se enseña la siguiente carta. 

El juego acaba cuando se adivinen todas las palabras, en cuyo caso hay que borrar el fichero "words_to_learn.csv" para reiniciarlo. 

## Implementación
La interfaz está hecha con tkinter, y para manejar la lista de palabras personalizadas del usuario se usa pandas

## Posibles mejoras
- dar a elegir al usuario al inicio qué idioma quiere aprender y en qué idioma quiere que estén las respuestas
- añadir botón que permita reiniciar el juego
