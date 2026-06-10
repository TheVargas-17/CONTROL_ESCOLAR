# CONTROL ESCOLAR

## Descripción

Control Escolar es una aplicación desarrollada en Python utilizando Flet y MySQL que permite administrar información académica de estudiantes.

El sistema permite registrar alumnos, iniciar sesión, consultar información personal y administrar calificaciones de diferentes materias.

---

## Objetivo

Desarrollar una aplicación de escritorio que facilite la gestión de estudiantes y calificaciones mediante una interfaz gráfica amigable conectada a una base de datos MySQL.

---

## Funcionalidades

### Inicio de Sesión

* Validación de usuario y contraseña.
* Contraseñas cifradas mediante bcrypt.
* Acceso al sistema únicamente con credenciales válidas.

### Registro de Alumnos

* Registro de nuevos estudiantes.
* Validación de datos obligatorios.
* Validación de CURP.
* Validación de correo electrónico.
* Validación de matrícula.
* Validación de número telefónico.
* Prevención de usuarios duplicados.

### Dashboard

* Visualización de información del alumno.
* Consulta de especialidad.
* Consulta de promedio general.
* Acceso a módulos del sistema.

### Calificaciones

* Registro de calificaciones.
* Consulta de historial académico.
* Cálculo automático de promedio.
* Actualización de registros.
* Eliminación de registros.

### Perfil

* Consulta de información personal del alumno.

---

## Tecnologías Utilizadas

* Python 3.12
* Flet
* MySQL
* MySQL Connector
* bcrypt

---

## Estructura del Proyecto

CONTROL_ESCOLAR/

├── assets/

├── database/

│   └── conexion.py

├── models/

│   ├── usuario_model.py

│   ├── calificacion_model.py

│   └── materia_model.py

├── views/

│   ├── login.py

│   ├── registro.py

│   ├── dashboard.py

│   ├── perfil.py

│   └── calificaciones.py

├── main.py

└── README.md

---

## Base de Datos

La base de datos utilizada se llama:

control_escolar

Tablas principales:

* usuarios
* especialidades
* materias
* calificaciones

---

## Instalación

1. Instalar Python.
2. Instalar las dependencias:

pip install flet

pip install mysql-connector-python

pip install bcrypt

3. Crear la base de datos MySQL.
4. Configurar los datos de conexión en:

database/conexion.py

5. Ejecutar:

python main.py

---

## Autor

Leonardo Vargas

Proyecto desarrollado para la materia de Programación.
