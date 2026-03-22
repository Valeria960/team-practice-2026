"""
Модуль для расчета скидок
"""

def discount(price, percent):
    """
    Рассчитывает цену со скидкой
    
    Аргументы:
        price (float): Исходная цена
        percent (float): Процент скидки
    
    Возвращает:
        float: Цена со скидкой
    
    Исключения:
        ValueError: Если процент скидки отрицательный или больше 100
    """
    if percent < 0:
        raise ValueError("Процент скидки не может быть отрицательным")
    if percent > 100:
        raise ValueError("Процент скидки не может быть больше 100")
    
    return price - price * percent / 100


def apply_discount_to_cart(cart_items, discount_percent):
    """
    Применяет скидку ко всем товарам в корзине
    
    Аргументы:
        cart_items (list): Список цен товаров
        discount_percent (float): Процент скидки
    
    Возвращает:
        list: Список цен со скидкой
    """
    if not cart_items:
        return []
    
    return [discount(item_price, discount_percent) for item_price in cart_items]


# Пример использования
if __name__ == "__main__":
    # Тестируем функцию скидки
    print(f"Цена со скидкой 20% от 1000: {discount(1000, 20)}")
    
    # Тестируем корзину
    cart = [100, 200, 300, 400, 500]
    discounted_cart = apply_discount_to_cart(cart, 10)
    print(f"Корзина: {cart}")
    print(f"Со скидкой 10%: {discounted_cart}")
    
    # Проверяем обработку ошибок
    try:
        discount(1000, -5)
    except ValueError as e:
        print(f"Ошибка (ожидаемо): {e}")
    
    try:
        discount(1000, 150)
    except ValueError as e:
        print(f"Ошибка (ожидаемо): {e}")