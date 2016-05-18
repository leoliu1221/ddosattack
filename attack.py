import re
from mechanize import Browser
br = Browser()
br.addheaders = [('User-agent','Firefox')]
br.open('http://www-qq-com-loading.osodicoiscvo.top/657456378/admin/ceshi.php?user=swhe3_JcheMnPYYv')
br.select_form('form1')
br.form['username'] = 'nimashishabi'
br.form['password'] = 'nimashidashabi'
res = br.submit()
