class Plane():
    def __init__(self, model, company, source, destiny, numberOfPassengers, flightNumber):
        self.model = model
        self.company = company
        self.source = source
        self.destiny = destiny
        self.numberOfPassengers = numberOfPassengers
        self.flightNumber = flightNumber

Plane01 = Plane('Boeing 737', 'Boeing', 'Paris, France', 'New York - United State', 250, 5856)
Plane02 = Plane('Boeing 777', 'Boeing', 'Paris, France', 'Vancouver - Canada', 280, 5886)
Plane03 = Plane('Boeing 767', 'Boeing', 'Paris, France', 'Texas - United State', 150, 5786)

class AirportRunway:
    def __init__(self):
        self.airplanes = []
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        self.airplanes.append(elem)
        self.last = elem    
        self.first = self.airplanes[0]
        self._size = self._size + 1
        print('Avião com o número de vôo ' + str(elem.flightNumber) + ' acaba de entrar na lista de espera para decolagem.')

    def lastAirPlane(self): 
        if self.last is None:
            return print("A pista está vázia!")
        
        if self._size == 1:
            return print('O avião com o número de vôo ' + str(self.last.flightNumber) + ' é o único avião na lista de espera para á decolagem.')

        return print('O avião com o número de vôo ' + str(self.last.flightNumber) + ' é o ultimo na lista de espera para á decolagem.')

    def pop(self):
        if self.first is None:
            return print("A pista está vázia!")

        elem = self.first

        if self._size > 1:
            self.first = self.airplanes[1]
            self._size = self._size - 1
            del self.airplanes[0]
            return print('O avião com o número de vôo ' + str(elem.flightNumber) + ', acaba de decolar!')

        del self.airplanes[0]
        self._size = self._size - 1
        return print('O ultimo avião na pista, com o número de vôo ' + str(elem.flightNumber) + ', acaba de decolar!')

    def planePosition(self, elem: type=None):
        position = 0
        
        if not elem:
            return print('Número de vôo é obrigatório!')

        for airplane in self.airplanes:
            position = position + 1
            if airplane.flightNumber == elem:
                return print('Avião com o número de vôo ' + str(elem) + ' foi encontrado! Ele pertence a empresa ' + airplane.company + ', seu modelo é um ' + airplane.model + ', o seu destino atual é ' + airplane.destiny + ' e possui um total de ' + str(airplane.numberOfPassengers) + '. Ele é o ' + str(position) + '° na fila de decolagem.')     
        else: 
            return print('Nenhum avião com este número de vôo foi encontrado!')

    def listAllPlanes(self):
        if self.first is None:
            return print("A pista está vázia!")  

        for airplane in self.airplanes:
            print('Modelo:' + airplane.model + ' / Empresa: ' + airplane.company + ' / Destino: ' + airplane.destiny + ' / Origem: ' + airplane.source + ' / Número de voo: ' + str(airplane.flightNumber) + ' / Número de passageiros: ' + str(airplane.numberOfPassengers))
        else:
            return print('Todos os aviões da fila de decolagem foram listados com sucesso!')

    def takeTheFirstPlaneInLine(self):
        if self.first is None:
            return print("A pista está vázia!") 

        return print('Modelo:' + self.first.model + ' / Empresa: ' + self.first.company + ' / Destino: ' + self.first.destiny + ' / Origem: ' + self.first.source + ' / Número de voo: ' + str(self.first.flightNumber) + ' / Número de passageiros: ' + str(self.first.numberOfPassengers))

    def lenght(self):
        return print('Existe um total de ' + str(self._size) + ' aviões para decolagem.')

# a) Permitir a decolagem do primeiro avião na fila. - airportRunway.pop()
# b) Adicionar um avião na fila de decolagem. - airportRunway.push()
# c) Mostrar o total de aviões aguardando na fila de decolagem. - airportRunway.lenght()
# d) Lista todos os aviões na fila de decolagem. - airportRunway.listAllPlanes()
# e) Listar as características do próximo a decolar (o avião que está na frente da fila). - takeTheFirstPlaneInLine()
# f) Mostrar a posição de um avião conforme o número do voo. - airportRunway.planePosition()

airportRunway = AirportRunway()

airportRunway.push(Plane01)
airportRunway.push(Plane02)
airportRunway.push(Plane03)
