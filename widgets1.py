import wx

def main():
    app = wx.App()
    # widget padre es None. title y size son personalizados
    ven= wx.Frame(None, title='Hola Mundo!', size=(700,300))
    ven.Show() # obligatorio mostrar siempre la ventana
    app.MainLoop()
    return None
if __name__ == '__main__':
    main()