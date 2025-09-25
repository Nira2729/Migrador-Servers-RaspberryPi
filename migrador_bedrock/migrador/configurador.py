import os
import shutil
import click

def configurar_server_properties(ruta_servidor, nombre_mundo):
    path = os.path.join(ruta_servidor, "server.properties")

    if not os.path.exists(path):
        click.secho(f"❌ No se encontró server.properties en: {ruta_servidor}", fg='red')
        return

    # Crear backup
    backup_path = path + ".bak"
    shutil.copy(path, backup_path)
    click.secho(f"🧾 Backup creado: {backup_path}", fg='cyan')

    # Leer y modificar
    with open(path, "r") as f:
        lines = f.readlines()

    with open(path, "w") as f:
        modificados = 0
        for line in lines:
            if line.startswith("level-name="):
                f.write(f"level-name={nombre_mundo}\n")
                modificados += 1
            else:
                f.write(line)

    if modificados:
        click.secho("⚙️ server.properties actualizado con nuevo nombre de mundo.", fg='green')
    else:
        click.secho("⚠️ No se encontró 'level-name=' en server.properties. No se modificó.", fg='yellow')