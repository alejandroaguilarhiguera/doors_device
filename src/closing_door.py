import time

def closing_door(doc_ref):
    print('🗝️ closing the door.... tarea corriendo en 2do plano')
    doc_ref.update({ "status": "in_progress", "action": "" })
    time.sleep(10)
    doc_ref.update({ "status": "closed" })
    print('done')