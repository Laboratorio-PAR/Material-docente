'''
Se utiliza herencia de orientación a objetos en los widgets. Sirve
para reutilizar código y personalizar el contenido class MiVentana(wx.Frame):
'''

import wx
# Heredamos de wx.Frame para crear nuestra propia ventana
# Nos referimos a ventana cuando hablamos de wx.Frame
class MiVentana(wx.Frame):
    '''
    Ventana centrada y con titulo y tamanio personalizados
    '''
    def __init__(self, parent, title, size):
        # Siempre llamamos a super + __init__
        super(MiVentana, self).__init__(parent, title=title, size=size)
        # Centramos la ventana
        self.Centre()
        return None

def main():
    app = wx.App()
    ven = MiVentana(None, title='Segundo ejemplo', size=(600, 200))
    ven.Show()
    app.MainLoop()
    return None

if __name__ == '__main__':
    main()