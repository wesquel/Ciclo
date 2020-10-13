    def ciclo_hamiltoniano(self):
        dic = {}
        for x in self.N:
            dic[x] = []
        dic = list(dic.items())
        caminho = self.pecorrer_ciclo(self.N[0], [], [], dic)

        if len(caminho) == len(self.N) + 1:
            return caminho
        else:
            return False

    def pecorrer_ciclo(self, vertice, visitados, caminho, dic):

        caminho.append(vertice)
        Lvizinho = self.vizinho(vertice)

        v_main = self.pos_vertice(vertice)

        if (len(caminho) == len(self.N)) and (caminho[0] in Lvizinho):
            caminho.append(caminho[0])
            return caminho
        for x in Lvizinho:
            if x not in caminho and (x not in dic[v_main][1]):
                dic[v_main][1].append(x)
                return self.pecorrer_ciclo(x, visitados,caminho, dic)

        v_inicial = self.pos_vertice(caminho[0])

        if len(dic[v_inicial][1]) == len(self.vizinho(self.N[v_inicial])):
            return caminho

        v_anterior = self.pos_vertice(caminho[-1])

        caminho.pop(-1)
        vizinho = caminho[-1]
        caminho.pop(-1)

        for x in range(len(dic[v_anterior][1])):
            dic[v_anterior][1].pop(0)

        return self.pecorrer_ciclo(vizinho,visitados,caminho,dic)

    def pos_vertice(self, vertice):
        for x in range(len(self.N)):
            if self.N[x] == vertice:
                return x
        return False
    
    def vizinho(self, vertice):
        vizinhos = []
        for x in range(len(self.N)):
            if self.N[x] == vertice:
                for y in range(len(self.M[x])):
                    if self.M[x][y] == 1:
                        vizinhos.append(self.N[y])
                    if self.M[y][x] == 1:
                        vizinhos.append(self.N[y])
        return vizinhos
