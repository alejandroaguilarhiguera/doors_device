import time

def opening_door(doc_ref):
    print('🚪 door opening.... tarea corriendo en 2do plano')
    doc_ref.update({ "status": "in_progress", "action": "" })
    time.sleep(10)
    doc_ref.update({ "status": "open" })
    print('done')
