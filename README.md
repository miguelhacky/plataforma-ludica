# Plataforma lúdica: Geografía de Colombia

Plataforma web educativa para aprender **Geografía de Colombia** mediante actividades cortas, retroalimentación y una progresión visual basada en la recolección de **Estrellas**. El prototipo está desarrollado con FastAPI, plantillas Jinja2 y una interfaz web instalable como PWA.

- **Aprendiz:** Miguel Fajardo
- **Curso:** Geografía de Colombia
- **Mecánica de aprendizaje basado en juegos:** Estrellas
- **Aplicación publicada:** pendiente de configurar en `app/proyecto.py`

## Funcionamiento de la plataforma

La aplicación separa la capa web de la identificación del proyecto:

1. FastAPI recibe las solicitudes y registra las rutas principales.
2. La página de inicio presenta el curso, el aprendiz y la mecánica de Estrellas usando una plantilla Jinja2.
3. La API expone un indicador de salud y los datos oficiales del proyecto, útiles para integraciones, validaciones y despliegue.
4. La documentación interactiva se genera automáticamente con OpenAPI en `/docs` y `/redoc`.
5. Los archivos estáticos incluyen la hoja de estilos, el JavaScript, el manifiesto y los iconos de la PWA. El service worker se sirve desde `/sw.js` para permitir el control del sitio desde la raíz.

### Mecánica de Estrellas

Las Estrellas representan el avance del estudiante en Geografía de Colombia. En la evolución del prototipo, cada actividad puede otorgar estrellas cuando el estudiante identifica correctamente una región, departamento, capital, relieve, río o característica cultural del país. La mecánica debe conservar estas reglas:

- la recompensa debe estar asociada a una actividad completada;
- la retroalimentación debe explicar el resultado y apoyar el aprendizaje;
- la cantidad de estrellas debe ser visible y acumulable durante la sesión;
- las estrellas son un indicador de progreso, no una calificación definitiva;
- una actividad no debe otorgar repetidamente la misma recompensa por un reintento, salvo que la regla pedagógica lo defina expresamente.

En esta versión inicial, la estructura de datos y las rutas de actividades aún no están implementadas: el proyecto entrega la base FastAPI y los endpoints de identificación necesarios para continuar el desarrollo del juego.

## Rutas principales

| Método | Ruta | Uso | Respuesta esperada |
| --- | --- | --- | --- |
| GET | `/` | Página inicial del curso | HTML con Miguel Fajardo, Geografía de Colombia y Estrellas |
| GET | `/salud` | Comprobación del servicio | `{"estado": "ok"}` |
| GET | `/api/proyecto` | Datos oficiales del proyecto | JSON con aprendiz, curso, mecánica y versión |
| GET | `/docs` | Documentación interactiva | Swagger UI de FastAPI |
| GET | `/redoc` | Documentación alternativa | ReDoc de FastAPI |
| GET | `/static/manifest.json` | Metadatos de la PWA | JSON del manifiesto |
| GET | `/sw.js` | Service worker | JavaScript servido desde la raíz |

Ejemplo de respuesta de `/api/proyecto`:

```json
{
  "aprendiz": "Miguel Fajardo",
  "curso": "Geografía de Colombia",
  "mecanica": "Estrellas",
  "version": "0.1.0"
}
```

## Ejecutar en el equipo

En Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

En Linux o macOS, cree el entorno con `python3 -m venv .venv` y actívelo con `source .venv/bin/activate`.

Abra http://127.0.0.1:8000 en el navegador. La documentación de la API está en http://127.0.0.1:8000/docs.

## Verificar las rutas y la calidad del código

```bash
pytest -v
ruff check .
```

Las pruebas automatizadas verifican que la página inicial cargue los datos de la temática, que `/salud` responda correctamente, que `/api/proyecto` devuelva la identificación oficial, que `/docs` esté disponible, y que los recursos de la PWA y `/sw.js` se sirvan correctamente.

## Despliegue en Vercel

El proyecto incluye `vercel.json` y `api/index.py` para publicar la aplicación FastAPI como una función ASGI en Vercel.

1. Inicia sesión en Vercel con la cuenta que tenga acceso al repositorio.
2. Selecciona **Add New Project** y elige `miguelhacky/plataforma-ludica`.
3. Mantén el framework como **Other**.
4. Usa `pip install -r requirements.txt` como comando de instalación si Vercel lo solicita.
5. Pulsa **Deploy**.

Después del despliegue, comprueba estas rutas usando el dominio asignado por Vercel:

```text
https://tu-proyecto.vercel.app/
https://tu-proyecto.vercel.app/salud
https://tu-proyecto.vercel.app/api/proyecto
https://tu-proyecto.vercel.app/docs
```

Vercel ejecuta `api/index.py`, que importa la instancia FastAPI definida en `app/main.py`. La aplicación no utiliza una base de datos persistente en esta versión; si posteriormente se agregan puntajes o perfiles, se deberá usar una base de datos externa compatible con despliegues serverless.

## Estructura

| Carpeta o archivo | Contenido |
| --- | --- |
| `app/` | Aplicación FastAPI: rutas, servicios, modelos, plantillas y archivos estáticos |
| `app/proyecto.py` | Datos de identificación del proyecto |
| `tests/` | Pruebas automatizadas |
| `specs/` | Especificación, flujo de usuario, plan técnico, tareas y decisiones |
| `prompts/` | Prompts versionados |
| `entregas/` | Respuestas semanales; `entregar.py` genera el PDF |
| `AGENTS.md` | Contexto del proyecto para los agentes de IA |
| `STATE.md` | Estado, decisiones y siguiente paso |
| `render.yaml` | Configuración del despliegue en Render |

## Licencia

MIT. Consulte el archivo LICENSE.
