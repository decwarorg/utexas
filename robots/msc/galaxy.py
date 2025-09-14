import json

class Galaxy:
    
    def __init__(self):
        self.galaxy = {'ships': []}
        
    def update(self, raw):
        if not raw: return 
        self.galaxy['ships'] = [] # reset
        for rec in raw:
            try:
                tmp = rec.split('@')
                name = tmp[0].strip()
                tmp1, tmp2 = tmp[1][:5], tmp[1][5:]
                tmp3 = tmp1.split('-')
                v = int(tmp3[0].strip())
                h = int(tmp3[1].strip())
                self.galaxy['ships'].append({'position': {'v': v, 'h': h}, 'name': name})
            except: pass
        fp = open('galaxy.json', 'w')
        json.dump(self.galaxy, fp)
        fp.flush()
        fp.close()
    