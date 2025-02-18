from enum import Enum

class States(Enum):

    RECEIVED = 'RECIBIDA'
    IN_PROCESS = 'EN_PROCESO'
    COMPLETED = 'COMPLETADA'
    CANCELED = 'CANCELADA'

