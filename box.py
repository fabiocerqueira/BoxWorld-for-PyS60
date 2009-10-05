#-*- coding: utf-8 -*-
#------------------------------------------------------------------------+
#   Sokoban pys60
#   por Fábio Cerqueira
#   Versão 1.0 
#
# Licença
#    Copyright (C) 2009  Fábio Cerqueira
#
#    Este programa é software livre; você pode redistribuí-lo e/ou
#    modificá-lo sob os termos da Licença Pública Geral GNU, conforme
#    publicada pela Free Software Foundation; tanto a versão 2 da
#    Licença como (a seu critério) qualquer versão mais nova.
#    Este programa é distribuído na expectativa de ser útil, mas SEM
#    QUALQUER GARANTIA; sem mesmo a garantia implícita de
#    COMERCIALIZAÇÃO ou de ADEQUAÇÃO A QUALQUER PROPÓSITO EM
#    PARTICULAR. Consulte a Licença Pública Geral GNU para obter mais
#    detalhes.
#    Para consultar texto em inglês visite:
#	http://www.gnu.org/licenses/gpl.txt
#
#------------------------------------------------------------------------+

import os

import appuifw
import e32
import key_codes
import graphics


#lista de mapas que podem ser jogados.
MAPS = [
    {"text":"###########0#00##0.##0!000#00##0#0!0*00##000#0#0.###########", "size": (10,6), "pos": (1,1)},
    {"text":"#############8#000#0000000#8##0!000#0!#!#8#000#00000#0##########0!000#8888888##0!00#88888888#..*##88888888#...#888888888#####8", "size": (14,9), "pos": (1,3)},
    {"text":"###########000#0000##0#0!0##0##00.0.000##00!*0!0###00*0.00#8###0000##888#000##8888#####888", "size": (10,9), "pos": (1,1)},
    {"text":"88888######888###0000#888#0#0!00#888#000!00#888#0#0!0######000!00##...00#!0###...000!00############", "size": (11,9), "pos": (9,1)},
    {"text":"88888888888########88888888888#00....#############00....##0000#00!0!000....##0!!!#!00!0#00....##00!00000!0#00....##0!!0#!0!0!#########00!0#00000#8888888##0#########8888888#0000#0000##8888888#00000!000##8888888#00!!#!!000#8888888#0000#0000##8888888###########88888888", "size": (19,14), "pos": (10,11)},
    {"text":"88888888#####888888888888#000#####88888888#0#!##00#88888888#00000!0##########0###000##....00##0!00!####....0000!0!!0##8#....00##!00!00#8#########00!00##888888888#0!0!00#888888888###0##0#88888888888#0000#88888888888######8", "size": (17,13), "pos": (14,7)},
    {"text":"######88###8#..00#8##0###..00###000##..00000!!0##..00#0#0!0##..###0#0!0#####0!0#!00#888#00!#0!0#888#0!00!00#888#00##000#888#########", "size": (12,11), "pos": (9,1)},
    {"text":"8888888#####88#######000####0#00##0!!0##0000!000000##00!00###000####0#####!####0!00###0..#8#0!0!0!0...#8#0000###...#8#0!!0#8#...#8#00###8#####8####888888888", "size": (13,12), "pos": (5,2)},
    {"text":"88####888888888888#00###########88#0000!000!0!0#88#0!#0!0#00!00#88#00!0!00#0000####0!#0#00####0##0#!0!0!00##000##0000!0#!#000#0##000!0000!0!0!0######00#########88#000000#88888888#000000#88888888#......#88888888#......#88888888#......#88888888########888888", "size": (16,16), "pos": (1,6)},
    {"text":"8888888888#######8888888888#00...#888888#####00...#888888#000000.0.#888888#00##00...#888888##0##00...#88888###0########88888#0!!!0##88888#####00!0!0#######000#!0!000#000##00!00!0000!00!0#######0!!0!0#####88888#000000#888888888########8888", "size": (17,14), "pos": (1,10)},
    {"text":"8###88###############0####0000000#000##0!!000!!00!0!0...##00!!!#0000!00#...##0!000#0!!0!!0#...####000#00!0000#...##00000#0!0!0!0#...##0000######0###...###0#00#00!0!00#...##00##0#0!!0!0!##..##0..#0#00!000000#.##0..#0#0!!!0!!!0#.######0#0000000#0#.#8888#0#########0#.#8888#00000000000#.#8888###############", "size": (19,16), "pos": (2,1)},
    {"text":"8888888888####8888888888####8#00#88888888###00###!0#8888888##000000!00#888888##00!0!!##0##888888#00#!##00000#888888#0#0!0!!0#0###88888#000!0#00#0!0#########0000#00!!0#000#####0##0!000000000##.0000###00#########..0..#8####8888888#...#.#888888888888#.....#888888888888#######888888888888", "size": (19,15), "pos": (7,2)},
    {"text":"################8#00000000000000#8#0#0######00000#8#0#00!0!0!0!#00#8#0#000!0!000##0###0#00!0!0!###...##0#000!0!00##...##0###!!!0!0##...##00000#0##0##...######000##0##...#8888#####00000###88888888#00000#8888888888#######88", "size": (17,13), "pos": (7,4)},
    {"text":"888#########888888888##000##00#####888###00000#00#0000####00!0#!0#00#00...0##0#0!#0!##0#0#.#.0##00#0#!00#0000.0.0##0!0000!0#0#0#.#.0##000##00##!0!0.0.0##0!0#000#00#!#.#.0###0!00!000!00!...0#8#!0######0000##00#8#00#8888##########8####88888888888888", "size": (19,13), "pos": (6,4)},
    {"text":"8888888#######88888#######00000#88888#00000#0!0!0#88888#!!0#000#########8#0###......##000#8#000!......##0#0#8#0###......00000###000####0###0#!###00#!000#00!00#0#8#00!0!!!00#0!##0#8#000!0!0###!!0#0#8#####00000!000#0#88888###0###000#0#8888888#00000#000#8888888########00#88888888888888####8", "size": (18,16), "pos": (10,2)},
    {"text":"888########888888888#000#00#888888888#00!000#8888888###0#!000####8888#00!00##!000#8888#00#000!0#0!#8888#00#000000!0####8##0####!##00000#8#0!#.....#0#000#8#00!..**.0!#0#####00#.....#000#88#000###0#######88#0!!00#00#8888888#00#00000#8888888######000#888888888888#####8888888", "size": (17,16), "pos": (6,5)}
]

class BMap:
    """Classe com as funções de desenho e verificação de mapa"""

    if e32.in_emulator():
        SRC_IMAGE = 'C:\\Python\\bpic15.png'
    else:
        SRC_IMAGE = 'E:\\Python\\bpic15.png'
    SIMBOLS = '@.#!+*08'
    BOX_SIZE = 15


    def __init__(self, text, size, pos):
        self.setMap(text, size, pos)


    def setMap(self, text, size, pos):
        self.text = list(text)
        self.size = size
        self.pos  = pos
 

    def cropImage(self,simbol):
        """ Retorna as coordenadas de corte na imagem
        obj.cropImage('@') -> (x,y)"""
        if simbol != '8':
            s = BMap.SIMBOLS.find(simbol)
            return 0,1+s+(BMap.BOX_SIZE * s)
        else:
            return (-100,-100)       

    def isFinalize(self):
        """Verifica se o mapa foi finalizado ou não"""
        return not ('.' in self.text or '!' in self.text)




class Character:
    """Classe que representa o personagem e é responsável pela movimentação"""
    def __init__(self, boxmap):
        self.bmap = boxmap                      #objeto de BMap que o boneco irá atualizar.


    def move(self, moviment):
        """ Move o personagem pelo mapa e atualiza a posição e a lista do mapa
        retorna as posições em volta do movimento [pos anterior, pos atual, pos da frente]"""
        x,y = self.bmap.pos 
        w = self.bmap.size[0]
        pos_now = (y * w) + x
        refresh = [pos_now]

        if moviment in ['up','left']: inc_mov = -1
        else: inc_mov = 1

        if moviment in ['up','down']: 
            next_box = pos_now + (w * inc_mov)
            nnext_box = pos_now + (2 * w * inc_mov)
        else:
            next_box = pos_now + inc_mov
            nnext_box = pos_now + (2 * inc_mov) 

        refresh += [next_box]
        #movimentos livres
        if self.bmap.text[next_box] in ['0','.']:
            if moviment in ['up','down']:
                y += inc_mov
            else:
                x += inc_mov

        elif self.bmap.text[next_box] in ['*','!']: #movimentos com a caixa
            if self.bmap.text[nnext_box] in ['0','.']: 
                if self.bmap.text[nnext_box] == '0': #segundo piso
                    self.bmap.text[nnext_box] = '!'
                elif self.bmap.text[nnext_box] == '.': #segundo ponto de caixa
                    self.bmap.text[nnext_box] = '*'
                
                if self.bmap.text[next_box] == '*': self.bmap.text[next_box] = '.' 
                else: self.bmap.text[next_box] = '0'

                refresh += [nnext_box]

                if moviment in ['up','down']:
                    y += inc_mov
                else:
                    x += inc_mov
        #atualiza posição do personagem
        self.bmap.pos = (x,y)
        return refresh
 
                
            
class BoxWorld:
    def __init__(self):
        """Configura o início do jogo"""
        self.img = None             #base para o desenho 
        self.num_map = 0            #mapa que está sendo jogado.
        self.undoStack = []         #pilha para desfazer
        self.center = (0,0)         #ponto de inicio do mapa
        self.canvas = None          #canvas principal
        self.bmap = BMap(**MAPS[self.num_map])  #Objeto do mapa
        self.char = Character(self.bmap)        #Objeto do personagem
        appuifw.app.screen = "large"
        appuifw.app.menu = [
            (u"Reiniciar", lambda:self.startMap(self.num_map)),
            (u"Ir para", self.changeMap),
            (
                u"Modo",
                (
                    (u"Retrato", lambda:self.modeGame('portrait')),
                    (u"Paisagem", lambda:self.modeGame('landscape'))
                )
            )
        ]
        appuifw.app.exit_key_handler = self.quit
        self.lock = e32.Ao_lock()
        self.bpic = graphics.Image.open(BMap.SRC_IMAGE) 
        self.canvas = appuifw.Canvas(redraw_callback = self.handleRedraw, event_callback = self.handleEvent)
        appuifw.app.body = self.canvas
        self.img = graphics.Image.new(self.canvas.size)
        

    def run(self):
        """Roda e "segura" a aplicação em execução"""
        self.modeGame('portrait')
        self.lock.wait()
            

    def drawBox(self, pos, simbol):
        """ Recebe a posição e o simbolo do objeto que é para desenhar"""
        x,y = self.bmap.cropImage(simbol)
        pos = pos[0] + self.center[0],pos[1] + self.center[1]
        self.img.blit(self.bpic, target = pos, source = ((x,y) ,(BMap.BOX_SIZE + x,BMap.BOX_SIZE + y)))


    def moveCamera(self,center):
        """Atualiza posição da câmera"""
        self.center = center[:]
        self.update()


    def moveToCenter(self):
        """Atualiza posição da câmera para o centro."""
        if self.canvas and self.bmap:
            w,h = self.bmap.size
            self.center = (self.canvas.size[0] - (w * BMap.BOX_SIZE)) / 2,(self.canvas.size[1] - (h * BMap.BOX_SIZE)) / 2
            self.update()

       
    def update(self, refresh = []):
        """Atualiza o desenho do mapa
         refresh = [posicao anterior, posição atual, posição a frente]"""
        w = self.bmap.size[0]
        if not refresh:
            self.img.clear((0,0,0))
            for i in range(len(self.bmap.text)):
                simbol = self.bmap.text[i]
                x,y = (i % self.bmap.size[0]) * BMap.BOX_SIZE, (i / self.bmap.size[0]) * BMap.BOX_SIZE
                self.drawBox((x,y),simbol)
        else:
            # Atualizando posição anteior
            s = self.bmap.text[refresh[0]]
            x,y = (refresh[0] % w) * BMap.BOX_SIZE, (refresh[0] / w) * BMap.BOX_SIZE
            self.drawBox((x,y),s)
            # Atualizando posição a frente caso tenha uma caixa
            if len(refresh) == 3:
                s = self.bmap.text[refresh[2]]
                x,y = (refresh[2] % w) * BMap.BOX_SIZE, (refresh[2] / w) * BMap.BOX_SIZE
                self.drawBox((x,y),s)

        # Atualizando boneco
        x,y = self.bmap.pos[0] * BMap.BOX_SIZE, self.bmap.pos[1] * BMap.BOX_SIZE
        self.drawBox((x,y),'@')
        self.handleRedraw(None)
        

    def quit(self):
        self.lock.signal()

     
    def handleEvent(self, event):
        ev = event["keycode"]
        ret = []

        if ev in [self.keys['up'],self.keys['down'],self.keys['left'],self.keys['right']]:
            self.addUndoStack((self.bmap.text[:], self.bmap.pos))
            if ev == self.keys['up']:
                ret = self.char.move('up')
            elif ev == self.keys['down']:
                ret = self.char.move('down')
            elif ev == self.keys['left']:
                ret = self.char.move('left')
            elif ev == self.keys['right']:
                ret = self.char.move('right')
            self.update(ret)
            if self.bmap.isFinalize():
                self.win()

        elif ev == key_codes.EKeyBackspace:
            self.undo()  
        elif ev == key_codes.EKeyLeftArrow:
            self.moveCamera((self.center[0] - BMap.BOX_SIZE,self.center[1]))
        elif ev == key_codes.EKeyRightArrow:
            self.moveCamera((self.center[0] + BMap.BOX_SIZE,self.center[1]))
        elif ev ==  key_codes.EKeyDownArrow: 
            self.moveCamera((self.center[0],self.center[1]  + BMap.BOX_SIZE))
        elif ev == key_codes.EKeyUpArrow: 
            self.moveCamera((self.center[0],self.center[1]  - BMap.BOX_SIZE))


    def handleRedraw(self, rect):
        if self.img:
            self.canvas.blit(self.img)


    def addUndoStack(self,state):
        """Salva os estados na pilha de desfazer"""
        if len(self.undoStack) == 5:
            del self.undoStack[0]
        self.undoStack.append(state)


    def undo(self):
        """Defaz os últimos movimentos"""
        if self.undoStack:
            state = self.undoStack.pop()
            self.bmap.text,self.bmap.pos = state[0][:],state[1]
            self.update()


    def modeGame(self,mode):
        """Altera o modo do game entre paisagem e retrato"""
        if mode == 'portrait':
            appuifw.app.orientation = mode
            self.keys = {
                'up': key_codes.EKey2,
                'down': key_codes.EKey8,
                'left': key_codes.EKey4,
                'right': key_codes.EKey6
            }
        elif mode == 'landscape':
            appuifw.app.orientation = mode
            self.keys = {
                'up': key_codes.EKey6,
                'down': key_codes.EKey4,
                'left': key_codes.EKey2,
                'right': key_codes.EKey8
            }
        self.img = graphics.Image.new(self.canvas.size)
        self.moveToCenter()


    def startMap(self, idMap):
        """Inicia o mapa com o idMap"""
        self.undoStack = []
        self.num_map = idMap % len(MAPS)
        self.bmap.setMap(**MAPS[self.num_map])
        self.moveToCenter()


    def changeMap(self):
        """Troca de mapa com entrada do usuário"""
        mapID = appuifw.query(u"Digite o id do mapa","number")
        if mapID != None:
            self.startMap(int(mapID))


    def win(self):
        """Avança para o próximo mapa com mensagem de vitória"""
        appuifw.note(u"Voce ganhou!",'conf')
        self.startMap(self.num_map + 1)   




def createImage():
    img = """\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0f\x00\x00\x00p\x08\x02\x00\x00\x00N\xc0\xbd\t\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\tpHYs\x00\x00\x0b\x13\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\x07tIME\x07\xd9\t\x13\x13\r9B\x92\x96+\x00\x00\x06)IDATX\xc3\xed\x97]h[\xe7\x19\xc7\x7f\xef\x89p\x8e\xe2\x8c\x8d:\x03\x07R\x08\x84\xc6\xd9RG\x9e\xe3\xc4a\x1f\xb1C\xa1\xf5`\x0c\xe1\xd0\x8b\xba\xbdh\x06\x19nWO2euVJ\xa4\xc0\x98b\xe8\xb0\x924\x8d\x87;t\xb1\xcc\x1b+st\xe3Vf\x18i\xa5\xe08\xd2\\i\xb6\x89\xbd.\x03\x9b\xccK\x99k<w\xf69\xe0\xe4<\xbb\x90\xce\xd1\xd1GIL)\xb4\x90\x97sq\xce\xf3\xf5>\x1f\xff\xf79\xcf\xab\x04\xe1\x81\x97")\xa4\x9cO\x01\x85\x0e\xea\xe7\xac\xfc\x12\xaf\x02\x0b\xb4\x023\x15\x86\x90@\xfe\xf9)\xcc\xc3c0\x07\xc0<\xbc\x02\xe7\x01\xb8\x0e\x02!\x8fm\xf5\x1d\xf8\x074\x00p\x00\xb0\xdf\xf3k\x04Z\x81m\xac\xae\xf2Q\x02V`\xc8a\xd6\xd7\xd7\x1f<x\xb0\xb7\xb7\xf7\xc4\x89\x13\xe3\xe3\xe3p\x17\xa6a\xcc\xc3\xf3Q\x00/t\xc7\xf7\xecY\xbey\xf3\xe6\xce\x9d;\x97\x97\x97gffVVV:;;\xef\xdd\xfb\xdfk\xc9g\xf8\xc1A\'2\x01y\xf9\xe5O\x00\x11\x19\x19\x19\x11\x91\x8b\x17/\x8a\x88\x88\x0c\r\xbd\xf5\xfa\xeb\x7f\xce\xcbl\x830\xa4"\x91\xbd\xdf~\xc2\xfa\xf7\xc2\xc4\xe6\xe6\xe6\xde\xbd{GGG\x97\x96\x96n\xdd\xba\x95N\xa7w\xef\xde}\xf8\xf0\xb6+W\xf6\x01\x8aH\x80k#2\xb9\xc87\x98=;\xbb\xfa\xe8*\xaa\xe0\xfd\xe6\xe6\xe6\xdd\xaf\xdc\xdd\xff\xab\xfd\x1fd\xeb\xfd7\x0f\x81\xae\xe8\x13\xfai<\xfe\xdc\xdf\xde\xbb\n\xa4\xdfJ[M\xda\xdd\xfc\xc65\xeb\xdf\xf27\xd7\xfe\xb3V\xa1\x92\x1f$\'\x13\x93\xc5|7\xf2\xac \x82|\x13~\x01\'!y\xf8}KY\x82<\xc7c2q=\x14\ni\xe8\x85}\xa7\xb9\xea\xe3\x95$\xad\x9d\xf0\t\xf4F\xa3m\x99\xef\x8c}o\xf2\xc7\xb4\xfe\x96\x0f\x93\xa9\xa4\xae\xeb\x8aH\xa0\xa0\x10O\xa0\xd7\xcb\xd8_l\x00\x00\x84\xc0\x0b\xd7\x9ej\xbd\xd1\xde\x0e(\x8a\xa8:\xc3\xd1d\xb2\xb3\xb3\xdd0\xf0z\xd5\x993p\x16\x14\x83a\xba\x0b\x12\x9a\xab\xbc\xde\x0e\xafJn,\x85Y\rm,ut4\xc09X\xc5pc\x90\xb0m\xfe]\xfc?"n\xb8X+0\xc6S~\xc6\xcc\x02\xe9\xb3\xe0\x1b\x00\x1d\xcc f\xd4I\x97\x83o\x0f)8Wad\x00z\xab\xd8\xd6\xd8\xcaR\xf8\x02\xe4\n9\x81u\xa8k;\xbf\xfd\xfbmq\xc6:\xce\x84\x15\x18`\xd8\xd9O\xc1\x80\x14\x9e\xa3?C\xd6\x10&,,\xc1\xb2.\x88\xd0\xd8\xd3\xc6\x82\x14e\x1c|C\x18\xa15\x8f\x15\xc9\x8a\xdc\x13\xc9\x8a\xc0YG@\x8a~\xff\xf0\xf8v\xe0\xd7\xa5\xf9\x148\xafB\xce\xa7\x87H0\x9f)s\xe3z\xc78O?\xc1\xdfAhR\\\x80\x80\x02\xa3c\x8c\xaf\xfd\x17 \x91\x82\xbe\xc2.{vM|w\x8a\xc0\x87\xf4Y\x8c\x16\xfcA\x84V\xdf\x84\xed\x89\x0b\xb1\xb7\x97\x8f\x1d\xbb|(\xf5/>Zd\xc7-\x1e\x85\xf7a>{h2w\xcc\xe5ZD\\\x81\xca\x93\xc7\x07\x02q\x9e\xfc+\xaf\x0e\xf3\xd5S\x03n\x16DJ\xf1\xed\xf7\x83\x81\xf1\x08J\x10\x85w\x85\xf8\x18~?\x986$\x8a\xaa\x81\xb2}*\x89Z9\x9e*\x97\x8b\xe8\x81s6\xbe\xaf\x938oo\xea\xac\x12\xe2\xd6\xf0\xed\x11K\x94R\x0f"\x1a\x8b\xc5<J\xa9d2\xe9\xf1x\xeec\xd5\xe3Y\\\\\xf4\xe4\xdf\x1eDZD\xb6v\x1a>Oi\xcf\xd2\xd2\xd2\xc2\xc2\x82\xa6\xddGM\xd34M\xd3\xd4\xf8\xf8xY\x88\xba\xae\xcf\xce\xce\xee\xdb\xb7\xaf\xca)^\\\\,#e2\x99\xba\xba:\x9f\xcf\xb7\xb6\xb6V\xee\xc9\xed\xdb\xb7\xcbH\x86a\x00kkk\x95\xac/P\x06+k\x9e\xcffMMM%\xcb3::ZU:\x91H\xd4\xd4\xd4\x94gpk\xfd\xbb\xad\x8d\xf6v\xf4|\x032\xab\x1d4\x9b\x95JA(\x84\x08\x81\x00\x81@\xb1\xe3\xb8\x1f\x87\x15\n\xa1"\x11\xee\xdc\xe1\xd4)\x86\x87Q\x1a\xba\x85\xf3\xe7F05\xc4\xa2\xab\x8bX\x8c\xfaz\nQ\x0f\x0f\xd3\xdfO.C\xd3 \x1c\xb0\x7f\x8csd\xbb\xf1\xb5\xd0\xd7g\'\xc04\x89FQ\x1a\xb9\x0c\x8d\xcd\xe4NC\x166 K\xee4\x8d\xcd\xe42(\x8dh\x14\xd3\xb4\xab\xa3[4\r2\x93\xe6\xf1#\xe4z N\xf6%\x1e?\xc2L\x9a\xa6At\xab\xac\x96\n\x0e\xe0\xbbTP\x98\xbc\xc2\x8a\xc1\xf4\r|\x97l\xc7\xca+\xaf\xa0\x01\xdf\x8bd2\xb4\xb4P[K\xd3O\xa0\xc1\x15t\x89\xb4\xc0<\xd9\xcb\xac\xaf\x17\x14ro\xc2<\xee\xeaiE\xd19r=4\x1e\xe5\x11/\xad/\xb8b\x98+*\x14\xa4M\x8dl\xb7\x1d\xd6\x1b\xe0/\xc6\x90\xed\xc6\xb4mj\xbaN0\x88X\xf8Z\x98\x9e\xc27\x04M\xb0\x03\x9a\xf0\r1=\x85\xaf\x05\xb1\x08\x06\xd1\xf5\xfb\xd5R\xd5\xf2\xbb\xab\xbc\xfd\xb6]\xcb|u\x82A\x80h\xb4\x1cR"\x98\x06\xb1\x18\xd1(\xe1\xf0\x161\xa8\x1e\xce\xdf\x0f\xe7\xef\x87\xf3\xb7\xd3\xbf\xa1\xdd\x9e\x86\xccO\x1f\x94LH\xe5\xa3\x16\x08@\xa0b\x00\x93RV\x08T\x04\xee\xc0)\x18\x06\rJ\x8f|\x81\xd2\x051\xa8wr2\x0c\xfdp\x12>\x86]\xf0u\xd8\x05\x1f\xc3I\xe8\x87a\xa7\xb3\x99\x10\x05\r2\xd0\x0c\xae\xf6\xcdih\x86\x0ch\x10\x05\xd3\xb1m\xc1 \xa4\xe1\x08\xf4@\x1c^\x82#\x90\x86A\xb0\xca\xba\xa6\x82\x03p\xc9V\xb8\x02\x06\xdc\x80\xd2\xf6\xed\xaa\xa5\x82\x06x\x112\xd0\x02\xb5P\xd1\xbe]\xd2\x02\xf3p\x19\xd6m\x85\x8a\xf6mK\x0b\xccA\x0f\x1c\x05/\xbc\xe0\x8a\xc1\xd5\xbemi\r\xba\xed\xb0\xde\x00\xbf+\x86n\x97\x03\x9a\x0eA\xb0\xa0\x05\xa6\xc0\xd5\xbe\x19\x82)h\x01\x0b\x82\xa0;j]\xd0\x07\x7f\x82:X\x86\xff\xc02\xd4\xc1;\xb0\x1f\xba\x9c\x89#_\x9d \x00\x15\xed\x1b\x01\x03b\x10\x85\xf0V1\xf8e\xbd_z\x88\x07\x9d3\x0f\x1b\xa0@\xe7\x0f\t;O\x0e\x11H\xa9\xfc\xad\x11\xe0\xf7}\xfc\xb1\x9fk\xa5\xd6*\x88\xae\x138P\xedX\x0eT\xbf\x1dm\xc7[\xe9j\t\xd1\xd5\x07\x95\x97\x8d\r\xbc\n\xaf\xceo\xe2<\xdb\x81\xb8\x88e\xf7\xcb\x92\xe7B\xd5~\xe1\xea\xc8%\xcb\xfa\xb4\x19\xb9\xaa\xb4w{U\xc8T\xde/M\x10\x8c\x1d\xec0\x107\xf1\x8bu\xbf\xfc?\xce`\xd76\r\xf8<n\x00\x00\x00\x00IEND\xaeB`\x82"""
    if e32.in_emulator():
        fileImage = 'C:\\Python\\bpic15.png'
    else:
        fileImage = 'E:\\Python\\bpic15.png'
    if not os.path.exists(fileImage):
        imagem = open(fileImage,'wa')
        imagem.write(img)
        imagem.close()


if __name__ == "__main__":
    createImage()
    game = BoxWorld()
    game.run()
