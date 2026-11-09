from app.extensions import db
from app.models.task import Task


def list_tasks(user_id: int) -> Task | None:
    return Task.query.filter_by(user_id=user_id).order_by(Task.created_at.desc()).all()

def get_task(user_id: int, task_id: int)  -> Task | None:
    return Task.query.filter_by(id=task_id, user_id=user_id).first()

def create_task(user_id: int, data: dict) -> Task:
    task = Task(user_id=user_id, **data)
    db.session.add(task)
    db.session.commit()
    return task
