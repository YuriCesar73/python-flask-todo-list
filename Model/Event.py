from datetime import datetime

class Event:
    
    id:id
    deadline:datetime
    descricao:str
    
    def __init__(self, deadline=datetime.utcnow,descricao="Sem descrição") -> None:
        pass