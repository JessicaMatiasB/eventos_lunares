# Diseño y Flujo de Datos del Proyecto

==================

## 1 Explicacion del Flujo de datos
Expliación del flujo de datoa desde la simulación hasta el DataMart

## 1.1 Simulacion de los datos
- Fuente: datos simulados que representan eventos lunares
- Formato: los datos se presentan en un formato CSV
- Frecuencia: Los datos se generean de manera semanal por lotes

## 1.2 Ingesta de Datos
- Proceso: Los datos se cargan en un sistema de almacenamiento intermedio Amazon S3
- Herramientas: Tecnología propuesta para producción Databricks, permite una integracion con servicios de almacenamiento en la nube como Amazon S3, ademas de utilizar Apache Spark para el procesamiento de los datos y proporciona una solida gobernanza y seguridad de los datos

## 1.3 Procesamiento de Datos
- Limpieza y transformación:
    - Estandarizacion de las fechas
    - Convertir datos a tipos apropiados
    - Manejo de valores faltantes

## 1.4 Carga al DataMart
- Estructura del DataMart: Esquema dimensional dasado en Hechos y Dimensiones
- Herramienta Databricks para cargar los datos procesados al DataMart


## 2 Justificación del Diseño dimensional
Al descomponer los datos de manera dimensional los datos se observan de una forma más simple,
y el diseño ayuda a comprender la relación entre los datos además de poder realizar consultas complejas de una manera más eficiente.

Este tipo de diseño dimensional nos permite expandirlo sin modificar las consultas previas.

## 2.1 Tabla de Hechos: eventos_lunares
- Propósito: Centralizar las métricas cuantitativas (e.g., clima, duración, hora).
- Claves Foráneas: Relación directa con las dimensiones ubicacion y tipo_evento.
- Beneficio: Facilita cálculos como promedios y  totales.

## 2.2 Dimensiones
- Ubicacion: Detalles geográficos (e.g., continente, region, país, ciudad) para segmentar datos por región.
- TipoEvento: Clasificación y descripción de eventos para análisis categóricos.

## 2.3 Diseño Estrella
- Beneficio: Permite realizar consultas rápidas y segmentadas sobre atributos específicos.


## 3 3. Herramientas Propuestas para Implementación en Producción

## 3.1 Orquestación
- Airflow: Para gestionar el flujo de trabajo desde la ingesta hasta la carga al DataMart.

## 3.2 Procesamiento
- Databricks: Plataforma ideal para procesar grandes volúmenes de datos con Apache Spark.

## 3.3 Almacenamiento
- Amazon S3: Almacenamiento escalable y de bajo costo para datos en bruto y procesados.

## 3.4 Monitorización
- Grafana y SparkUI: Para monitorizar el rendimiento del sistema y detectar problemas.

==================
## Documentación de Git
## 1. Crear el repositorio en tu cuenta de GitHub
## 2. Crear La estructuctura de las carpetas en Pycharm
## 3. Inicializar Git

```bash
    git init
```
## 4. Configuramos el repositorio remoto y vefrificamos
```bash
    git remote add origin <URL-del-repositorio>
    git remote -v
```
## 5. Creamos un branch para subir el código
```bash
    git checkout -b nueva_rama
```
## 6. Agregamos los archivos que queremos en preparacion
```bash
    git add mi_archivo_a_subir.txt
```
## 7. Agregamos un commit con la descripcion del cambio
```bash
    git commit -m "Añadir mi_archivo.txt a nueva_rama"
```
## 8. Subimos el cambio de local al repositorio remoto
```bash
    git push origin nueva_rama
```
## 9. Creamos una Pull Request en Github
En el repositorio de GitHub crear una nueva PR para integrar los cambios a main haciendo click en "Compare & pull request"
Asegúrate de que la base branch es master y la compare branch es nueva_rama.

Añade un título y una descripción para tu pull request.
Haz clic en "Create pull request".# Diseño y Flujo de Datos del Proyecto

==================

## 1 Explicacion del Flujo de datos
Expliación del flujo de datoa desde la simulación hasta el DataMart

## 1.1 Simulacion de los datos
- Fuente: datos simulados que representan eventos lunares
- Formato: los datos se presentan en un formato CSV
- Frecuencia: Los datos se generean de manera semanal por lotes

## 1.2 Ingesta de Datos
- Proceso: Los datos se cargan en un sistema de almacenamiento intermedio Amazon S3
- Herramientas: Tecnología propuesta para producción Databricks, permite una integracion con servicios de almacenamiento en la nube como Amazon S3, ademas de utilizar Apache Spark para el procesamiento de los datos y proporciona una solida gobernanza y seguridad de los datos

## 1.3 Procesamiento de Datos
- Limpieza y transformación:
    - Estandarizacion de las fechas
    - Convertir datos a tipos apropiados
    - Manejo de valores faltantes

## 1.4 Carga al DataMart
- Estructura del DataMart: Esquema dimensional dasado en Hechos y Dimensiones
- Herramienta Databricks para cargar los datos procesados al DataMart


## 2 Justificación del Diseño dimensional
Al descomponer los datos de manera dimensional los datos se observan de una forma más simple,
y el diseño ayuda a comprender la relación entre los datos además de poder realizar consultas complejas de una manera más eficiente.

Este tipo de diseño dimensional nos permite expandirlo sin modificar las consultas previas.

## 2.1 Tabla de Hechos: eventos_lunares
- Propósito: Centralizar las métricas cuantitativas (e.g., clima, duración, hora).
- Claves Foráneas: Relación directa con las dimensiones ubicacion y tipo_evento.
- Beneficio: Facilita cálculos como promedios y  totales.

## 2.2 Dimensiones
- Ubicacion: Detalles geográficos (e.g., continente, region, país, ciudad) para segmentar datos por región.
- TipoEvento: Clasificación y descripción de eventos para análisis categóricos.

## 2.3 Diseño Estrella
- Beneficio: Permite realizar consultas rápidas y segmentadas sobre atributos específicos.


## 3 3. Herramientas Propuestas para Implementación en Producción

## 3.1 Orquestación
- Airflow: Para gestionar el flujo de trabajo desde la ingesta hasta la carga al DataMart.

## 3.2 Procesamiento
- Databricks: Plataforma ideal para procesar grandes volúmenes de datos con Apache Spark.

## 3.3 Almacenamiento
- Amazon S3: Almacenamiento escalable y de bajo costo para datos en bruto y procesados.

## 3.4 Monitorización
- Grafana y SparkUI: Para monitorizar el rendimiento del sistema y detectar problemas.

==================
## Documentación de Git
## 1. Crear el repositorio en tu cuenta de GitHub
## 2. Crear La estructuctura de las carpetas en Pycharm
## 3. Inicializar Git

```bash
    git init
```
## 4. Configuramos el repositorio remoto y vefrificamos
```bash
    git remote add origin <URL-del-repositorio>
    git remote -v
```
## 5. Creamos un branch para subir el código
```bash
    git checkout -b nueva_rama
```
## 6. Agregamos los archivos que queremos en preparacion
```bash
    git add mi_archivo_a_subir.txt
```
## 7. Agregamos un commit con la descripcion del cambio
```bash
    git commit -m "Añadir mi_archivo.txt a nueva_rama"
```
## 8. Subimos el cambio de local al repositorio remoto
```bash
    git push origin nueva_rama
```
## 9. Creamos una Pull Request en Github
En el repositorio de GitHub crear una nueva PR para integrar los cambios a main haciendo click en "Compare & pull request"
Asegúrate de que la base branch es master y la compare branch es nueva_rama.

Añade un título y una descripción para tu pull request.
Haz clic en "Create pull request".

## 10. Mergeamos la PR desde GitHub
Hacemos el merge de la PR desde GitHub