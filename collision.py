# Função que determina se houve ou não uma colisão entre 2 elementos
def check_collision(rect1, rect2):
    return rect1.rect.colliderect(rect2.rect)