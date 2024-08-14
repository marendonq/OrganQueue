# main.py
from heap import MinHeap
from utils import create_patients, add_patient, print_patients
from visualize import plot_life_expectation_distribution, plot_waiting_time_distribution, plot_transplants_over_time, plot_patient_status
import random as r
import datetime
import logging

# Configuración del registro
logging.basicConfig(filename='event_log.txt', filemode="w",level=logging.INFO, format='%(asctime)s %(message)s')

def main():
    heap, current_id = create_patients(MinHeap(), 10000)
    transplanted_count = 0
    donor_times = []
    events = int(input("Ingrese cuántos eventos quiere simular: "))

    if events <= 20:
        for _ in range(events):
            print_patients(heap)
                
            event = r.randint(0, 1)  # 0: Donor arrives, 1: Patient arrives
            if event == 0:
                if not heap.vacio():
                    patient = heap.extraer_minimo()
                    print(f'\n............................\n¡Ha ingresado un donador!\n............................\nEl paciente:\n{patient}\nHa recibido el transplante.\n\n')
                    print("==================================")
                else:
                        print("++++++++++++++++++++++++++++++++++++++++")
                        print("¡No hay pacientes para recibir transplante!")
                        print("++++++++++++++++++++++++++++++++++++++++")
            else:
                current_id,patient = add_patient(heap,current_id)
                print(f'............................\nHa ingresado a la lista de pacientes el señor/ra:\n............................\n{patient}\n\n')


        print_patients(heap)
    else:
        for _ in range(events):
            event = r.randint(0, 1)  # 0: Ingresa un donante, 1: Ingresa un paciente
            if event == 0:
                patient = heap.extraer_minimo()
                if patient:
                    transplanted_count += 1
                    donor_times.append(datetime.datetime.now())
                    logging.info(f'Ha ingresado un donador! El paciente {patient.getName()}, con espectativa de vida de {patient.getLifeExpectation()} dias, ha recibido el trasplante.')
                else:
                    logging.info("No hay pacientes para recibir trasplante!")
            else:
                current_id, patient = add_patient(heap, current_id)
                logging.info(f'Ha ingresado a la lista de pacientes: {patient.getName()}, con espectativa de vida de {patient.getLifeExpectation()} dias.')

    print("\nResumen de eventos:")
    print(f'Total de eventos simulados: {events}')
    print(f'Pacientes en espera: {heap.tamanio()}')
    print(f'Trasplantes realizados: {transplanted_count}')
    if heap.tamanio() > 0:
        life_expectations = [patient.getLifeExpectation() for patient in heap.heapOrdenado]
        avg_life_expectation = sum(life_expectations) / len(life_expectations)
        print(f'Expectativa de vida promedio de pacientes en espera: {avg_life_expectation:.2f} días')

    # Visualizaciones
    plot_life_expectation_distribution(heap.heapOrdenado)
    plot_waiting_time_distribution(heap.heapOrdenado)
    plot_transplants_over_time(donor_times)
    plot_patient_status(heap.heapOrdenado, transplanted_count)

if __name__ == "__main__":
    main()
