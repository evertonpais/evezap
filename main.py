import flet as ft

def main(page):
    texto = ft.Text('evezap')
    page.add(texto)
    entrada_usuario = ft.TextField(label = 'escreva seu nome')
    
    chat= ft.Column()
    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        page.update()
    page.pubsub.subscribe(enviar_mensagem_tunel)
    def enviar_mensagem(event):
        
        texto_campo_mensagem = f'{entrada_usuario.value} diz : \n {entrada_chat.value}'
        
        
        page.pubsub.send_all(texto_campo_mensagem)
        entrada_chat.value=''
        page.update()
    entrada_chat = ft.TextField(label='Digite sua mensagem',on_submit=enviar_mensagem)    
    botao_enviar = ft.ElevatedButton('enviar',on_click=enviar_mensagem)
    
    def entrar_chat(event):
        popup.open = False
        page.remove(botao_iniciar)
        nome = ft.Text(f' {entrada_usuario.value} entrou no chat',color='grey',size=15)
        
        page.add(chat)
        
        linha_mensagem = ft.Row([entrada_chat,botao_enviar])
        page.add(linha_mensagem)
        
        page.pubsub.send_all(nome.value)
        page.update
        
    popup = ft.AlertDialog(open= False,modal = True,
                           title= ft.Text('Bem vindo ao evezap',color='red'),
                           content=entrada_usuario,
                           actions=[ft.ElevatedButton('Entrar',on_click=entrar_chat)])
    def iniciar_chat(event):
        page.dialog = popup
        popup.open = True
        page.update()
    botao_iniciar = ft.ElevatedButton('iniciar chat',on_click=iniciar_chat)
    page.add(botao_iniciar)
    
    

ft.app(main,view=ft.WEB_BROWSER)

