

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib
import getpass


def _format_addr(s):
    name, addr = parseaddr(s)
    return Header(name, 'utf-8')

from_addr = 'ggsky02@163.com'
password = getpass.getpass(('password:'))#'********'
to_addr = '1609696537@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEText('你明天再吗？', 'plain', 'utf-8')
msg['From'] = '<ggsky02@163.com>'
msg['To'] = "1609696537@qq.com"
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8')

print('-----------------------------------------------')

server = smtplib.SMTP(smtp_server)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

