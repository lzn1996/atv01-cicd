import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True,
                     use_numbers=True, use_special_chars=True):
    """Gera uma senha aleatória.

    Args:
        length: Comprimento da senha.
        use_uppercase: Incluir letras maiúsculas.
        use_lowercase: Incluir letras minúsculas.
        use_numbers: Incluir números.
        use_special_chars: Incluir caracteres especiais.

    Returns:
        str: Senha gerada.
    """

    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password