# Migrador Bedrock para Raspberry Pi

Herramienta modular en Python para automatizar la migración de mundos Bedrock a servidores dedicados en Raspberry Pi. Incluye vinculación de addons, configuración automática y control del servidor desde CLI.

##  Instalación

Clona el repositorio y ejecuta la instalación local:

```bash
git clone https://github.com/tu_usuario/migrador-bedrock.git
cd migrador-bedrock
pip install .

Comandos disponibles
migrador-bedrock migrar --mundo "/ruta/al/mundo.mcworld" --servidor "/ruta/al/servidor" --nombre "AgeOfBerk"


- migrar: Extrae el mundo, vincula addons y configura el servidor.
- iniciar: Inicia el servidor Bedrock (opcionalmente con log).
- detener: Detiene el proceso del servidor.
- monitorear: Muestra el log en tiempo real.
- verificar-red: Muestra IP local, pública y estado del puerto 19132.
 Estructura esperada
bedrock_server/
├── bedrock_server        # binario ejecutable
├── server.properties     # archivo de configuración
├── behavior_packs/       # addons de comportamiento
├── resource_packs/       # addons de recursos
└── worlds/
    └── AgeOfBerk/        # mundo migrado


 Requisitos
- Python 3.7+
- Raspberry Pi OS o Linux compatible
- Paquetes: click, psutil, requests
Instalación manual de dependencias:
pip install -r requirements.txt


 Ejemplo rápido
migrador-bedrock migrar \
  --mundo "/home/pi/Descargas/AgeOfBerk.mcworld" \
  --servidor "/home/pi/bedrock_server" \
  --nombre "AgeOfBerk"


