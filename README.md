# [SUPPORT] Python Ideas
🤖BOT DE SOPORTE PARA :
@Python_Insights 🐍
@Python_Ideas_Community 💬

👨‍💻Bot Creado por : @AresDza

**CREADO 100% Python 3.10.3
BOT DE TELEGRAM PARA DAR SOPORTE**

# >INTEGRACIONES :
<details><summary>Función de Respuesta para el Comando /start</summary>
<p>
```  
Al mandar /start se ejecuta la Función start_handler que te mandará un mensaje con unos botones que llevarán a el canal @Python_Insights 🐍 y al Chat @Python_Ideas_Community 💬.
```
</details></p>
<details><summary>Mensaje de Bienvenida Automatizado para Usuarios que entren al Chat</summary>
<p>
```  
Este comando estará filtrando por nuevos miembros, y al unirse alguien se ejecutaría la función welcomemsg.
```  
</details> </p>
<details><summary>Mensaje de Despedida Automatizado para Usuarios que salgan del Chat</summary>
<p>
```  
Este comando estará filtrando por miembros que salgan o sean expulsados, y al salir alguien se ejecutaría la función goodbyemsg.
```  
</details> </p>
<details><summary>Comando /ban (Expulsar Usuario y no lo Permite volver al Chat)</summary>
<p>
```  
Al ejecutar el comando /ban haciendole reply a un mensaje tomará el ID y el CHAT de ese Usuario, y luego lo Expulsará del Chat evitando que pueda volver a entrar a no ser que sea desbaneado.
```  
</details> </p>
<details><summary>Comando /unban (Permite a un Usuario Expulsado volver al Chat)</summary>
<p>
```  
Al ejecutar el comando /unban haciendole reply a un mensaje tomará el ID y el CHAT de ese Usuario, y luego le permitirá entrar denuevo al Chat, anulando su baneo.
```  
</details> </p>

  
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
