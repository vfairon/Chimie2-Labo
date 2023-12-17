import numpy as np
import matplotlib
import matplotlib.pyplot as plt 

#Have to create a graph where O2 and H2 concentration are shown. 1 droite per pH

####################################### DATA Fixed #######################################




R = 8.314
T = 314 #[K]
ZO2 = 4
ZH2 = 2
F = 96485.3
p = 101325 #UNITE ????
Volume = 3 #[L]

####################################### DATA Experience #######################################
Tension1 = 10
Tension2 = 12
Tension3 = 13
Tension4 = 14
Tension = np.array([Tension1,Tension2,Tension3,Tension4])
Courrant = np.array([1,2,3,4])



degree_vitesse = 2#MIGHT HAVE TO CHANGE DEGREE HERE WILL SET TWO
degree_rendement_energetique = 2 #MIGHT HAVE TO CHANGE DEGREE HERE WILL SET TWO

time1 = np.array([1,2,3,4,5]) #[s]
O_2_Tension1 = np.array([1,2,3,4,5]) #[mol/L]
time1 = np.array([1,2,3,4,5]) #[s]
H_2_Tension1 = np.array([2,4,6,8,10]) #[mol/L]


time2 = np.array([1,2,3,4,5]) #[s]
O_2_Tension2 = np.array([-0.5,0,0.5,1,1.5]) #[mol/L]
time2 = np.array([1,2,3,4,5]) #[s]
H_2_Tension2 = np.array([-0.69,-0.4,-0.1,0.2,0.5]) #[mol/L]


time3 = np.array([1,2,3,4,5]) #[s]
O_2_Tension3 = np.array([-1,-2,-3,-4,-5]) #[mol/L]
time3 = np.array([1,2,3,4,5]) #[s]
H_2_Tension3 = np.array([-2,-3,-4,-5,-6]) #[mol/L]

time4 = np.array([1,2,3,4,5]) #[s]
O_2_Tension4 = np.array([2,3,4,5,6]) #[mol/L]
time4 = np.array([1,2,3,4,5]) #[s]
H_2_Tension4 = np.array([1.5,2,2.5,3,3.5]) #[mol/L]


####################################### Plot First GRAPH f : t -> [O2], t -> [H2] for different I level #######################################

ax = plt.subplot(1, 1, 1)
ax.plot(time1,O_2_Tension1, label="[O2] pour V = " + str(Tension1) + " V", color="blue")
ax.plot(time2,O_2_Tension2, label="[O2] pour V =  " + str(Tension2)+ " V",color="blue")
ax.plot(time3,O_2_Tension3, label="[O2] pour V = "+ str(Tension3)+ " V",color="blue")
ax.plot(time4,O_2_Tension4, label="[O2] pour V = "+ str(Tension4)+ " V",color="blue")


ax.plot(time1,H_2_Tension1, label="[H2] pour V =  " + str(Tension1)+ " V" ,color="red")
ax.plot(time2,H_2_Tension2, label="[H2] pour V =  " + str(Tension2)+ " V",color="red")
ax.plot(time3,H_2_Tension3, label="[H2] pour V =  " + str(Tension3)+ " V",color="red")
ax.plot(time4,H_2_Tension4, label="[H2] pour V =  " + str(Tension4)+ " V",color="red")
    
plt.title("Variation de [O2] et [H2] pour differentes tensions")
ax.grid(color='gray',linestyle='dashed') 
ax.grid(color='gray',linestyle='dashed')
ax.legend()
plt.xlabel("Temps [s]")
plt.ylabel("Concentration [mol/L]")

plt.show()


####################################### Calculating the speed of of apparition at each Tension level #######################################
### d[O2]/dt
coef = np.polyfit(time1, O_2_Tension1,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_O2_Tension1 = der.coef[0]

coef = np.polyfit(time2, O_2_Tension2,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_O2_Tension2 = der.coef[0]

coef = np.polyfit(time3, O_2_Tension3,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_O2_Tension3 = der.coef[0]


coef = np.polyfit(time4, O_2_Tension4,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_O2_Tension4 = der.coef[0]


### Now the d[H2]/dt

coef = np.polyfit(time1, H_2_Tension1,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_H2_Tension1 = der.coef[0]

coef = np.polyfit(time2, H_2_Tension2,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_H2_Tension2 = der.coef[0]

coef = np.polyfit(time3, H_2_Tension3,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_H2_Tension3 = der.coef[0]


coef = np.polyfit(time4, H_2_Tension4,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_H2_Tension4 = der.coef[0]


##Calculating arrays to plot
speed_H2 = np.array([speed_H2_Tension1,speed_H2_Tension2, speed_H2_Tension3, speed_H2_Tension4])
speed_O2 =  np.array([speed_O2_Tension1,speed_O2_Tension2,speed_O2_Tension3,speed_O2_Tension4])

##Courbe de tendance des vitesse
speed_poly_H2 = np.polyfit(Tension,speed_H2,degree_vitesse)
polytoplot_H2 = np.poly1d(speed_poly_H2)
speed_poly_O2 = np.polyfit(Tension,speed_O2,degree_vitesse)
polytoplot_O2 = np.poly1d(speed_poly_O2)
x = np.linspace(Tension[0],Tension[-1],100)

##Plot
ax2 = plt.subplot(1, 1, 1)
plt.title("Evolution de la vitesse d'apparition de O2 et H2 pour differentes tensions")

ax2.scatter(Tension,speed_H2)
ax2.scatter(Tension,speed_O2)
ax2.plot(x,polytoplot_H2(x),label=" d[H2]/dt(Tension)")
ax2.plot(x,polytoplot_O2(x),label="d[O2]/dt(Tension)")
plt.xlabel("Tension [V]")
plt.ylabel("Vitesse de concentration [mol/(L*s)]")
ax2.legend()
plt.show()



####################################### Calculating the rendement Faradique #######################################
##Formule = vitesse_observée/vitesse_théorique

##ATTENTION MAINTENANT I et V sont des ARRAYS DE VALEURS    
vitesse_theorique_O2 = (Tension*R*T)/(ZO2*F)
vitesse_theorique_H2 = (Tension*R*T)/(ZH2*F)

evolution_rendement_faradique_O2 = np.empty_like(speed_O2)
evolution_rendement_faradique_H2 = np.empty_like(speed_H2)


evolution_rendement_faradique_H2 = speed_H2/vitesse_theorique_H2
evolution_rendement_faradique_O2 =  speed_O2/vitesse_theorique_O2


##Courbe de tendance rendement faradique
evolution_rendement_faradique_H2_poly = np.polyfit(Tension,evolution_rendement_faradique_H2,degree_vitesse)
polytoplot_rendement_faradique_H2 = np.poly1d(evolution_rendement_faradique_H2_poly)
evolution_rendement_faradique_O2_poly = np.polyfit(Tension,evolution_rendement_faradique_O2,degree_vitesse)#MIGHT HAVE TO CHANGE DEGREE HERE WILL SET TWO
polytoplot_rendement_faradique_O2 = np.poly1d(evolution_rendement_faradique_O2_poly)
x = np.linspace(Tension[0],Tension[-1],100)

##Plot
ax3 = plt.subplot(1, 1, 1)
plt.title("Evolution du rendement faradique pour differentes tensions")
ax3.scatter(Tension,evolution_rendement_faradique_H2)
ax3.scatter(Tension,evolution_rendement_faradique_O2)
ax3.plot(x,polytoplot_rendement_faradique_H2(x),label="Rendement faradique de [H2]")
ax3.plot(x,polytoplot_rendement_faradique_O2(x),label="Rendement faradique de [O2]")
ax3.legend()
plt.xlabel("Tension [V]")
plt.ylabel("Rendement Faradique")
plt.show()


####################################### Calculating the rendement Energétique #######################################
##Formule = Energie consommee/Energie necessaire

Energie_necessaire = 285.8*(p*np.array([O_2_Tension1[-1]-O_2_Tension1[0], O_2_Tension2[-1]-O_2_Tension2[0], O_2_Tension3[-1]-O_2_Tension3[0], O_2_Tension4[-1]-O_2_Tension4[0]]))/(R*T)
Energie_consommee = (Courrant*Tension*(time1[-1]-time1[0]))##LE TEMPS DOIT ETRE LE MEME POUR TOUT PH

evolution_rendement_energetique = Energie_consommee/Energie_necessaire #tension est un array


##Courbe de tendance rendement Energétique
evolution_rendement_energetique_poly = np.polyfit(Tension,evolution_rendement_energetique,degree_rendement_energetique)
polytoplot_rendement_energetique = np.poly1d(evolution_rendement_energetique_poly)

x = np.linspace(Tension[0],Tension[-1],100)

##Plot
ax4 = plt.subplot(1, 1, 1)
ax4.scatter(Tension,evolution_rendement_energetique)
ax4.set_title("Evolution du rendement énergétique en fonction de l'intensité")
ax4.plot(x,polytoplot_rendement_energetique(x),label="Rendement énergétique")
ax4.legend()
plt.xlabel("Intensité [A]")
plt.ylabel("Rendement Faradique")
plt.show()
