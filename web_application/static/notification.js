/**
 * @param {string} message 
 * @param {number} duration 
**/
function showNotification(message, duration = 3000) {
    const notification = document.createElement('div');
    notification.className = 'toast-notification';
    notification.textContent = message;

    Object.assign(notification.style, {
        position: 'fixed',
        bottom: '20px',
        right: '20px',
        padding: '12px 24px',
        borderRadius: '8px',
        fontSize: '14px',
        fontWeight: '500',
        zIndex: '99999',
        opacity: '0',
        transform: 'translateY(20px)',
        transition: 'opacity 0.3s ease, transform 0.3s ease',
        pointerEvents: 'none',
        boxShadow: '0 4px 12px rgba(0, 0, 0, 0.3)',
        backgroundColor: 'rgba(26, 26, 46, 0.9)',
        border: '1px solid rgba(139, 92, 246, 0.3)',
        color: 'rgba(221, 214, 254, 1)'
    });

    document.body.appendChild(notification);

    requestAnimationFrame(() => {
        notification.style.opacity = '1';
        notification.style.transform = 'translateY(0)';
    });

    setTimeout(() => {
        notification.style.opacity = '0';
        notification.style.transform = 'translateY(20px)';
        setTimeout(() => notification.remove(), 300);
    }, duration);
}
