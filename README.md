# [SUPPORT] Python Ideas
🤖BOT DE SOPORTE PARA :
@Python_Insights 🐍
@Python_Ideas_Community 💬

👨‍💻Bot Creado por : @AresDza

**CREADO 100% Python 3.10.3
BOT DE TELEGRAM PARA DAR SOPORTE**

# >INTEGRACIONES :
<details><summary>Función de Respuesta para el Comando /start</summary><p>
  </details> 
<details><summary>Mensaje de Bienvenida Automatizado para Usuarios que entren al Chat
  </details> 
<details><summary>Mensaje de Despedida Automatizado para Usuarios que salgan del Chat
  </details> 
<details><summary>Comando /ban (Expulsar Usuario y no lo Permite volver al Chat)
  </details> 
<details><summary>Comando /unban (Permite a un Usuario Expulsado volver al Chat)
  </details> 

  
###### Desde aquí tomará el Token para Hacer Funcionar al Bot :
```ruby
if __name__ == '__main__':
    token = os.environ['TOKEN']
    bot = telegram.Bot(token=token)
    updater = Updater(token=token, use_context=True)
```
###### Luego aquí definimos los Dispatcher :
```ruby
    dp = updater.dispatcher
```
###### Para Ejecutar el Bot :
```ruby    
    updater.start_polling()
    print(f'Ejecutando el bot @{bot.username}')
    updater.idle()
```
