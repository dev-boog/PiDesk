function toggleWidget(widget_id, button) {
    const widget = document.getElementById(widget_id);
    if (!widget) return;
    
    const isVisible = localStorage.getItem('widget_' + widget_id) !== 'hidden';
    
    // Toggle state
    const newState = isVisible ? 'hidden' : 'visible';
    localStorage.setItem('widget_' + widget_id, newState);
    
    // Apply to widget and button
    widget.style.display = isVisible ? 'none' : '';
    if (button) {
        button.classList.toggle('bg-violet-500/20', !isVisible);
        button.classList.toggle('bg-white/5', isVisible);
    }
}

function applyWidgetStates() {
    // Apply saved states to all widgets
    document.querySelectorAll('[data-widget]').forEach(widget => {
        const state = localStorage.getItem('widget_' + widget.id);
        widget.style.display = state === 'hidden' ? 'none' : '';
    });
    
    // Apply saved states to all toggle buttons
    document.querySelectorAll('[data-toggle]').forEach(button => {
        const widget_id = button.dataset.toggle;
        const isHidden = localStorage.getItem('widget_' + widget_id) === 'hidden';
        button.classList.toggle('bg-violet-500/20', !isHidden);
        button.classList.toggle('bg-white/5', isHidden);
    });
}

document.addEventListener('DOMContentLoaded', applyWidgetStates);