# chat_con_flet

Pequeña app de chat con Flet.

Requisitos:
- Python 3.8+
- Virtualenv (opcional pero recomendado)

Instalación (PowerShell en Windows):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
```

Ejecutar la app (PowerShell):

```powershell
.\.venv\Scripts\python.exe app.py
```

Notas:
- El ajuste de tamaño de la ventana intenta usar Pillow para leer `assets/fondo.png`. Si no quieres instalar Pillow, la app seguirá funcionando sin ajustar la ventana.
- Si quieres que siempre se instale Pillow, deja `pillow` en `requirements.txt` (ya incluido).

Cómo crear un repositorio remoto en GitHub y empujar (sin `gh`):

1. Entra en https://github.com y crea un nuevo repositorio (privado o público) desde la web. Copia la URL del repositorio (por ejemplo: https://github.com/tu_usuario/nombre_repo.git).

2. En PowerShell, desde la carpeta del proyecto ejecuta:

```powershell
# Reemplaza la URL por la de tu repositorio
git remote add origin https://github.com/tu_usuario/nombre_repo.git
git branch -M main
git push -u origin main
```

Si tu repositorio usa autenticación por token, cuando Git pregunte usuario/contraseña, usa tu usuario y como contraseña el Personal Access Token (PAT).


