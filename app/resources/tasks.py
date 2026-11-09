from flask.views import MethodView
from flask_smorest import Blueprint

from app.services import task_service
from app.extensions import auth
from app.models import User

blp = Blueprint("tasks",
                 __name__,
                 url_prefix="/tasks",
                 description="Tasks")

@auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first
    if user and user.check_password(password):
        return user
    return None

@blp.route("/")
class TaskList(MethodView):

    @auth.login_required
    @blp.response(200)
    def get(self):
        return task_service.list_tasks(auth.current_user().id)

    @auth.login_required
    @blp.response(201)
    def post(self, data):
        return task_service.create_task(auth.current_user().id, data)