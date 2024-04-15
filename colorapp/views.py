from django.shortcuts import render, redirect
from .forms import RGBForm
from .color_identifier import predict_color  # Importa a função do modelo

def home(request):
    form = RGBForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        # Extrai os valores RGB do formulário
        rgb = form.cleaned_data['rgb']
        r, g, b = map(int, rgb.split(','))  # Assume que a entrada será no formato "255,0,255"
        # Prediz a cor usando o modelo
        color_name = predict_color(r, g, b)
        message = f'A cor identificada é: {color_name}'
        # Armazena o resultado na sessão
        request.session['message'] = message
        # Redireciona para a mesma página mas com método GET
        return redirect('home')

    # Tenta recuperar a mensagem da sessão se disponível
    message = request.session.pop('message', None)
    return render(request, 'colorapp/home.html', {'form': form, 'message': message})
