function hide_widget(widget_id) 
{
    document.getElementById(widget_id).style.display = 'none';
}

function show_widget(widget_id) 
{
    document.getElementById(widget_id).style.display = 'block';
}

function toggleWidget(widget_id, button) 
{
    const widget = document.getElementById(widget_id);
    const isVisible = localStorage.getItem('widget_' + widget_id) !== 'hidden';
    const newState = isVisible ? 'hidden' : 'visible';

    localStorage.setItem('widget_' + widget_id, newState);
    
    widget.style.display = isVisible ? 'none' : '';
    button.classList.toggle('bg-emerald-700', !isVisible);
    button.classList.toggle('bg-zinc-700', isVisible);
}

function applyWidgetStates() {
    document.querySelectorAll('[data-widget]').forEach(widget => {
        const state = localStorage.getItem('widget_' + widget.id);
        widget.style.display = state === 'hidden' ? 'none' : '';
    });
    
    document.querySelectorAll('[data-toggle]').forEach(button => {
        const widget_id = button.dataset.toggle;
        const isHidden = localStorage.getItem('widget_' + widget_id) === 'hidden';
        button.classList.toggle('bg-emerald-700', !isHidden);
        button.classList.toggle('bg-zinc-700', isHidden);
    });
}

document.addEventListener('DOMContentLoaded', applyWidgetStates);