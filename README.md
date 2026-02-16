# Cifrado César en Python

Programa de consola para **cifrar y descifrar textos** usando el algoritmo clásico de cifrado César. Compatible con Español (incluye ñ), Inglés, mayúsculas y minúsculas, vocales acentuadas (á é í ó ú). Mantiene espacios y signos y limpia la pantalla automáticamente en Windows.

---

# Formas de usar el programa en Windows

El proyecto puede ejecutarse de 2 maneras:

1) Ejecutando el archivo `.exe` (NO requiere Python)  
2) Ejecutando el archivo `.py` (requiere Python instalado)

---

# Opción 1 — Usar el ejecutable (.exe)

No necesitas instalar nada.

Pasos:

1. Descarga o clona el proyecto.
2. Ejecuta el Cesar.exe

```
Cesar.exe
```

Se abrirá la consola automáticamente y podrás usar el programa.

---

# Opción 2 — Usar el archivo Python (.py)

Requiere tener Python instalado.

Verificar instalación:

```
python --version
```

Si aparece una versión, ya puedes usarlo.  
Si no, instala Python desde: https://python.org

Ejecutar el programa:

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta:

```
python Cesar.py
```

---

# Obtener el proyecto desde GitHub

```
git clone https://github.com/ALetsee/Cifrado-Cesar.git
cd Cifrado-Cesar
```

---

# Uso paso a paso

Al iniciar el programa verás un menú.

1. Elegir operación:

```
1. Cifrar
2. Descifrar
```

- 1 → Convierte texto normal a cifrado  
- 2 → Recupera el texto original  

2. Elegir alfabeto:

```
1. Ingles
2. Español
```

- Inglés → abcdefghijklmnopqrstuvwxyz  
- Español → abcdefghijklmnñopqrstuvwxyz  

3. Escribir texto:

Puedes escribir cualquier frase.  
El programa conserva espacios, signos, mayúsculas y procesa tildes correctamente.

Ejemplo:

```
Texto: Hola Mundo
```

4. Elegir desplazamiento:

Número de posiciones que se moverá cada letra.

Ejemplo:

```
Desplazamiento: 3
```

---

# Ejemplo completo

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

# Cómo funciona internamente

El programa:

1. Convierte cada letra a minúscula.
2. Quita acentos temporalmente.
3. Busca su posición en el alfabeto.
4. Aplica desplazamiento (suma o resta).
5. Usa módulo (%) para no salir del alfabeto.
6. Obtiene la nueva letra.
7. Restaura mayúsculas.
