import csv,os
import pprint
   
def one_level(start_point, l_graph_data):
    l_child = []
    for i in range(len(l_graph_data)):
       parent,child = l_graph_data[i]
       if l_graph_data[i][0] == start_point:
          if child not in l_child:
             l_child.append(child)
    print ("one_level: " + str(l_child))
    return(l_child)

def one_node_sub(start_point, start_graph, l_graph_data):
    print ("start_point: " + start_point)
    res_graph = start_graph
    l_child = one_level(start_point, l_graph_data)
    if l_child == []:
       return(res_graph)
    res_graph[start_point] = l_child
    for i in range(len(l_child)):
       if l_child[i] not in res_graph.keys():
          res_graph = one_node_sub(l_child[i],res_graph,l_graph_data)	
    return(res_graph)	

	
if __name__ == "__main__": 
    csv_file = open("graph.csv")
    csv_reader = csv.reader(csv_file, delimiter=';')
    full_graph_data = list(csv_reader)
    print full_graph_data
    start_point = "f"
    part_graph = {"xxx":["xx","yy"]}
    res_graph = one_node_sub(start_point,part_graph, full_graph_data)
    csv_file.close()
    print "Result:"
    pprint.pprint(res_graph)
