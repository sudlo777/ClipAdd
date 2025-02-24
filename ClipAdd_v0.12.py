#! python3
# -*- coding: utf-8 -*-
import pyperclip

print('''[ClipAdd_v0.12]Working...
hanyang@2025-02-24''','\n')
print('0.0',end='',flush=True)
x = 0.0

while True:
    pyperclip.copy(round(x,2))
    tip = ' [%.2f]' % x
    tip_len = len(tip)

    print(tip,end='',flush=True)
    contxt = pyperclip.waitForNewPaste().replace(',','').replace('+',' ').replace('-',' -').strip()
    contxt = contxt.replace(' ','\n').replace('\t','\n').replace('\v','\n').replace('\r','\n').split('\n')
    print(tip_len*'\b',end='',flush=True)
    txt_List = list(filter(None,contxt))
    if len(txt_List) == 0:
        txt_List.append('x')

    for txt in txt_List:
        try:
            sun = round(float(txt.strip()),2)
            op = ' +' if sun > 0.0 else ''
            print(op,sun,end='',flush=True)
            x += sun
        except:
            pyperclip.copy(round(x,2))
            input(' = %.2f [Enter]' % x)
            print('0.0',end='',flush=True)
            x = 0.0
            break

#Complete
