"""
Módulo de geometría para el paquete matemático.
Contiene funciones para calcular áreas y perímetros de figuras geométricas.
"""

import math


def area_circulo(radio):
    """
    Calcula el área de un círculo.
    
    Args:
        radio (float): Radio del círculo. Debe ser positivo.
    Returns:
        float: Área del círculo.
    Raises:
        ValueError: Si el radio es negativo.
    
    Ejemplo:
        >>> area_circulo(5)
        78.53981633974483
    """
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    return math.pi * radio ** 2


def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Args:
        base (float): Base del rectángulo. Debe ser positiva.
        altura (float): Altura del rectángulo. Debe ser positiva.
    Returns:
        float: Área del rectángulo.
    Raises:
        ValueError: Si base o altura son negativos.
    
    Ejemplo:
        >>> area_rectangulo(4, 5)
        20
    """
    if base < 0 or altura < 0:
        raise ValueError("Base y altura deben ser positivos")
    return base * altura


def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.
    
    Args:
        base (float): Base del triángulo. Debe ser positiva.
        altura (float): Altura del triángulo. Debe ser positiva.
    Returns:
        float: Área del triángulo.
    Raises:
        ValueError: Si base o altura son negativos.
    
    Ejemplo:
        >>> area_triangulo(6, 4)
        12.0
    """
    if base < 0 or altura < 0:
        raise ValueError("Base y altura deben ser positivos")
    return (base * altura) / 2


def hipotenusa(cateto_a, cateto_b):
    """
    Calcula la hipotenusa de un triángulo rectángulo (Teorema de Pitágoras).
    
    Args:
        cateto_a (float): Primer cateto. Debe ser positivo.
        cateto_b (float): Segundo cateto. Debe ser positivo.
    Returns:
        float: Longitud de la hipotenusa.
    Raises:
        ValueError: Si algún cateto es negativo.
    
    Ejemplo:
        >>> hipotenusa(3, 4)
        5.0
    """
    if cateto_a < 0 or cateto_b < 0:
        raise ValueError("Los catetos deben ser positivos")
    return math.sqrt(cateto_a ** 2 + cateto_b ** 2)


# ── Test rápido al ejecutar el módulo directamente ──────────────────────────
if __name__ == "__main__":
    print("=== Test del módulo geometria ===\n")
    print(f"Área círculo (r=5):          {area_circulo(5):.4f}")
    print(f"Área rectángulo (4x5):       {area_rectangulo(4, 5)}")
    print(f"Área triángulo (b=6, h=4):   {area_triangulo(6, 4)}")
    print(f"Hipotenusa (3, 4):           {hipotenusa(3, 4)}")
