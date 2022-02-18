#Nombre, fecha de nacimiento, motivo de consulta, medicamentos que consume o diagnostico, peso y edad, calcular dosis recomendada,
#la dosis sera:"3cm**3 2 veces al dia" o "1 pastilla 3 veces al dia"
#fecha de la siguiente cita(dias) (dado por el doctor)
#valor de la venta del medicamento:(costo de fabricacion+ % de ganancia( se determina a partir del costo de fabricacion)+ % de impuesto)
#En un consultorio de medicina alternativa se desea llevar un control de los medicamentos que se han recetado a cada paciente. Debido a que en el mismo consultorio se preparan los medicamentos, se conoce el nombre del mismo, su presentación (pastillas, jarabe, etc.), si es pediátrico o no,  la sustancia base para su preparación y el costo de fabricación del medicamento.  

def valor_total():
  costo_fab=7000
  ganancia=(costo_fab+15/100*costo_fab)
  iva=(19/100*ganancia)
  costo_final=(ganancia+iva)
  return costo_final

def pediatrico(edad):
  if edad<13:
    adjetivo=("(Pediatrico)")
  else:
    adjetivo=("(Para adultos)")
  return adjetivo

def dosis_total (f):
  if f==("Jarabe") or ("jarabe") :
    dosis= ("Debe tomar 3 cm3 2 veces al dia.")
  if f==("Pastillas") or ("pastillas"):
    dosis= ("Debe tomar 1 pastilla 3 veces al dia")
    return dosis

def bases(d):
  if d==("Dolex") or ("dolex") :
    base= ("Excipientes")
  if d==("Acetaminofen") or ("acetaminofen"):
    base= ("Acetamida")
  return base


def principal() :
  a=input("Ingrese nombre del paciente: ")
  edad=int(input("Ingrese edad: "))
  c=input("Ingrese el motivo de consulta: ")
  d=input("Ingrese el medicamento que consume (Dolex o acetaminofen): ")
  f=input("Que presentacion prefiere (Jarabe o pastillas): ")
  e=int(input("Ingrese su peso (kg): "))
  tipo_medicamento=pediatrico(edad)
  dosis=dosis_total(f)
  g=input("Ingrese fecha asignada para la siguiente cita (D/M/A): ")
  h=input("Ingrese la fecha de nacimiento (D/M/A):")
  base=bases(d)
  print(f"Su recibo es: ")
  print(f"Nombre: {a}")
  print(f"Su fecha de nacimiento es: {h}")
  print(f"Su edad es: {edad}")
  print (f"Diagnostico: {c}")
  print (f"Su peso: {e}")
  valor=valor_total()
  print (f"Medicamento a consumir: {d} {tipo_medicamento} {f} {dosis} {base} y su costo es {valor} ")
  print (f"Fecha de la siguiente consulta {g}")



if __name__ == '__main__':
  principal()
