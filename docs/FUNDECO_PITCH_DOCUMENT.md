# FUNDECO — Pitch Ejecutivo

## Elevator Pitch
FUNDECO produce fundas agrícolas biodegradables hechas a base de almidón de papa, diseñadas para proteger cultivos y, al finalizar su ciclo, degradarse naturalmente y aportar al suelo en lugar de contaminarlo. Ofrecemos soluciones de producción personalizada, distribución regional y asesoría técnica para acelerar la adopción de prácticas de agricultura sostenible en la región sur del Ecuador y mercados afines.

---

## El problema
- La agricultura intensiva depende de plásticos tradicionales para protección de cultivos (fundas, mulch, cobertores), que generan residuos persistentes y contaminación del suelo y agua.
- Los costos operativos aumentan por la recolección y gestión de estos residuos y por pérdidas de productividad asociadas a prácticas no sostenibles.
- Pequeños y medianos agricultores carecen de alternativas locales, accesibles y técnicamente soportadas.

---

## Nuestra solución
- Productos: fundas biodegradables formuladas con almidón de papa (material local, renovable) que mantienen la resistencia necesaria durante el cultivo y se degradan al finalizar el ciclo, favoreciendo la economía circular.
- Servicios: producción personalizada (tamaños, grosores, tiempos de degradación), distribución regional optimizada, asesoría técnica, capacitación y programas de compostaje/gestión de residuos.
- Plataforma web: sitio corporativo informativo (home, beneficios, tecnología, servicios) con navegación fluida, paleta FUNDECO y experiencia responsiva.
- Asistente virtual (chatbot): integrado en el sitio, disponible en modo demo o con OpenAI (GPT-3.5+), responde preguntas sobre producto, servicios, precios y contacto; facilita la captación de leads y soporte 24/7.

---

## Producto y características
- Fundas biodegradables a base de almidón de papa.
- Ventajas: sostenibilidad, ahorro de tiempo y dinero (menos limpieza), incremento de eficiencia agrícola y aporte a la economía circular.
- Servicios complementarios: I+D, certificaciones, gestión de residuos, análisis de impacto, alianzas con cooperativas.
- Disponibilidad: producción por encargo con mínimos flexibles y planes (Básico, Profesional, Enterprise).

---

## Tecnología y proceso
- Proceso de manufactura documentado en la web (timeline de 5 pasos): consulta, diseño, producción, entrega/implementación y seguimiento.
- Especificaciones técnicas y certificaciones en la sección de tecnología.
- Herramientas técnicas del proyecto:
  - Backend: Flask (rutas y APIs implementadas en `src/api/app.py`), endpoint `/api/chat` para el chatbot.
  - Frontend: plantillas Jinja2 en `src/templates/` y CSS personalizado (`src/static/css/fullpage-menu.css`, `chatbot.css`).
  - Chatbot: `src/static/js/chatbot.js` integrado en `home/home.html` y `chatbot-example.html` con modo demo y soporte OpenAI.
  - Assets: imágenes Unsplash en plantillas, Google Fonts (Teko, Poppins) y Font Awesome para íconos.

---

## Mercado y clientes objetivo
- Inicio: agricultores y cooperativas del sur de Ecuador (Loja y zonas aledañas).
- Expansión: distribuidores agrícolas regionales y empresas agroindustriales en mercados latinoamericanos con demanda de soluciones sostenibles.
- Clientes potenciales: productores hortícolas, viveros, productores orgánicos y empresas interesadas en certificación sostenible.

---

## Modelo de negocio
- Venta de productos por hectárea / por lote (precios orientativos: Plan Básico desde $50/ha, Profesional desde $120/ha, Enterprise con cotización personalizada).
- Servicios recurrentes: contratos de suministro, asesoría y seguimiento técnico.
- Servicios de valor agregado: I+D por contrato, programas de certificación, gestión de residuos y capacitación.

---

## Go-to-Market (GT M)
- Pilotos locales con cooperativas y agricultores clave en Loja.
- Alianzas con distribuidores regionales y autoridades locales (extensión agrícola).
- Marketing digital y contenido: sitio web informativo, SEO local, testimonios de pilotos, presencia en ferias agrícolas.
- Uso del chatbot para captura de leads y calificación automática.

---

## Tracción y estado del proyecto (Mínimos Viables)
- Sitio web corporativo funcional con secciones: Home, Beneficios, Tecnología, Servicios, Contacto.
- Páginas de detalle para beneficios y tecnología, y página completa de servicios (`src/templates/fundeco/` y `home/home.html`).
- Chatbot integrado y funcional en modo demo; opcionalmente se activa OpenAI si se provee API key (`.env`).
- Rutas y API implementadas en `src/api/app.py` (incluye `/fundeco/*`, `/login/*`, `/api/chat`).
- Código listo para pruebas locales (Flask corriendo en `http://127.0.0.1:5000`).

---

## Equipo
- Fundadores / Operaciones: (por definir) — conocimiento local y cadena de proveedores de almidón de papa.
- Desarrollo: repositorio con implementaciones front-end y back-end, chatbot y documentación técnica (`CHATBOT_DOCUMENTATION.md`).
- Colaboradores: ingenieros en I+D y técnicos en procesos bio-basados (por reclutar/alianzas).

---

## Roadmap corto plazo (6-12 meses)
1. Pilotos de campo con 3-5 productores y medición de impacto en rendimiento y suelo.
2. Ajustes de formulación y producción según resultados de piloto (I+D).
3. Obtener certificaciones clave (orgánico, biodegradabilidad) y documentarlas en el sitio.
4. Integrar OpenAI en producción (API key) y entrenar prompts/contextos específicos del negocio.
5. Lanzamiento comercial regional y primeras ventas B2B con distribuidores.

---

## Riesgos y mitigaciones
- Riesgo técnico (degradación no uniforme): ensayo en piloto y ajuste de formulación.
- Riesgo de aceptación del mercado: precios competitivos y programas de capacitación/soporte técnico.
- Riesgo regulatorio: trabajar con certificadoras locales y cumplir normativas ambientales.

---

## Request / Ask
- Financiamiento semilla para ejecutar pilotos de campo y validar formulación y logística.
- Acceso a redes de distribución regional para primeros volúmenes comerciales.
- Mentores técnicos en polímeros/bio-degradación y agricultura sostenible.
- Soporte para completar certificaciones y validaciones de impacto.

---

## Contacto
FUNDECO — Loja, Ecuador
- Email: info@fundeco.ec
- Teléfono: +593 99 123 4567

---

> Nota técnica: el repositorio incluye la implementación del chatbot (modo demo + dependencia opcional de OpenAI), páginas web, rutas Flask y la hoja de estilos para mantener la identidad visual FUNDECO. Para activar respuestas OpenAI en producción, añadir `OPENAI_API_KEY` válido en el archivo `.env` y reiniciar el servidor.