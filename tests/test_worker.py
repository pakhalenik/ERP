from entities.worker import Worker

def test_worker():
    worker = Worker(worker_id=1, name="Alice")
    assert worker.is_available() is True

    worker.assign_task("Mixing ingredients")
    assert worker.is_available() is False

    worker.complete_task()
    assert worker.is_available() is True
    assert worker.total_tasks_completed == 1

    print(worker)

test_worker()
