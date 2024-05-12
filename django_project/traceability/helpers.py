from models import Traceability
from serializers import TraceabilitySerializer

def get_traceability(traceability):
    qset = Traceability.objects.all()
    qset = TraceabilitySerializer(qset, many=True).data
    return qset