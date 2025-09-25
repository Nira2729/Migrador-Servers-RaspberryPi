import json, os
import click

def vincular_addons(ruta_servidor, nombre_mundo, tipo):
    carpeta = os.path.join(ruta_servidor, f"{tipo}_packs")
    salida = os.path.join(ruta_servidor, "worlds", nombre_mundo, f"world_{tipo}_packs.json")
    packs = []

    if not os.path.exists(carpeta):
        click.secho(f"⚠️ Carpeta de addons no encontrada: {carpeta}", fg='yellow')
        return

    addons = os.listdir(carpeta)
    if not addons:
        click.secho(f"⚠️ No se encontraron addons en: {carpeta}", fg='yellow')
        return

    for addon in addons:
        manifest = os.path.join(carpeta, addon, "manifest.json")
        if os.path.exists(manifest):
            try:
                with open(manifest) as f:
                    data = json.load(f)
                    uuid = data["header"]["uuid"]
                    version = data["header"]["version"]
                    packs.append({
                        "pack_id": uuid,
                        "version": version
                    })
                    click.secho(f"✅ Vinculado: {addon} ({uuid})", fg='green')
            except Exception as e:
                click.secho(f"❌ Error al procesar {addon}: {e}", fg='red')
        else:
            click.secho(f"⚠️ No se encontró manifest.json en: {addon}", fg='yellow')

    if packs:
        with open(salida, "w") as f:
            json.dump(packs, f, indent=2)
        click.secho(f"🔗 {tipo.capitalize()} vinculados en: {salida}", fg='cyan')
    else:
        click.secho(f"⚠️ No se pudo vincular ningún addon válido para tipo: {tipo}", fg='yellow')