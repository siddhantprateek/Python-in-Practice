# can team A beat team B
# DFS

# here teams are the edges and 
from collections import defaultdict
from collections import namedtuple
MatchResult = namedtuple('MatchResult', ('winning_team', 'losing_team'))

def can_team_a_beat_team_b(matches, team_a, team_b):
    def build_graph():
        graph = defaultdict(set)
        for match in matches:
            graph[match.winning_team].add(match.losing_team)
    return graph

    def is_reachable_dfs(graph, curr, dest, visited=set()):
        if curr == dest:
            return True
        elif curr in visited or curr not in graph:
            return False 
        visited.add(curr)
        return any(is_reachable_dfs(graph, team_a, team_b) for team in graph[curr])

    return is_reachable_dfs(build_graph(), team_a, team_b)

print(can_team_a_beat_team_b(10, 2, 4))