import numpy as np
import matplotlib
import matplotlib.pyplot as plt 

#Have to create a graph where O2 and H2 concentration are shown. 1 droite per pH

####################################### DATA Fixed #######################################




R = 8.314
I = 4  #[A]
T = 314 #[K]
ZO2 = 4
ZH2 = 2
F = 96485.3
p = 101325 #UNITE ????
Volume = 3 #[L]

####################################### DATA Experience #######################################
pH1 = 10
pH2 = 12
pH3 = 13
pH4 = 14
Tension = np.array([1,2,3,4])



degree_vitesse = 2#MIGHT HAVE TO CHANGE DEGREE HERE WILL SET TWO
degree_rendement_energetique = 2 #MIGHT HAVE TO CHANGE DEGREE HERE WILL SET TWO

time1 = np.array([1,2,3,4,5]) #[s]
O_2_pH1 = np.array([1,2,3,4,5]) #[L]
time1 = np.array([1,2,3,4,5]) #[s]
H_2_pH1 = np.array([2,4,6,8,10]) #[L]


time2 = np.array([1,2,3,4,5]) #[s]
O_2_pH2 = np.array([-0.5,0,0.5,1,1.5]) #[L]
time2 = np.array([1,2,3,4,5]) #[s]
H_2_pH2 = np.array([-0.69,-0.4,-0.1,0.2,0.5]) #[L]


time3 = np.array([1,2,3,4,5]) #[s]
O_2_pH3 = np.array([-1,-2,-3,-4,-5]) #[L]
time3 = np.array([1,2,3,4,5]) #[s]
H_2_pH3 = np.array([-2,-3,-4,-5,-6]) #[L]

time4 = np.array([1,2,3,4,5]) #[s]
O_2_pH4 = np.array([2,3,4,5,6]) #[L]
time4 = np.array([1,2,3,4,5]) #[s]
H_2_pH4 = np.array([1.5,2,2.5,3,3.5]) #[L]


####################################### Plot First GRAPH f : t -> [O2], t -> [H2] for different pH level #######################################

ax = plt.subplot(1, 1, 1)
ax.plot(time1,O_2_pH1, label="Volume d'O2 pour pH = " + str(pH1), color="blue")
ax.plot(time2,O_2_pH2, label="Volume d'O2 pour pH =  " + str(pH2),color="blue")
ax.plot(time3,O_2_pH3, label="Volume d'O2 pour pH = "+ str(pH3),color="blue")
ax.plot(time4,O_2_pH4, label="Volume d'O2 pour pH = "+ str(pH4),color="blue")


ax.plot(time1,H_2_pH1, label="Volume d'H2 pour pH =  " + str(pH1) ,color="red")
ax.plot(time2,H_2_pH2, label="Volume d'H2 pour pH =  " + str(pH2),color="red")
ax.plot(time3,H_2_pH3, label="Volume d'H2 pour pH =  " + str(pH3),color="red")
ax.plot(time4,H_2_pH4, label="Volume d'H2 pour pH =  " + str(pH4),color="red")
    
plt.title("Variation de volume d'H2 et d'O2 pour different pH")
ax.grid(color='gray',linestyle='dashed') 
ax.grid(color='gray',linestyle='dashed')
ax.legend()
plt.xlabel("Temps [s]")
plt.ylabel("Volume [L]")

plt.show()


####################################### Calculating the speed of of apparition at each pH level #######################################
### d[O2]/dt
coef = np.polyfit(time1, O_2_pH1,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_O2_pH1 = der.coef[0]

coef = np.polyfit(time2, O_2_pH2,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_O2_pH2 = der.coef[0]

coef = np.polyfit(time3, O_2_pH3,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_O2_pH3 = der.coef[0]


coef = np.polyfit(time4, O_2_pH4,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_O2_pH4 = der.coef[0]


### Now the d[H2]/dt

coef = np.polyfit(time1, H_2_pH1,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_H2_pH1 = der.coef[0]

coef = np.polyfit(time2, H_2_pH2,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_H2_pH2 = der.coef[0]

coef = np.polyfit(time3, H_2_pH3,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_H2_pH3 = der.coef[0]


coef = np.polyfit(time4, H_2_pH4,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_H2_pH4 = der.coef[0]


##Calculating arrays to plot
pH_levels = np.array([pH1,pH2,pH3,pH4])
speed_H2 = np.array([speed_H2_pH1,speed_H2_pH2, speed_H2_pH3, speed_H2_pH4])
speed_O2 =  np.array([speed_O2_pH1,speed_O2_pH2,speed_O2_pH3,speed_O2_pH4])

##Courbe de tendance des vitesse
speed_poly_H2 = np.polyfit(pH_levels,speed_H2,degree_vitesse)
polytoplot_H2 = np.poly1d(speed_poly_H2)
speed_poly_O2 = np.polyfit(pH_levels,speed_O2,degree_vitesse)
polytoplot_O2 = np.poly1d(speed_poly_O2)
x = np.linspace(pH_levels[0],pH_levels[-1],100)

##Plot
ax2 = plt.subplot(1, 1, 1)
ax2.scatter(pH_levels,speed_H2)
ax2.scatter(pH_levels,speed_O2)
plt.title("Evolution de la vitesse de d'apparition d'H2 et d'O2 en fonction du pH")
ax2.plot(x,polytoplot_H2(x),label="dV(H2)/dt (pH)")
ax2.plot(x,polytoplot_O2(x),label="dV(O2)/dt (pH) ")
plt.xlabel("pH")
plt.ylabel("Vitesse de concentration [L/(s)]")
ax2.legend()
plt.show()



####################################### Calculating the rendement Faradique #######################################
##Formule = vitesse_observée/vitesse_théorique

vitesse_theorique_O2 = (I*R*T)/(ZO2*F)
vitesse_theorique_H2 = (I*R*T)/(ZH2*F)

evolution_rendement_faradique_O2 = np.empty_like(speed_O2)
evolution_rendement_faradique_H2 = np.empty_like(speed_H2)

##Filling rendement faradique
for i,vexpH2 in enumerate(speed_H2) :
    evolution_rendement_faradique_H2[i] = speed_H2[i]/vitesse_theorique_H2

for i,vexpO2 in enumerate(speed_O2) :
    evolution_rendement_faradique_O2[i] = speed_O2[i]/vitesse_theorique_O2


##Courbe de tendance rendement faradique
evolution_rendement_faradique_H2_poly = np.polyfit(pH_levels,evolution_rendement_faradique_H2,degree_vitesse)
polytoplot_rendement_faradique_H2 = np.poly1d(evolution_rendement_faradique_H2_poly)
evolution_rendement_faradique_O2_poly = np.polyfit(pH_levels,evolution_rendement_faradique_O2,degree_vitesse)#MIGHT HAVE TO CHANGE DEGREE HERE WILL SET TWO
polytoplot_rendement_faradique_O2 = np.poly1d(evolution_rendement_faradique_O2_poly)
x = np.linspace(pH_levels[0],pH_levels[-1],100)

##Plot
ax3 = plt.subplot(1, 1, 1)
ax3.scatter(pH_levels,evolution_rendement_faradique_H2)
ax3.scatter(pH_levels,evolution_rendement_faradique_O2)
plt.title("Evolution du rendement faradique de H2 et O2 en fonction du pH")
ax3.plot(x,polytoplot_rendement_faradique_H2(x),label="Rendement faradique de [H2]")
ax3.plot(x,polytoplot_rendement_faradique_O2(x),label="Rendement faradique de [O2]")
ax3.legend()
plt.xlabel("pH")
plt.ylabel("Rendement Faradique")
plt.show()


####################################### Calculating the rendement Energétique #######################################
##Formule = Energie consommee/Energie necessaire

Energie_necessaire = 285.8*(p*Volume)/(R*T)
Energie_consommee = (I*Volume*Tension)
evolution_rendement_energetique = Energie_consommee/Energie_necessaire #tension est un array


##Courbe de tendance rendement Energétique
evolution_rendement_energetique_poly = np.polyfit(pH_levels,evolution_rendement_energetique,degree_rendement_energetique)
polytoplot_rendement_energetique = np.poly1d(evolution_rendement_energetique_poly)

x = np.linspace(pH_levels[0],pH_levels[-1],100)

##Plot
ax4 = plt.subplot(1, 1, 1)
ax4.scatter(pH_levels,evolution_rendement_energetique)

ax4.plot(x,polytoplot_rendement_energetique(x),label="Evolution du rendement énergétique en fonction du pH")
ax4.legend()
plt.xlabel("pH")
plt.ylabel("Rendement Faradique")
plt.show()
