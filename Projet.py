# Voici le code pour mon projet personel
# Écrit par: Ryan McCracken, 10e, PÉI
#
# Github: @R-aMcC
# Repository: https://github.com/R-aMcC/ProjetPersonel/blob/main/Projet.py



import cmath
import math
from time import sleep
import sys

i = None
a = None
b = None
c = None
d = None
e = None
true = True
def isflt(i, nomvar):
  #Vérifie qu'un varialbe est un float
  try:
    float(i)
    return(True)
  except:
    print()
    print(f'Ce varialbe doit être un nombre (reçu "{i}")')
    print()
    return(False)


def getflt(nomvar):
  #cherche une valeur float de l'utilisateur
  while True:
        b = input(f'SVP donner une valeur pour {nomvar}  : ')
        if isflt(b, nomvar):
          return float(b)
          break
  
def sq_rt(x):
  #calcule la racine carée
    return x**0.5



def round_(zx):
  #Arrondis un nombre 
  zx= zx*10000
  zx= round(zx, 0)
  zx = float(zx)
  zx = zx/10000
  return zx

def quad_eq(a,b,c):
  #Prends les valeurs de A, B, et C pour trouver les 2 racines de l'équation avec l'équation quadratique.
  if a==0:
    print("A ne peut pas être 0, sinon la fonction n'est pas quadratique")
  else:
    
    x1 = (-b + sq_rt(b**2 -4*a*c))/(2*a)
    x2 = (-b - sq_rt(b**2 -4*a*c))/(2*a)
    if isinstance(x1, complex):
      print('Le variable X1 est un nombre complex et peut pas être arrodis')
    else:
      (round(x1, 4))
    if isinstance(x2, complex):
      print('Le variable x2 est un nombre complex et peut pas être arrodis')
    else:
      round(x2, 4)
    #Donne la réponse sur la console 
    if x1==x2:
      print(f'x1 = {x1}')
      print(f'x2 = {x2}')
    else:
      print(f'x1 = {x1}')
      print(f'x2 = {x2}')

      

  
def cubic_eq(a,b,c,d):
  #   Source pour équation cubique: https://www.1728.org/cubic2.htm
  #Calcule l'équation quadratique avec les nombres, calculent les valeurs de x ou y=0
  if a == 0:
    #Pour chaque équation, le variable A ne peut pas être 0
    print("Le variable a ne peut pas être 0, sinon l'équation n'est pas cubique" )
  else:
    f = ((3*c/a) - ((b*b)/(a*a)))/3
    g = ((2*(b*b*b)/(a*a*a)) - ((9*b*c)/(a*a)) + (27*d/a))/27
    h = ((g*g)/4) + ((f*f*f)/27)
    if h>0:
      #seulement une vraie racine
       i = (((g*g)/4) - h)**(1/2)
       r = -(g/2) + (h)**(1/2)
       s = (r)**(1/3)
       t = -(g/2) - (h)**(1/2)
      # Si t est négatif, Python ne fait pas correctement **(1/3) et retourne |u| comme étant un nombre complexe
       if t < 0:
        u = (-t)**(1/3)
        u = -u
       else:
        u = (t)**(1/3)
       x1 = (s + u) - (b/(3*a))
       x1 = round_(x1)
       x2 = -(s + u)/2 - (b/(3*a)) + i*(s-u)*((3)**(1/2))/2
       x3 = -(s + u)/2 - (b/(3*a)) - i*(s-u)*((3)**(1/2))/2
       xs = [x1, x2, x3] 
       return (xs)
    else: 
      if f==0 and g==0 and h==0 :
       #Toute les 3 racines sont vraies et égale
       x1 = (d/a)**(1/3)*(-1)
       x2 = (d/a)**(1/3)*(-1)
       x3 = (d/a)**(1/3)*(-1)
      else: 
        if h <= 0:
          #Les 3 racines sont vraies
           i = (((g*g)/4) - h)**(1/2)
           j = (i)**(1/3)
           k = math.acos((- (g / (2*i))))
           l = j * (-1)
           m = math.cos(k/3)
           n = sq_rt(3) * math.sin(k/3)
           p = (b/(3*a))*(-1)
          
           x1 = (2*j) * math.cos(k/3) -(b/(3*a))
           x2 = l * (m+n) + p
           x3 = l * (m-n) + p
           x1 = round_(x1)
           x2 = round_(x2)
           x3 = round_(x3)
           xs = [x1, x2, x3] 
           return (xs)


def quart_eq(a, b, c, d, e):
  #Ce fonction calcule la les 4 racines, ou réponses, de l'équation.
  if a==0:
    print("Le variable a ne peut pas être 0, sinon l'équation n'est pas quartique")
  else:
  #Simplifiant les varialbes pour le faire plus facile en divisant chaque variable par la valeur de a
    b = b/a
    c = c/a
    d = d/a
    e = e/a
    a = a/a
    # définit les autres fonctions utilisées pour trouver la réponse
    f = c - ((3*b*2)/8)
    g = d + ((b**3) / 8) - ((b*c)/2)
    h = e - ((3*b**4)/256) + (b**2 * c/16) - ( (b*d)/4)
    i = f/2
    j = ((f**2 - 4*h)/16)
    k = -((g**2)/64)
    #Maintenant, nous avons une équation de la forme ax^3 + bx^2 + cx +d = 0, alors on calule l'équation cubique 
    Xs = cubic_eq(1, i, j, k)
    # La réponse est sous forme d'une liste, alors nous devons le mettre en floats
    y1 = Xs[0]
    y2 = Xs[1]
    y3 = Xs[2]
    #Pour trouver la réponse, p et q sont équale aux racines de 2 variables qui ne sont pas 0
    if y1 and y2 != 0:
      p = sq_rt(y1)
      q = sq_rt(y2)
      r = -g/(8*p*q)
      s = b/(4*a)
      true = True
    elif y1 and y3 != 0:
      p = sq_rt(y1)
      q = sq_rt(y3)
      r = -g/(8*p*q)
      s = b/(4*a)
      true = True
    elif y2 and y3 != 0:
      p = sq_rt(y2)
      q = sq_rt(y3)
      r = -g/(8*p*q)
      s = b/(4*a)
      true = True
    else:
      #Un cas où l'équation ne fonctionne pas (Au cas d'une érreure, pas vue au paravant )
      print('solution invalide. Vérifie tes numéros')
      true = False
    if true == True:
      x1 = p + q + r -s  
      x2 = p - q - r -s 
      x3 = -p + q - r -s 
      x4 = -p - q + r -s 
      #mets les variables sur l'interface
      print(f'x1 = {x1}')
      print(f'x2 = {x2}')
      print(f'x3 = {x3}')
      print(f'x4 = {x4}')
def func():
  #Créé un loop infini, et qui fait toute fonctionner. Elle prends les informations données par l'utilisateur et décide quoi faire.
  loop = 1
  #Indique toutes les fonctions
  print('0 = Aide')
  print('1 = Équation quadratique (ax^2 + bx + c = 0)')
  print('2 = Équation cubique (ax^3 + bx^2 + cx + d = 0)')
  print('3 = Équation quartique (ax^4 + bx^3 + cx^2 + dx + e = 0)')
  print('4 = Mettre un nombre au carée')
  print('5 = Trouve la racine carée du nombre donnée')
  print('6 = Mettre un nombre au cube')
  print('7 = Trouve la racine cube du nombre donnée')
  print("8 = Mets un nombre au pouvoir d'un autre nombre")
  print("9 = Met le premier nombre à la racine de pouvoir de l'autre")
  print('-1 = Fin')
  print(' ')
  print('-'*50)
  while loop == 1 :
    print(' ')
    inp = input("SVP entrer le numéro qui correspond à la fonction dont tu veux calculer :  ")
    print()
    #Cherche un nombre et le compare aux données pour voir si c'est un nombre valide, et exécute la fonction
    if inp == '1':
      # Si l'utilisatuer entre 1, le programme demande pour 3 varaibles et calcule l'équation quadratique
      a = getflt('a NOTE: "a" ne peut pas être 0')
      b = getflt('b')
      c = getflt('c')
      quad_eq(a, b, c)
     
    elif inp == '2':
      #Si l'utilisateur entre 2, le programme cherche pour 4 variables décimales et calcule l'équation cubique
      a = getflt('a NOTE: "a" ne peut pas être 0')
      b = getflt('b')
      c = getflt('c')
      d = getflt('d')
      print()
      print()
      #j'utilise l cette équation à autre part, alors j'ai besoin qu'elle n'imprimme rient. Alors, je retourne les 3 valeurs et les imprimment individuellement
      Xs = cubic_eq(a, b, c, d, )
      x1 = Xs[0]
      x2 = Xs[1]
      x3 = Xs[2]
      
      print(f'x1: {x1}')
      print(f'x2: {x2}')
      print(f'x3: {x3}')
    elif inp == '3':
      #Si 3 est entré, le code cherche 5 variables et calcule l'équation quartique
      a = getflt('a NOTE: "a" ne peut pas être 0')
      b = getflt('b')
      c = getflt('c')
      d = getflt('d')
      e = getflt('e')
      print()
      print()
      quart_eq(a, b, c, d, e)
    elif inp == '4':
      # pour 5, il met le numéro au carrée
      a = getflt('mettre au carée')
      aq = a**2 
      print(f'{a} au caré est {aq}')
    elif inp == '5':
      # 6 cherche la racine carrée d'un nombre
      a = getflt('trouvé la racine carrée')
      if a < 0:
        #Un nombre négatif n'as pas de racine carrée
        print(f"{a} n'as pas de racine carrées car elle est négative")
      aq = a**(1/2)
      print(f'La racine carée de {a} est {aq}')
    elif inp == '6':
      #Cherche la valeur cubé (^3)
      a = getflt('mettre au cube')
      aq = a**3
      print(f'Le cube de {a} est {aq}')
    elif inp == '7':
      # trouve la racine cube
      a = getflt('trouver la racine cube')
      if a<0:
        a = -a
        aq = -(a**(1/3))
        a = -a
      else:
        aq = a**(1/3)
      print(f'la racine cube de {a} est {aq} ')
    elif inp == '8':
      #Mets un nombre à un autre nombre
      a = getflt('être mis au pouvoir de la prochaine variable')
      b = getflt("être la degrée de l'équation")
      aq = a**b
      print(f'{a} au pouvoir de {b} est {aq}')
    elif inp == '9':
      #Mets le premier nombre à la racine du 2e nombre
      a = getflt('touver la racine de la prochaine varialbe ')
      b = getflt('la dégrée de la racine (Positif)')
      if b < 0:
        print()
        print('SVP enter un nombre positif  pour b')
      
      elif (b%2) == 0:
        if (a < 0):
          print()
          print(f"Un nombre négatif n'as pas de racine {b}")
          
        else:
          aq = a**(1/b)
          print()
          print(f'{a} à la racine {b} est {aq}')
          a = a
        
      elif (b%2) == 1:
        if a<0:
          aq = -((-a)**(1/b))
          print()
          print(f'{a} à la racine {b} est {aq}')
        else:
          aq = a**(1/b)
          print(f'{a} à la racine {b} est {aq}')

    elif inp == '-1':
      #ferme le code
      print(" ")
      print('Merci! À la prochaine!')
      sys.exit(1)
    elif inp == '0':
      #Indique toute les fonctions et ce qu'ils font
      print('Voici ce que les fonctions font:')
      print('')
      print('1 = Équation quadratique de la forme "ax^2 + bx + c = 0"')
      print()
      print("Cette fonction prends 3 varialbes, a, b, et c, et trouve les 2 racines, ou réponses, (Valeur de x) de l'équation. Elle est un polynome du 2e degrée." )
      print()
      print()
      print('2 = Équation cubique de la forme "ax^3 + bx^2 + cx + d = 0"')
      print()
      print("Cette fonction prends 4 varialbes, a, b, c et d, et trouve les 3 racines, ou réponses, (Valeur de x) de l'équation. Les 3 racines peuvent être soit : Tous les 3 égales et réelles, les 3 sont réelles,  et une réelle et 2 complexes (de la forme n+m*1 où m et n sont des nombres décimales). Elle est un polynome du 3e degrée")
      print()
      print()
      print('3 = Équation quarique de la forme "ax^4 + bx^3 + cx^2 + dx + e = 0"')
      print()
      print()
      print("Cette fonction prends 5 variavles, a, b, c, d et c, et trouve les 4 racines, ou réponses, (Valeurs de x ou y =0) de l'équation. Parfois, certaines des racines sont complexe, alors sous la forme de (n + m*i) où n est un nombre décimale et m est un nombre décimale.Cette fonction est la plus grade fonction qui est possible d'être résoud avec un radical, et est un polynome du 4e degrée.")
    else:
      print('SVP Entrer un numéro qui correspond à une fonction.')
func()
