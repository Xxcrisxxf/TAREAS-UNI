class Libro:
    def __init__(self, titulo, autor, Pagina = 0):
        self.titulo = titulo
        self.autor = autor
        self.pagina_actual = Pagina

    def mostrar_informacion(self):
        print(f"Libro: {self.titulo} - Autor: {self.autor} ")

    def pagina (self):
        self.pagina_actual += 10
        print(f"Has avanzado a la página {self.pagina_actual} del libro '{self.titulo}'.")

libro1 = Libro("El Hobbit", "J.R.R. Tolkien " )
libro2 = Libro("1984", "George Orwell")

print("--- El Hobbit ---")
libro1.mostrar_informacion()
libro1.pagina()

print("\n--- 1984 ---")
libro2.mostrar_informacion()
libro2.pagina()
