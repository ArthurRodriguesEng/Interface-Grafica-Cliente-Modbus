import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from clientemodbus import ClienteMODBUS

from kivy.clock import Clock


class MyWidget(GridLayout):
    c = ClienteMODBUS

    def connect(self):
        ip = str(self.ids.T_ip.text)
        port = int(self.ids.T_port.text)
        global c
        c = ClienteMODBUS(ip, int(port))

    def LerDados(self, tipo):
        global c
        addr = int(self.ids.T_endereco.text)
        print(c.lerDado(int(tipo), int(addr)))
        self.ids.label.text = str(c.lerDado(int(tipo), int(addr)))
        # if self.ids.c_box.active == True:
        #     self.ids.label.text = str(Clock.schedule_interval(c.lerDado(int(tipo), int(addr)),0.5))
        # else:
        #     self.ids.label.text = str(c.lerDado(int(tipo), int(addr)))

    # def command(self, tipo):
    #     if self.ids.c_box.active == True:
    #         self._ev = Clock.schedule_interval(self.LerDados(tipo), 2)
    #     else:
    #         self._ev.cancel()


class BasicApp(App):
    def build(self):
        """
        Método para construção do aplicativo com base no widget criado
        """
        return MyWidget()


if __name__ == '__main__':
    Config.set('graphics', 'resizable', True)
    BasicApp().run()
