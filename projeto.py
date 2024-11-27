import threading
import time
import random

# Configurações iniciais
S = 5  # Pontos de redistribuição
C = 3  # Veículos
P = 20  # Encomendas
A = 5  # Capacidade de carga por veículo

redistribution_points = [threading.Semaphore(1) for _ in range(S)]
queues = [[] for _ in range(S)]  # Filas nos pontos de redistribuição
vehicles = [{} for _ in range(C)]  # Estado dos veículos
packages_status = {}  # Status das encomendas
stop = False

# Função para salvar o rastro de uma encomenda
def save_package_log(package_id, log):
    filename = f"package_{package_id}_log.txt"
    with open(filename, "w") as file:
        file.write("Número da Encomenda: {}\n".format(package_id))
        file.write("Ponto de Origem: {}\n".format(log["origin"]))
        file.write("Ponto de Destino: {}\n".format(log["destination"]))
        file.write("Horário de Chegada ao Ponto de Origem: {}\n".format(log["arrival_time"]))
        file.write("Horário de Carregamento no Veículo: {}\n".format(log["load_time"]))
        file.write("Identificador do Veículo: {}\n".format(log["vehicle_id"]))
        file.write("Horário de Descarregamento: {}\n".format(log["unload_time"]))

def vehicle_loop(vehicle_id, capacity):
    current_point = random.randint(0, S - 1)
    load = []

    while not stop:
        # Tenta acessar o ponto atual
        redistribution_points[current_point].acquire()
        
        # Carrega encomendas
        while len(load) < capacity and queues[current_point]:
            package = queues[current_point].pop(0)
            package["status"] = "Em trânsito"
            package["vehicle_id"] = vehicle_id
            package["load_time"] = time.time()
            load.append(package)

        redistribution_points[current_point].release()

        # Descarrega encomendas no destino
        delivered = [pkg for pkg in load if pkg["destination"] == current_point]
        for pkg in delivered:
            load.remove(pkg)
            pkg["unload_time"] = time.time()
            packages_status[pkg["id"]] = "Entregue"
            save_package_log(pkg["id"], pkg)

        # Move para o próximo ponto
        next_point = (current_point + 1) % S
        time.sleep(random.uniform(0.1, 0.5))  # Simula tempo de viagem
        current_point = next_point

        # Atualiza status do veículo
        vehicles[vehicle_id] = {"point": current_point, "load": len(load)}

        # Verifica se todas as encomendas foram entregues
        if all(status == "Entregue" for status in packages_status.values()):
            break

def package_loop(package_id, origin, destination):
    global packages_status
    # Cria o log inicial da encomenda
    package_log = {
        "id": package_id,
        "origin": origin,
        "destination": destination,
        "arrival_time": time.time(),
        "load_time": None,
        "vehicle_id": None,
        "unload_time": None,
    }
    # Coloca a encomenda no ponto de origem
    packages_status[package_id] = "Aguardando coleta"
    queues[origin].append(package_log)
    while packages_status[package_id] != "Entregue":
        time.sleep(0.1)

def monitor():
    while not stop:
        print("\n--- Monitoramento em tempo real ---")
        for i in range(S):
            print(f"Ponto {i}: {len(queues[i])} encomendas aguardando.")
        for i, vehicle in enumerate(vehicles):
            print(f"Veículo {i}: No ponto {vehicle.get('point', 'N/A')} com {vehicle.get('load', 0)} encomendas.")
        print("------------------------------------")
        time.sleep(1)

# Inicialização dos threads
threads = []

# Cria threads para veículos
for i in range(C):
    thread = threading.Thread(target=vehicle_loop, args=(i, A))
    threads.append(thread)
    thread.start()

# Cria threads para encomendas
for i in range(P):
    origin = random.randint(0, S - 1)
    destination = random.randint(0, S - 1)
    while destination == origin:
        destination = random.randint(0, S - 1)
    packages_status[i] = "Inicializando"
    thread = threading.Thread(target=package_loop, args=(i, origin, destination))
    threads.append(thread)
    thread.start()

# Thread de monitoramento
monitor_thread = threading.Thread(target=monitor)
monitor_thread.start()

# Aguarda a finalização dos threads
for thread in threads:
    thread.join()

stop = True
monitor_thread.join()

# Resumo final
print("\n--- Resumo Final ---")
for package_id, status in packages_status.items():
    print(f"Encomenda {package_id}: {status}")
