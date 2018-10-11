from gmail import GMail, Message
from random import choice
gmail = GMail('Nhân <nhantov0504@gmail.com>','viettinbank123')
html_template = '''
<p><em><strong>Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</strong></em></p>
<p><strong>Độc lập</strong> - <em>Tự do</em> - <span style="text-decoration: underline;">Hạnh ph&uacute;c</span></p>
<p>Hello {{ people }}&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cool.gif" alt="cool" /></p>
'''
peoplelist = ['Quân','Nhân','Việt','Nam']
html_content = html_template.replace("{{ people }}",choice(peoplelist))
msg = Message('Test test test',to='danhnhan0504@gmail.com',html=html_content)
gmail.send(msg)