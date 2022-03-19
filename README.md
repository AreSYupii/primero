# [SUPPORT] Python Ideas
![photo_2022-03-16_21-21-11](https://user-images.githubusercontent.com/101855063/159123528-b4a91112-03c7-4dca-9573-60a91dcff332.jpg)



🤖BOT DE SOPORTE PARA :

[@Python_Insights 🐍](https://t.me/Python_Insights)

[@Python_Ideas_Community 💬](https://t.me/Python_Ideas_Community)

👨‍💻Bot Creado por : [AresDza Developer 👾](https://t.me/AresDza)

**CREADO 100% Python 3.10.3
BOT DE TELEGRAM PARA DAR SOPORTE**

# >INTEGRACIONES :
1. Función de Respuesta para el Comando /start[^1]
2. Mensaje de Bienvenida Automatizado para Usuarios que entren al Chat[^2]
3. Mensaje de Despedida Automatizado para Usuarios que salgan del Chat[^3]
4. Comando /ban (Expulsar Usuario y no lo Permite volver al Chat)[^4]
5. Comando /unban (Permite a un Usuario Expulsado volver al Chat)[^5]
6. Comando /pin (Anclar un Mensaje al que se le haga reply)[^6]
7. Comando /unpin (Desanclar un Mensaje al que se le haga reply)[^7]
8. Comando /yinfo (Te da el ID del Usuario y del Chat al que se le haga reply, y tu usuario)[^8]
  
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

[^1]:Al mandar /start se ejecuta la Función start_handler que te mandará un mensaje con unos botones que llevarán a el canal @Python_Insights 🐍 y al Chat @Python_Ideas_Community 💬.
[^2]:Este comando estará filtrando por nuevos miembros, y al unirse alguien se ejecutaría la función welcomemsg.
[^3]:Este comando estará filtrando por miembros que salgan o sean expulsados, y al salir alguien se ejecutaría la función goodbyemsg.
[^4]:Al ejecutar el comando /ban haciendole reply a un mensaje tomará el ID y el CHAT de ese Usuario, y luego lo Expulsará del Chat evitando que pueda volver a entrar a no ser que sea desbaneado.
[^5]:Al ejecutar el comando /unban haciendole reply a un mensaje tomará el ID y el CHAT de ese Usuario, y luego le permitirá entrar denuevo al Chat, anulando su baneo.
[^6]:Al ejecutar el comando /pin haciendole reply a un mensaje tomará el ID del mensaje y el ID del chat, lo anclará a en el chat y eliminará el mensaje desde el que se ejecutó el comando.
[^7]:Al ejecutar el comando /unpin haciendole reply a un mensaje tomará el ID del mensaje y el ID del chat, lo desanclará del chat y eliminará el mensaje desde el que se ejecutó el comando.
[^8]:Al ejecutar el comando /yinfo te dirá el ID de usuario , el Chat y tu ID cuando le hagas reply a un mensaje.
