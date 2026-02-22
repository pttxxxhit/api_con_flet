import flet
from flet import Colors, Page, TextField, ElevatedButton, Text, Column, BoxFit, ScrollMode

# Intentar cargar Pillow dinámicamente para leer el tamaño de la imagen (opcional)
try:
    import importlib
    _pil_module = importlib.import_module("PIL.Image")
    PILImage = _pil_module
    _HAS_PIL = True
except Exception:
    _HAS_PIL = False


def main(page: Page):
    page.title = "ChatPttex"
    page.bgcolor = Colors.BLUE_GREY_900 if hasattr(Colors, 'BLUE_GREY_900') else Colors.BLUE_GREY

    # Imagen de fondo
    fondo = flet.Image(
        src="assets/fondo.png",
        expand=True,
        fit=BoxFit.COVER,
        opacity=0.2
    )

    # Ajustar el tamaño de la ventana según la imagen, si Pillow está disponible
    if _HAS_PIL:
        try:
            img = PILImage.open("assets/fondo.png")
            w, h = img.size
            # Asignar tamaño de ventana (si la plataforma/versión de flet lo permite)
            try:
                page.window_width = w
                page.window_height = h
            except Exception:
                # Algunas versiones o entornos pueden no exponer estas propiedades; ignorar si falla
                pass
        except Exception:
            pass

    # Campo de entrada
    input_box = TextField(
        label="¿En qué piensas?",
        label_style=flet.TextStyle(color=Colors.WHITE),
        color=Colors.WHITE,
        border_color=Colors.BLUE_200,
        focused_border_color=Colors.BLUE_400,
        cursor_color=Colors.YELLOW_400,
        expand=False
    )

    # Área de chat
    chat_area = Column(
        expand=True,
        scroll=ScrollMode.AUTO
    )

    preguntas = []

    def send_message(e):
        nonlocal preguntas
        # No enviar mensajes vacíos
        raw = (input_box.value or "").strip()
        if not raw:
            try:
                input_box.focus()
                page.update()
            except Exception:
                pass
            return

        user_message = raw.lower()
        if "hola" in user_message:
            response = "¡Hola! ¿Cómo puedo ayudarte hoy?"
        elif "clima" in user_message:
            response = "No puedo predecir el clima en tu ciudad."
        else:
            response = "Lo siento, no entiendo tu mensaje."

        preguntas.append((raw, response))
        # Mantener solo las últimas 5 interacciones
        if len(preguntas) > 5:
            preguntas = preguntas[-5:]

        # Actualizar área de chat
        chat_area.controls.clear()
        for pregunta, respuesta in preguntas:
            chat_area.controls.append(Text(f"Tú: {pregunta}", color=Colors.YELLOW_200))
            chat_area.controls.append(Text(f"Bot: {respuesta}", color=Colors.WHITE))

        # Mostrar solo las últimas 10 líneas por seguridad
        chat_area.controls = chat_area.controls[-10:]

        input_box.value = ""
        try:
            input_box.focus()
        except Exception:
            pass
        page.update()

    # Enviar con Enter
    input_box.on_submit = send_message

    send_button = ElevatedButton(
        "Enviar",
        on_click=send_message,
        bgcolor=Colors.BLUE_700,
        color=Colors.WHITE
    )

    page.add(
        flet.Stack([
            fondo,
            flet.Column([
                input_box,
                send_button,
                chat_area
            ], expand=True)
        ], expand=True)
    )


if __name__ == "__main__":
    flet.app(target=main)
