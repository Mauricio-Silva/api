from app import repository

def warning(mensage: str) -> str: return f'\033[92m{mensage}\033[m' 


class Student:
    def __init__(self, name: str, email: str, password: str) -> None:
        self.id = repository.generate_id()
        if not isinstance(name, str):
            raise TypeError(warning('The Name of the Student must be a string'))
        if not isinstance(email, str):
            raise TypeError(warning('The Email of the Student must be a string'))
        if not isinstance(password, str):
            raise TypeError(warning('The Password of the Student must be a string'))
        self.name = name
        self.email = email
        self.password = password
        