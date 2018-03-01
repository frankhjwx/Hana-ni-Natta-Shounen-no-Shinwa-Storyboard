from LyricsParser import *
import random
from BeatmapParser.beatmapparser import *

spacing = 4
pi = 3.1415926


def Command(*args):
    s = ','.join(str(arg) for arg in args)
    return s


# single arg = 1 control point, 2 args = multiple control points
def get_control_points(cp, *t):
    if len(t) == 1:
        for point in cp:
            if abs(point[0] - t[0]) < 5:
                return point[1]
    if len(t) == 2:
        points = []
        for point in cp:
            if t[0]-5 <= point[0] <= t[1]+5:
                points.append(point)
        return points


class Obj():
    def __init__(self, filename, alignment='Centre', x=320, y=240):
        self.type = 'Sprite'
        self.placement = 'Foreground'
        self.alignment = alignment
        self.filename = filename
        self.x = x
        self.y = y
        self.codes = []
        self.codes.append(','.join([self.type, self.placement, self.alignment, self.filename, str(self.x), str(self.y)]))

    def addM(self, fade, *args):
        if len(args) == 6:
            self.codes.append(Command(' M', fade, *args))
        if len(args) == 4:
            self.codes.append(Command(' M', fade, *args))
        if len(args) == 3:
            self.codes.append(Command(' M', fade, args[0], '', args[1], args[2]))

    def addV(self, fade, *args):
        if len(args) == 6:
            self.codes.append(Command(' V', fade, *args))
        if len(args) == 4:
            self.codes.append(Command(' V', fade, *args))
        if len(args) == 3:
            self.codes.append(Command(' V', fade, args[0], '', args[1], args[2]))

    def addF(self, fade, *args):
        if len(args) == 4:
            self.codes.append(Command(' F', fade, *args))
        if len(args) == 3:
            self.codes.append(Command(' F', fade, *args))
        if len(args) == 2:
            self.codes.append(Command(' F', fade, args[0], '', args[1]))

    def addR(self, fade, *args):
        if len(args) == 4:
            self.codes.append(Command(' R', fade, *args))
        if len(args) == 3:
            self.codes.append(Command(' R', fade, *args))
        if len(args) == 2:
            self.codes.append(Command(' R', fade, args[0], '', args[1]))

    def addS(self, fade, *args):
        if len(args) == 4:
            self.codes.append(Command(' S', fade, *args))
        if len(args) == 3:
            self.codes.append(Command(' S', fade, *args))
        if len(args) == 2:
            self.codes.append(Command(' S', fade, args[0], '', args[1]))

    def addVX(self, fade, *args):
        if len(args) == 4:
            self.codes.append(Command(' VX', fade, *args))
        if len(args) == 3:
            self.codes.append(Command(' VX', fade, *args))
        if len(args) == 2:
            self.codes.append(Command(' VX', fade, args[0], '', args[1]))

    def addVY(self, fade, *args):
        if len(args) == 4:
            self.codes.append(Command(' VY', fade, *args))
        if len(args) == 3:
            self.codes.append(Command(' VY', fade, *args))
        if len(args) == 2:
            self.codes.append(Command(' VY', fade, args[0], '', args[1]))

    def addMX(self, fade, *args):
        if len(args) == 4:
            self.codes.append(Command(' MX', fade, *args))
        if len(args) == 3:
            self.codes.append(Command(' MX', fade, *args))
        if len(args) == 2:
            self.codes.append(Command(' MX', fade, args[0], '', args[1]))

    def addMY(self, fade, *args):
        if len(args) == 4:
            self.codes.append(Command(' MY', fade, *args))
        if len(args) == 3:
            self.codes.append(Command(' MY', fade, *args))
        if len(args) == 2:
            self.codes.append(Command(' MY', fade, args[0], '', args[1]))

    def addC(self, fade, *args):
        if len(args) == 8:
            self.codes.append(Command(' C', fade, *args))
        if len(args) == 5:
            self.codes.append(Command(' C', fade, *args))
        if len(args) == 4:
            self.codes.append(Command(' C', fade, args[0], '', args[1], args[2], args[3]))

    def addP(self, fade, *args):
        if len(args) == 3:
            self.codes.append(Command(' P', fade, *args))
        if len(args) == 2:
            self.codes.append(Command(' P', fade, args[0], '', args[1]))

    def add(self, s):
        self.codes.append(s)


    def printObj(self):
        for code in self.codes:
            print(code)

def timeParser(s):
    args = s.split(':')
    m = int(args[0])
    s = int(args[1])
    ms = int(args[2])
    return (m*60+s)*1000+ms

def scene1(sentences):
    objs = []
    scale = 0.5
    # Lyrics 0-9
    for i in range(10):
        sen = sentences[i]
        length = 0
        for ch in sen.letters:
            length += ch.width + spacing
        length -= spacing
        x = 320 - length * scale / 2
        y = 200
        for ch in sen.letters:
            obj = Obj(ch.filename, alignment='BottomLeft')
            obj.addM(0, ch.start_t, sen.end_t, x, y)
            obj.addF(0, ch.start_t - 100, ch.start_t + 100, 0, 1)
            obj.addF(0, sen.end_t, sen.end_t + 500, 1, 0)
            obj.addS(0, ch.start_t, scale)
            obj.addC(0, ch.start_t, 235, 193, 67)
            obj.addP(0, ch.start_t, 'A')
            x += (ch.width + spacing) * scale
            objs.append(obj)

    # bottom effect
    s1 = Obj('SB/s1.png', alignment='Centre')
    s1.addF(0, 39019 - 1000, 39019, 0, 1)
    s1.addF(0, timeParser('01:55:819') - 1000, timeParser('01:55:819'), 1, 0)
    s1.addC(0, 39019, 235, 193, 67)
    s1.addP(0, 39019, 'A')
    objs.append(s1)

    # Generate Particles
    for i in range(1000):
        t0 = random.randint(39019 - 7000, timeParser('01:55:819'))
        t1 = t0 + 8000
        particle = Obj('SB/particle.png', alignment='Centre')
        x = random.randint(-107, 747)
        particle.addM(2, t0, t1, x, 500, x + random.randint(-20, 20), 480 - random.randint(200, 300))
        if t0 < 39019:
            particle.addF(0, 39019, 39019 + 1000, 0, 1)
        if t1 > timeParser('01:55:819'):
            particle.addF(0, timeParser('01:55:819')-1000, timeParser('01:55:819'), 1, 0)
        else:
            particle.addF(0, t1 - 1000, t1, 1, 0)
        particle.addC(0, t0, 235, 193, 67)
        particle.addP(0, t0, 'A')
        particle.addS(0, t0, random.randint(40,100)/100)
        objs.append(particle)
    return objs

def scene2(sentences, cp):
    objs = []
    start_t = timeParser('02:15:041')
    end_t = timeParser('03:10:122')
    # BG
    bg = Obj('SB/BG1.jpg')
    bg.addS(0, start_t, end_t, 0.6)
    bg.addM(0, start_t, end_t, 320, 240, 360, 240)
    bg.addF(0, start_t-1000, start_t, 0, 1)
    bg.addF(0, start_t, timeParser('02:15:368'), 1, 0.4)
    bg.addF(0, timeParser('02:30:450'), timeParser('02:30:778'), 0.4, 1)
    bg.addF(0, timeParser('02:46:516')-500, timeParser('02:46:516'), 1, 0.4)
    bg.addF(0, timeParser('02:54:385')-500, timeParser('02:54:385'), 0.4, 1)
    bg.addF(0, end_t-1000, end_t, 1, 0)
    objs.append(bg)

    # add title things
    scale = 0.5
    sen = sentences[110]
    movespeed = -0.004
    length = 0
    for ch in sen.letters:
        length += ch.width + spacing
    length -= spacing
    length = length * scale
    x = 100
    y = 150
    start_t = timeParser('02:15:041')
    end_t = timeParser('02:22:745')
    for ch in sen.letters:
        obj = Obj(ch.filename, alignment='BottomLeft')
        obj.addM(0, start_t, end_t + 500, x, y, x + movespeed * (end_t - start_t), y)
        obj.addF(0, start_t + int(x), start_t + int(x) + 500, 0, 1)
        obj.addF(0, end_t, end_t + 200, 1, 0)
        obj.addS(0, start_t, scale)
        # obj.addC(0, start_t + 2000 + int(x), start_t + 2200 + int(x), 255, 255, 255, 235, 193, 67)
        # obj.addC(0, start_t + 2200 + int(x), start_t + 2400 + int(x), 235, 193, 67, 255, 255, 255)
        obj.addP(0, start_t, 'A')
        x += (ch.width + spacing) * scale
        objs.append(obj)

    sen = sentences[111]
    movespeed = -0.004
    length = 0
    for ch in sen.letters:
        length += ch.width + spacing
    length -= spacing
    length = length * scale
    x = 200
    y = 220
    for ch in sen.letters:
        obj = Obj(ch.filename, alignment='BottomLeft')
        obj.addM(0, start_t, end_t + 500, x, y,
                 x + movespeed * (end_t - start_t), y)
        obj.addF(0, start_t + int(x), start_t + int(x) + 500, 0, 1)
        obj.addF(0, end_t, end_t + 200, 1, 0)
        obj.addS(0, start_t, scale)
        # obj.addC(0, start_t + 2000 + int(x), start_t + 2200 + int(x), 255, 255, 255, 235, 193, 67)
        # obj.addC(0, start_t + 2200 + int(x), start_t + 2400 + int(x), 235, 193, 67, 255, 255, 255)
        obj.addP(0, start_t, 'A')
        x += (ch.width + spacing) * scale
        objs.append(obj)

    scale = 0.5
    sen = sentences[112]
    movespeed = -0.004
    length = 0
    for ch in sen.letters:
        length += ch.width + spacing
    length -= spacing
    length = length * scale
    x = 100
    y = 150
    start_t = timeParser('02:22:745')
    end_t = timeParser('02:30:778')
    for ch in sen.letters:
        obj = Obj(ch.filename, alignment='BottomLeft')
        obj.addM(0, start_t, end_t + 500, x, y, x + movespeed * (end_t - start_t), y)
        obj.addF(0, start_t + int(x), start_t + int(x) + 500, 0, 1)
        obj.addF(0, end_t, end_t + 200, 1, 0)
        obj.addS(0, start_t, scale)
        # obj.addC(0, start_t + 2000 + int(x), start_t + 2200 + int(x), 255, 255, 255, 235, 193, 67)
        # obj.addC(0, start_t + 2200 + int(x), start_t + 2400 + int(x), 235, 193, 67, 255, 255, 255)
        obj.addP(0, start_t, 'A')
        x += (ch.width + spacing) * scale
        objs.append(obj)

    sen = sentences[113]
    movespeed = -0.004
    length = 0
    for ch in sen.letters:
        length += ch.width + spacing
    length -= spacing
    length = length * scale
    x = 300
    y = 220
    for ch in sen.letters:
        obj = Obj(ch.filename, alignment='BottomLeft')
        obj.addM(0, start_t, end_t + 500, x, y,
                 x + movespeed * (end_t - start_t), y)
        obj.addF(0, start_t + int(x), start_t + int(x) + 500, 0, 1)
        obj.addF(0, end_t, end_t + 200, 1, 0)
        obj.addS(0, start_t, scale)
        # obj.addC(0, start_t + 2000 + int(x), start_t + 2200 + int(x), 255, 255, 255, 235, 193, 67)
        # obj.addC(0, start_t + 2200 + int(x), start_t + 2400 + int(x), 235, 193, 67, 255, 255, 255)
        obj.addP(0, start_t, 'A')
        x += (ch.width + spacing) * scale
        objs.append(obj)

    # Lyrics 10 - 13
    for i in range(10, 14):
        sen = sentences[i]
        x = random.randint(0, 200)
        y = random.randint(100, 300)
        movespeed = -0.005
        length = 0
        for ch in sen.letters:
            length += ch.width + spacing
        length -= spacing
        length = length * 0.4
        blackrect = Obj('SB/dot.png', alignment='BottomLeft')
        blackrect.addV(0, sen.start_t, sen.start_t + 500, 0, 61 * 0.4 + 10, length + 10, 61 * 0.4 + 10)
        blackrect.addM(0, sen.start_t, sen.end_t + 500, x - 5, y + 5, x + movespeed * (sen.end_t - sen.start_t) - 5, y + 5)
        blackrect.addC(0, sen.start_t, 0, 0, 0)
        blackrect.addF(0, sen.start_t, 0.4)
        blackrect.addF(0, sen.end_t, 0)
        objs.append(blackrect)
        blackrect2 = Obj('SB/dot.png', alignment='BottomRight')
        blackrect2.addV(0, sen.end_t, sen.end_t + 500, length + 10, 61 * 0.4 + 10, 0, 61 * 0.4 + 10)
        blackrect2.addM(0, sen.start_t, sen.end_t + 500, x + length + 5, y + 5, x + movespeed * (sen.end_t - sen.start_t) + length + 5, y + 5)
        blackrect2.addC(0, sen.start_t, 0, 0, 0)
        blackrect2.addF(0, sen.start_t, 0)
        blackrect2.addF(0, sen.end_t, 0.4)
        objs.append(blackrect2)
        for ch in sen.letters:
            obj = Obj(ch.filename, alignment='BottomLeft')
            obj.addM(0, sen.start_t, sen.end_t + 500, x, y, x + movespeed * (sen.end_t - sen.start_t), y)
            obj.addF(0, ch.start_t - 100, ch.start_t + 100, 0, 1)
            obj.addF(0, sen.end_t - 10 * (len(sen.letters) - sen.letters.index(ch)), sen.end_t + 500 - 10 * (len(sen.letters) - sen.letters.index(ch)), 1, 0)
            obj.addS(0, ch.start_t, 0.4)
            #obj.addC(0, ch.start_t, 235, 193, 67)
            #obj.addP(0, ch.start_t, 'A')
            x += (ch.width + spacing) * 0.4
            objs.append(obj)

    # object spotlight
    timings = ['02:46:516', '02:46:680', '02:47:500', '02:47:663', '02:48:483', '02:48:647', '02:50:450', '02:50:614',
               '02:51:434', '02:51:598', '02:52:418', '02:52:581']
    for timing in timings:
        light = Obj('SB/s2.png')
        t = timeParser(timing)
        pos = get_control_points(cp, t)
        light.addF(0, t - 50, t, 0, 0.6)
        light.addF(0, t, t + 500, 0.6, 0)
        light.addM(0, t, pos[0] + 56, 240)
        light.addP(0, t, 'A')
        light.addV(0, t, 1, 5)
        objs.append(light)

    cp2 = get_control_points(cp, timeParser('02:49:467'), timeParser('02:50:450'))
    light = Obj('SB/s2.png')
    light.addF(0, cp2[0][0] - 50, cp2[0][0], 0, 0.6)
    light.addF(0, cp2[len(cp2)-1][0], cp2[len(cp2)-1][0] + 500, 0.6, 0)
    light.addP(0, cp2[0][0], 'A')
    #light.addV(0, cp2[0][0], 1, 5)
    for i in range(len(cp2)-1):
        light.addM(1, cp2[i][0], cp2[i+1][0], cp2[i][1][0] + 56, 240, cp2[i+1][1][0] + 56, 240)
    objs.append(light)

    cp2 = get_control_points(cp, timeParser('02:53:401'), timeParser('02:54:385'))
    light = Obj('SB/s2.png')
    light.addF(0, cp2[0][0] - 50, cp2[0][0], 0, 0.6)
    light.addF(0, cp2[len(cp2) - 1][0], cp2[len(cp2) - 1][0] + 500, 0.6, 0)
    light.addP(0, cp2[0][0], 'A')
    light.addV(0, cp2[0][0], 1, 5)
    for i in range(len(cp2) - 1):
        light.addM(1, cp2[i][0], cp2[i + 1][0], cp2[i][1][0] + 56, 240, cp2[i + 1][1][0] + 56, 240)
    objs.append(light)

    return objs


def dropEffect(timing):
    objs = []
    for i in range(100):
        x0 = -107 - 20
        y0 = random.randint(0, 480)
        x1 = random.randint(50, 100)
        y1 = y0 + random.randint(50, 200)
        t0 = random.randint(timing, timing + 100)
        duration = random.randint(200, 400)
        particle = Obj('SB/particle.png')
        particle.addMX(0, t0, t0 + duration, x0, x1)
        particle.addMY(2, t0, t0 + duration, y0, y1)
        particle.addC(0, t0, 235, 193, 67)
        particle.addF(0, t0 + duration - 150, t0 + duration, 1, 0)
        particle.addP(0, t0, 'A')
        particle.addS(0, t0, random.randint(40, 80)/100)
        objs.append(particle)
    for i in range(100):
        x0 = 747 + 20
        y0 = random.randint(0, 480)
        x1 = random.randint(540, 600)
        y1 = y0 + random.randint(50, 200)
        t0 = random.randint(timing, timing + 100)
        duration = random.randint(200, 400)
        particle = Obj('SB/particle.png')
        particle.addMX(0, t0, t0 + duration, x0, x1)
        particle.addMY(2, t0, t0 + duration, y0, y1)
        particle.addC(0, t0, 235, 193, 67)
        particle.addF(0, t0 + duration - 150, t0 + duration, 1, 0)
        particle.addP(0, t0, 'A')
        particle.addS(0, t0, random.randint(40, 80)/100)
        objs.append(particle)
    return objs


def scene3(sentences, cp):
    objs = []
    scale = 0.75
    # effects
    timings = ['03:10:122', '03:10:613', '03:11:761', '03:12:253', '03:13:400', '03:13:892', '03:16:679', '03:17:171',
               '03:18:318', '03:18:810']
    for timing in timings:
        t = timeParser(timing)
        effect = Obj('SB/s3.png')
        effect.addF(0, t, t+500, 1, 0)
        effect.addP(0, t, 'A')
        effect.addC(0, t, 235, 193, 67)
        objs.append(effect)
        objs.extend(dropEffect(t))

    # SAY! SAY!
    for i in [14, 16, 18, 20, 22]:
        sen = sentences[i]
        length = 0
        for ch in sen.letters:
            length += ch.width + spacing
        length -= spacing
        x = 320 - length * scale / 2
        y = 180
        for ch in sen.letters:
            obj = Obj(ch.filename, alignment='BottomLeft')
            obj.addM(0, ch.start_t, sen.end_t, x, y)
            obj.addF(0, ch.start_t - 100, ch.start_t, 0, 1)
            obj.addF(0, ch.end_t, ch.end_t + 100, 1, 0)
            obj.addS(0, ch.start_t, scale)
            obj.addC(0, ch.start_t, 235, 193, 67)
            obj.addP(0, ch.start_t, 'A')
            x += (ch.width + spacing) * scale
            objs.append(obj)

    # 愛して
    for i in [15, 17, 19, 21]:
        sen = sentences[i]
        length = 0
        for ch in sen.letters:
            length += ch.width + spacing
        length -= spacing
        x = 320 - length * scale / 2
        y = 250
        for ch in sen.letters:
            obj = Obj(ch.filename, alignment='BottomLeft')
            obj.addM(0, ch.start_t, sen.end_t, x, y)
            obj.addF(0, ch.start_t - 100, ch.start_t, 0, 1)
            obj.addF(0, sen.end_t - 100, sen.end_t, 1, 0)
            obj.addS(0, ch.start_t, scale)
            obj.addC(0, ch.start_t, 235, 193, 67)
            obj.addP(0, ch.start_t, 'A')
            x += (ch.width + spacing) * scale
            objs.append(obj)

    sen = sentences[23]
    length = 0
    for ch in sen.letters:
        length += ch.width + spacing
    length -= spacing
    x = 320 - length * scale / 2
    y = 250
    for ch in sen.letters:
        obj = Obj(ch.filename, alignment='BottomLeft')
        obj.addM(0, ch.start_t, sen.end_t, x, y)
        obj.addF(0, ch.start_t - 100, ch.start_t + 100, 0, 1)
        obj.addF(0, sen.end_t, sen.end_t + 1000, 1, 0)
        obj.addS(0, ch.start_t, scale)
        obj.addC(0, ch.start_t, 235, 193, 67)
        obj.addP(0, ch.start_t, 'A')
        x += (ch.width + spacing) * scale
        objs.append(obj)

    # spotlights
    cp2 = get_control_points(cp, timeParser('03:10:122'), timeParser('03:25:859'))
    spotlight = Obj('SB/spotlight.png')
    spotlight.addC(0, cp2[0][0], 235, 193, 67)
    spotlight.addP(0, cp2[0][0], 'A')
    spotlight.addF(0, cp2[0][0], cp2[0][0] + 400, 0, 1)
    for i in range(len(cp2)-1):
        spotlight.addM(1, cp2[i][0], cp2[i+1][0], cp2[i][1][0] + 56, 400, cp2[i+1][1][0] + 56, 400)
    spotlight.addF(0, cp2[len(cp2)-1][0], cp2[len(cp2)-1][0] + 400, 0.4, 0)
    spotlight.addS(0, cp2[0][0], 2)
    objs.append(spotlight)
    objs.append(spotlight)

    return objs


def ring(timing):
    t = timeParser(timing)
    pos = get_control_points(cp, t)
    obj = Obj('SB/ring.png', x=pos[0]+56, y=400)
    obj.addS(0, t - 100, t + 500, 0, 1)
    obj.addP(0, t, 'A')
    obj.addF(0, t + 200, t + 500, 1, 0)
    return obj


def scene4(sentences, cp):
    objs = []
    # bg
    bg = Obj('SB/BG2.jpg')
    bg.addM(0, timeParser('03:26:843'), timeParser('04:15:362'), 320, 240, 400, 240)
    bg.addF(0, timeParser('03:26:843'), timeParser('03:27:171'), 0, 1)
    bg.addF(0, timeParser('03:36:426'), timeParser('03:36:745'), 1, 0.4)
    bg.addF(0, timeParser('03:37:383'), timeParser('03:37:702'), 0.4, 1)
    bg.addF(0, timeParser('03:44:724'), timeParser('03:45:043'), 1, 0.4)
    bg.addF(0, timeParser('03:57:490'), timeParser('03:57:809'), 0.4, 1)
    bg.addF(0, timeParser('04:06:506'), timeParser('04:08:022'), 1, 0.4)
    bg.addF(0, timeParser('04:15:362'), timeParser('04:15:362') + 500, 0.4, 0)
    bg.addS(0, timeParser('03:26:843'), 0.6)
    objs.append(bg)

    # lyrics
    scale1 = 0.4
    scale2 = 0.6
    for i in range(24, 32):
        sen = sentences[i]
        x = random.randint(100, 400)
        x0 = x
        y = random.randint(100, 300)
        movespeed = -0.005
        length = 0
        for ch in sen.letters:
            length += ch.width + spacing
        length -= spacing
        length = length * scale1
        for ch in sen.letters:
            obj = Obj(ch.filename, alignment='BottomLeft')
            obj.addM(0, sen.start_t, sen.end_t + 500, x, y, x + movespeed * (sen.end_t - sen.start_t), y)
            obj.addF(0, ch.start_t - 100, ch.start_t + 100, 0, 1)
            obj.addF(0, sen.end_t - 10 * (len(sen.letters) - sen.letters.index(ch)),
                     sen.end_t + 500 - 10 * (len(sen.letters) - sen.letters.index(ch)), 1, 0)
            obj.addS(0, ch.start_t, scale1)
            # obj.addC(0, ch.start_t, 235, 193, 67)
            obj.addP(0, ch.start_t, 'A')
            x += (ch.width + spacing) * scale1
            objs.append(obj)

        length = 0
        for ch in sen.letters:
            length += ch.width + spacing
        length -= spacing
        dx = length * (scale2 - scale1)/2
        x = x0
        for ch in sen.letters:
            obj = Obj(ch.filename, alignment='BottomLeft')
            obj.addM(0, sen.start_t, sen.end_t + 500, x - dx, y - 30, x + movespeed * (sen.end_t - sen.start_t) - dx, y - 30)
            obj.addF(0, ch.start_t - 100, ch.start_t + 100, 0, 0.5)
            obj.addF(0, sen.end_t - 10 * (len(sen.letters) - sen.letters.index(ch)),
                     sen.end_t + 500 - 10 * (len(sen.letters) - sen.letters.index(ch)), 0.5, 0)
            obj.addS(0, ch.start_t, scale2)
            # obj.addC(0, ch.start_t, 235, 193, 67)
            obj.addP(0, ch.start_t, 'A')
            x += (ch.width + spacing) * scale2
            objs.append(obj)

    # spotlight
    cp2 = get_control_points(cp, timeParser('03:36:745'), timeParser('03:37:383'))
    light = Obj('SB/s2.png')
    light.addF(0, cp2[0][0] - 50, cp2[0][0], 0, 0.6)
    light.addF(0, cp2[len(cp2) - 1][0], cp2[len(cp2) - 1][0] + 500, 0.6, 0)
    light.addP(0, cp2[0][0], 'A')
    light.addV(0, cp2[0][0], 1, 5)
    for i in range(len(cp2) - 1):
        light.addM(1, cp2[i][0], cp2[i + 1][0], cp2[i][1][0] + 56, 240, cp2[i + 1][1][0] + 56, 240)
    objs.append(light)

    cp2 = get_control_points(cp, timeParser('03:45:043'), timeParser('03:47:596'))
    light = Obj('SB/s2.png')
    light.addF(0, cp2[0][0] - 50, cp2[0][0], 0, 0.6)
    light.addF(0, cp2[len(cp2) - 1][0], cp2[len(cp2) - 1][0] + 500, 0.6, 0)
    light.addP(0, cp2[0][0], 'A')
    for i in range(len(cp2) - 1):
        light.addM(1, cp2[i][0], cp2[i + 1][0], cp2[i][1][0] + 56, 240, cp2[i + 1][1][0] + 56, 240)
    objs.append(light)

    cp2 = get_control_points(cp, timeParser('03:47:596'), timeParser('04:13:447'))
    spotlight = Obj('SB/spotlight.png')
    # spotlight.addC(0, cp2[0][0], 235, 193, 67)
    spotlight.addP(0, cp2[0][0], 'A')
    spotlight.addF(0, cp2[0][0], cp2[0][0] + 400, 0, 1)
    for i in range(len(cp2) - 1):
        spotlight.addM(1, cp2[i][0], cp2[i + 1][0], cp2[i][1][0] + 56, 400, cp2[i + 1][1][0] + 56, 400)
    spotlight.addF(0, cp2[len(cp2) - 1][0], cp2[len(cp2) - 1][0] + 400, 0.4, 0)
    spotlight.addS(0, cp2[0][0], 2.5)
    objs.append(spotlight)

    timings = ['04:08:022', '04:08:181', '04:08:819', '04:08:979', '04:09:617', '04:09:777', '04:11:373', '04:11:532',
               '04:12:011', '04:12:490', '04:13:447']

    for timing in timings:
        light = Obj('SB/s2.png')
        t = timeParser(timing)
        pos = get_control_points(cp, t)
        light.addF(0, t - 50, t, 0, 0.6)
        light.addF(0, t, t + 500, 0.6, 0)
        light.addM(0, t, pos[0] + 56, 240)
        light.addP(0, t, 'A')
        objs.append(light)

    cp2 = get_control_points(cp, timeParser('04:14:724'), timeParser('04:15:362'))
    light = Obj('SB/s2.png')
    light.addF(0, cp2[0][0] - 50, cp2[0][0], 0, 0.6)
    light.addF(0, cp2[len(cp2) - 1][0], cp2[len(cp2) - 1][0] + 200, 0.6, 0)
    light.addP(0, cp2[0][0], 'A')
    for i in range(len(cp2) - 1):
        light.addM(1, cp2[i][0], cp2[i + 1][0], cp2[i][1][0] + 56, 240, cp2[i + 1][1][0] + 56, 240)
    objs.append(light)

    timings = ['03:47:596', '03:50:149', '03:52:702', '03:55:256', '03:57:809', '04:00:362', '04:02:915', '04:05:468',
               '04:06:107']
    for timing in timings:
        objs.append(ring(timing))
    return objs

def drawClock(start_t, end_t, TimeH, TimeM, cx, cy):
    objs = []
    clock = Obj('SB/clock.png', x=cx, y=cy)
    clock.addC(0, start_t, int((start_t + end_t) / 2), 0, 0, 0, 30, 30, 30)
    clock.addC(0, int((start_t + end_t) / 2), end_t, 30, 30, 30, 0, 0, 0)
    clock.addS(0, start_t, 2)
    ArmH = Obj('SB/dot.png', alignment='BottomCentre', x=cx, y=cy)
    ArmH.addV(0, start_t, 20, 150)
    ArmH.addR(0, start_t, end_t, (TimeH + TimeM/60) / 12 * (2 * pi), (TimeH + (TimeM + 1)/60) / 12 * (2 * pi))
    ArmH.addC(0, start_t, int((start_t + end_t) / 2), 0, 0, 0, 30, 30, 30)
    ArmH.addC(0, int((start_t + end_t) / 2), end_t, 30, 30, 30, 0, 0, 0)
    ArmM = Obj('SB/dot.png', alignment='BottomCentre', x=cx, y=cy)
    ArmM.addV(0, start_t, 10, 300)
    ArmM.addR(0, start_t, end_t, TimeM / 60 * (2 * pi), (TimeM + 1) / 60 * (2 * pi))
    ArmM.addC(0, start_t, int((start_t + end_t) / 2), 0, 0, 0, 30, 30, 30)
    ArmM.addC(0, int((start_t + end_t) / 2), end_t, 30, 30, 30, 0, 0, 0)
    objs.append(clock)
    objs.append(ArmH)
    objs.append(ArmM)
    return objs


def scene5():
    objs = []
    objs.extend(drawClock(timeParser('04:15:362'), timeParser('04:17:362'), 1, 13, 140, 400))
    objs.extend(drawClock(timeParser('04:17:362'), timeParser('04:19:362'), 8, 36, 600, 250))
    objs.extend(drawClock(timeParser('04:19:362'), timeParser('04:21:362'), 11, 4, 300, 380))
    objs.extend(drawClock(timeParser('04:21:362'), timeParser('04:23:362'), 5, 31, 160, 100))
    return objs

def scene6(sentences, cp):
    objs = []
    # BG
    bg = Obj('SB/BG3.jpg')
    start_t = timeParser('04:23:362')
    end_t = timeParser('05:03:361')
    bg.addM(0, start_t, end_t, 320, 240, 350, 240)
    bg.addF(0, start_t - 500, start_t, 0, 0.4)
    bg.addF(0, timeParser('04:30:695'), timeParser('04:31:362'), 0.4, 1)
    bg.addF(0, timeParser('04:38:528'), timeParser('04:38:695'), 1, 0.4)
    bg.addF(0, timeParser('04:39:195'), timeParser('04:39:362'), 0.4, 1)
    bg.addF(0, timeParser('04:46:528'), timeParser('04:46:695'), 1, 0.4)
    bg.addF(0, timeParser('04:47:195'), timeParser('04:47:361'), 0.4, 1)
    bg.addF(0, timeParser('04:47:361'), timeParser('04:48:361'), 1, 0.2)
    bg.addF(0, end_t, end_t + 500, 1, 0)
    bg.addS(0, start_t, 0.6)
    objs.append(bg)

    # lyrics
    scale = 0.4
    wiggle = 800
    wigglestrength = 60
    for i in range(32, 34):
        sen = sentences[i]
        x = random.randint(150, 200)
        y = random.randint(200, 300)
        xmovespeed = -0.03
        length = 0
        for ch in sen.letters:
            length += ch.width + spacing
        length -= spacing
        for ch in sen.letters:
            obj = Obj(ch.filename, alignment='BottomLeft')
            obj.addMX(2, sen.start_t - 200, sen.end_t + 1000, x, x + xmovespeed * (sen.end_t - sen.start_t + 1200))
            t1 = sen.start_t - 200 - sen.letters.index(ch) * 50
            while t1 - wiggle * 4 < sen.end_t + 1000:
                obj.addMY(1, t1, t1 + wiggle, y, y - wigglestrength)
                obj.addMY(2, t1 + wiggle, t1 + wiggle * 2, y - wigglestrength, y)
                obj.addMY(1, t1 + wiggle * 2, t1 + wiggle * 3, y, y + wigglestrength)
                obj.addMY(2, t1 + wiggle * 3, t1 + wiggle * 4, y + wigglestrength, y)
                t1 += wiggle * 4
            obj.addF(0, ch.start_t - 200, ch.start_t + 200, 0, 1)
            obj.addF(0, sen.end_t - (len(sen.letters)-sen.letters.index(ch)) * 50, sen.end_t - (len(sen.letters)-sen.letters.index(ch)) * 50 + 1000, 1, 0)
            obj.addS(0, sen.start_t, scale)
            obj.addP(0, sen.start_t, 'A')
            x += (ch.width + spacing) * scale
            objs.append(obj)

    wiggle = 800
    wigglestrength = 40
    for i in range(34, 38):
        scale1 = 0.4
        scale2 = 0.6
        sen = sentences[i]
        if i%2 == 0:
            x = random.randint(100, 150)
            y = random.randint(100, 150)
        else:
            x = random.randint(250, 300)
            y = random.randint(300, 350)
        x0 = x
        xmovespeed = -0.03
        length = 0
        for ch in sen.letters:
            length += ch.width + spacing
        length -= spacing
        for ch in sen.letters:
            obj = Obj(ch.filename, alignment='BottomLeft')
            obj.addMX(2, sen.start_t - 200, sen.end_t + 1500, x, x + xmovespeed * (sen.end_t - sen.start_t + 1200))
            t1 = sen.start_t - 200 - sen.letters.index(ch) * 50
            while t1 - wiggle * 4 < ch.end_t + 1500:
                obj.addMY(1, t1, t1 + wiggle, y, y - wigglestrength)
                obj.addMY(2, t1 + wiggle, t1 + wiggle * 2, y - wigglestrength, y)
                obj.addMY(1, t1 + wiggle * 2, t1 + wiggle * 3, y, y + wigglestrength)
                obj.addMY(2, t1 + wiggle * 3, t1 + wiggle * 4, y + wigglestrength, y)
                t1 += wiggle * 4
            obj.addF(0, ch.start_t - 200, ch.start_t + 200, 0, 1)
            obj.addF(0, ch.end_t + 1000, ch.end_t + 1500, 1, 0)
            obj.addS(0, sen.start_t, scale1)
            obj.addP(0, sen.start_t, 'A')
            x += (ch.width + spacing) * scale1
            objs.append(obj)

        x = x0 - length * (scale2 - scale1)/2
        for ch in sen.letters:
            obj = Obj(ch.filename, alignment='BottomLeft')
            obj.addMX(2, sen.start_t - 200, sen.end_t + 1500, x, x + xmovespeed * (sen.end_t - sen.start_t + 1200))
            t1 = sen.start_t - 200 - sen.letters.index(ch) * 50
            while t1 - wiggle * 4 < ch.end_t + 1500:
                obj.addMY(1, t1, t1 + wiggle, y, y - wigglestrength * scale2/scale1)
                obj.addMY(2, t1 + wiggle, t1 + wiggle * 2, y - wigglestrength * scale2/scale1, y)
                obj.addMY(1, t1 + wiggle * 2, t1 + wiggle * 3, y, y + wigglestrength * scale2/scale1)
                obj.addMY(2, t1 + wiggle * 3, t1 + wiggle * 4, y + wigglestrength * scale2/scale1, y)
                t1 += wiggle * 4
            obj.addF(0, ch.start_t - 200, ch.start_t + 200, 0, 0.4)
            obj.addF(0, ch.end_t + 1000, ch.end_t + 1500, 0.4, 0)
            obj.addS(0, sen.start_t, scale2)
            obj.addP(0, sen.start_t, 'A')
            x += (ch.width + spacing) * scale2
            objs.append(obj)

    return objs


def drawScene(objs):
    for obj in objs:
        obj.printObj()


# preprocess lyrics
lp = LP()
lp.AssReader('C:/Users/沈尧/Desktop/SB/ceui/lyrics.ass')
sentences = lp.sentences

# preprocess beatmap
parser = BeatmapParser()
parser.parseFile('F:/osu!/Songs/588046 Ceui - Hana ni Natta Shounen no Shinwa/Ceui - Hana ni Natta Shounen no Shinwa (Yumeno Himiko) [Ancient Myth].osu')
parser.build_beatmap()
cp = parser.control_points


s1 = scene1(sentences)
s2 = scene2(sentences, cp)
s3 = scene3(sentences, cp)
s4 = scene4(sentences, cp)
s5 = scene5()
s6 = scene6(sentences, cp)

drawScene(s1)
drawScene(s2)
drawScene(s3)
drawScene(s5)
drawScene(s4)
drawScene(s6)
