from utils import Queue, Stack, Graph


def earliest_ancestor(ancestors, starting_node, visited=None, path=None):

    # initialize path = [starting_node]
    # path = [starting_node]
    # get parents - only care about parent not starting node i.e: node[1]
    # loop to check for number of connections
    # if no connections return -1

    print('ancestors:', ancestors)
    print('starting_node:', starting_node)

    graph = Graph()
    stack = Stack()
    path = [starting_node]
    stack.push(path)

    graph = {}
    for key, value in ancestors:
        # print('k,v:',key, value)
        if value not in graph:
            # print('aa',value)
            graph[value] = set()
        if key not in graph:
            print('aa', value)
            graph[key] = set()
        graph[value].add(key)

    print('graph:', graph)
    if len(graph[starting_node]) == 0:
        return -1
    visited = set()
    paths = list()
    print('paths:', paths)

    while stack.size() > 0:
        current_path = stack.pop()
        print('current_path:', current_path)
        current_node = current_path[-1]
        print('current_node:', current_node)

        if current_node not in visited:
            visited.add(current_node)
            print('visited', visited)

            for parent in graph[current_node]:
                if parent not in visited:
                    new_path = list(current_path)
                    new_path.append(parent)
                    print('new_path:', new_path)
                    stack.push(new_path)
            if len(graph[current_node]) == 0:
                paths.append(current_path)
                print('paths:', paths)
    sorted_paths = sorted(paths, reverse=True)  # key=lambda x: len(x))
    print('*****', sorted_paths[-1][-1])
    return sorted_paths[-1][-1]


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 8)
