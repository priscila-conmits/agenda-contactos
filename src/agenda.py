# src/agenda.py - Agenda de Contactos 
contactos = []
def mostrar_menu():
  print("\n===== AGENDA DE CONTACTOS =====")
  print("1. Agregar contactos")
  print("2. Ver todos los contactos")
  print("3. Buscar contacto")
  print("4. Eliminar contacto")
  print("5. Guardar y salir")
  print("===============================")

def main():
  print("¡Bienvenido a la Agenda de Contactos!")
  while True:
    mostrar_menu()
    opcion = input("\nElegi una opcion: ")
    if opcion == "5":
      print("\n¡Hasta luego!")
      break
    else:
      print("Opcion no implementada todavia.")

if _name_ == "_main_":
  main()
