import turtle
import sys
def placerP(x,y,couleur):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.dot(50, couleur)
def deplacer(x,y):
	turtle.up()
	turtle.goto(x,y)
	turtle.down()
def carre(taile):
	for i in range(4):
		turtle.forward(taile)
		turtle.left(90)
def ligne_plateaux(x,y,couleur):
	y+=80
	x_ini=x
	for i in range(6):
		y-=80
		x=x_ini
		for k in range(7):
			placerP(x,y,couleur)
			x+=70
def plateaux():
	turtle.hideturtle() #rend invisible le turtle
	turtle.fillcolor("blue")
	turtle.begin_fill()
	carre(500)
	turtle.end_fill()
	turtle.left(90)
	ligne_plateaux(-215,210,"grey")
	x=-230
	y=260
	for k in range (8):
		if k !=0:
			deplacer(x,y)
			turtle.write(k, move=False, align="left", font=("Arial", 50, "normal")) # arg – object to be written to the TurtleScreen || move – True/False || align – one of the strings “left”, “center” or right” || font – a triple (fontname, fontsize, fonttype)
			x+=70
def piont_joueur(emplacement,):
	global joueur
	if joueur=="joueur2":
		couleur_joueur="yellow"
		joueur="joueur1"
	else :
		couleur_joueur="red"
		joueur="joueur2"
	if ligne_F[emplacement][0]==0:
		ligne_F[emplacement][0]=1
		ligne_F[emplacement][3]=couleur_joueur
		placerP(ligne_F[emplacement][1],ligne_F[emplacement][2],couleur_joueur)
	elif ligne_E[emplacement][0]==0:
		ligne_E[emplacement][0]=1
		ligne_E[emplacement][3]=couleur_joueur
		placerP(ligne_E[emplacement][1],ligne_E[emplacement][2],couleur_joueur)
	elif ligne_D[emplacement][0]==0:
		ligne_D[emplacement][0]=1
		ligne_D[emplacement][3]=couleur_joueur
		placerP(ligne_D[emplacement][1],ligne_D[emplacement][2],couleur_joueur)
	elif ligne_C[emplacement][0]==0:
		ligne_C[emplacement][0]=1
		ligne_C[emplacement][3]=couleur_joueur
		placerP(ligne_C[emplacement][1],ligne_C[emplacement][2],couleur_joueur)
	elif ligne_B[emplacement][0]==0:
		ligne_B[emplacement][0]=1
		ligne_B[emplacement][3]=couleur_joueur
		placerP(ligne_B[emplacement][1],ligne_B[emplacement][2],couleur_joueur)
	elif ligne_A[emplacement][0]==0:
		ligne_A[emplacement][0]=1
		ligne_A[emplacement][3]=couleur_joueur
		placerP(ligne_A[emplacement][1],ligne_A[emplacement][2],couleur_joueur)
	verif_victoire()
def appui_sur_1():
	if ligne_A["1"][0]==0:
		piont_joueur("1")
	else:
		print("impossible")
def appui_sur_2():
	if ligne_A["2"][0]==0:
		piont_joueur("2")
	else:
		print("impossible")
def appui_sur_3():
	if ligne_A["3"][0]==0:
		piont_joueur("3")
	else:
		print("impossible")
def appui_sur_4():
	if ligne_A["4"][0]==0:
		piont_joueur("4")
	else:
		print("impossible")
def appui_sur_5():
	if ligne_A["5"][0]==0:
		piont_joueur("5")
	else:
		print("impossible")
def appui_sur_6():
	if ligne_A["6"][0]==0:
		piont_joueur("6")
	else:
		print("impossible")
def appui_sur_7():
	if ligne_A["7"][0]==0:
		piont_joueur("7")
	else:
		print("impossible")
def main():
    global joueur
    joueur="joueur1"
    deplacer(-250,-250)
    turtle.speed(10)
    plateaux()  
    print("c'est au {} de jouer\n".format(joueur))
    turtle.listen()
    joueur = turtle.onkeypress(appui_sur_1, "1") #La touche 1 est désormais associée à appui_sur_1
    joueur = turtle.onkeypress(appui_sur_2, "2")
    joueur = turtle.onkeypress(appui_sur_3, "3")
    joueur = turtle.onkeypress(appui_sur_4, "4")
    joueur = turtle.onkeypress(appui_sur_5, "5")
    joueur = turtle.onkeypress(appui_sur_6, "6")
    joueur = turtle.onkeypress(appui_sur_7, "7")
    turtle.mainloop()
def verif_ligne(ligne):
	for k in range(5):
		compteurR=0
		compteurY=0
		if k!=0:
			if ligne[str(k)][0]==1:
				if ligne[str(k)][3]=="red":
					compteurR+=1
				elif ligne[str(k)][3]=="yellow":
					compteurY+=1
			if ligne[str(k+1)][0]==1:
				if ligne[str(k+1)][3]=="red":
					compteurR+=1
				elif ligne[str(k+1)][3]=="yellow":
					compteurY+=1
			if ligne[str(k+2)][0]==1:
				if ligne[str(k+2)][3]=="red":
					compteurR+=1
				elif ligne[str(k+2)][3]=="yellow":
					compteurY+=1
			if ligne[str(k+3)][0]==1:
				if ligne[str(k+3)][3]=="red":
					compteurR+=1
				elif ligne[str(k+3)][3]=="yellow":
					compteurY+=1
		if compteurR>=4:
			victoire()
		elif compteurY>=4:
			victoire()
def verif_colonne(ligne1,ligne2,ligne3,ligne4):
	for k in range(4):
		compteurR=0
		compteurY=0
		if k!=0:
			if ligne1[str(k)][0]==1:
				if ligne1[str(k)][3]=="red":
					compteurR+=1
				elif ligne1[str(k)][3]=="yellow":
					compteurY+=1
			if ligne2[str(k)][0]==1:
				if ligne2[str(k)][3]=="red":
					compteurR+=1
				elif ligne2[str(k)][3]=="yellow":
					compteurY+=1
			if ligne3[str(k)][0]==1:
				if ligne3[str(k)][3]=="red":
					compteurR+=1
				elif ligne3[str(k)][3]=="yellow":
					compteurY+=1
			if ligne4[str(k)][0]==1:
				if ligne4[str(k)][3]=="red":
					compteurR+=1
				elif ligne4[str(k)][3]=="yellow":
					compteurY+=1
		if compteurR>=4:
			victoire()
		elif compteurY>=4:
			victoire()
def verif_diagonale(ligne1,ligne2,ligne3,ligne4):
	for k in range(5):
		compteurY=0
		compteurR=0
		if k!=0:
			if ligne1[str(k)][0]==1:
				if ligne1[str(k)][3]=="red":
					compteurR+=1
				elif ligne1[str(k)][3]=="yellow":
					compteurY+=1
			if ligne2[str(k+1)][0]==1:
				if ligne2[str(k+1)][3]=="red":
					compteurR+=1
				elif ligne2[str(k+1)][3]=="yellow":
					compteurY+=1
			if ligne3[str(k+2)][0]==1:
				if ligne3[str(k+2)][3]=="red":
					compteurR+=1
				elif ligne3[str(k+2)][3]=="yellow":
					compteurY+=1
			if ligne4[str(k+3)][0]==1:
				if ligne4[str(k+3)][3]=="red":
					compteurR+=1
				elif ligne4[str(k+3)][3]=="yellow":
					compteurY+=1
		if compteurR>=4:
			victoire()
		elif compteurY>=4:
			victoire()
def verif_victoire():
	verif_ligne(ligne_F)
	verif_ligne(ligne_E)
	verif_ligne(ligne_D)
	verif_ligne(ligne_C)
	verif_ligne(ligne_B)
	verif_ligne(ligne_A)
	verif_diagonale(ligne_F,ligne_E,ligne_D,ligne_C)
	verif_diagonale(ligne_E,ligne_D,ligne_C,ligne_B)
	verif_diagonale(ligne_D,ligne_C,ligne_B,ligne_A)
	verif_colonne(ligne_F,ligne_E,ligne_D,ligne_C)
	verif_colonne(ligne_E,ligne_D,ligne_C,ligne_B)
	verif_colonne(ligne_D,ligne_C,ligne_B,ligne_A)
	print("c'est au {} de jouer".format(joueur))
def victoire():
	global joueur
	print("victoire ",joueur)
	turtle.bye()
if __name__ == '__main__':
    ligne_A={"1":[0,-215,210,"grey"],"2":[0,-145,210,"grey"],"3":[0,-75,210,"grey"],"4":[0,-5,210,"grey"],"5":[0,65,210,"grey"],"6":[0,135,210,"grey"],"7":[0,205,210,"grey"]}
    ligne_B={"1":[0,-215,130,"grey"],"2":[0,-145,130,"grey"],"3":[0,-75,130,"grey"],"4":[0,-5,130,"grey"],"5":[0,65,130,"grey"],"6":[0,135,130,"grey"],"7":[0,205,130,"grey"]}
    ligne_C={"1":[0,-215,50,"grey"],"2":[0,-145,50,"grey"],"3":[0,-75,50,"grey"],"4":[0,-5,50,"grey"],"5":[0,65,50,"grey"],"6":[0,135,50,"grey"],"7":[0,205,50,"grey"]}
    ligne_D={"1":[0,-215,-30,"grey"],"2":[0,-145,-30,"grey"],"3":[0,-75,-30,"grey"],"4":[0,-5,-30,"grey"],"5":[0,65,-30,"grey"],"6":[0,135,-30,"grey"],"7":[0,205,-30,"grey"]}
    ligne_E={"1":[0,-215,-110,"grey"],"2":[0,-145,-110,"grey"],"3":[0,-75,-110,"grey"],"4":[0,-5,-110,"grey"],"5":[0,65,-110,"grey"],"6":[0,135,-110,"grey"],"7":[0,205,-110,"grey"]}
    ligne_F={"1":[0,-215,-190,"grey"],"2":[0,-145,-190,"grey"],"3":[0,-75,-190,"grey"],"4":[0,-5,-190,"grey"],"5":[0,65,-190,"grey"],"6":[0,135,-190,"grey"],"7":[0,205,-190,"grey"]}
    main()
    finit=input("joueur")
    
