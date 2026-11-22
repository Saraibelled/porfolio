# Un mar de cosas: cómo subirlo a GitHub

## Archivos

- `index.html`: el mar entero, con el diseño, la lógica, el móvil, el tesoro y la lista.
- `piezas_porfolio.csv`: tus piezas. El mar lee este archivo cada vez que alguien entra.

Los dos archivos tienen que estar **en la misma carpeta**.

## Subirlo (repositorio `Saraibelled/porfolio`)

1. Si quieres conservar el porfolio actual, crea una carpeta `version-2025/` y mueve ahí el `index.html` actual y su CSV. Así seguirá visible en `saraibelled.github.io/porfolio/version-2025/`.
2. En la raíz del repositorio, usa **Add file → Upload files**, arrastra `index.html` y `piezas_porfolio.csv` y haz **Commit**.
3. GitHub Pages ya está activado en ese repositorio. En uno o dos minutos el mar estará en **https://saraibelled.github.io/porfolio/**.

> Si abres `index.html` con doble clic en tu ordenador, el navegador no deja leer el CSV y el mar usa una copia de las piezas que va dentro de la propia página. En GitHub Pages lee siempre `piezas_porfolio.csv`, así que lo que cambies en el CSV es lo que se verá online. La copia interna solo sirve para verlo en local.

## Actualizarlo

Solo hay que tocar el CSV y volver a subirlo. Columnas que usa el mar:

| Columna | Qué hace |
|---|---|
| `en_el_mar` | `sí` = la botella flota en el mar |
| `formato` | La zona: `Datos e IA`, `Juegos`, `Última hora`, `Narrativas` o `Grandes investigaciones` |
| `premio` | Nombre del premio. La botella lleva corcho dorado y guarda un trozo del mapa del tesoro |
| `candidata_premios` | `sí` = etiqueta "Candidata a premios" |
| `mi_nota` | Texto libre: lo que hiciste en la pieza. Sale en el recuadro «Lo que hice». Vacía = no sale |
| `rota` | `sí` = botella agrietada y aviso de pieza dañada |
| `nota_rota` | Opcional: qué falla |
| `captura` | Opcional: enlace a un vídeo o captura de cómo era |
| `imagen` | Imagen que se ve al abrir la botella |
| `imagen_alt` | Descripción de la imagen, para la accesibilidad |
| `titulo`, `url`, `fecha`, `medio`, `antetitulo`, `subtitulo`, `autores`, `tipo_multimedia` | Datos de la pieza |

## Imágenes

Para rellenar o arreglar las imágenes automáticamente, abre una terminal en la carpeta del repositorio y ejecuta `python3 actualizar_imagenes.py`. Entra en cada pieza del mar, coge su imagen de portada (la que sale al compartirla en redes) y la escribe en la columna `imagen`. Antes guarda una copia del CSV. Con `--todas` revisa todas las piezas, no solo las del mar.

Las imágenes que son vídeo (`.mp4`) se reproducen en bucle y sin sonido al abrir la botella.

Ahora la columna `imagen` apunta al servidor de imágenes de Vocento. Algunas imágenes ya fallan, y en ese caso el mensaje muestra un bloque de color con el antetítulo. Para que no dependan de nadie, crea una carpeta `img/` en el repositorio, sube ahí las imágenes y escribe en el CSV la ruta relativa, por ejemplo `img/adamuz.jpg`.

## Textos fijos

Los textos del puerto ("Sobre mí"), del Astillero, del faro, del tesoro y del diploma están dentro de `index.html`, en la función `openMsg`. Puedes editarlos con cualquier editor de texto.

## Estadísticas (Umami)

1. Crea una cuenta gratuita en https://cloud.umami.is/signup (plan Hobby).
2. Añade la web `saraibelled.github.io` y copia su **Website ID**.
3. Ya está configurado en `index.html` y `en.html` (ID b95301f6-41be-4e6d-a2d2-fa3e8d129957).

Eventos que verás en Umami (Events):
- **Abrir botella**: título, zona, medio, si es premiada y si llegó navegando o por un remolino.
- **Leer pieza**: clic en "Leer la pieza" (desde la botella o desde la lista).
- **Lugar**: puerto, astillero, faro, tesoro, diploma.
- **Contacto**: clics en Gmail, mailto o LinkedIn.
- **Buscar**: lo que escriben en el buscador.
- **Remolino**, **Botón** (lista, novedades, seguir buscando, copiar correo, empezar de cero).
- **Salida**: al irse, cuántas botellas abrió, % explorado y trozos de mapa.

Solo cuenta visitas en saraibelled.github.io (no cuando lo abres en local). No usa cookies.

## Versión en inglés

- Sube también `en.html` junto a `index.html` y `piezas_porfolio.csv`.
- El botón ES / EN cambia de una página a otra y recuerda la elección. Si alguien entra con el navegador en otro idioma que no sea español, va directo a la versión inglesa.
- Las botellas abiertas, la niebla y el mapa del tesoro se comparten entre las dos versiones.
- Textos de las piezas en inglés: columnas `titulo_en`, `antetitulo_en`, `subtitulo_en`, `mi_nota_en` y `nota_rota_en` del CSV. Si una está vacía, se muestra la española.
