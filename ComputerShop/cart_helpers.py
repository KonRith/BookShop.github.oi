def cart_count(request):
    cart = request.session.get('cart', {})
    total_quantity = sum(item['quantity'] for item in cart.values())
    return {'cart_count': total_quantity}
