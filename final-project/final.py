
# coding: utf-8

# In[176]:

class Query:
    def __init__(self, promoters_file='averaged_promoters.json', repressors_file='averaged_repressors.json'):
        with open(promoters_file) as r:
            self.gene_to_affecteds_zscore_promoters = json.load(r)
        with open(repressors_file) as r:
            self.gene_to_affecteds_zscore_repressors = json.load(r)
            
    def gene_info(self, gene_id):
        r = self.gene_represses(gene_id)
        p = self.gene_promotes(gene_id)
        if r is not None and p is not None:
            return r + p
        if r is not None:
            return r
        if p is not None:
            return p
        return None
    
    def gene_promotes(self, gene_id):
        if gene_id in self.gene_to_affecteds_zscore_promoters:
            return self.gene_to_affecteds_zscore_promoters[gene_id]
        return None
    
    def gene_represses(self, gene_id):
        if gene_id in self.gene_to_affecteds_zscore_repressors:
            return self.gene_to_affecteds_zscore_repressors[gene_id]
        return None
    
    def gene_vis_promotes(self, gene_id, n=5):
        get_ipython().magic('matplotlib inline')
        import networkx as nx
        G = nx.Graph()
        base = gene_id
        nodes = [gene_id]
        count = 0
        p = self.gene_promotes(gene_id)
        if p is None:
            return
        for node in p:
            nodes.append(node['gene'])
            if count >= n:
                break
            count += 1
        G.add_nodes_from(nodes)
        for node in nodes:
            G.add_edge(base, node)
        import matplotlib.pyplot as plt
        nx.draw_networkx(G, with_labels=True)
        plt.show()
        
    def gene_vis_represses(self, gene_id, n=5):
        get_ipython().magic('matplotlib inline')
        import networkx as nx
        G = nx.Graph()
        base = gene_id
        nodes = [gene_id]
        count = 1
        p = self.gene_represses(gene_id)
        if p is None:
            return
        for node in p:
            nodes.append(node['gene'])
            if count >= n:
                break
            count += 1
        G.add_nodes_from(nodes)
        for node in nodes:
            G.add_edge(base, node)
        import matplotlib.pyplot as plt
        nx.draw_networkx(G, with_labels=True)
        plt.show()


# In[177]:

promoters_file = 'averaged_promoters.json'
repressors_file = 'averaged_repressors.json'
q = Query(promoters_file, repressors_file)


# In[178]:

q.gene_info('BCL2')


# In[179]:

q.gene_promotes('BUB1B')


# In[180]:

q.gene_represses('BRCA1')


# In[182]:

q.gene_vis_promotes('BUB1B')


# In[183]:

q.gene_vis_represses('BRCA1', n=10)

