class CPU:
    def __init__(self, cores):
        self.cores = cores

    def __repr__(self):
        return self.cores
        
class RAM:
    def __init__(self, size):
        self.size = size

class HardDisk:
    def __init__(self, capacity):
        self.capacity = capacity

class Computer:
    def __init__(self, cores, ram_size, hd_capacity):
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hard_disk = HardDisk(hd_capacity)

    def __repr__(self):
         return f'My computer has {self.cpu} cores'

delux = Computer('6', 16, 1024)
print(delux)

        