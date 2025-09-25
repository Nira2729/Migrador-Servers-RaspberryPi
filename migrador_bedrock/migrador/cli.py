import click
from .extractor import extraer_mundo
from .vinculos import vincular_addons
from .configurador import configurar_server_properties
from .controlador import iniciar_servidor, detener_servidor, monitorear_log

import socket
import requests

@click.group()
def main():
    """Migrador Bedrock CLI: automatiza la migración y control de servidores Bedrock."""
    pass

@main.command()
@click.option('--mundo', required=True, help='Ruta al archivo .mcworld, .zip o carpeta del mundo')
@click.option('--servidor', required=True, help='Ruta base del servidor Bedrock')
@click.option('--nombre', default='MigradoWorld', help='Nombre del mundo en el servidor')
def migrar(mundo, servidor, nombre):
    """Migrar un mundo Bedrock con addons al servidor local."""
    nombre_final = extraer_mundo(mundo, servidor, nombre)
    vincular_addons(servidor, nombre_final, tipo='behavior')
    vincular_addons(servidor, nombre_final, tipo='resource')
    configurar_server_properties(servidor, nombre_final)
    click.secho("✅ Migración completada.", fg='green')

@main.command()
@click.option('--servidor', required=True, help='Ruta base del servidor Bedrock')
@click.option('--log', default=None, help='Ruta opcional para guardar logs del servidor')
def iniciar(servidor, log):
    """Iniciar el servidor Bedrock."""
    iniciar_servidor(servidor, log)

@main.command()
def detener():
    """Detener el servidor Bedrock."""
    detener_servidor()

@main.command()
@click.option('--log', required=True, help='Ruta al archivo de log del servidor')
def monitorear(log):
    """Monitorear el log del servidor en tiempo real."""
    monitorear_log(log)

@main.command()
def verificar_red():
    """Verifica IP local, IP pública y estado del puerto 19132."""
    ip_local = socket.gethostbyname(socket.gethostname())
    try:
        ip_publica = requests.get('https://api.ipify.org').text
    except:
        ip_publica = "No disponible"

    click.secho(f"🌐 IP local: {ip_local}", fg='cyan')
    click.secho(f"🌍 IP pública: {ip_publica}", fg='cyan')

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    resultado = sock.connect_ex((ip_local, 19132))
    if resultado == 0:
        click.secho("✅ Puerto 19132 abierto localmente", fg='green')
    else:
        click.secho("❌ Puerto 19132 cerrado", fg='red')
    sock.close()