#!/usr/bin/python3

class Dijkstra:
    def __init__( self, node_list, node_source_index, queue):
        self.node_list = node_list
        self.node_dict = {}
        self.priority_queue = queue()
        self.start_node = 0


        for node in self.node_list.nodes:
            node.cost = 'infinity'
            self.node_dict[node.node_id] = node

        #Starts everything:
        self.start_node = self.node_dict.get(node_source_index)
        self.start_node.cost = 0
        self.traverse_neighbors(self.start_node)
        self.priority_queue.insert(self.start_node)



        print("NODE DICT: ", self.node_dict.get(2))

        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("DATA STRUC: ", self.priority_queue.dumper())

    def traverse_neighbors(self, node):
        print("cost of root was set to: ", node.cost)
        for edge in node.neighbors:
            # (src=Node(id:0,neighbors:[2, 4, 6]) dest=Node(id:2,neighbors:[0, 1, 4]) length=150.80734056039023)
            print("whos your neighbor: ", edge)
            print("NE Weigth: ",edge.length )

            print("src cost: ", edge.src.cost)
            print("dest cost: ", edge.dest.cost)
            # print("cost: ", neighbor.cost)
            #check whos the neightbors
                #get its edge value. Look for its weigth.
                #if no visited yet
                # this.neighbors.weight = if current.weigth + this.neghbors.weigth < this.neghbors.weigth
                    #this.neightbors.prev = this current Neighbor
                #quee.insert(NODE)

        #sticl into visited dictionary currentNode
        #quee.get_next()
        #self.traverse_neighbors(queen.get_next())
        #how did we know we are done
