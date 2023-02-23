'''
En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y 
que contenga un botón de reinicio para que deje todo como al principio.

Al principio no tiene que haber una opción seleccionada.
'''
import tkinter
from tkinter import Tk, ttk, StringVar, Text
from readOnlyTex import ReadOnlyTex

# Configuración de Ventana
window = Tk()
window.title("Ejercicio 1 GUI - Radio Buttons")
window.geometry("700x300")
window.resizable(0, 0)

# Configuración de grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)


#Label de la ventana
label_titulo = ttk.Label(
    window, text = "CUAL ES TU EQUIPO FAVORITO?", foreground="black"
)
label_titulo.grid(column=1, row=0, sticky=tkinter.W, columnspan=3, padx= 10)

#Label de la descripcion
label_titulo = ttk.Label(
    window, text = "Datos", foreground="black"
)
label_titulo.grid(column=2, row=0, sticky=tkinter.W, columnspan=3, padx= 10)

#Label del escudo
label_titulo = ttk.Label(
    window, text = "Escudo", foreground="black"
)
label_titulo.grid(column=3, row=0, sticky=tkinter.W, columnspan=3, padx= 10)

# Variable Equipo seleccionado
equipo = StringVar()

# Descripción del Equipo seleccionado
text_equipo = ReadOnlyTex(window, height=15, width=60,
                            font=('Times New Roman', 10, 'normal'), background='#FFFFE0')
text_equipo.grid(column=2, row=1, rowspan=7, sticky='w', padx=10, pady=5)


# Función seleccionar Equipo para mostrar una descripcion al elegir un Radio Button
def seleccionarEquipo():
    descripcion = {'River Plate': '- El Club Atlético River Plate es una entidad polideportiva de Argentina.\n-Fue fundado el 25 de mayo de 1901 en el barrio de La Boca, tras la fusión de los clubes Santa Rosa y La Rosales, y su nombre proviene de la antigua denominación que se le daba en el inglés británico al Río de la Plata.\n- Primera División de Argentina. \n- Disputa sus partidos en el estadio Monumental, el de mayor capacidad del país y el segundo en América, con una capacidad para 83196 espectadores.',
                   'Boca Juniors': '- El Club Atlético Boca Juniors es una entidad deportiva argentina, con sede en el barrio de La Boca, Buenos Aires. \n- Fue fundado el 3 de abril de 1905 por seis vecinos adolescentes hijos de italianos. \n- Actualmente se desempeña en la Liga Profesional de Fútbol Argentino. \n - El equipo juega sus partidos como local en el estadio Alberto J. Armando, conocido mundialmente como «La Bombonera»'  ,
                   'Independiente': '- El Club Atlético Independiente, conocido popularmente como Independiente de Avellaneda, Independiente, o por sus siglas CAI, es una entidad deportiva de Argentina de la ciudad de Avellaneda, situado en el sur del Gran Buenos Aires. \n- Fue fundado el 1 de enero de 1904 por unos jóvenes empleados independentistas del Club Maipú.\n- Ejerce su localía en el Estadio Libertadores de América-Ricardo Enrique Bochini, que cuenta con un aforo de 49.592 espectadores',
                   'Racing': '- Racing Club, conocido como Racing Club de Avellaneda o simplemente Racing, es una entidad deportiva oriunda de Argentina. \n- Fundada el 25 de marzo de 1903 en la ciudad de Avellaneda, provincia de Buenos Aires. Tiene la particularidad de ser el primer equipo argentino fundado íntegramente por criollos. \n- Su estadio es el Presidente Perón, popularmente conocido como «El Cilindro» y «El Coliseo». Es el tercero con más aforo del país con una capacidad de más de 55 000 espectadores',
                   'San Lorenzo': '- El Club Atlético San Lorenzo de Almagro, mayormente conocido como San Lorenzo de Almagro o simplemente San Lorenzo, es una entidad deportiva argentina con sede en el barrio de Boedo, Buenos Aires. \n- Fue fundado el 1 de abril de 1908 por iniciativa de un grupo de jóvenes con la colaboración del sacerdote salesiano R.P. Lorenzo Massa. \n - Su estadio, el Pedro Bidegain, más conocido como El Nuevo Gasómetro y la Ciudad Deportiva se encuentran ubicados en la Comuna 7 de la ciudad de Buenos Aires, en el barrio de Bajo Flores, tiene capacidad para 47.964 espectadores y está dentro de los diez estadios más grandes de Argentina.'
                   }

    text_equipo.set_Text(descripcion[equipo.get()])



#Lista de opciones (Radio buttons)

radio_button_River = ttk.Radiobutton(window,
                                     text="River Plate", variable=equipo, value="River Plate", command=seleccionarEquipo)
radio_button_River.grid(column=1, row=1, padx=5, pady=5, sticky='w')
radio_button_Boca = ttk.Radiobutton(window,
                                      text="Boca Juniors", variable=equipo, value="Boca Juniors", command=seleccionarEquipo)
radio_button_Boca.grid(column=1, row=2, padx=5, pady=5, sticky='w')
radio_button_Independiente = ttk.Radiobutton(window,
                                      text="Independiente", variable=equipo, value="Independiente", command=seleccionarEquipo)
radio_button_Independiente.grid(column=1, row=3, padx=5, pady=5, sticky='w')
radio_button_Racing = ttk.Radiobutton(window,
                                      text="Racing", variable=equipo, value="Racing", command=seleccionarEquipo)
radio_button_Racing.grid(column=1, row=4, padx=5, pady=5, sticky='w')
radio_button_San_Lorenzo = ttk.Radiobutton(window,
                                      text="San Lorenzo", variable=equipo, value="San Lorenzo", command=seleccionarEquipo)
radio_button_San_Lorenzo.grid(column=1, row=5, padx=5, pady=5, sticky='w')


# Funcion reiniciar radiobuttons
def reiniciar():
    equipo.set("")
    text_equipo.set_Text("")

# Boton reiniciar
style_button = ttk.Style()
style_button.configure('btnReiniciar.TButton',
                       background='blue')
button_reiniciar = ttk.Button(
    window,  text="REINICIAR", style='btnReiniciar.TButton', command=reiniciar)
button_reiniciar.grid(column=2, row=8, sticky='s', pady=10)


window.mainloop()