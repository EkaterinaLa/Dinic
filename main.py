class Dinic:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0]*vertices for _ in range(vertices)]
        self.level = [-1] * vertices
        self.ptr = [0] * vertices

    def add_edge(self, u, v, w):
        self.graph[u][v] = w

    def bfs(self, source, sink):
        for i in range(self.vertices):
            self.level[i] = -1
        queue = [source]
        self.level[source] = 0

        while queue:
            u = queue.pop(0)
            for v in range(self.vertices):
                if self.level[v] == -1 and self.graph[u][v] > 0:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
                    if v == sink:
                        return True

        return False

    def dfs(self, u, sink, flow):
        if u == sink:
            return flow

        while self.ptr[u] < self.vertices:
            v = self.ptr[u]
            if self.level[v] == self.level[u] + 1 and self.graph[u][v] > 0:
                current_flow = min(flow, self.graph[u][v])
                pushed_flow = self.dfs(v, sink, current_flow)

                if pushed_flow > 0:
                    self.graph[u][v] -= pushed_flow
                    self.graph[v][u] += pushed_flow
                    return pushed_flow

            self.ptr[u] += 1

        return 0

    def dinic(self, source, sink):
        flow = 0
        while True:
            if not self.bfs(source, sink):
                break
            self.ptr = [0] * self.vertices
            while True:
                pushed = self.dfs(source, sink, float('Inf'))
                if pushed == 0:
                    break
                flow += pushed

        return flow


dinic = Dinic(5)
dinic.add_edge(0, 1, 10)
dinic.add_edge(0, 2, 5)
dinic.add_edge(1, 4, 10)
dinic.add_edge(2, 3, 10)
dinic.add_edge(3, 4, 5)

max_flow = dinic.dinic(0, 4)
print(max_flow)