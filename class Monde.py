class Monde(dimension,duree_repousse,carte):
  def init(self):
    self.duree_repousse = duree_repousse
    self.dimension = dimension
    
  def nbHerbe(self):
    cpt = 0
    for i in range(self.dimension):
      for j in range(self.dimension):
        if self.contenu[i][j]>self.duree_repousse:
          cpt += 1
    return cpt
  
  def Herbepousse(self):
    for i in range(self.dimension):
