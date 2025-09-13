import math

class Galaxy:
    
    def __init__(self):
        self.vhs = []
        
    def update(self, raw):
        if not raw: return 
        vhs = []
        for rec in raw:
            try:
                tmp = rec.split('@')
                ship = tmp[0].strip()
                tmp1, tmp2 = tmp[1][:5], tmp[1][5:]
                tmp3 = tmp1.split('-')
                v = int(tmp3[0].strip())
                h = int(tmp3[1].strip())
                vhs.append([v, h, ship])
            except: pass
        if vhs: self.vhs = vhs
        for rec in self.vhs: print(rec)
        return
    