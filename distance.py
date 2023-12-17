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
distance1 = 10
distance2 = 12
distance3 = 13
distance4 = 14
Tension = np.array([1,2,3,4])



degree_vitesse = 2#MIGHT HAVE TO CHANGE DEGREE HERE WILL SET TWO
degree_rendement_energetique = 2 #MIGHT HAVE TO CHANGE DEGREE HERE WILL SET TWO

time1 = np.array([1,2,3,4,5]) #[s]
O_2_distance1 = np.array([1,2,3,4,5]) #[mol/L]
time1 = np.array([1,2,3,4,5]) #[s]
H_2_distance1 = np.array([2,4,6,8,10]) #[mol/L]


time2 = np.array([1,2,3,4,5]) #[s]
O_2_distance2 = np.array([-0.5,0,0.5,1,1.5]) #[mol/L]
time2 = np.array([1,2,3,4,5]) #[s]
H_2_distance2 = np.array([-0.69,-0.4,-0.1,0.2,0.5]) #[mol/L]


time3 = np.array([1,2,3,4,5]) #[s]
O_2_distance3 = np.array([-1,-2,-3,-4,-5]) #[mol/L]
time3 = np.array([1,2,3,4,5]) #[s]
H_2_distance3 = np.array([-2,-3,-4,-5,-6]) #[mol/L]

time4 = np.array([1,2,3,4,5]) #[s]
O_2_distance4 = np.array([2,3,4,5,6]) #[mol/L]
time4 = np.array([1,2,3,4,5]) #[s]
H_2_distance4 = np.array([1.5,2,2.5,3,3.5]) #[mol/L]


####################################### Plot First GRAPH f : t -> [O2], t -> [H2] for different distances #######################################

ax = plt.subplot(1, 1, 1)
ax.plot(time1,O_2_distance1, label="[O2] pour distance = " + str(distance1) + " cm", color="blue")
ax.plot(time2,O_2_distance2, label="[O2] pour distance =  " + str(distance2)+ " cm",color="blue")
ax.plot(time3,O_2_distance3, label="[O2] pour distance = "+ str(distance3)+ " cm",color="blue")
ax.plot(time4,O_2_distance4, label="[O2] pour distance = "+ str(distance4)+ " cm",color="blue")


ax.plot(time1,H_2_distance1, label="[H2] pour distance =  " + str(distance1)+ " cm" ,color="red")
ax.plot(time2,H_2_distance2, label="[H2] pour distance =  " + str(distance2)+ " cm",color="red")
ax.plot(time3,H_2_distance3, label="[H2] pour distance =  " + str(distance3)+ " cm",color="red")
ax.plot(time4,H_2_distance4, label="[H2] pour distance =  " + str(distance4)+ " cm",color="red")
    
plt.title("Variation de [O2] et [H2] pour differentes distances entre les électrodes")
ax.grid(color='gray',linestyle='dashed') 
ax.grid(color='gray',linestyle='dashed')
ax.legend()
plt.xlabel("Temps [s]")
plt.ylabel("Concentration [mol/L]")

plt.show()


####################################### Calculating the speed of of apparition at each distnace #######################################
### d[O2]/dt
coef = np.polyfit(time1, O_2_distance1,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_O2_distance1 = der.coef[0]

coef = np.polyfit(time2, O_2_distance2,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_O2_distance2 = der.coef[0]

coef = np.polyfit(time3, O_2_distance3,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_O2_distance3 = der.coef[0]


coef = np.polyfit(time4, O_2_distance4,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_O2_distance4 = der.coef[0]


### Now the d[H2]/dt

coef = np.polyfit(time1, H_2_distance1,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_H2_distance1 = der.coef[0]

coef = np.polyfit(time2, H_2_distance2,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_H2_distance2 = der.coef[0]

coef = np.polyfit(time3, H_2_distance3,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_H2_distance3 = der.coef[0]


coef = np.polyfit(time4, H_2_distance4,1)
poly = np.poly1d(coef)
der = np.polyder(poly)

speed_H2_distance4 = der.coef[0]


##Calculating arrays to plot
distances = np.array([distance1,distance2,distance3,distance4])
speed_H2 = np.array([speed_H2_distance1,speed_H2_distance2, speed_H2_distance3, speed_H2_distance4])
speed_O2 =  np.array([speed_O2_distance1,speed_O2_distance2,speed_O2_distance3,speed_O2_distance4])

##Courbe de tendance des vitesse
speed_poly_H2 = np.polyfit(distances,speed_H2,degree_vitesse)
polytoplot_H2 = np.poly1d(speed_poly_H2)
speed_poly_O2 = np.polyfit(distances,speed_O2,degree_vitesse)
polytoplot_O2 = np.poly1d(speed_poly_O2)
x = np.linspace(distances[0],distances[-1],100)

##Plot
ax2 = plt.subplot(1, 1, 1)
ax2.scatter(distances,speed_H2)
ax2.scatter(distances,speed_O2)
plt.title("Evolution de la vitesse de [H2] et [O2] en fonction de la distance entre les deux électrodes")
ax2.plot(x,polytoplot_H2(x),label="d[H2]/dt(d) ")
ax2.plot(x,polytoplot_O2(x),label="d[O2]/dt(d) ")
plt.xlabel("distance [cm]")
plt.ylabel("Vitesse de concentration [mol/(L*s)]")
ax2.legend()
plt.show()



####################################### Calculating the rendement Faradique #######################################
##Formule = vitesse_observée/vitesse_théorique

vitesse_theorique_O2 = (I*R*T)/(ZO2*F)
vitesse_theorique_H2 = (I*R*T)/(ZH2*F)

evolution_rendement_faradique_O2 = np.empty_like(speed_O2)
evolution_rendement_faradique_H2 = np.empty_like(speed_H2)

##Filling rendement faradique
for i,vexdistance2 in enumerate(speed_H2) :
    evolution_rendement_faradique_H2[i] = speed_H2[i]/vitesse_theorique_H2

for i,vexpO2 in enumerate(speed_O2) :
    evolution_rendement_faradique_O2[i] = speed_O2[i]/vitesse_theorique_O2


##Courbe de tendance rendement faradique
evolution_rendement_faradique_H2_poly = np.polyfit(distances,evolution_rendement_faradique_H2,degree_vitesse)
polytoplot_rendement_faradique_H2 = np.poly1d(evolution_rendement_faradique_H2_poly)
evolution_rendement_faradique_O2_poly = np.polyfit(distances,evolution_rendement_faradique_O2,degree_vitesse)#MIGHT HAVE TO CHANGE DEGREE HERE WILL SET TWO
polytoplot_rendement_faradique_O2 = np.poly1d(evolution_rendement_faradique_O2_poly)
x = np.linspace(distances[0],distances[-1],100)

##Plot
ax3 = plt.subplot(1, 1, 1)
ax3.scatter(distances,evolution_rendement_faradique_H2)
ax3.scatter(distances,evolution_rendement_faradique_O2)
plt.title("Evolution du rendement faradique de [H2] et [O2] en fonction de la distance entre les électrodes")
ax3.plot(x,polytoplot_rendement_faradique_H2(x),label="Rendement faradique de [H2] ")
ax3.plot(x,polytoplot_rendement_faradique_O2(x),label="Rendement faradique de [O2]")
ax3.legend()
plt.xlabel("distance [cm]")
plt.ylabel("Rendement Faradique")
plt.show()


####################################### Calculating the rendement Energétique #######################################
##Formule = Energie consommee/Energie necessaire

Energie_necessaire = 285.8*(p*Volume)/(R*T)
Energie_consommee = (I*Volume*Tension)
evolution_rendement_energetique = Energie_consommee/Energie_necessaire #tension est un array


##Courbe de tendance rendement Energétique
evolution_rendement_energetique_poly = np.polyfit(distances,evolution_rendement_energetique,degree_rendement_energetique)
polytoplot_rendement_energetique = np.poly1d(evolution_rendement_energetique_poly)

x = np.linspace(distances[0],distances[-1],100)

##Plot
ax4 = plt.subplot(1, 1, 1)
ax4.scatter(distances,evolution_rendement_energetique)
plt.title("Evolution du rendement énergétique en fonction de la distance entre les électrodes")
ax4.plot(x,polytoplot_rendement_energetique(x),label="Rendement energétique")
ax4.legend()
plt.xlabel("distance [cm]")
plt.ylabel("Rendement Faradique")
plt.show()
