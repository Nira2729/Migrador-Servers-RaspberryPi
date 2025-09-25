import subprocess, os
import click
import psutil
import time

def iniciar_servidor(ruta_servidor, ruta_log=None):
    binario = os.path.join(ruta_servidor, 'bedrock_server')

    if not os.path.exists(binario):
        click.secho(f"❌ No se encontró el ejecutable: {binario}", fg='red')
        return

    try:
        if ruta_log:
            with open(ruta_log, 'w') as log_file:
                subprocess.Popen([binario], stdout=log_file, stderr=subprocess.STDOUT)
            click.secho(f"🚀 Servidor iniciado con logs en: {ruta_log}", fg='green')
        else:
            subprocess.Popen([binario])
            click.secho("🚀 Servidor iniciado sin log externo.", fg='green')
    except Exception as e:
        click.secho(f"❌ Error al iniciar el servidor: {e}", fg='red')

def detener_servidor():
    encontrado = False
    for proc in psutil.process_iter(['pid', 'name']):
        if 'bedrock_server' in proc.info['name']:
            proc.terminate()
            click.secho("🛑 Servidor detenido.", fg='yellow')
            encontrado = True
            break
    if not encontrado:
        click.secho("⚠️ No se encontró el proceso del servidor.", fg='red')

def monitorear_log(ruta_log):
    if not os.path.exists(ruta_log):
        click.secho(f"❌ Log no encontrado: {ruta_log}", fg='red')
        return

    click.secho(f"📡 Monitoreando log: {ruta_log}", fg='cyan')
    try:
        with open(ruta_log, 'r') as f:
            f.seek(0, 2)  # Ir al final
            while True:
                line = f.readline()
                if line:
                    click.secho(f"[LOG] {line.strip()}", fg='white')
                else:
                    time.sleep(0.5)
    except KeyboardInterrupt:
        click.secho("🛑 Monitoreo detenido por el usuario.", fg='yellow')