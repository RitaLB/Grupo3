from pessoa import Pessoa
import PySimpleGUI as sg

linha0 = [sg.Text('Qual seu peso?'), sg.InputText('', key = 'peso'), sg.Text('kg')]
linha1 = [sg.Text('Qual sua altura?'), sg.InputText('', key = 'altura'), sg.Text('m')]
linha2 = [sg.Text('Seu IMC é'), sg.Text('', key = 'imc', size = (6, 1))]
linha3 = [sg.Text('Classificação:'), sg.Text('', key = 'classificacao')]
linha4 = [sg.Text('', size = (14, 1)), sg.Button('Calcular IMC')]
container = [linha0, linha1, linha2, linha3, linha4]

#Janela Principal
window = sg.Window('Calculadora de IMC', container, font=('Helvetica', 14))

#Loop de eventos
rodando = True
while rodando:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        rodando = False
    elif event == 'Calcular IMC':
        try:
            peso = float(values['peso'])
            altura = float(values['altura'])
            pessoa = Pessoa(peso, altura)
            imc = pessoa.calcular_imc()
            window.Element('imc').Update(imc)
            if imc < 18.5:
                window.Element('classificacao').Update('Baixo Peso')
            elif imc < 25:
                window.Element('classificacao').Update('Peso normal')
            elif imc < 10:
                window.Element('classificacao').Update('Sobrepeso')
            else:
                window.Element('classificacao').Update('Obesidade')

        except ValueError:
            rodando = True
        