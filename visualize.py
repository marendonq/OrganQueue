import matplotlib.pyplot as plt
import datetime
import pandas as pd

def plot_life_expectation_distribution(patients):
    life_expectations = [patient.getLifeExpectation() for patient in patients]
    plt.hist(life_expectations, bins=30, edgecolor='black')
    plt.title('Distribución de la Expectativa de Vida')
    plt.xlabel('Expectativa de Vida (días)')
    plt.ylabel('Número de Pacientes')
    plt.show()

def plot_waiting_time_distribution(patients):
    waiting_times = [(datetime.datetime.now() - patient.getIngressTime()).total_seconds() for patient in patients]
    plt.hist(waiting_times, bins=30, edgecolor='black')
    plt.title('Distribución del Tiempo de Espera')
    plt.xlabel('Tiempo de Espera (segundos)')
    plt.ylabel('Número de Pacientes')
    plt.show()

def plot_transplants_over_time(donor_times):
    if len(donor_times) < 2:
        print("No hay suficientes eventos de donadores para calcular diferencias de tiempo.")
        return

    time_differences = [(donor_times[i] - donor_times[i - 1]).total_seconds() for i in range(1, len(donor_times))]

    
    df = pd.DataFrame({'Time Differences': time_differences})

    plt.scatter(range(len(time_differences)), df['Time Differences'], alpha=0.5, edgecolor='black')
    plt.title('Intervalos entre Eventos de Donadores')
    plt.xlabel('Evento de Donador')
    plt.ylabel('Intervalo de Tiempo (segundos)')
    plt.show()

def plot_patient_status(patients, transplanted):
    labels = ['En Espera', 'Trasplantados']
    sizes = [len(patients), transplanted]
    colors = ['#ff9999','#66b3ff']
    explode = (0.1, 0)  # explode 1st slice
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Proporción de Pacientes por Estado')
    plt.show()
