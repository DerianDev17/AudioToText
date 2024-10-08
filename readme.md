# Proyecto de Transcripción de Audio

Este proyecto permite transcribir archivos de audio en formato WAV a texto utilizando la biblioteca `speech_recognition`. Además, incluye herramientas para dividir archivos de audio en segmentos y convertir archivos de audio de otros formatos a WAV.

## Características

- Transcripción de segmentos de audio a texto.
- División de archivos de audio en segmentos de duración específica.
- Conversión de archivos de audio de formato M4A a WAV.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas de Python:

- `speech_recognition`
- `pydub`
- `ffmpeg` (necesario para `pydub`)

Puedes instalar las bibliotecas necesarias usando pip:

```bash
pip install SpeechRecognition pydub
```

## Instalación de FFmpeg

Para que `pydub` funcione correctamente, necesitas tener FFmpeg instalado en tu sistema. Puedes descargarlo desde [FFmpeg](https://ffmpeg.org/download.html) y seguir las instrucciones de instalación.

## Uso

### 1. Convertir un archivo de audio a WAV

Para convertir un archivo de audio en formato M4A a WAV, utiliza el script `convertir.py`:

```bash
python convertir.py
```

### 2. Separar el audio en segmentos

Una vez que tengas el archivo WAV, puedes dividirlo en segmentos de 5 minutos utilizando el script `separaraudio.py`:

```bash
python separaraudio.py
```

### 3. Transcribir los segmentos de audio

Finalmente, para transcribir los segmentos de audio generados, ejecuta el script `audiotranscript.py`:

```bash
python audiotranscript.py
```

Esto generará un archivo `transcripcion_completa.txt` con la transcripción de cada segmento.

## Contribuciones

Si deseas contribuir, por favor sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz un commit (`git commit -m 'Añadir nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

