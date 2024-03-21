# IMPORTAMOS LAS LIBRERIAS NECESARIAS
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

#INICIALIZAMOS LAS VARIABLES A UTILIZAR
theta=0
x0=0.
y0=50.
v0=330.
g=9.8

#CREAMOS LAS FUNCIONES PARA CREAR DATOS 
def x_pos(theta,t,v0,x0):
    x=x0+v0*np.cos(theta)*t
    return x

def y_pos(theta,t,v0,y0):
    y=y0+(v0*np.sin(theta)*t)-((g*t**2)/2)
    return y

def velocidad_x(theta, t, v0):
    return v0 * np.cos(theta)

def velocidad_y(theta, t, v0):
    return v0 * np.sin(theta) - g * t

def velocidad(vx, vy):
    velocidad_punto = np.sqrt(vx**2 + vy**2)

    return velocidad_punto

def magnitud( x0,y0,x,y ):
    magnitud = np.sqrt((x**2 - x0**2)+(y**2 - y0**2))

    return magnitud

def pausar_animacion(event):
    global animacion_pausada
    animacion_pausada = not animacion_pausada
    if animacion_pausada:
        anim.event_source.stop()
        boton_pausa.label.set_text('Reanudar')
    else:
        anim.event_source.start()
        boton_pausa.label.set_text('Pausar')

def actualizar(i):
    ln.set_data(x[i],y[i])
    position_text.set_text(f"Tiempo: {t[i]:.2f} s\nPosición (x, y): {x[i]:.2f}, {y[i]:.2f} m\nVelocidad: {vmagnitude[i]:.2f} m/s \n distancia: {distancia[i]:.2f} m")
    position_text.xy = (x[i], y[i])
    return ln, position_text

t=np.linspace(0,8,50)
x=x_pos(theta,t,v0,0)
y=y_pos(theta,t,v0,0)
a=magnitud(x0,y0,x,y)
N=len(t)
vx = velocidad_x(theta, t, v0)
vy = velocidad_y(theta, t, v0)
vmagnitude = velocidad(vx, vy)
distancia = magnitud(x0,y0,x,y)

fig, ax=plt.subplots()
ln, = plt.plot(x,y,'ro')
ax.set_xlim(0,280)
ax.set_ylim(0,100)

#AÑADEMOS LA FORMA DE IMPRIMIR EN PANTALLA LOS RESULTADOS
position_text = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="w"))

#INICIALIZAMOS LA PAUSA DE LA ANIMACIÓN
animacion_pausada = False

anim = animation.FuncAnimation(fig,actualizar,range(N),interval=0.00001)

plt.plot(x,y)
plt.grid()

# CREAMOS UN BOTÓN DE PAUSAR Y RENUDAR
ax_boton = plt.axes([0.81, 0.025, 0.1, 0.04])
boton_pausa = Button(ax_boton, 'Pausar')
boton_pausa.on_clicked(pausar_animacion)

#POR ÚLTIMO, MOSTRAMOS EN INTERFAZ GRÁFICA
plt.show()