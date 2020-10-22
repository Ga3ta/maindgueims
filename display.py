from display_math_problems import *
from display_physics_problems import *
from display_chemistry_problems import *
from display_orthography_problems import *
from display_screen_elements import *
from display_answers import *

#Una clase principal que sirve para mostrar los diferentes juegos
class Display:
    # La función con la que se instancia el objeto
    def __init__(self, size, screen):
        self.size = size
        self.screen = screen
    # La función que inicializa el resto de displays
    # función que se llama solo 1 vez
    def init_var(self):
        self.display_orthography=DisplayOrthography(self.size,self.screen)
        self.display_orthography.init_var()
        self.display_math=DisplayMath(self.size,self.screen)
        self.display_math.init_var()
        self.display_physics=DisplayPhysics(self.size,self.screen)
        self.display_physics.init_var()
        self.display_chemestry=DisplayChemistry(self.size,self.screen)
        self.display_chemestry.init_var()
        self.display_screen_elements=DisplayScreen(self.size,self.screen)
        self.display_screen_elements.init_var()
    # Una función que nos ayuda a reiniciar todas las variables para que los problemas varíen
    def new_window(self):
        self.display_orthography=DisplayOrthography(self.size,self.screen)
        self.display_orthography.init_var()
        self.display_math=DisplayMath(self.size,self.screen)
        self.display_math.init_var()
        self.display_physics=DisplayPhysics(self.size,self.screen)
        self.display_physics.init_var()
        self.display_chemestry=DisplayChemistry(self.size,self.screen)
        self.display_chemestry.init_var()
        self.display_screen_elements.init_var()
    # Una función que esta en un ciclo mostrando los elementos
    def show(self,game):
        self.game=game
        self.display_screen_elements.show()
        if self.game == 1:
            self.display_orthography.show()
        elif self.game == 2:
            self.display_math.show()
        elif self.game == 3:
            self.display_physics.show()
        elif self.game == 4:
            self.display_chemestry.show()


