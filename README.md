# Cifrado César en Python

Programa de consola que permite **cifrar y descifrar textos** utilizando el algoritmo clásico de cifrado César.

Soporta:

* Español (incluye ñ)
* Inglés
* Mayúsculas
* Vocales acentuadas (á é í ó ú)
* Limpieza automática de pantalla en Windows

---

## Requisitos

* Python 3 instalado
* Sistema operativo Windows (usa `cls` para limpiar pantalla)

Verificar instalación:

```bash
python --version
```

---

## Obtener el proyecto

Clona el repositorio desde GitHub:

```bash
git clone https://github.com/ALetsee/Cifrado-Cesar.git
cd Cifrado-Cesar
```

## Ejecución

Coloca el archivo `Cesar.py` en una carpeta y abre una terminal en esa ubicación.

Ejecuta:

```bash
python Cesar.py
```

---

## Uso paso a paso

### 1. Elegir operación

```
1. Cifrar
2. Descifrar
```

* `1` → Convierte texto normal a cifrado
* `2` → Recupera el texto original

---

### 2. Elegir alfabeto

```
1. Ingles
2. Español
```

* Inglés: abcdefghijklmnopqrstuvwxyz
* Español: abcdefghijklmnñopqrstuvwxyz

---

### 3. Escribir texto

Ingresa cualquier frase. El programa:

* Mantiene espacios
* Mantiene signos
* Mantiene mayúsculas
* Procesa letras con tilde correctamente

Ejemplo:

```
Texto: Hola Mundo
```

---

### 4. Elegir desplazamiento

Número de posiciones que se moverá cada letra.

Ejemplo:

```
Desplazamiento: 3
```

---

## Ejemplo completo

Entrada:

```
Opcion: 2
Alfabeto: 2
Texto: oa ah ywixel nqa nqeañao rañ aj ah iqjzl iwdwpiw cwjzde
Desplazamiento: 4
```

Salida:

```
Resultado: Sé el cambio que quieres ver en el mundo Mahatma Gandhi
```

---

## Cómo funciona internamente

El programa realiza:

1. Convierte cada letra a minúscula
2. Elimina acentos temporalmente
3. Busca su posición en el alfabeto
4. Aplica desplazamiento (suma o resta)
5. Usa módulo (%) para no salir del alfabeto
6. Devuelve la letra
7. Restaura mayúsculas



