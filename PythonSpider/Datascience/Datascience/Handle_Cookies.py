import re
import json
import base64

# def base_code(username, password):
#     str = '%s:%s' % (username, password)
#     encodestr = base64.b64encode(str.encode('utf-8'))
#     return '%s' % encodestr.decode() 

# username = "1227237489@qq.com"
# passwd = "FA755uNUXjFrkaJ"

# base = base_code(username,passwd)

# print(base)

cookie = "UM_distinctid=1720bca5544332-0cd2cfadbd793f-d373666-144000-1720bca5545728; _fbp=fb.1.1590743287656.21116350; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; _uab_collina=159235982430406268484295; t=8d1c8eea4b497af13dd510ad8e0d4349; cna=UE3aFtB3ewICAXWyAKJ4C5QN; mt=ci=91_1; cookie2=17cf4a978b672711776465cc39fd0937; _tb_token_=76e1e3eee80d8; v=0; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _m_h5_tk=e20a6042b45c563f03e1c6a133c69752_1592708310251; _m_h5_tk_enc=61ab9e244965e0046c0d967468fcc6b0; x5sec=7b227365617263686170703b32223a226430646437316131313233613632623836623330316139623036386166623137434b376d7576634645497971684f32682b2b377176414561444449344e7a41774d7a4d324d4459374d773d3d227d; _samesite_flag_=true; sgcookie=Ejwf1rGs79AjdCCrIBKPJ; unb=1732072239; uc3=vt3=F8dBxGGVoWGTJJ4pR4k%3D&nk2=rpw2T3kdsl6NqyspWhk%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&id2=UoYdXzNbaaJOug%3D%3D; csg=75695e10; lgc=%5Cu5F80%5Cu4E8B%5Cu968F%5Cu98CE741229; cookie17=UoYdXzNbaaJOug%3D%3D; dnk=%5Cu5F80%5Cu4E8B%5Cu968F%5Cu98CE741229; skt=4bccba6f46940c80; existShop=MTU5MjcwMzM0Mg%3D%3D; uc4=nk4=0%40rMYjj0o7sVO6CE0AZjBgY56tgHbOiYtbdw%3D%3D&id4=0%40UO6U%2BcKIhhPIJ42J8cyr0qqPp%2FtX; tracknick=%5Cu5F80%5Cu4E8B%5Cu968F%5Cu98CE741229; _cc_=VT5L2FSpdA%3D%3D; _l_g_=Ug%3D%3D; sg=996; _nk_=%5Cu5F80%5Cu4E8B%5Cu968F%5Cu98CE741229; cookie1=UNlhx%2FmXGtHmTIi2KSVsiHC3Yjxuiu0rpGvAOmp7VFs%3D; tfstk=cvT5B-OJs82SbJoUzQGVYOfhAW7FZ0Hfi06JNnjtvt4-YNO5iz4NCsPkx-4AXs1..; uc1=existShop=false&cookie15=V32FPkk%2Fw0dUvg%3D%3D&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&pas=0&cookie14=UoTV7gbqm%2FqhoA%3D%3D&cookie21=Vq8l%2BKCLjhS4UhJVbhgU; enc=SdXUE9%2B%2Fq7I%2FEMrLA0%2BUNxRJfLiuC81fLcuS3iWTfaMlupngpiWkII2zZ%2BKsEpIr5%2BYevVW4nGGjBp47xTVMCQ%3D%3D; JSESSIONID=D15180D2054C956A0A3FC8885F0574C1; l=eBPo2UwmQldQqqBkBOfwourza77tsIRjjuPzaNbMiOCPOQ5p5NxVWZxUEU89CnGNHspDR3lil4lwBfThpydq0-Y3L3k_J_Dr3dC..; isg=BGtrPyL4sVxQv-3dm4Vo5iE8-o9VgH8Cj65mX93oQqoBfIreZVF5UnPe0rQS79f6"

# url = 'https://detail.tmall.com/item.htm?id=589887260553&ns=1&abbucket=4'

cookies = dict(i.split('=',1) for i in cookie.split(';'))

print(cookies)
# if 'tmall' in url:
#     print('Tmail')