import numpy as np
import matplotlib
import matplotlib.pyplot as plt 

#Have to create a graIntensité where O2 and H2 concentration are shown. 1 droite per Intensité

####################################### DATA Fixed #######################################

R = 8.314
T = 314 #[K]
ZO2 = 4
ZH2 = 2
F = 96485.3
p = 101325 #UNITE ????
Volume = 3 #[L]

####################################### DATA Experience #######################################
I1 = 10
I2 = 12
I3 = 13
I4 = 14
Tension = np.array([1,2,3,4])



degree_vitesse = 2#MIGHT HAVE TO CHANGE DEGREE HERE WILL SET TWO
degree_rendement_energetique = 2 #MIGHT HAVE TO CHANGE DEGREE HERE WILL SET TWO

time1 = np.array([1,2,3,4,5]) #[s]
O_2_I1 = np.array([1,2,3,4,5]) #[mol/L]
time1 = np.array([1,2,3,4,5]) #[s]
H_2_I1 = np.array([2,4,6,8,10]) #[mol/L]


time2 = np.array([1,2,3,4,5]) #[s]
O_2_I2 = np.array([-0.5,0,0.5,1,1.5]) #[mol/L]
time2 = np.array([1,2,3,4,5]) #[s]
H_2_I2 = np.array([-0.69,-0.4,-0.1,0.2,0.5]) #[mol/L]


time3 = np.array([1,2,3,4,5]) #[s]
O_2_I3 = np.array([-1,-2,-3,-4,-5]) #[mol/L]
time3 = np.array([1,2,3,4,5]) #[s]
H_2_I3 = np.array([-2,-3,-4,-5,-6]) #[mol/L]

time4 = np.array([1,2,3,4,5]) #[s]
O_2_I4 = np.array([2,3,4,5,6]) #[mol/L]
time4 = np.array([1,2,3,4,5]) #[s]
H_2_I4 = np.array([1.5,2,2.5,3,3.5]) #[mol/L]


####################################### Plot First GRAIntensité f : t -> [O2], t -> [H2] for different I level #######################################

ax = plt.subplot(1, 1, 1)
ax.plot(time1,O_2_I1, label="[O2] pour I = " + str(I1), color="blue")
ax.plot(time2,O_2_I2, label="[O2] pour I =  " + str(I2),color="blue")
ax.plot(time3,O_2_I3, label="[O2] pour I = "+ str(I3),color="blue")
ax.plot(time4,O_2_I4, label="[O2] pour I = "+ str(I4),color="blue")


ax.plot(time1,H_2_I1, label="[H2] pour I =  " + str(I1) ,color="red")
ax.plot(time2,H_2_I2, label="[H2] pour I =  " + str(I2),color="red")
ax.plot(time3,H_2_I3, label="[H2] pour I =  " + str(I3),color="red")
ax.plot(time4,H_2_I4, label="[H2] pour I =  " + str(I4),color="red")
    
plt.title("Variation de [O2] et [H2] pour differentes intensités")
ax.grid(color='gray',linestyle='dashed') 
ax.grid(color='gray',linestyle='dashed')
ax.legend()
plt.xlabel("Temps [s]")
plt.ylabel("Concentration [mol/L]")

plt.show()


####################################### Calculating the speed of of apparition at each I level #######################################
### d[O2]/dt
coef = np.polyfit(time1, O_2_I1,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_O2_I1 = der.coef[0]

coef = np.polyfit(time2, O_2_I2,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_O2_I2 = der.coef[0]

coef = np.polyfit(time3, O_2_I3,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_O2_I3 = der.coef[0]


coef = np.polyfit(time4, O_2_I4,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_O2_I4 = der.coef[0]


### Now the d[H2]/dt

coef = np.polyfit(time1, H_2_I1,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_H2_I1 = der.coef[0]

coef = np.polyfit(time2, H_2_I2,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_H2_I2 = der.coef[0]

coef = np.polyfit(time3, H_2_I3,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_H2_I3 = der.coef[0]


coef = np.polyfit(time4, H_2_I4,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_H2_I4 = der.coef[0]


##Calculating arrays to plot
I_levels = np.array([I1,I2,I3,I4])
speed_H2 = np.array([speed_H2_I1,speed_H2_I2, speed_H2_I3, speed_H2_I4])
speed_O2 =  np.array([speed_O2_I1,speed_O2_I2,speed_O2_I3,speed_O2_I4])

##Courbe de tendance des vitesse
speed_poly_H2 = np.polyfit(I_levels,speed_H2,degree_vitesse)
polytoplot_H2 = np.poly1d(speed_poly_H2)
speed_poly_O2 = np.polyfit(I_levels,speed_O2,degree_vitesse)
polytoplot_O2 = np.poly1d(speed_poly_O2)
x = np.linspace(I_levels[0],I_levels[-1],100)

##Plot
ax2 = plt.subplot(1, 1, 1)
ax2.scatter(I_levels,speed_H2)
ax2.scatter(I_levels,speed_O2)
ax2.plot(x,polytoplot_H2(x),label="d[H2]/dt(I)")
ax2.plot(x,polytoplot_O2(x),label="d[O2]/dt(I)")
plt.xlabel("Intensité [A]")
ax2.set_title("Evolution de la vitesse de [H2] et [O2] en fonction de l'intensité")
plt.ylabel("Vitesse de concentration [mol/(L*s)]")
ax2.legend()
plt.show()



####################################### Calculating the rendement Faradique #######################################
##Formule = vitesse_observée/vitesse_théorique

##ATTENTION MAINTENANT I EST UN ARRAY DE VALEURS    
vitesse_theorique_O2 = (I_levels*R*T)/(ZO2*F)
vitesse_theorique_H2 = (I_levels*R*T)/(ZH2*F)

evolution_rendement_faradique_O2 = np.empty_like(speed_O2)
evolution_rendement_faradique_H2 = np.empty_like(speed_H2)

evolution_rendement_faradique_H2 = speed_H2/vitesse_theorique_H2

evolution_rendement_faradique_O2 = speed_O2/vitesse_theorique_O2



##Courbe de tendance rendement faradique
evolution_rendement_faradique_H2_poly = np.polyfit(I_levels,evolution_rendement_faradique_H2,degree_vitesse)
polytoplot_rendement_faradique_H2 = np.poly1d(evolution_rendement_faradique_H2_poly)
evolution_rendement_faradique_O2_poly = np.polyfit(I_levels,evolution_rendement_faradique_O2,degree_vitesse)#MIGHT HAVE TO CHANGE DEGREE HERE WILL SET TWO
polytoplot_rendement_faradique_O2 = np.poly1d(evolution_rendement_faradique_O2_poly)
x = np.linspace(I_levels[0],I_levels[-1],100)

##Plot
ax3 = plt.subplot(1, 1, 1)
ax3.scatter(I_levels,evolution_rendement_faradique_H2)
ax3.scatter(I_levels,evolution_rendement_faradique_O2)
plt.title("Evolution du rendement faradique de [H2] et [O2] en fonction de l'intensité")
ax3.plot(x,polytoplot_rendement_faradique_H2(x),label="Rendement faradique de [H2]")
ax3.plot(x,polytoplot_rendement_faradique_O2(x),label="Rendement faradique de [O2]")
ax3.legend()
plt.xlabel("Intensité [A]")
plt.ylabel("Rendement Faradique")
plt.show()


####################################### Calculating the rendement Energétique #######################################
##Formule = Energie consommee/Energie necessaire

Energie_necessaire = 285.8*(p*Volume)/(R*T)
Energie_consommee = (I_levels*Volume*Tension)
evolution_rendement_energetique = Energie_consommee/Energie_necessaire #tension est un array


##Courbe de tendance rendement Energétique
evolution_rendement_energetique_poly = np.polyfit(I_levels,evolution_rendement_energetique,degree_rendement_energetique)
polytoplot_rendement_energetique = np.poly1d(evolution_rendement_energetique_poly)

x = np.linspace(I_levels[0],I_levels[-1],100)

##Plot
ax4 = plt.subplot(1, 1, 1)
ax4.scatter(I_levels,evolution_rendement_energetique)
ax4.set_title("Evolution du rendement énergétique en fonction de l'intensité")
ax4.plot(x,polytoplot_rendement_energetique(x),label="Rendement énergétique")
ax4.legend()
plt.xlabel("Intensité [A]")
plt.ylabel("Rendement Faradique")
plt.show()
