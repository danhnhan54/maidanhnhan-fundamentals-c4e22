from gmail import GMail, Message
from random import choice
from datetime import datetime
gmail = GMail('Nhân <nhantov0504@gmail.com>','zxc123')
html_template = '''
<p>Dear anh,</p>
<p>H&ocirc;m nay e bị {{ bệnh }} n&ecirc;n xin ph&eacute;p nghỉ l&agrave;m để đi kh&aacute;m. Mong anh chấp thuận.</p>
<p>Em cảm ơn!&nbsp;</p>
'''
sicklist = ['đau bụng','đau đầu','ốm','đau dạ dày']
html_content = html_template.replace("{{ bệnh }}",choice(sicklist))
msg = Message('Đơn xin nghỉ ốm',to='danhnhan0504@gmail.com',html=html_content)
while True:
    if datetime.now().hour == 7:
        gmail.send(msg)    
        break

