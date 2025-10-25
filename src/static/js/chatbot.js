// FUNDECO Chatbot JavaScript
class FundecoBot {
    constructor() {
        this.isOpen = false;
        this.isLoading = false;
        this.messages = [];
        this.init();
    }

    init() {
        this.createChatbotHTML();
        this.bindEvents();
        this.showWelcomeMessage();
    }

    createChatbotHTML() {
        // Crear el HTML del chatbot
        const chatbotHTML = `
            <!-- Botón flotante del chatbot -->
            <button class="chatbot-toggle" id="chatbotToggle">
                <i class="fa fa-comments"></i>
            </button>

            <!-- Ventana del chatbot -->
            <div class="chatbot-window" id="chatbotWindow">
                <!-- Header -->
                <div class="chatbot-header">
                    <div class="chatbot-avatar">
                        <i class="fa fa-leaf"></i>
                    </div>                    <div class="chatbot-info">
                        <h3>Asistente Comercial</h3>
                        <p>Especialista en agricultura sostenible</p>
                    </div>
                </div>                <!-- Área de mensajes -->
                <div class="chatbot-messages" id="chatbotMessages">
                    <div class="welcome-message">
                        <h4>¡Bienvenido a FUNDECO! 🌱</h4>
                        <p>Soy tu asistente comercial especializado en fundas biodegradables para agricultura sostenible. ¿En qué puedo ayudarte hoy?</p>
                        <div class="quick-suggestions">
                            <span class="suggestion-chip" data-suggestion="Quiero conocer los productos FUNDECO">🛒 Ver Productos</span>
                            <span class="suggestion-chip" data-suggestion="¿Cuáles son los precios y paquetes disponibles?">💰 Precios</span>
                            <span class="suggestion-chip" data-suggestion="¿Cómo hago un pedido?">📦 Hacer Pedido</span>
                            <span class="suggestion-chip" data-suggestion="¿Hacen envíos a mi zona?">🚚 Envíos</span>
                            <span class="suggestion-chip" data-suggestion="¿Por qué elegir FUNDECO?">⭐ Beneficios</span>
                            <span class="suggestion-chip" data-suggestion="Necesito una cotización personalizada">📋 Cotización</span>
                        </div>
                    </div>
                </div>

                <!-- Área de entrada -->
                <div class="chatbot-input">
                    <div class="input-group">
                        <input 
                            type="text" 
                            class="message-input" 
                            id="messageInput" 
                            placeholder="Escribe tu mensaje..."
                            autocomplete="off"
                        >
                        <button class="send-button" id="sendButton">
                            <i class="fa fa-paper-plane"></i>
                        </button>
                    </div>
                </div>
            </div>
        `;

        // Agregar al body
        document.body.insertAdjacentHTML('beforeend', chatbotHTML);
    }

    bindEvents() {
        // Botón toggle
        document.getElementById('chatbotToggle').addEventListener('click', () => {
            this.toggleChatbot();
        });

        // Botón enviar
        document.getElementById('sendButton').addEventListener('click', () => {
            this.sendMessage();
        });

        // Enter en input
        document.getElementById('messageInput').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.sendMessage();
            }
        });

        // Sugerencias rápidas
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('suggestion-chip')) {
                const suggestion = e.target.getAttribute('data-suggestion');
                this.sendMessage(suggestion);
            }
        });

        // Cerrar al hacer click fuera
        document.addEventListener('click', (e) => {
            const chatbotWindow = document.getElementById('chatbotWindow');
            const chatbotToggle = document.getElementById('chatbotToggle');
            
            if (this.isOpen && 
                !chatbotWindow.contains(e.target) && 
                !chatbotToggle.contains(e.target)) {
                this.toggleChatbot();
            }
        });
    }

    toggleChatbot() {
        const window = document.getElementById('chatbotWindow');
        const toggle = document.getElementById('chatbotToggle');
        
        this.isOpen = !this.isOpen;
        
        if (this.isOpen) {
            window.classList.add('open');
            toggle.classList.add('active');
            // Enfocar el input
            setTimeout(() => {
                document.getElementById('messageInput').focus();
            }, 300);
        } else {
            window.classList.remove('open');
            toggle.classList.remove('active');
        }
    }

    showWelcomeMessage() {
        // El mensaje de bienvenida ya está en el HTML
    }

    async sendMessage(customMessage = null) {
        const input = document.getElementById('messageInput');
        const message = customMessage || input.value.trim();
        
        if (!message || this.isLoading) return;

        // Limpiar input
        input.value = '';
        
        // Agregar mensaje del usuario
        this.addMessage(message, 'user');
        
        // Mostrar indicador de escritura
        this.showTypingIndicator();
        
        try {
            this.isLoading = true;
            document.getElementById('sendButton').disabled = true;
            
            // Llamada a la API
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();
            
            // Ocultar indicador de escritura
            this.hideTypingIndicator();
            
            if (response.ok) {
                // Agregar respuesta del bot
                this.addMessage(data.response, 'bot');
            } else {
                this.addMessage('Lo siento, hubo un error. Por favor intenta nuevamente.', 'bot');
            }
            
        } catch (error) {
            console.error('Error:', error);
            this.hideTypingIndicator();
            this.addMessage('No pude conectarme al servidor. Verifica tu conexión.', 'bot');
        } finally {
            this.isLoading = false;
            document.getElementById('sendButton').disabled = false;
        }
    }

    addMessage(content, sender) {
        const messagesContainer = document.getElementById('chatbotMessages');
        
        // Remover mensaje de bienvenida si existe
        const welcomeMessage = messagesContainer.querySelector('.welcome-message');
        if (welcomeMessage) {
            welcomeMessage.remove();
        }
        
        const messageHTML = `
            <div class="message ${sender}">
                <div class="message-avatar">
                    <i class="fa fa-${sender === 'user' ? 'user' : 'leaf'}"></i>
                </div>
                <div class="message-content">
                    ${this.formatMessage(content)}
                </div>
            </div>
        `;
        
        messagesContainer.insertAdjacentHTML('beforeend', messageHTML);
        this.scrollToBottom();
        
        // Guardar mensaje
        this.messages.push({ content, sender, timestamp: new Date() });
    }

    formatMessage(content) {
        // Convertir URLs en enlaces
        const urlRegex = /(https?:\/\/[^\s]+)/g;
        content = content.replace(urlRegex, '<a href="$1" target="_blank">$1</a>');
        
        // Convertir saltos de línea
        content = content.replace(/\n/g, '<br>');
        
        return content;
    }

    showTypingIndicator() {
        const messagesContainer = document.getElementById('chatbotMessages');
        const typingHTML = `
            <div class="message bot typing-message">
                <div class="message-avatar">
                    <i class="fa fa-leaf"></i>
                </div>
                <div class="typing-indicator">
                    <div class="typing-dots">
                        <span class="typing-dot"></span>
                        <span class="typing-dot"></span>
                        <span class="typing-dot"></span>
                    </div>
                </div>
            </div>
        `;
        
        messagesContainer.insertAdjacentHTML('beforeend', typingHTML);
        this.scrollToBottom();
    }

    hideTypingIndicator() {
        const typingMessage = document.querySelector('.typing-message');
        if (typingMessage) {
            typingMessage.remove();
        }
    }

    scrollToBottom() {
        const messagesContainer = document.getElementById('chatbotMessages');
        setTimeout(() => {
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }, 100);
    }

    // Métodos públicos para integración
    openChatbot() {
        if (!this.isOpen) {
            this.toggleChatbot();
        }
    }

    closeChatbot() {
        if (this.isOpen) {
            this.toggleChatbot();
        }
    }

    sendPredefinedMessage(message) {
        this.openChatbot();
        setTimeout(() => {
            this.sendMessage(message);
        }, 500);
    }
}

// Inicializar el chatbot cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    // Verificar que Font Awesome esté disponible
    if (typeof FontAwesome === 'undefined') {
        console.warn('Font Awesome no está cargado. Los iconos del chatbot podrían no mostrarse correctamente.');
    }
    
    // Crear instancia global del chatbot
    window.fundecoBot = new FundecoBot();
    
    console.log('🌱 FUNDECO Bot inicializado correctamente');
});

// Funciones de utilidad global
window.openFundecoBot = function() {
    if (window.fundecoBot) {
        window.fundecoBot.openChatbot();
    }
};

window.sendToFundecoBot = function(message) {
    if (window.fundecoBot) {
        window.fundecoBot.sendPredefinedMessage(message);
    }
};