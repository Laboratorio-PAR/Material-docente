'''
Barra menú
'''

import wx
class MiVentana(wx.Frame):
    def __init__(self):
        super(MiVentana, self).__init__(None)
        self.InitUI()
        return None

    def InitUI(self):
        barra = wx.MenuBar()
        miMenu = wx.Menu()
        fileItem = miMenu.Append(wx.ID_EXIT, 'Salir', 'Sale de la app')
        barra.Append(miMenu, 'Archivo')
        self.SetMenuBar(barra)
        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)
        self.SetSize((300, 200))
        self.SetTitle('Menu simple')
        self.Centre()
        return None

    def OnQuit(self, event):  # siempre poner el parámetro event en los métodos callback
        self.Close()
        return None

def main():
    app = wx.App()
    ventana = MiVentana()
    ventana.Show()
    app.MainLoop()
    return None
if __name__ == '__main__':
    main()