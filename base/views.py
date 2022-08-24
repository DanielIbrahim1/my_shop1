
from unicodedata import category
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse
from .models import Profile,Category,Cart,Order,Product
from rest_framework.response import Response

# @api_view(['POST'])
# def admin_registser(request):
#     User.objects.create_user(email=request.data["email"],password=request.data["pwd"],username=request.data["usr"],
#     is_staff=1,is_superuser=1)
#     return HttpResponse('Register')

# @api_view(['POST'])
# def user_registser(request):
#     User.objects.create_user(email=request.data["email"],password=request.data["pwd"],username=request.data["usr"])
#     return HttpResponse('Register')


# token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['first_name'] = user.first_name
        token['email'] = user.email
        # send params into the token
        # should export it in the Loginslicer
        return token

# log in
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# admin/user register
@api_view(['POST'])
def register(request):
    isStaff = request.data["staff"]
    user = User.objects.create_user(
        email=request.data["email"], password=request.data["password"],
        is_staff=isStaff, first_name=request.data['first_name'],
        last_name=request.data['last_name'])
    Profile.objects.create(user=user, phone=request.data['phone'],
                           address=request.data['address'], gender=request.data['gender'])
    return JsonResponse({'user':'added'})


# log out from the back??



#creating/dispaly products

@api_view(['POST'])
@permission_classes([IsAuthenticated])
# only for admin
def add_category(request):
#    name= models.CharField(max_length=50, null=True, blank=True)
    Category.objects.create(name=request.data['name'])
    return JsonResponse({'category':'added'})



@api_view(['GET'])
# admin/user
def get_category(request):
    categoryLst=[]
    for cat in Category.objects.all():
        categoryLst.append({
            'name':cat.name,
            'id':cat._id})
    return JsonResponse(categoryLst)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
# only for admin
def add_product(request):
    Product.objects.create(
    description=request.data['description'],
    photo=request.data['photo'],
    price=request.data['price'],
    category=request.data['category'],
    )
    return JsonResponse({'Product':'added'})



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_products(request,id=-1):
    if int(id)>-1: #get single product
        product=Product.objects.get(_id=id)
        return JsonResponse({
            "description":product.description,
            "photo":product.photo,
            "category":product.category,
            "price":product.price,
            "id":product._id})
    else:
        productsLst=[] #get all products
        for product in Product.objects.all():
            productsLst.append({
            "description":product.description,
            "photo":product.photo,
            "category":product.category,
            "price":product.price,
            "id":product._id})
    return JsonResponse(productsLst,safe=False)


@api_view(['POST'])
def addToCart(request):
    Cart.objects.create(
    # user=request.data['user'],
    cat=request.data['cat'],
    prod=request.data['prod'],
    amount=request.data['amount'],
    total_price=request.data['total_price'],
    )
    return JsonResponse({'CART':"added"})




def test(request):
    return HttpResponse('hello world')
