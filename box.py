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




if __name__ == "__main__":
    game = BoxWorld()
    game.run()
