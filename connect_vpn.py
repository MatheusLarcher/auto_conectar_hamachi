from subprocess import Popen
from pywinauto import Desktop

app = Popen(r"C:\Program Files (x86)\LogMeIn Hamachi\hamachi-2-ui.exe", shell = True)


dialog = Desktop(backend='uia').window(title='LogMeIn Hamachi:')
dialog.wait('visible')

def ligar_hamachi():
    try:
        last_child_text = dialog.child_window(title="Offline", control_type="Tree").window_text()
        if(last_child_text == "Offline"):
            dialog.child_window(title='Power', control_type='Button').click()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        
def conectar_vpn(nome_vpn):
    tree = dialog.child_window(title="Matheus-2D", control_type="Tree")
    tree.wait('visible', 300)
    tree.get_item('\\' + nome_vpn).focus
    tree.get_item('\\' + nome_vpn).click_input(double=True)
    

ligar_hamachi()
conectar_vpn('empresa')
