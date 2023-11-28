"""Демонстратор взаимного компоновщика."""

from typing import Self


class Neuron:
    def __init__(self, name: str):
        self.name = name
        self.inputs: list[Neuron] = []
        self.outputs: list[Neuron] = []
    
    def connect_to(self, other: Self) -> None:
        self.outputs.append(other)
        other.inputs.append(self)
    
    def __iter__(self):
        yield self
    
    def __str__(self):
        return f'<{self.name}>'
    
    def show_connections(self) -> str:
        res = '\tinputs:\n'
        res += '\n'.join(f'\t\t{neuron}' for neuron in self.inputs)
        res += '\n\toutputs:\n'
        res += '\n'.join(f'\t\t{neuron}' for neuron in self.outputs)
        return res


class NeuronLayer(list):
    def __init__(self, name: str, count: int = 2):
        super().__init__()
        self.name = name
        for i in range(1, count+1):
            self.append(Neuron(f'{self.name} Нейрон {i}'))
    
    def connect_to(self, other: Neuron | Self) -> None:
        if self is other:
            return
        for neuron_out in self:
            for neuron_in in other:
                neuron_out.connect_to(neuron_in)
    
    def __str__(self):
        return '\n'.join(str(neuron) for neuron in self)


# >>> n1 = Neuron('Отдельный Нейрон 1')
# >>> n2 = Neuron('Отдельный Нейрон 2')
# >>> n1.connect_to(n2)
# >>>
# >>> print(n1)
# <Отдельный Нейрон 1>
# >>> print(n1.show_connections())
# 	inputs:
#
# 	outputs:
# 		<Отдельный Нейрон 2>
# >>>
# >>> print(n2)
# <Отдельный Нейрон 2>
# >>> print(n2.show_connections())
# 	inputs:
# 		<Отдельный Нейрон 1>
# 	outputs:
#
# >>>
# >>> nl1 = NeuronLayer('Слой 1')
# >>> nl1.connect_to(n1)
# >>>
# >>> print(n1)
# <Отдельный Нейрон 1>
# >>> print(n1.show_connections())
# 	inputs:
# 		<Слой 1 Нейрон 1>
# 		<Слой 1 Нейрон 2>
# 	outputs:
# 		<Отдельный Нейрон 2>
