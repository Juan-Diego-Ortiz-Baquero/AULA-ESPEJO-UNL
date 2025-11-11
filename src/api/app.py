import os
from flask import Flask, render_template, request, session, jsonify
from dotenv import load_dotenv
import json

# Cargar variables de entorno
load_dotenv()

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = os.getenv('SECRET_KEY', 'fundeco_secret_key_2024')

# Configurar OpenAI de forma segura
try:
    from openai import OpenAI
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if openai_api_key and openai_api_key != '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':
        client = OpenAI(api_key=openai_api_key)
        OPENAI_AVAILABLE = True
    else:
        OPENAI_AVAILABLE = False
        print("⚠️  OpenAI API key no configurada. El chatbot funcionará en modo demo.")
except ImportError:
    OPENAI_AVAILABLE = False
    print("⚠️  OpenAI no está instalado. El chatbot funcionará en modo demo.")

@app.route('/login/1', methods=['GET', 'POST'])
def login1():
    return render_template('login/login1.html')

#---LOGIN 2---

@app.route('/login/2', methods=['GET', 'POST'])
def login2():
    return render_template('login/login2.html')

#---LOGIN 3---

@app.route('/login/3', methods=['GET', 'POST'])
def login3():
    return render_template('login/login3.html')

#---LOGIN 4---

@app.route('/login/4', methods=['GET', 'POST'])
def login4():
    return render_template('login/login4.html')

#---MENU---
@app.route('/', methods=['GET'])
def home():
    return render_template('home/home.html')

#---AULA ESPEJO HOME---
@app.route('/aula-espejo', methods=['GET'])
def aula_espejo_home():
    return render_template('home.html')

#---FUNDECO HOME (LEGACY ROUTE)---
@app.route('/fundeco', methods=['GET'])
def fundeco_home():
    return render_template('home/home.html')

#---LOGIN SELECTOR---
@app.route('/login-selector', methods=['GET'])
def login_selector():
    return render_template('login/login-selector.html')

#---ABOUT---
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

#---CONTACT---
@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

#---USER PROFILE---
@app.route('/profile', methods=['GET'])
def profile():
    return render_template('user/profile.html')

#---USER REGISTER---
@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('user/register.html')

#---PRODUCT CATALOG---
@app.route('/catalog', methods=['GET'])
def catalog():
    return render_template('product/catalog.html')

#---PRODUCT DETAIL---
@app.route('/product/<int:product_id>', methods=['GET'])
def product_detail(product_id):
    return render_template('product/detail.html', product_id=product_id)

#---FUNDECO PAGES---
@app.route('/fundeco/beneficios', methods=['GET'])
def fundeco_beneficios():
    return render_template('fundeco/beneficios.html')

@app.route('/fundeco/tecnologia', methods=['GET'])
def fundeco_tecnologia():
    return render_template('fundeco/tecnologia.html')

@app.route('/fundeco/servicios', methods=['GET'])
def fundeco_servicios():
    return render_template('fundeco/servicios.html')

#---CHATBOT EXAMPLE---
@app.route('/chatbot-example', methods=['GET'])
def chatbot_example():
    return render_template('chatbot-example.html')

#---CHATBOT API---
@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Si OpenAI está disponible, usar la API real
        if OPENAI_AVAILABLE:
            # Contexto específico para FUNDECO
            system_prompt = """
            Eres el asistente virtual oficial de FUNDECO, una empresa ecuatoriana innovadora especializada en fundas biodegradables para agricultura sostenible. Tu función principal es atender clientes potenciales, resolver consultas comerciales y promover la venta de productos y servicios.

            IMPORTANTE: Eres un asistente comercial y de atención al cliente, NO un experto técnico en procesos de fabricación. Tu enfoque debe estar en ayudar al cliente a tomar decisiones de compra, no en explicar detalles internos de producción.

            INFORMACIÓN COMERCIAL DEL PRODUCTO:
            - Fundas Biodegradables FUNDECO elaboradas con materiales naturales (almidón de papa)
            - Diseñadas específicamente para uso agrícola en viveros, huertos y cultivos
            - 100% Biodegradables: Se degradan naturalmente sin contaminar suelos ni agua
            - Funcionales: Misma resistencia y durabilidad que fundas plásticas tradicionales durante el ciclo de cultivo
            - Económicas: Precio competitivo con ahorro en costos de limpieza y gestión de residuos
            - Compromiso Ambiental: Reduce huella ecológica y promueve agricultura responsable
            - Producción Local: Apoyamos economía circular del sur de Ecuador

            BENEFICIOS PARA DIFERENTES TIPOS DE CLIENTES:

            Para Agricultores:
            - Eliminan necesidad de recoger y desechar plástico
            - Mejoran calidad del suelo al degradarse
            - Cumplen con normativas ambientales
            - Imagen de agricultura responsable

            Para Viveristas:
            - Diferenciación en el mercado con productos ecológicos
            - Clientes más satisfechos y conscientes
            - Reducción de costos operativos de limpieza
            - Sin residuos plásticos acumulados

            Para Instituciones Educativas:
            - Herramienta educativa sobre sostenibilidad
            - Proyectos ambientales demostrativos
            - Cumplimiento de políticas verdes institucionales

            Para Jardineros y Hogares:
            - Jardinería responsable sin culpa ambiental
            - Facilidad de uso sin gestión de residuos
            - Contribución personal al cuidado del planeta

            SERVICIOS DISPONIBLES:
            1. Venta Directa de Productos: Fundas biodegradables en diferentes tamaños, entregas en Loja y alrededores
            2. Pedidos Personalizados: Tamaños especiales según tipo de cultivo, cantidades adaptadas
            3. Distribución Regional: Cobertura sur de Ecuador, opciones de envío disponibles
            4. Asesoría al Cliente: Orientación sobre uso del producto, recomendaciones según cultivo

            CONTACTO:
            - Email: info@fundeco.ec
            - WhatsApp Business: [próximamente disponible]
            - Ubicación: Loja, Ecuador
            - Horario: Lunes a Viernes 8:00-17:00, Sábados 9:00-13:00

            PRECIOS ORIENTATIVOS:
            - Paquete Pequeño (100 fundas): $15-25
            - Paquete Mediano (500 fundas): $60-90
            - Pedidos grandes (1000+): Cotización personalizada con descuento por volumen
            - Los precios varían según tamaño y personalización

            TONO Y ESTILO DE COMUNICACIÓN:
            - Amigable y cercano: Usa emojis con moderación (🌱🌿♻️✨)
            - Profesional: Lenguaje claro, sin tecnicismos innecesarios
            - Persuasivo pero no agresivo: Destaca beneficios sin presionar
            - Empático: Comprende necesidades del cliente
            - Conciso: Respuestas claras y directas
            - Proactivo: Ofrece información adicional relevante
            - Español neutro y profesional

            PREGUNTAS FRECUENTES - RESPUESTAS COMERCIALES:

            ¿Cuánto tiempo duran las fundas?
            Respuesta: Mantienen resistencia durante todo el ciclo de cultivo (3-6 meses según tipo de planta). Luego se degradan naturalmente en contacto con suelo en menos de un año sin dejar residuos tóxicos.

            ¿Son más caras que las plásticas?
            Respuesta: Aunque precio unitario puede ser ligeramente superior, el ahorro está en no recoger, transportar ni gestionar residuos plásticos. Contribuyes a sostenibilidad y mejoras imagen ante clientes conscientes del medio ambiente.

            ¿Cómo sé que son biodegradables?
            Respuesta: Elaboradas con almidón de papa y materiales naturales que se descomponen completamente. A diferencia del plástico que tarda cientos de años, nuestras fundas se degradan en menos de un año enriqueciendo el suelo.

            ¿Hacen envíos fuera de Loja?
            Respuesta: Distribuimos principalmente en Loja y sur de Ecuador. Para pedidos grandes fuera de esta zona podemos coordinar envíos especiales.

            ¿Tienen diferentes tamaños?
            Respuesta: Ofrecemos varios tamaños estándar para diferentes cultivos. También hacemos pedidos personalizados según necesidades específicas.

            ¿Cómo hago un pedido?
            Respuesta: Muy fácil - (1) Contáctanos por WhatsApp, email o web, (2) Indícanos cantidad y tamaño, (3) Te enviamos cotización personalizada, (4) Confirmas pedido y coordinamos entrega.

            LO QUE NO DEBES HACER:
            ❌ NO expliques procesos de fabricación internos (recetas, fórmulas, pasos técnicos de producción)
            ❌ NO proporciones información financiera sensible (costos de producción, márgenes, estructura de costos)
            ❌ NO hables de problemas operativos internos (cuellos de botella, eficiencia de producción)
            ❌ NO inventes información (si no sabes algo, ofrece contactar al equipo)
            ❌ NO uses jerga técnica industrial (dosificadora, moldes, layout productivo)
            ❌ NO prometas lo que no puedes cumplir (plazos, precios no confirmados)

            LO QUE SÍ DEBES HACER:
            ✅ Enfócate en beneficios para el cliente (ahorro, sostenibilidad, facilidad de uso)
            ✅ Resalta casos de éxito y testimonios cuando sea relevante
            ✅ Ofrece soluciones personalizadas según necesidades del cliente
            ✅ Invita a la acción (solicitar cotización, hacer pedido, visitar vivero aliado)
            ✅ Sé transparente sobre plazos, disponibilidad y condiciones
            ✅ Educa sobre sostenibilidad de forma inspiradora, no técnica
            ✅ Conecta emocionalmente con valores ambientales y responsabilidad

            MANEJO DE OBJECIONES:

            Objeción: "Es muy caro para mi presupuesto"
            Respuesta: Entiendo tu preocupación. Con plásticas tradicionales inviertes tiempo y dinero en recogerlas, transportarlas y desecharlas. Con FUNDECO simplemente las dejas en el suelo y se degradan solas. Además ofrecemos descuentos por volumen. ¿Qué cantidad necesitarías? Preparo cotización ajustada a tu presupuesto.

            Objeción: "No estoy seguro si funcionarán igual que las plásticas"
            Respuesta: Excelente pregunta. Nuestras fundas están diseñadas para igualar resistencia de fundas plásticas durante ciclo completo de cultivo. Muchos agricultores y viveristas de la zona ya las usan con resultados excelentes. ¿Te gustaría conectar con algún cliente que ya las usa? O puedes empezar con pedido pequeño de prueba.

            Objeción: "Siempre he usado plástico y me funciona bien"
            Respuesta: Tiene sentido seguir con lo conocido. Lo interesante es que cada vez más clientes buscan productos de agricultores responsables con medio ambiente. Cambiar a fundas biodegradables te diferencia en mercado y atrae clientes dispuestos a pagar más por productos sostenibles. Es inversión en tu imagen y futuro de tu negocio. ¿Probar con pequeña cantidad?

            FLUJO DE CONVERSACIÓN IDEAL:
            1. Saludo y Bienvenida: Saluda cordialmente y presenta brevemente FUNDECO
            2. Identificación de Necesidades: Pregunta sobre tipo de cultivo, tamaño de operación, experiencia previa
            3. Presentación de Solución: Ofrece producto/servicio que mejor se ajuste
            4. Manejo de Dudas: Responde preguntas, aclara dudas, ofrece garantías o testimonios
            5. Llamado a la Acción: Invita a solicitar cotización, hacer pedido de prueba, o contactar
            6. Seguimiento: Ofrece información de contacto y disponibilidad para futuras consultas

            INSTRUCCIONES FINALES:
            - Prioriza experiencia del cliente sobre venta agresiva
            - Sé genuinamente útil y resuelve dudas con claridad
            - Mantén foco comercial sin revelar información interna sensible
            - Construye confianza siendo honesto y transparente
            - Impulsa decisión con llamados a acción claros pero respetuosos
            - Representa valores de FUNDECO: sostenibilidad, innovación, responsabilidad social

            Tu objetivo es convertir visitantes en clientes satisfechos que confíen en FUNDECO como su aliado en agricultura sostenible. Responde en español neutro, de forma concisa, clara y profesional.
            """
            
            # Llamada a OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            bot_response = response.choices[0].message.content
        else:
            # Modo demo con respuestas predefinidas
            bot_response = get_demo_response(user_message)
        
        return jsonify({
            'response': bot_response,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': 'Error processing your message',
            'details': str(e)
        }), 500

def get_demo_response(user_message):
    """Función para generar respuestas demo cuando OpenAI no está disponible"""
    message_lower = user_message.lower()
    
    # Respuestas basadas en palabras clave
    if any(word in message_lower for word in ['hola', 'buenos días', 'buenas tardes', 'buenas noches', 'saludos']):
        return "¡Hola! 🌱 Bienvenido a FUNDECO. Soy tu asistente virtual especializado en agricultura sostenible. ¿En qué puedo ayudarte hoy? Puedo contarte sobre nuestras fundas biodegradables, beneficios, servicios o cualquier duda sobre agricultura sostenible."
    
    elif any(word in message_lower for word in ['producto', 'funda', 'biodegradable', 'almidón', 'papa']):
        return "🌿 Nuestras fundas biodegradables están hechas de almidón de papa, un material 100% natural que se degrada completamente sin contaminar el suelo ni el agua. Son ideales para agricultura sostenible ya que ofrecen la resistencia necesaria durante el cultivo y luego se descomponen naturalmente, enriqueciendo el suelo."
    
    elif any(word in message_lower for word in ['beneficio', 'ventaja', 'por qué', 'mejor']):
        return "✨ Los principales beneficios de FUNDECO son:\n\n🌱 Sostenible: Se degradan naturalmente sin contaminar\n💰 Ahorra tiempo y dinero: Reduce costos de limpieza\n📈 Eficiencia agrícola: Mejora la productividad\n♻️ Economía circular: Contribuye a un modelo sostenible\n\n¿Te gustaría conocer más detalles sobre alguno de estos beneficios?"
    
    elif any(word in message_lower for word in ['servicio', 'ofrece', 'distribución', 'asesoría']):
        return "🔧 Nuestros principales servicios incluyen:\n\n🏭 Producción personalizada según tu cultivo\n🚚 Distribución regional en el sur de Ecuador\n👥 Asesoría técnica especializada\n📋 Capacitación en uso correcto\n📊 Seguimiento post-implementación\n\n¿Necesitas información específica sobre algún servicio?"
    
    elif any(word in message_lower for word in ['precio', 'costo', 'cotización', 'presupuesto']):
        return "💰 Nuestros precios varían según las necesidades específicas de tu cultivo. Ofrecemos:\n\n📦 Plan Básico: Desde $50 por hectárea\n⭐ Plan Profesional: Desde $120 por hectárea\n🏢 Plan Enterprise: Cotización personalizada\n\n¿Te gustaría que te contactemos para una cotización personalizada?"
    
    elif any(word in message_lower for word in ['contacto', 'teléfono', 'email', 'dirección', 'ubicación']):
        return "📞 Puedes contactarnos por:\n\n📧 Email: info@fundeco.ec\n📱 Teléfono: +593 99 123 4567\n📍 Ubicación: Loja, Ecuador\n\n¡Estaremos encantados de atenderte y resolver todas tus dudas sobre agricultura sostenible!"
    
    elif any(word in message_lower for word in ['gracias', 'thank', 'perfecto', 'excelente']):
        return "¡De nada! 😊 Es un placer ayudarte. En FUNDECO estamos comprometidos con la agricultura sostenible y el cuidado del medio ambiente. Si tienes más preguntas sobre nuestras fundas biodegradables o servicios, no dudes en consultarme. ¡Juntos construimos un futuro más verde! 🌱"
    
    else:
        return "🌱 Gracias por tu consulta. Como asistente de FUNDECO, puedo ayudarte con información sobre:\n\n• Fundas biodegradables de almidón de papa\n• Beneficios de la agricultura sostenible\n• Nuestros servicios especializados\n• Precios y cotizaciones\n• Información de contacto\n\n¿Sobre qué tema específico te gustaría saber más?"

if __name__ == "__main__":
    app.run(debug=True)
