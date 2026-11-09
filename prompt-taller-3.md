# Taller 3 — Prompt para Copilot

Abre tu proyecto plataforma-ludica, entra al chat de Copilot (Ctrl + Alt + I) y pega este mensaje:

Quiero que realices TODO el Taller 3 de mi proyecto plataforma-ludica siguiendo las instrucciones de la guía que te proporcionaré.

Tu función será actuar como desarrollador senior y asistente de programación. Quiero que hagas el trabajo técnico directamente en los archivos del proyecto, no solamente que me expliques cómo hacerlo.

ACTIVIDAD 1. PREPARACIÓN
- Analiza todo el proyecto.
- Comprueba la estructura.
- Revisa las dependencias.
- Comprueba las pruebas existentes.
- Identifica cualquier problema antes de continuar.

ACTIVIDAD 2. CONTEXTO DEL AGENTE
- Crea o actualiza AGENTS.md.
- Máximo 40 líneas con contenido.
- Incluye proyecto, tecnologías, estructura, comandos, convenciones y reglas.
- Incluye la sección Qué no hacer.
- Añade que nunca debes hacer commit ni push.
- Añade que debes leer STATE.md al iniciar cada sesión.
- Crea o actualiza STATE.md con el estado real del proyecto.

ACTIVIDAD 3. SECRETOS Y PERMISOS
- Revisa .env.example.
- Prepara el archivo .env sin inventar secretos reales.
- Verifica que .env esté protegido en .gitignore.
- Busca posibles secretos expuestos en el código.
- Configura los permisos de Copilot según la guía.
- Crea opencode.json con los permisos indicados.
- No muestres ni publiques secretos.

ACTIVIDAD 4. PRE-COMMIT
- Revisa .pre-commit-config.yaml.
- Comprueba que Ruff y pytest estén configurados.
- Verifica que pre-commit esté disponible.
- Explícame cómo probar que el hook bloquea un error sin dejar modificaciones accidentales.

ACTIVIDAD 5. PAIR PROGRAMMING
- Crea la rama tarea/version solamente cuando yo te lo indique.
- Lee AGENTS.md.
- Analiza app/proyecto.py para encontrar la versión real.
- Implementa GET /api/version en app/rutas/api.py.
- Agrega su prueba en tests/test_inicio.py.
- No modifiques otros archivos para esta tarea sin autorización.
- Primero presenta el plan y espera mi aprobación.
- Ejecuta y verifica las pruebas.
- Comprueba Ruff.
- Prepara prompts/semana-1-version.md siguiendo prompts/README.md.

REGLAS OBLIGATORIAS:
1. Haz tú las modificaciones de código y archivos.
2. No te limites a dar instrucciones: trabaja directamente en el proyecto.
3. Antes de cada modificación, explícame qué vas a cambiar.
4. Muéstrame los cambios para revisarlos.
5. No elimines funcionalidades existentes.
6. No inventes información del proyecto.
7. No escribas secretos reales.
8. Nunca modifiques ni publiques .env.
9. Nunca ejecutes git commit ni git push.
10. Nunca fusiones un pull request por mí.
11. No ejecutes comandos destructivos.
12. Si una instrucción de la guía no puede automatizarse, explícame exactamente qué debo hacer yo.

IMPORTANTE: Trabajaremos una actividad a la vez. Puedes realizar automáticamente las tareas técnicas después de explicarme el plan y recibir mi aprobación.

Al terminar cada actividad, dame:
- Archivos creados.
- Archivos modificados.
- Comprobaciones realizadas.
- Resultados de las pruebas.
- Evidencias que debo tomar.
- Acciones que debo realizar personalmente.

Primero analiza mi proyecto y dime qué encontraste. No modifiques nada todavía.
