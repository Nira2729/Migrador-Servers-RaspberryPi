import zipfile, os
import click
import shutil

def extraer_mundo(ruta_entrada, ruta_servidor, nombre_mundo=None):
    if not os.path.exists(ruta_entrada):
        click.secho(f"❌ Ruta no encontrada: {ruta_entrada}", fg='red')
        return

    # Detectar tipo de entrada
    es_zip = zipfile.is_zipfile(ruta_entrada)
    es_carpeta = os.path.isdir(ruta_entrada)

    if es_zip:
        with zipfile.ZipFile(ruta_entrada, 'r') as zip_ref:
            nombres = zip_ref.namelist()
            carpetas = list(set([n.split('/')[0] for n in nombres if '/' in n]))

            if len(carpetas) == 1:
                nombre_detectado = carpetas[0]
                click.secho(f"📦 Carpeta detectada en ZIP: {nombre_detectado}", fg='cyan')
                nombre_mundo = nombre_mundo or nombre_detectado
            else:
                nombre_mundo = nombre_mundo or "MigradoWorld"
                click.secho("⚠️ No se detectó carpeta única, usando nombre predeterminado.", fg='yellow')

            destino = os.path.join(ruta_servidor, "worlds", nombre_mundo)
            os.makedirs(destino, exist_ok=True)
            zip_ref.extractall(destino)
            click.secho(f"🗂️ Mundo extraído en: {destino}", fg='green')

    elif es_carpeta:
        nombre_mundo = nombre_mundo or os.path.basename(ruta_entrada.rstrip('/'))
        destino = os.path.join(ruta_servidor, "worlds", nombre_mundo)
        shutil.copytree(ruta_entrada, destino, dirs_exist_ok=True)
        click.secho(f"🗂️ Mundo copiado desde carpeta: {destino}", fg='green')

    else:
        click.secho("❌ Formato de entrada no reconocido. Usa carpeta, .zip o .mcworld", fg='red')
        return

    # Validar archivos esenciales
    archivos_requeridos = ["level.dat", "db"]
    faltantes = []
    for item in archivos_requeridos:
        path = os.path.join(destino, item)
        if not os.path.exists(path):
            faltantes.append(item)

    if faltantes:
        click.secho(f"⚠️ Advertencia: faltan archivos esenciales: {', '.join(faltantes)}", fg='yellow')
    else:
        click.secho("✅ Archivos esenciales detectados correctamente.", fg='green')

    return nombre_mundo