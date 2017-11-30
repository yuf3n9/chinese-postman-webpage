import csvparser
from chinesepostman import eularian, network

def solver():
    """ Make it so. """
    edges = None
    edges = csvparser.parse('graph/graph.csv')

    original_graph = network.Graph(edges)

    #print('{} edges'.format(len(original_graph)))
    if not original_graph.is_eularian:
        #print('Converting to Eularian path...')
        graph = eularian.make_eularian(original_graph)
        #print('Conversion complete')
        #print('\tAdded {} edges'.format(len(graph) - len(original_graph)))
        #print('\tTotal cost is {}'.format(graph.total_cost))
    else:
        graph = original_graph

    #print('Attempting to solve Eularian Circuit...')
    route, attempts = eularian.eularian_path(graph, start=1)
    if not route:
        #print('\tGave up after {} attempts.'.format(attempts))
        return 'Failed to find a route after '+ str(attempts) + ' attempts.'
    else:
        #print('\tSolved in {} attempts'.format(attempts, route))
        #print('Solution: ({} edges)'.format(len(route) - 1))
        #print('\t{}'.format(route))
        return 'Find path '+'->'.join(map(str,route))