from datetime import datetime
from datetime import timedelta

def calcularFecha(diasSigCita):
    fechaCita=datetime.now()    
    fechaSigCita= fechaCita+timedelta(diasSigCita)

    return fechaSigCita 

def calcularPagoTotal(costoFabricacion, porcentajeG, porcentajeI):
    pagoTotal= (costoFabricacion*porcentajeG/100+costoFabricacion)*porcentajeI

    return pagoTotal


def principal():
    nombre= input("Digite el nombre del paciente: ")
    fechaN= input("Digite la fecha de nacimiento del paciente(AAAA/MM/DD): ")
    mConsulta: input("Digite el motivo de la consulta: ")
    nMedicamento= input("Digite el nombre del medicamento:")
    dosis= input("Digite la dosis recomendada:")
    diasSigCita= int(input("Digite los días para la siguiente cita:"))
    costoFabricacion= int(input("Digite el costo de fabricación del medicamento:"))
    porcentajeG= int(input("Digite el porcentaje de ganancia: "))
    porcentajeI= 1.19

    sigCita=calcularFecha(diasSigCita)
    totalPagar=calcularPagoTotal(costoFabricacion, porcentajeG, porcentajeI)
    
    print("Nombre del paciente: "+ nombre)
    print("Fecha de nacimiento del paciente: "+ fechaN)
    print("Nombre del medicamento: "+ nMedicamento)
    print("Dosis recomendada:"+ dosis)
    print("Fecha de la siguiente cita:"+ str(sigCita))
    print("Total a Pagar:"+ str(totalPagar))
    
    

if __name__=='__main__':
    principal()
