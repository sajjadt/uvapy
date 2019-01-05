def topological_sort(in_edges):
  '''
  Returns topoligically sorted ordering of nodes
  :param list in_edges: List of tuples (vertex_id, list of vertex_ids(that are connected to it)  )
  :return: ordering of vertex ids
  :rtype: list
  '''
  order = []
  while len(in_edges) > 0:
    target = -1
    for i in range(len(in_edges)):
      if len(in_edges[i][1]) == 0:
        target = i
        order.append(in_edges[i][0])
        break
     
    if target >= 0:
      v_id = in_edges[target][0]
      in_edges.remove(in_edges[target])
    
      for i in range(len(in_edges)):
        if v_id in in_edges[i][1]:
          in_edges[i][1].remove(v_id)
  return order