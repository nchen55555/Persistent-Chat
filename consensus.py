class Replica: 
    def __init__(self, replica_id, stub, persistent_storage): 
        # a local log for each replica for specific messages 
        self.log = [] 
        self.id = replica_id 
        self.storage = persistent_storage
        self.stub = stub

    
