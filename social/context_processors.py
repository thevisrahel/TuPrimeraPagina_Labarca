from comentarios.models import Notificacion

def notificaciones_globales(request):                                     # Inyecta datos globales en todos los templates
    if request.user.is_authenticated:
        solicitudes_pendientes_count = request.user.solicitudes_recibidas.filter(
            estado='pendiente'
        ).count()

        notificaciones_count = request.user.notificaciones.filter(        # Cuenta notificaciones no leídas
            leida=False
        ).count()

        total = solicitudes_pendientes_count + notificaciones_count       # Total combinado para la campana

        return {
            'solicitudes_pendientes_count': total,                        # Se reutiliza la misma variable del navbar
        }
    return {'solicitudes_pendientes_count': 0}