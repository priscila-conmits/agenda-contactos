# src/agenda.py - Agenda de Contactos 
contactos = []
def agregar_contacto():
  nombre = input("Nombre del contacto: "). strip()
  if nombre == "":
    print("El nombre no puede estar vacío.")
    return
  telefono = input("Telefono: ").strip()
  if telefono == "":
    print("El telefono no puede estar vacío.")
    return
  contactos.append({"nombre": nombre, "telefono": telefono})
  print(f"Contacto '{nombre}' agregando correctamente.")
  def ver_contactos():
    if len(contactos) == 0:
      print("\n La agenda esta vacía.")
      return
    print("\n LISTA DE CONTACTOS:")
    print("-" * 30)
    for i, c in enumerate(contactos, 1):
      print(f" {i}.  {c['nombre']} - {c['telefono']}")
    print("-" * 30)
    print(f"Total: {len(contactos)} contacto(s)")


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
