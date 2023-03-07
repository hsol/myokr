import pynecone

from app import AuthUser


class AuthService:
    def get_session_user(self, email: str):
        with pynecone.session() as s:
            session_user = (
                s.query(AuthUser).filter(AuthUser.email.__eq__(email)).one_or_none()
            )
            if session_user is None:
                session_user = AuthUser(email=email)
                s.add(session_user)
                s.flush()
            s.commit()
            s.refresh(session_user)
            return session_user


auth_service: AuthService = AuthService()
