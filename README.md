# CC-22-23-Extraordinaria
Estudiante: Javier Sáez de la Coba

Repositorio utilizado para la realización y entrega de la convocatoria extraordinaria de la asignatura Cloud Computing del Máster en Ingeniería Informática de la Universidad de Granada.


## Descripción del servicio.

En este repositorio se puede encontrar un microservicio para consultar si un número es primo o no.
Por si mismo no hace ninguna comprobación, sino que es capaz de almacenar la primalidad de un número dado para su posterior consulta. Para la facilidad de pruebas los números del 1 al 10 ya están precargados en la base de datos.

El servicio expone una API REST para la consulta y modificación de los datos usando el estandar REST (así como los verbos HTTP estándares).

### Endpoint /primes

Ejemplo de consulta:
GET /primes

Respuesta: HTTP 200
```json
[{"number":1,"prime":false},{"number":2,"prime":true},{"number":3,"prime":true},{"number":4,"prime":false},{"number":5,"prime":true},{"number":6,"prime":false},{"number":7,"prime":true},{"number":8,"prime":false},{"number":9,"prime":false},{"number":10,"prime":false}]
```

GET /primes/1/
Respuesta: HTTP 200
```json
{"number":1,"prime":false}
```

POST /primes/
Cuerpo de la petición:
{"number": 13, "prime": true}

(Ejemplo con curl en localhost)
```bash
curl -XPOST http://localhost:8000/primes/ --data '{"number":13,"prime":true}' -H "Content-Type: application/json"
```

Respuesta: HTTP 201 (Creado)
```json
{"number":13,"prime":true}
```

PATCH /primes/13/
Cuerpo de la petición:
{"number": 13, "prime": false}

(Ejemplo con curl en localhost)
```bash
curl -XPATCH http://localhost:8000/primes/13/ --data '{"number":13,"prime":false}' -H "Content-Type: application/json"
```

Respuesta: HTTP 200
```json
{"number":13,"prime":false}
```

DELETE /primes/13/

Respuesta: HTTP 204 No Content


### Tecnología del servicio

El servicio se ha construido utilizando Django y Django Rest Framework para su desarrollo. Esto se debe a las facilidades de integración con distintos sistemas de bases de datos y la rapidez de programación y seguridad integrada de las APIs REST generadas con estas herramientas.

## Empaquetamiento del servicio como contenedor.

El servicio se puede empaquetar como un contenedor. Para ello se puede generar una imagen docker con el Dockerfile proporcionado. Esta imagen está basada en python:slim, por lo que el tamaño de la imagen es reducido (para lo sencillo que es el servicio no nos hacen falta más librerías en la imagen base.). Se podría haber usado python con base alpine pero a veces da problemas dentro de RedUGR, por lo que se ha usado la versión basada en Debian.

Se puede construir (y correr) usando el comando:
```bash
docker build -t jscobaccextra:1 .
docker run  -p 8080:8000 -it jscobaccextra:1
```

En este modo el servicio todavía no es persistente (no se guardan datos entre reinicios).