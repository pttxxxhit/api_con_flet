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
