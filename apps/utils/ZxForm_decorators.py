import functools
import jwt

from apps.users.models import User


def authenticated_sync(method):
    @functools.wraps(method)
    async def wrapper(self, *args, **kwargs):
        tsession_id = self.request.headers.get("tsessionid", None)
        if tsession_id:
            try:
                send_data = jwt.decode(tsession_id, self.settings["secrect_key"],
                                       leeway=self.settings["jwt_expire"], options={"verify_exp": True})
                user_id = send_data.get("id")

                # 从数据库中获取到user并赋值给_current_user
                try:
                    user = await self.application.objects.get(User, id=user_id)
                    self._current_user = user

                    # 关键
                    await method(self, *args, **kwargs)
                except User.DoesNotExist as e:
                    self.set_status(401)
            except jwt.ExpiredSignature as e:
                self.set_status(401)
        else:
            self.set_status(401)
        self.finish({})

    return wrapper()