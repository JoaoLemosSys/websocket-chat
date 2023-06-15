import tornado.ioloop
import tornado.web
import tornado.websocket


class ChatHandler(tornado.websocket.WebSocketHandler):
    clients = set()

    def check_origin(self, origin):
        # Allow all origins
        return True

    def open(self):
        ChatHandler.clients.add(self)

    def on_message(self, message):
        for client in ChatHandler.clients:
            objmessagem= message.strip().split(',')
            horario = objmessagem[0]
            nickname = objmessagem[1]
            mensagem = objmessagem[2]

            messagem_formatada= f"<p>({horario}) <strong> {nickname} fala </strong> {mensagem}</p>"

            client.write_message(messagem_formatada)

    def on_close(self):
        ChatHandler.clients.remove(self)


app = tornado.web.Application([(r"/chat", ChatHandler), ])

if __name__ == "__main__":
    print("Servidor escutando na porta 8888")    
    app.listen(8888, address="0.0.0.0")
    tornado.ioloop.IOLoop.current().start()
