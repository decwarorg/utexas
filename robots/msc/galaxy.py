import json
import shutil
from .definitions import fed, emp

class Galaxy:
    
    def __init__(self):
        self.galaxy = {'ships': []}
        
    def update(self, raw):
        if not raw: return 
        self.galaxy['ships'] = [] # reset
        for rec in raw:
            try:
                tmp = rec.split('@')
                name = tmp[0].strip()[-1]
                if name in fed: side = 'f'
                elif name in emp: side = 'e'
                else: side = 'r'
                tmp1, tmp2 = tmp[1][:5], tmp[1][5:]
                tmp3 = tmp1.split('-')
                v = int(tmp3[0].strip())
                h = int(tmp3[1].strip())
                self.galaxy['ships'].append({'position': {'v': v, 'h': h}, 'name': name, 'side': side})
            except: pass
        fp = open('galaxy.json', 'w')
        json.dump(self.galaxy, fp)
        fp.flush()
        fp.close()
        try: shutil.copy('galaxy.json', '../galaxy/galaxy.json')
        except: pass
    