# Voici le code pour mon projet personel
# Écrit par: Ryan McCracken, 10e, PÉI
#
# Github: @R-aMcC



import cmath
import math
from time import sleep
import sys
i = 'a'
a = None
b = None
c = None
d = None
e = None
true? = True
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
    f = c - ((3*b*2)/8)
    g = d + ((b**3) / 8) - ((b*c)/2)
    h = e - ((3*b**4)/256) + (b**2 * c/16) - ( (b*d)/4)
    i = f/2
    j = ((f**2 - 4*h)/16)
    k = -((g**2)/64)
    #Maintenant, nous avons une équation de la forme ax^3 + bx^2 + cx +d = 0, alors on calule l'équation cubique 
    Xs = cubic_eq(1, i, j, k)
    y1 = Xs[0]
    y2 = Xs[1]
    y3 = Xs[2]
    #Pour trouver la réponse, p et q sont équale aux racines de 2 variables qui ne sont pas 0
    if y1 and y2 != 0:
      p = sq_rt(y1)
      q = sq_rt(y2)
      r = -g/(8*p*q)
      s = b/(4*a)
      true? = True
    elif y1 and y3 != 0:
      p = sq_rt(y1)
      q = sq_rt(y3)
      r = -g/(8*p*q)
      s = b/(4*a)
      true? = True
    elif y2 and y3 != 0:
      p = sq_rt(y2)
      q = sq_rt(y3)
      r = -g/(8*p*q)
      s = b/(4*a)
      true? = True
    else:
      #Un cas où l'équation ne fonctionne pas
      print('solution invalide. Vérifie tes numéros')
      true? = False
      sys.exit()
    if true? = True:
      x1 = p + q + r -s  
      x2 = p - q - r -s 
      x3 = -p + q - r -s 
      x4 = -p - q + r -s 
      print(f'x1 = {x1}')
      print(f'x2 = {x2}')
      print(f'x3 = {x3}')
      print(f'x4 = {x4}')
def func():
  #Créé un loop infini, et qui fait toute fonctionner. Elle prends les informations données par l'utilisateur et décide quoi faire.
  loop = 1
  
  print('0 = Aide')
  print('1 = Équation quadratique (ax^2 + bx + c = 0)')
  print('2 = Équation cubique (ax^3 + bx^2 + cx + d = 0)')
  print('3 = Équation quartique (ax^4 + bx^3 + cx^2 + dx + e = 0)')
  print('9 = Fin')
  print(' ')
  print('-'*50)
  while loop == 1 :
    print(' ')
    inp = input("SVP entrer le numéro qui correspond à la fonction dont tu veux calculer :  ")
    print()
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
      a = getflt('a NOTE: "a" ne peut pas être 0')
      b = getflt('b')
      c = getflt('c')
      d = getflt('d')
      e = getflt('e')
      print()
      print()
      quart_eq(a, b, c, d, e)
    elif inp == '9':
      print(" ")
      print('Merci! À la prochaine!')
      sys.exit(1)
    elif inp == '0':
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
