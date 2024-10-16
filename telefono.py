"""
Aplicación de simulación de llamada telefónica usando Tkinter

Este script crea una interfaz gráfica que simula una pantalla de llamada telefónica
con opciones para contestar o rechazar la llamada.

Bibliotecas necesarias:
    - tkinter: Viene preinstalada con Python, no requiere instalación adicional.
    - Pillow: Instalar con 'pip install Pillow'
    - pygame: Instalar con 'pip install pygame'

Asegúrate de tener todas las bibliotecas instaladas antes de ejecutar el script.
"""

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import pygame
from tkinter import messagebox

class LlamadaApp:
    """
    Clase principal que maneja la interfaz y lógica de la aplicación de llamada.
    """

    def _init_(self, master):
        """
        Inicializa la aplicación y crea la interfaz principal.

        :param master: Ventana raíz de Tkinter
        """
        self.master = master
        master.title("Llamada Entrante")
        master.geometry("300x500")
        
        # Carga y procesa la imagen de perfil
        self.cargar_imagen_perfil()
        
        # Crea los widgets de la interfaz
        self.crear_widgets()
        
    def cargar_imagen_perfil(self):
        """
        Carga la imagen de perfil, la hace circular y la prepara para su uso en la interfaz.
        """
        # Carga y redimensiona la imagen del perfil
        image = Image.open("F:\todos los archivos\carrera programacion\tkinter\telefono\pascual.jpg")
        image = image.resize((150, 150), Image.LANCZOS)
        
        # Crea una máscara circular para la imagen de perfil
        mask = Image.new('L', (150, 150), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 150, 150), fill=255)
        
        # Aplica la máscara para hacer la imagen circular
        self.profile_image = ImageTk.PhotoImage(image.convert("RGBA"))
        self.profile_image.paste(0, (0, 0), mask)

    def crear_widgets(self):
        """
        Crea y coloca todos los widgets en la ventana principal.
        """
        # Crea y coloca las etiquetas y la imagen de perfil
        ttk.Label(self.master, text="Call").pack(pady=10)
        ttk.Label(self.master, image=self.profile_image).pack()
        ttk.Label(self.master, text="Pascual").pack(pady=10)
        
        # Crea un frame para los botones
        button_frame = ttk.Frame(self.master)
        button_frame.pack(pady=20)
        
        # Carga las imágenes para los botones
        self.rechazar_img = ImageTk.PhotoImage(Image.open("E:\todos los archivos\carrera programacion\tkinter\telefono\rechazar.png").resize((50, 50)))
        self.contestar_img = ImageTk.PhotoImage(Image.open("E:\todos los archivos\carrera programacion\tkinter\telefono\contestar.png").resize((50, 50)))
        
        # Crea y coloca los botones con sus respectivas imágenes
        ttk.Button(button_frame, image=self.rechazar_img, command=self.rechazar).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, image=self.contestar_img, command=self.contestar).pack(side=tk.RIGHT, padx=10)

    def rechazar(self):
        """
        Maneja la acción de rechazar la llamada.
        Abre una nueva ventana con un GIF y reproduce un sonido.
        """
        self.abrir_ventana_gif("ruta/a/gif_rechazar.gif", "E:\todos los archivos\carrera programacion\tkinter\telefono\rechazar.mp3")
        
    def contestar(self):
        """
        Maneja la acción de contestar la llamada.
        Abre una nueva ventana con un GIF y reproduce un sonido.
        """
        self.abrir_ventana_gif("ruta/a/gif_contestar.gif", "E:\todos los archivos\carrera programacion\tkinter\telefono\contestar.mp3")
        
    def abrir_ventana_gif(self, gif_path, sound_path):
        """
        Crea una nueva ventana para mostrar el GIF y reproducir el sonido.

        :param gif_path: Ruta al archivo GIF
        :param sound_path: Ruta al archivo de sonido
        """
        ventana = tk.Toplevel(self.master)
        ventana.title("Respuesta")
        
        # Carga y muestra el GIF
        gif = Image.open(gif_path)
        gif_label = ttk.Label(ventana)
        gif_label.pack()
        
        def actualizar_gif(index):
            """
            Función interna para actualizar los frames del GIF.

            :param index: Índice del frame actual
            """
            frame = ImageTk.PhotoImage(gif.copy())
            gif_label.configure(image=frame)
            gif_label.image = frame
            ventana.after(50, actualizar_gif, (index + 1) % gif.n_frames)
        
        # Inicia la animación del GIF
        actualizar_gif(0)
        
        # Reproduce el sonido
        pygame.mixer.init()
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()

if __name__ == "__main__":
    root = tk.Tk()
    app = LlamadaApp(root)
    root.mainloop()