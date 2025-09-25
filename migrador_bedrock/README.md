# Migrador Bedrock 

Automatiza la migración de mundos Minecraft Bedrock con addons (mods) hacia servidores locales en Raspberry Pi. Incluye funciones para iniciar, detener y monitorear el servidor con trazabilidad real.

##  Instalación

### Requisitos
- Python 3.7+
- `pip`
- Raspberry Pi con Bedrock Dedicated Server instalado

### Instalación local

```bash
git clone https://github.com/tu_usuario/migrador-bedrock.git
cd migrador-bedrock
pip install .
```

Esto habilita el comando global:

```bash
migrador-bedrock
```

##  Comandos disponibles

### 1. Migrar mundo

```bash
migrador-bedrock migrar --mundo /ruta/al/archivo.mcworld --servidor /ruta/al/servidor --nombre NombreDelMundo
```

- `--mundo`: Ruta al archivo `.mcworld` descargado desde Aternos
- `--servidor`: Ruta base del servidor Bedrock en tu Raspberry Pi
- `--nombre`: Nombre que tendrá el mundo en el servidor (opcional, por defecto: `MigradoWorld`)

---

### 2. Iniciar servidor

```bash
migrador-bedrock iniciar --servidor /ruta/al/servidor --log /ruta/al/log.txt
```

- Inicia el servidor Bedrock
- Si se especifica `--log`, guarda la salida en ese archivo

### 3. Detener servidor

```bash
migrador-bedrock detener
```

- Termina el proceso activo del servidor Bedrock

### 4. Monitorear log

```bash
migrador-bedrock monitorear --log /ruta/al/log.txt
```

- Muestra en tiempo real el contenido del log del servidor

##  Estructura del proyecto

```
migrador_bedrock/
├── migrador/
│   ├── __init__.py
│   ├── cli.py
│   ├── extractor.py
│   ├── configurador.py
│   ├── vinculos.py
│   └── controlador.py
├── setup.py
├── requirements.txt
└── README.md
```

##  Extensiones futuras

- Validación de integridad de packs
- Activación de funciones experimentales
- Backups automáticos
- CLI interactiva para usuarios no técnicos

##  Autor

**Hendricks** Yo

---

##  Licencia

MIT — libre para modificar, distribuir y mejorar.
```


